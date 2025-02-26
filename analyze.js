import { execSync } from 'child_process';
import fs from 'fs';
import path from 'path';
import axios from 'axios';
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// 大模型审核配置
const AI_ENDPOINT = 'http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions';
const AI_MODEL = 'qwen2.5-72B-instruct';
const AI_PROMPT = `你是一个专业的文档审核专家，请严格检查以下用户手册内容：
1. 找出所有错别字（包括同音字、形近字错误）
2. 标记语法不通顺的句子（主谓宾不全、逻辑混乱等）
3. 指出不符合技术文档规范的内容（如口语化表达、不明确的指代）
4. 标注中英文标点混用的情况
请用markdown列表格式返回问题，按出现顺序编号，包含原文引用和修改建议`;

const logFile = 'result.md';
const mdDir = 'books/XX平台操作手册';

// 初始化日志文件
fs.writeFileSync(logFile, 'XX平台操作手册文档审核报告\n\n');

// 递归获取所有md文件
function getMarkdownFiles(dir) {
  const files = fs.readdirSync(dir, { withFileTypes: true });
  let results = [];

  for (const file of files) {
    const fullPath = path.join(dir, file.name);
    if (file.isDirectory()) {
      results = results.concat(getMarkdownFiles(fullPath));
    } else if (file.name.endsWith('.md')) {
      results.push(fullPath);
    }
  }
  return results;
}

// 执行四项检查
async function analyzeFile(filePath) {
  let report = `\n## ${filePath}\n`;

  try {
    // 1. markdownlint语法检查
    const lintResult = execSync(`markdownlint "${filePath}" --config .markdownlint.json`, {
      encoding: 'utf-8',
      stdio: 'pipe'
    });
    report += `### Markdown语法问题\n${lintResult}\n`;
  } catch (error) {
    report += `### Markdown语法问题\n\`\`\`markdown\n${error.stdout}\n\`\`\`\n`;
  }

  // 2. 英文标点检测（中文文档中不应出现）
  const content = fs.readFileSync(filePath, 'utf-8');
  const englishPunctuation = content.match(/[,.;:?!'"]/g);
  if (englishPunctuation) {
    report += `### 英文标点使用\n\`\`\`markdown\n发现${englishPunctuation.length}处英文标点（中文文档应使用中文标点）\n\`\`\`\n`;
  }

  // 3. 绝对路径图片检查
  const absoluteImages = content.match(/!\[.*?\]\((?:https?:\/\/|\/|\\|[a-zA-Z]:).+?\)/g);
  if (absoluteImages) {
    report += `### 绝对路径图片\n\`\`\`markdown\n${absoluteImages.join('\n')}\n\`\`\`\n`;
  }

  // 4. 改进的语句通顺度检测
  // 分句处理并检查标点使用
  const sentences = content.split(/[。！？]/);
  const problematicSentences = sentences.filter(sentence => {
    // 检查连续重复标点
    if (/([，；])\1{2,}/.test(sentence)) return true;
    // 检查中英文标点混用
    if (/[,.!?;:]/.test(sentence) && /[，。！？；：]/.test(sentence)) return true;
    // 检查过长句子（超过80字符）
    return sentence.trim().length > 80;
  });

  if (problematicSentences.length > 0) {
    report += `### 语句通顺问题\n\`\`\`markdown\n发现${problematicSentences.length}处可能问题：\n`;
    report += problematicSentences.slice(0,5).map(s => `· ${s.trim().substring(0,60)}...`).join('\n') + '\n\`\`\`\n';
  }

  // 大模型深度分析
  try {
    const content = fs.readFileSync(filePath, 'utf-8');
    const response = await axios.post(AI_ENDPOINT, {
      model: AI_MODEL,
      messages: [{
        role: "user",
        content: `${AI_PROMPT}\n\n${content.substring(0, 12000)}` // 限制上下文长度
      }],
      temperature: 0.1
    }, {
      headers: { Authorization: `Bearer ${process.env.LLM_API_KEY}` }
    });

    const aiAnalysis = response.data.choices[0].message.content;
    report += `### 智能语义审核\n\`\`\`markdown\n${aiAnalysis}\n\`\`\`\n`;
  } catch (error) {
    report += `### 智能审核异常\n\`\`\`markdown\n${error.message}\n\`\`\`\n`;
  }

  fs.appendFileSync(logFile, report);
}

// 主程序
try {
  const files = getMarkdownFiles(mdDir);
  // 串行处理保证日志顺序
  for (const file of files) {
    await analyzeFile(file);
    console.log(`已完成分析: ${file}`);
  }
  console.log('文档分析完成，结果已保存至 result.md');
} catch (error) {
  console.error('分析过程中发生错误:', error);
}
