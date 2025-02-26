import os
import re
import subprocess
from pathlib import Path
import requests
import json

# 配置项
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

def find_markdown_files(root_dir):
    md_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('.md'):
                md_files.append(Path(dirpath) / filename)
    return md_files

def analyze_file(file_path):
    report = f'\n## {file_path}\n'

    try:
        # Markdownlint检查
        result = subprocess.run(
            ['markdownlint', str(file_path), '--config', '.markdownlint.json'],
            capture_output=True, text=True, encoding='utf-8'
        )
        report += '### Markdown语法问题\n```markdown\n'
        report += result.stdout if result.returncode == 0 else result.stderr
        report += '\n```\n'
    except Exception as e:
        report += f'### Markdown语法异常\n```markdown\n{str(e)}\n```\n'

    # 英文标点检测
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    en_punctuation = re.findall(r'[,.;:?!\'"]', content)
    if en_punctuation:
        report += f'### 英文标点使用\n```markdown\n发现{len(en_punctuation)}处英文标点\n```\n'

    # 绝对路径图片检测
    abs_images = re.findall(
        r'!\[.*?\]\((?:https?://|/|\\|[a-zA-Z]:).+?\)', content)
    if abs_images:
        report += '### 绝对路径图片\n```markdown\n'
        report += '\n'.join(abs_images) + '\n```\n'

    # 语句通顺度分析
    sentences = re.split(r'[。！？]', content)
    problematic = []
    for sent in sentences:
        sent = sent.strip()
        if not sent:
            continue

        # 检查重复标点
        if re.search(r'([，；])\1{2,}', sent):
            problematic.append(sent)
            continue

        # 中英文标点混用
        if re.search(r'[,.!?;:]', sent) and re.search(r'[，。！？；：]', sent):
            problematic.append(sent)
            continue

        # 长句检测
        if len(sent) > 80:
            problematic.append(sent)

    if problematic:
        sample = '\n'.join([f'· {s[:60]}...' for s in problematic[:5]])
        report += f'### 语句通顺问题\n```markdown\n发现{len(problematic)}处问题\n{sample}\n```\n'

    # 大模型审核
    try:
        headers = {'Authorization': f'Bearer {os.getenv("LLM_API_KEY")}'}
        payload = {
            'model': AI_MODEL,
            'messages': [{
                'role': 'user',
                'content': f'{AI_PROMPT}\n\n{content[:12000]}'
            }],
            'temperature': 0.1
        }

        response = requests.post(AI_ENDPOINT,
            headers=headers,
            json=payload,
            timeout=300)
        response.raise_for_status()

        ai_result = response.json()['choices'][0]['message']['content']
        report += f'### 智能语义审核\n```markdown\n{ai_result}\n```\n'
    except Exception as e:
        report += f'### 智能审核异常\n```markmarkdown\n{str(e)}\n```\n'

    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(report)

if __name__ == '__main__':
    init_log()
    files = find_markdown_files(MD_DIR)

    for file in files:
        print(f'正在分析: {file}')
        analyze_file(file)

    print('文档分析完成，结果已保存至 result.md')
