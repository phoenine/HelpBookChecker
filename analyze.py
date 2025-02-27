import os
import re
import subprocess
import sys
import time
from pathlib import Path
import requests

# 大模型审核配置
AI_ENDPOINT = 'http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions'
AI_MODEL = 'vllm'
AI_PROMPT = """你是一个专业的文档审核专家，请严格检查以下用户手册内容：
1. 找出所有错别字（包括同音字、形近字错误）
2. 标记语法不通顺的句子（主谓宾不全、逻辑混乱等）
3. 指出不符合技术文档规范的内容（如口语化表达、不明确的指代）
4. 标注中英文标点混用的情况
请用markdown列表格式返回问题，按出现顺序编号，包含原文引用和修改建议"""

LOG_FILE = 'result.md'
MD_DIR = 'books/XX平台操作手册'

def init_log():
    with open(LOG_FILE, 'w', encoding='utf-8') as f:
        f.write('XX平台操作手册文档审核报告\n\n')

def get_markdown_files(dir_path):
    md_files = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def analyze_file(file_path):
    report = f"\n## {file_path}\n"

    try:
        # 1. Markdown语法检查
        result = subprocess.run(
            ['markdownlint', file_path, '--config', '.markdownlint.json'],
            capture_output=True, text=True, check=True
        )
        if result.stdout:
            report += f"### Markdown语法问题\n{result.stdout}\n"
        else:
            report += "### Markdown语法问题\n✅ 没有发现问题。\n"
    except subprocess.CalledProcessError as e:
        report += f"### Markdown语法问题\n```markdown\n{e.stdout}\n```\n"

    # 2. 英文标点检测
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 排除代码块和链接
    text_only = re.sub(r'```[\s\S]*?```|`.*?`|\[.*?\]\(.*?\)', '', content)

    # 检测中文上下文中的英文标点
    punctuation_matches = []
    for match in re.finditer(r'([\u4e00-\u9fa5])([,.;:?!\'"])|([,.;:?!\'"])(（)', text_only):
        start = max(0, match.start() - 20)
        end = min(len(text_only), match.end() + 20)
        context = text_only[start:end].replace('\n', '↵')

        line_num = text_only.count('\n', 0, match.start()) + 1
        punctuation_matches.append({
            'symbol': (match.group(2) or match.group(3)),
            'position': f"第{line_num}行",
            'context': f"...{context}..."
        })

    if punctuation_matches:
        report += "### 英文标点检测\n```markdown\n"
        report += f"发现 {len(punctuation_matches)} 处可能错误的英文标点：\n\n"
        for i, match in enumerate(punctuation_matches):
            report += f"{i+1}. 符号「{match['symbol']}」 {match['position']}\n"
            report += f"   上下文：{match['context']}\n"
            report += f"   建议替换为：「{get_chinese_punctuation(match['symbol'])}」\n\n"
        report += "```\n"
    else:
        report += "### 英文标点检测\n✅ 没有发现英文标点错误。\n"

    # 3. 绝对路径图片检查
    absolute_images = re.findall(r'!\[.*?\]\((?:https?://|/|\\|[a-zA-Z]:).+?\)', content)
    if absolute_images:
        report += "### 绝对路径图片\n```markdown\n"
        report += '\n'.join(absolute_images) + "\n```\n"
    else:
        report += "### 绝对路径图片\n✅ 没有绝对路径图片。\n"

    # 4. 本地链接检查
    local_links = re.findall(r'\[.*?\]\((?!https?://|mailto:|#)([^\)]+)\)', content)
    if local_links:
        report += "### 本地链接检查\n```markdown\n"
        for i, link in enumerate(set(local_links)):
            try:
                abs_path = Path(os.path.join(os.path.dirname(file_path), link)).resolve()

                if not abs_path.exists():
                    report += f"{i+1}. {link}\n   目标不存在: {abs_path}\n"
                    continue

                if abs_path.is_dir():
                    report += f"   注意：目标链接{abs_path}是一个目录结果，请手动确认。\n"

            except Exception as e:
                report += f"{i+1}. {link}\n   ❌ 错误: {str(e)}\n"
        report += "```\n"

    # 5. 大模型分析
    max_retries = 3
    for attempt in range(max_retries + 1):
        try:
            start_time = time.time()
            response = requests.post(
                AI_ENDPOINT,
                json={
                    "model": AI_MODEL,
                    "messages": [{
                        "role": "user",
                        "content": f"{AI_PROMPT}\n\n{content[:20000]}"
                    }],
                    "temperature": 0.1
                },
                headers={"Authorization": f"Bearer {os.getenv('LLM_API_KEY')}"},
                timeout=300
            )
            response.raise_for_status()

            analysis = response.json()['choices'][0]['message']['content']
            report += f"### 智能语义审核\n```markdown\n{analysis}\n```\n"
            break
        except Exception as e:
            if attempt < max_retries:
                report += f"### 智能审核异常（尝试 {attempt + 1}）\n```markdown\n{str(e)}\n```\n"
                time.sleep(2)  # 等待2秒后重试
            else:
                report += f"### 智能审核异常（最终尝试 {max_retries + 1}）\n```markdown\n{str(e)}\n```\n"

    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(report)

def get_chinese_punctuation(en_punctuation):
    punctuation_map = {
        ',': '，',
        '.': '。',
        ';': '；',
        ':': '：',
        '?': '？',
        '!': '！',
        "'": '‘',
        '"': '“'
    }
    return punctuation_map.get(en_punctuation, en_punctuation)

if __name__ == "__main__":
    try:
        init_log()
        md_files = get_markdown_files(MD_DIR)
        for file in md_files:
            analyze_file(file)
            print(f"已完成分析: {file}")
        print("文档分析完成，结果已保存至 result.log")
    except Exception as e:
        print(f"分析过程中发生错误: {str(e)}")
