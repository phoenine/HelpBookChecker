XX平台操作手册文档审核报告


## books/XX平台操作手册/工作流画布页面.md
### Markdown语法问题
```markdown
books/XX平台操作手册/工作流画布页面.md:1 MD032/blanks-around-lists Lists should be surrounded by blank lines [Context: "- [使用手册首页](./XX平台手册大纲.md)"]
books/XX平台操作手册/工作流画布页面.md:1 MD041/first-line-heading/first-line-h1 First line in a file should be a top-level heading [Context: "- [使用手册首页](./XX平台手册大纲.md)"]
books/XX平台操作手册/工作流画布页面.md:2 MD022/blanks-around-headings Headings should be surrounded by blank lines [Expected: 1; Actual: 0; Above] [Context: "# 工作流画布页面"]
books/XX平台操作手册/工作流画布页面.md:2 MD022/blanks-around-headings Headings should be surrounded by blank lines [Expected: 1; Actual: 0; Below] [Context: "# 工作流画布页面"]
books/XX平台操作手册/工作流画布页面.md:30 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]

```
### 英文标点使用
```markdown
发现40处英文标点
```
### 语句通顺问题
```markdown
发现1处问题
· - [使用手册首页](./XX平台手册大纲.md)
# 工作流画布页面
节点使用：

- [开始和结束节点：如何设置工作...
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容进行的审核，包括错别字、语法不通顺的句子、不符合技术文档规范的内容以及中英文标点混用的情况：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - 无明显语法不通顺的句子。

3. **不符合技术文档规范的内容**
   - **原文**：`[如何定时触发工作流](./开发工作流/工作流画布功能/定时触发/定时触发.md)`
     - **问题**：标题使用了“如何”，建议使用更规范的表述。
     - **修改建议**：`[定时触发工作流](./开发工作流/工作流画布功能/定时触发/定时触发.md)`
   - **原文**：`[怎样查看工作流运行历史记录](./开发工作流/工作流画布功能/运行历史/运行历史.md)`
     - **问题**：标题使用了“怎样”，建议使用更规范的表述。
     - **修改建议**：`[查看工作流运行历史记录](./开发工作流/工作流画布功能/运行历史/运行历史.md)`

4. **中英文标点混用**
   - **原文**：`[开始和结束节点：如何设置工作流输入和输出](./开发工作流/工作流节点/开始节点和结束节点/开始和结束节点.md )`
     - **问题**：链接末尾有空格。
     - **修改建议**：`[开始和结束节点：如何设置工作流输入和输出](./开发工作流/工作流节点/开始节点和结束节点/开始和结束节点.md)`
   - **原文**：`[通过模型分类节点：如何在工作流中进行意图识别或分类](./开发工作流/工作流节点/通过模型分类节点/通过模型分类节点.md)`
     - **问题**：链接末尾有空格。
     - **修改建议**：`[通过模型分类节点：如何在工作流中进行意图识别或分类](./开发工作流/工作流节点/通过模型分类节点/通过模型分类节点.md)`

总结：
- 无明显错别字。
- 无明显语法不通顺的句子。
- 有两处标题使用了口语化表达，建议修改。
- 有两处链接末尾有多余的空格，建议删除。
```

## books/XX平台操作手册/工作台界面.md
### Markdown语法问题
```markdown
books/XX平台操作手册/工作台界面.md:1 MD041/first-line-heading/first-line-h1 First line in a file should be a top-level heading [Context: "- [XX平台是什么，能做什么](./XX平台基本介绍/XX..."]
books/XX平台操作手册/工作台界面.md:9 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]

```
### 英文标点使用
```markdown
发现14处英文标点
```
### 语句通顺问题
```markdown
发现1处问题
· - [XX平台是什么，能做什么](./XX平台基本介绍/XX平台基本介绍.md)
- [怎样快速搭建一个AI智能体](....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容进行的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - 无明显语法不通顺的句子。

3. **不符合技术文档规范的内容**
   - **[XX平台是什么，能做什么](./XX平台基本介绍/XX平台基本介绍.md)**
     - **问题**：标题应更加具体，避免使用“是什么，能做什么”这种泛泛的表述。
     - **建议**：修改为“XX平台概述及功能介绍”。
   - **[怎样快速搭建一个AI智能体](./快速开始/搭建你的第一个AI智能体/搭建你的第一个智能体.md)**
     - **问题**：“怎样快速搭建一个AI智能体”中的“怎样”口语化，不够正式。
     - **建议**：修改为“如何快速搭建一个AI智能体”。
   - **[怎样快速搭建一个AI工作流](./快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md)**
     - **问题**：“怎样”口语化，不够正式。
     - **建议**：修改为“如何快速搭建一个AI工作流”。
   - **[怎样管理AI应用（创建，导入，导出，复制，编辑信息，删除）](./AI应用基础管理/AI应用基础管理.md)**
     - **问题**：“怎样”口语化，不够正式。
     - **建议**：修改为“如何管理AI应用（创建、导入、导出、复制、编辑信息、删除）”。
   - **[新用户怎样注册XX平台](./用户配置相关/新用户注册/新用户注册.md)**
     - **问题**：“怎样”口语化，不够正式。
     - **建议**：修改为“新用户如何注册XX平台”。
   - **[怎样邀请成员协作开发](./用户配置相关/邀请协作成员/邀请协作成员.md)**
     - **问题**：“怎样”口语化，不够正式。
     - **建议**：修改为“如何邀请成员协作开发”。
   - **[怎样修改用户名和密码](./用户配置相关/修改用户名和密码/修改用户名和密码.md)**
     - **问题**：“怎样”口语化，不够正式。
     - **建议**：修改为“如何修改用户名和密码”。

4. **中英文标点混用的情况**
   - **[怎样管理AI应用（创建，导入，导出，复制，编辑信息，删除）](./AI应用基础管理/AI应用基础管理.md)**
     - **问题**：括号内的内容使用了中文逗号，但括号是英文的。
     - **建议**：修改为“如何管理AI应用（创建、导入、导出、复制、编辑信息、删除）”。

总结：
- 无明显错别字。
- 无明显语法不通顺的句子。
- 多处标题使用了口语化的“怎样”，建议改为更正式的“如何”。
- 一处中英文标点混用，建议统一使用中文标点。
```

## books/XX平台操作手册/XX平台手册大纲.md
### Markdown语法问题
```markdown
books/XX平台操作手册/XX平台手册大纲.md:61 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]
books/XX平台操作手册/XX平台手册大纲.md:62 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 3]
books/XX平台操作手册/XX平台手册大纲.md:63 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 4]
books/XX平台操作手册/XX平台手册大纲.md:64 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 5]
books/XX平台操作手册/XX平台手册大纲.md:65 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 6]
books/XX平台操作手册/XX平台手册大纲.md:66 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 7]
books/XX平台操作手册/XX平台手册大纲.md:67 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 8]

```
### 英文标点使用
```markdown
发现101处英文标点
```
### 语句通顺问题
```markdown
发现1处问题
· # XX平台使用手册

- [XX平台基本介绍](./XX平台基本介绍/XX平台基本介绍.md)
- 快速开始
  - ...
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/智能体创建页面.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现16处英文标点
```
### 语句通顺问题
```markdown
发现1处问题
· # 智能体创建页面

- [如何快速搭建一个智能体](./快速开始/搭建你的第一个AI智能体/搭建你的第一个智能体.md...
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容进行的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - 无明显语法不通顺的句子。

3. **不符合技术文档规范的内容**
   - **原文**：[如何快速搭建一个智能体](./快速开始/搭建你的第一个AI智能体/搭建你的第一个智能体.md)
     - **问题**：标题中的“搭建你的第一个AI智能体”与链接中的文件名重复，建议简化或统一。
     - **修改建议**：[如何快速搭建一个智能体](./快速开始/搭建你的第一个智能体.md)
   - **原文**：[如何进行智能体设置](./开发智能体/智能体编排配置/智能体编排配置.md)
     - **问题**：标题中的“进行智能体设置”可以更具体，明确设置的内容。
     - **修改建议**：[如何配置智能体](./开发智能体/智能体编排配置.md)
   - **原文**：[怎样给智能体添加工具](./开发智能体/智能体编排配置/智能体编排配置.md)
     - **问题**：标题中的“怎样”口语化，建议使用更正式的表达。
     - **修改建议**：[如何为智能体添加工具](./开发智能体/智能体编排配置.md)
   - **原文**：[怎样批量验证智能体运行效果](./AI应用评估/AI应用评估.md)
     - **问题**：标题中的“怎样”口语化，建议使用更正式的表达。
     - **修改建议**：[如何批量验证智能体运行效果](./AI应用评估/AI应用评估.md)
   - **原文**：[如何查看智能体日常运行数据](./AI应用监控/AI应用监控.md)
     - **问题**：标题中的“日常”可以更具体，明确数据的类型。
     - **修改建议**：[如何查看智能体的运行数据](./AI应用监控/AI应用监控.md)
   - **原文**：[如何API访问智能体](./AI应用API访问/AI应用API访问.md)
     - **问题**：标题中的“API访问”可以更具体，明确访问的方式。
     - **修改建议**：[如何通过API访问智能体](./AI应用API访问/AI应用API访问.md)

4. **中英文标点混用的情况**
   - 无明显中英文标点混用的情况。

希望以上审核结果对您有所帮助。如有进一步的修改需求，请随时告知。
```

## books/XX平台操作手册/提示词编写/提示词编写.md
### Markdown语法问题
```markdown
books/XX平台操作手册/提示词编写/提示词编写.md:23:66 MD033/no-inline-html Inline HTML [Element: br]
books/XX平台操作手册/提示词编写/提示词编写.md:24:204 MD033/no-inline-html Inline HTML [Element: br]
books/XX平台操作手册/提示词编写/提示词编写.md:25:56 MD033/no-inline-html Inline HTML [Element: br]
books/XX平台操作手册/提示词编写/提示词编写.md:26:65 MD033/no-inline-html Inline HTML [Element: br]
books/XX平台操作手册/提示词编写/提示词编写.md:26:81 MD033/no-inline-html Inline HTML [Element: br]
books/XX平台操作手册/提示词编写/提示词编写.md:26:108 MD033/no-inline-html Inline HTML [Element: br]
books/XX平台操作手册/提示词编写/提示词编写.md:30:82 MD009/no-trailing-spaces Trailing spaces [Expected: 0 or 2; Actual: 1]
books/XX平台操作手册/提示词编写/提示词编写.md:32:29 MD009/no-trailing-spaces Trailing spaces [Expected: 0 or 2; Actual: 1]
books/XX平台操作手册/提示词编写/提示词编写.md:67 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]

```
### 英文标点使用
```markdown
发现12处英文标点
```
### 语句通顺问题
```markdown
发现11处问题
· | **内容模块** | **说明**                                         ...
· | ## 技能 <br />当用户询问最新的科技新闻时，先调用“getToutiaoNews” 搜索最新科技新闻，再调用...
· | 请参考如下格式回复：  <br />**新闻标题**  <br />- 新闻摘要：30 个字左右的新闻摘要  <br...
· ```Markdown
# 角色
你是一位资深且专业的数据分析专家，能够熟练运用 analyze 工具进行全面的数据处理...
· ## 技能
### 技能 1: 提取数据
1. 当用户提供一个数据源时，首先尝试使用 analyze 工具的 extra...
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md
### Markdown语法问题
```markdown
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:5 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:40 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:49:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:51:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:57:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 3; Style: 1/1/1]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:65:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:67:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:69:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:71:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:73:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:73:60 MD010/no-hard-tabs Hard tabs [Column: 60]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:92:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:94:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:94:61 MD010/no-hard-tabs Hard tabs [Column: 61]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:98:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:100:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:102:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:102:59 MD010/no-hard-tabs Hard tabs [Column: 59]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:104:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:106:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:110:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:112:68 MD009/no-trailing-spaces Trailing spaces [Expected: 0 or 2; Actual: 1]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:112:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:112:68 MD010/no-hard-tabs Hard tabs [Column: 68]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:114:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 4; Style: 1/1/1]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:116:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:118:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:122:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:124:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 5; Style: 1/1/1]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:128:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 6; Style: 1/2/3]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:132:1 MD029/ol-prefix Ordered list item prefix [Expected: 2; Actual: 7; Style: 1/2/3]
books/XX平台操作手册/快速开始/搭建你的第一个工作流AI应用/搭建你的第一个工作流AI应用.md:136:2 MD010/no-hard-tabs Hard tabs [Column: 2]

```
### 英文标点使用
```markdown
发现78处英文标点
```
### 语句通顺问题
```markdown
发现22处问题
· ![image-20250124172155080](./assets/image-20250124172155080....
· 基于以上功能规划，这个应用的用户界面会包含以下组件：

- 一个让用户可以输入翻译内容字段
- 一个让用户选择翻译语言的...
· 2. 在右上角**新建**，选择**工作流**...
· 3. 输入工作流名称并选择图标

   ![image-20250124173214354](./assets/imag...
· ​	i. 在用户输入区域，单击 **+** 图标，配置第一个变量 (content) 用于传入用户要翻译的内容，字段类型...
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/快速开始/搭建你的第一个AI智能体/搭建你的第一个智能体.md
### Markdown语法问题
```markdown
books/XX平台操作手册/快速开始/搭建你的第一个AI智能体/搭建你的第一个智能体.md:25 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]
books/XX平台操作手册/快速开始/搭建你的第一个AI智能体/搭建你的第一个智能体.md:26:2 MD010/no-hard-tabs Hard tabs [Column: 2]

```
### 英文标点使用
```markdown
发现48处英文标点
```
### 语句通顺问题
```markdown
发现13处问题
· ![image-20250117152223000-1737445405236-5](./assets/image-20...
· ### 步骤1：创建一个智能体

1. 登录XX平台...
· 2. 点击**新建**按钮，选择聊天型

3. 输入智能体名称和描述，可更换智能体图标...
· 4. 单击**确定**


​	![image-20250117152735375](./assets/image-20...
· ![image-20250117153003873](./assets/image-20250117153003873....
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/用户配置相关/新用户注册/新用户注册.md
### Markdown语法问题
```markdown

```
### 智能语义审核
```markdown
```markdown
1. **错别字**
   - 原文：XX平台当前尚未开放新用户自主注册账号，如需开通账号请联系XXXX工作人员。
   - 修改建议：XX平台当前尚未开放新用户自主注册账号，如需开通账号请联系**XX**XX工作人员。

2. **语法不通顺的句子**
   - 原文：XX平台当前尚未开放新用户自主注册账号，如需开通账号请联系XXXX工作人员。
   - 修改建议：XX平台当前尚未开放新用户自主注册功能，如需开通账号，请联系XXXX工作人员。

3. **不符合技术文档规范的内容**
   - 原文：XX平台当前尚未开放新用户自主注册账号，如需开通账号请联系XXXX工作人员。
   - 修改建议：XX平台当前尚未开放新用户自主注册功能，如需开通账号，请联系XXXX工作人员。

4. **中英文标点混用**
   - 原文：XX平台当前尚未开放新用户自主注册账号，如需开通账号请联系XXXX工作人员。
   - 修改建议：XX平台当前尚未开放新用户自主注册账号，如需开通账号，请联系XXXX工作人员。
```

### 说明
- **错别字**：原文中的“XX”应为“XX”。
- **语法不通顺的句子**：原句中“自主注册账号”改为“自主注册功能”，使句子更加通顺。
- **不符合技术文档规范的内容**：原句中“如需开通账号请联系”改为“如需开通账号，请联系”，使表达更加正式。
- **中英文标点混用**：原句中未发现中英文标点混用的情况。
```

## books/XX平台操作手册/用户配置相关/修改用户名和密码/修改用户名和密码.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现6处英文标点
```
### 语句通顺问题
```markdown
发现1处问题
· ![image-20250113144958649](./assets/image-20250113144958649....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - **原文**: "账户设置界面，进行用户名的修改与密码重置。"
     - **问题**: 句子缺少主语，导致逻辑不清晰。
     - **修改建议**: "在账户设置界面，您可以进行用户名的修改与密码重置。"

3. **不符合技术文档规范的内容**
   - **原文**: "点击工作台右上角账号，选择**设置**。"
     - **问题**: 表达不够明确，建议具体说明操作步骤。
     - **修改建议**: "点击工作台右上角的账号图标，然后选择**设置**。"

4. **中英文标点混用**
   - **原文**: "点击工作台右上角账号，选择**设置**。"
     - **问题**: 句号应使用中文标点。
     - **修改建议**: "点击工作台右上角的账号图标，然后选择**设置**。"
   - **原文**: "账户设置界面，进行用户名的修改与密码重置。"
     - **问题**: 句号应使用中文标点。
     - **修改建议**: "在账户设置界面，您可以进行用户名的修改与密码重置。"

总结：
- 无明显错别字。
- 有两处句子语法不通顺，建议修改。
- 有一处表达不够明确，建议具体化。
- 有两处中英文标点混用，建议统一使用中文标点。
```

## books/XX平台操作手册/用户配置相关/邀请协作成员/邀请协作成员.md
### Markdown语法问题
```markdown
books/XX平台操作手册/用户配置相关/邀请协作成员/邀请协作成员.md:15:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/用户配置相关/邀请协作成员/邀请协作成员.md:17:2 MD009/no-trailing-spaces Trailing spaces [Expected: 0 or 2; Actual: 1]
books/XX平台操作手册/用户配置相关/邀请协作成员/邀请协作成员.md:17:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/用户配置相关/邀请协作成员/邀请协作成员.md:19 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]
books/XX平台操作手册/用户配置相关/邀请协作成员/邀请协作成员.md:20 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 3]
books/XX平台操作手册/用户配置相关/邀请协作成员/邀请协作成员.md:21 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 4]
books/XX平台操作手册/用户配置相关/邀请协作成员/邀请协作成员.md:22 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 5]
books/XX平台操作手册/用户配置相关/邀请协作成员/邀请协作成员.md:23 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 6]
books/XX平台操作手册/用户配置相关/邀请协作成员/邀请协作成员.md:24 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 7]
books/XX平台操作手册/用户配置相关/邀请协作成员/邀请协作成员.md:25 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 8]

```
### 英文标点使用
```markdown
发现10处英文标点
```
### 语句通顺问题
```markdown
发现3处问题
· ![image-20250113143645278](./assets/image-20250113143645278....
· ![image-20250113144958649](./assets/image-20250113144958649....
· ![image-20250113145223882](./assets/image-20250113145223882....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - **原文**：添加团队成员中输入邀请成员的邮箱账号，并选择成员权限。
     - **修改建议**：在“添加团队成员”中输入邀请成员的邮箱账号，并选择成员权限。

3. **不符合技术文档规范的内容**
   - **原文**：登录XXXX平台后，即进入工作台界面。
     - **修改建议**：登录XXXX平台后，将进入工作台界面。
   - **原文**：点击工作台右上角账号，选择**设置**。
     - **修改建议**：点击工作台右上角的账号，选择**设置**。
   - **原文**：设置界面，点击**邀请成员**。
     - **修改建议**：在设置界面中，点击**邀请成员**。
   - **原文**：添加团队成员中输入邀请成员的邮箱账号，并选择成员权限。
     - **修改建议**：在“添加团队成员”中输入邀请成员的邮箱账号，并选择成员权限。

4. **中英文标点混用的情况**
   - **原文**：点击工作台右上角账号，选择**设置**。
     - **修改建议**：点击工作台右上角的账号，选择**设置**。
   - **原文**：设置界面，点击**邀请成员**。
     - **修改建议**：在设置界面中，点击**邀请成员**。
   - **原文**：添加团队成员中输入邀请成员的邮箱账号，并选择成员权限。
     - **修改建议**：在“添加团队成员”中输入邀请成员的邮箱账号，并选择成员权限。

### 修改后的文档内容

```markdown
# 邀请协作成员

登录XXXX平台后，将进入工作台界面。

![image-20250113143645278](./assets/image-20250113143645278.png)

1. 点击工作台右上角的账号，选择**设置**。

   ![image-20250113144958649](./assets/image-20250113144958649.png)

   在设置界面中，点击**邀请成员**。

   ![image-20250113145223882](./assets/image-20250113145223882.png)

   在“添加团队成员”中输入邀请成员的邮箱账号，并选择成员权限。
```

希望这些修改建议对您有所帮助。如果有任何进一步的问题或需要更多帮助，请随时告知。
```

## books/XX平台操作手册/AI应用API访问/AI应用API访问.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现6处英文标点
```
### 语句通顺问题
```markdown
发现1处问题
· ![image-20250213142523150](./assets/image-20250213142523150....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容进行的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - 无明显语法不通顺的句子。

3. **不符合技术文档规范的内容**
   - **原文**：XX平台上搭建的AI应用（智能体和工作流应用），可以通过API进行访问。
     - **问题**：句子结构较为松散，建议优化以增强清晰度。
     - **修改建议**：在XX平台上搭建的AI应用（包括智能体和工作流应用）可以通过API进行访问。
   - **原文**：进入搭建好的智能体，点击**开发**，可查看智能体API访问说明。
     - **问题**：句子中的“进入搭建好的智能体”表述不够明确，建议具体化。
     - **修改建议**：进入已搭建好的智能体，点击**开发**选项，可查看智能体API访问说明。
   - **原文**：进入搭建好的工作流，点击**开发**，可查看工作流API访问说明。
     - **问题**：与上一条类似，表述不够明确。
     - **修改建议**：进入已搭建好的工作流，点击**开发**选项，可查看工作流API访问说明。

4. **中英文标点混用的情况**
   - **原文**：XX平台上搭建的AI应用（智能体和工作流应用），可以通过API进行访问。
     - **问题**：括号内的内容使用了中文逗号，建议统一使用英文逗号。
     - **修改建议**：XX平台上搭建的AI应用（智能体和工作流应用）可以通过API进行访问。
   - **原文**：进入搭建好的智能体，点击**开发**，可查看智能体API访问说明。
     - **问题**：句子中的逗号为中文逗号，建议统一使用英文逗号。
     - **修改建议**：进入已搭建好的智能体，点击**开发**，可查看智能体API访问说明。
   - **原文**：进入搭建好的工作流，点击**开发**，可查看工作流API访问说明。
     - **问题**：句子中的逗号为中文逗号，建议统一使用英文逗号。
     - **修改建议**：进入已搭建好的工作流，点击**开发**，可查看工作流API访问说明。

以上是文档的审核结果，希望对您有所帮助。
```

## books/XX平台操作手册/AI应用评估/AI应用评估.md
### Markdown语法问题
```markdown
books/XX平台操作手册/AI应用评估/AI应用评估.md:11:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 2; Style: 1/2/3]
books/XX平台操作手册/AI应用评估/AI应用评估.md:13:1 MD029/ol-prefix Ordered list item prefix [Expected: 2; Actual: 3; Style: 1/2/3]
books/XX平台操作手册/AI应用评估/AI应用评估.md:17:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 4; Style: 1/1/1]

```
### 英文标点使用
```markdown
发现16处英文标点
```
### 语句通顺问题
```markdown
发现5处问题
· 1. 工作流发布后，点击工作流画布上方**评估**标签...
· ![image-20250123102346738](.\assets\image-20250123102346738....
· 3. 点击**新建评估**，选择版本，评估用例中上传问题集，选择系统推理模型和Embedding模型（评估时计算相似度和...
· ![image-20250123103735132](.\assets\image-20250123110412035....
· ![image-20250123110447657](.\assets\image-20250123110447657....
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/知识库概述/知识库概述.md
### Markdown语法问题
```markdown
books/XX平台操作手册/知识库概述/知识库概述.md:1 MD041/first-line-heading/first-line-h1 First line in a file should be a top-level heading [Context: "- [知识库创建](./知识库创建/知识库创建.md)"]
books/XX平台操作手册/知识库概述/知识库概述.md:8 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]
books/XX平台操作手册/知识库概述/知识库概述.md:38:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 2; Style: 1/1/1]
books/XX平台操作手册/知识库概述/知识库概述.md:42:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 3; Style: 1/1/1]
books/XX平台操作手册/知识库概述/知识库概述.md:46:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 4; Style: 1/1/1]

```
### 英文标点使用
```markdown
发现8处英文标点
```
### 语句通顺问题
```markdown
发现5处问题
· - [知识库创建](./知识库创建/知识库创建.md)
- [知识库配置](./知识库配置/知识库配置.md)

# 知...
· 1. 创建知识库

首先，需要将需要的知识内容导入到知识库中...
· 2. 使用知识库

完成知识库创建和内容导入后，你就可以在智能体和工作流中添加知识库内容进行调用了...
· 3. 配置检索和召回策略

在上传完知识内容后，可以通过相关配置来解决从哪里查、怎么查、用几条的问题...
· 4. 调试与优化

最后，你需要通过测试来不断优化回复的内容效果...
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md
### Markdown语法问题
```markdown
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:13 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:25:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:25:71 MD010/no-hard-tabs Hard tabs [Column: 71]
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:27:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 4; Style: 1/2/3]
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:33:1 MD029/ol-prefix Ordered list item prefix [Expected: 2; Actual: 5; Style: 1/2/3]
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:41:1 MD029/ol-prefix Ordered list item prefix [Expected: 3; Actual: 6; Style: 1/2/3]
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:55:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 7; Style: 1/1/1]
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:61:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:63:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 8; Style: 1/2/3]
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:67:1 MD029/ol-prefix Ordered list item prefix [Expected: 2; Actual: 9; Style: 1/2/3]
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:69:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:97:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:97:61 MD010/no-hard-tabs Hard tabs [Column: 61]
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:99:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:103:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 4; Style: 1/1/1]
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:105:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:105:66 MD010/no-hard-tabs Hard tabs [Column: 66]
books/XX平台操作手册/知识库概述/知识库创建/知识库创建.md:107:2 MD010/no-hard-tabs Hard tabs [Column: 2]

```
### 英文标点使用
```markdown
发现49处英文标点
```
### 语句通顺问题
```markdown
发现18处问题
· ![image-20250123141316947](./assets/image-20250123141316947....
· ![image-20250123141508601](./assets/image-20250123141508601....
· 2. **知识库描述**

   输入对知识库的描述，当同时使用多个知识库并使用由大模型自主判断调用模式下，知识库的描述...
· 3. **文档**

​	上传文档作为知识库的内容，文档支持TXT、MARKDOWN、PDF、HTML、XLSX、XLS...
· 4. **索引策略**

   **高质量**：使用Embedding模型，进行语义向量相似度检索，需要消耗token...
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/知识库概述/知识库配置/召回测试/召回测试.md
### Markdown语法问题
```markdown
books/XX平台操作手册/知识库概述/知识库配置/召回测试/召回测试.md:17 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]

```
### 英文标点使用
```markdown
发现9处英文标点
```
### 语句通顺问题
```markdown
发现3处问题
· # 召回测试

召回测试对追溯知识库回答正确率有非常大的作用，通过召回测试查看针对某问题知识库资料被召回的情况，以及可根...
· ![image-20250123203353082](./assets/image-20250123203353082....
· ![image-20250123203632655](./assets/image-20250123203632655....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档进行的审核结果：

1. **错别字**
   - 原文：召回测试对追溯知识库回答正确率有非常大的作用
     - 修改建议：召回测试对提升知识库回答正确率有非常大的作用
   - 原文：在未打开Rerank重排序时，此评分即为召回时计算的相似度评分。
     - 修改建议：在未启用Rerank重排序时，此评分即为召回时计算的相似度评分。

2. **语法不通顺的句子**
   - 原文：通过召回测试查看针对某问题知识库资料被召回的情况，以及可根据召回情况和评分进行文本片段的针对性优化处理，提升召回及回答正确率。
     - 修改建议：通过召回测试，可以查看针对某一问题的知识库资料被召回的情况，并根据召回情况和评分对文本片段进行针对性优化，从而提升召回率和回答的正确率。
   - 原文：在知识库**召回测试**，可对问题进行文本片段的召回测试。
     - 修改建议：在知识库的**召回测试**功能中，可以对问题进行文本片段的召回测试。
   - 原文：将问题输入到**源文本**，点击**测试**，在右侧**召回段落**可见召回的文本片段，片段上有相似度评分。
     - 修改建议：将问题输入到**源文本**框中，点击**测试**按钮，在右侧的**召回段落**区域可见召回的文本片段，每个片段上都有相似度评分。
   - 原文：可点击**检索配置**，打开重排序Rerank。
     - 修改建议：可以点击**检索配置**，启用重排序Rerank功能。
   - 原文：再进行召回测试，会将召回文本片段进行重新Rerank评分并进行重排序，文本片段上的评分为Rerank评分。
     - 修改建议：再次进行召回测试时，系统会重新对召回的文本片段进行Rerank评分并重排序，文本片段上的评分即为Rerank评分。

3. **不符合技术文档规范的内容**
   - 原文：通过召回测试查看针对某问题知识库资料被召回的情况，以及可根据召回情况和评分进行文本片段的针对性优化处理，提升召回及回答正确率。
     - 修改建议：通过召回测试，可以查看针对某一问题的知识库资料被召回的情况，并根据召回情况和评分对文本片段进行针对性优化，从而提升召回率和回答的正确率。
   - 原文：在知识库**召回测试**，可对问题进行文本片段的召回测试。
     - 修改建议：在知识库的**召回测试**功能中，可以对问题进行文本片段的召回测试。
   - 原文：将问题输入到**源文本**，点击**测试**，在右侧**召回段落**可见召回的文本片段，片段上有相似度评分。
     - 修改建议：将问题输入到**源文本**框中，点击**测试**按钮，在右侧的**召回段落**区域可见召回的文本片段，每个片段上都有相似度评分。
   - 原文：可点击**检索配置**，打开重排序Rerank。
     - 修改建议：可以点击**检索配置**，启用重排序Rerank功能。
   - 原文：再进行召回测试，会将召回文本片段进行重新Rerank评分并进行重排序，文本片段上的评分为Rerank评分。
     - 修改建议：再次进行召回测试时，系统会重新对召回的文本片段进行Rerank评分并重排序，文本片段上的评分即为Rerank评分。

4. **中英文标点混用的情况**
   - 原文：在未打开Rerank重排序时，此评分即为召回时计算的相似度评分。
     - 修改建议：在未启用Rerank重排序时，此评分即为召回时计算的相似度评分。
   - 原文：可点击**检索配置**，打开重排序Rerank。
     - 修改建议：可以点击**检索配置**，启用重排序Rerank功能。
   - 原文：再进行召回测试，会将召回文本片段进行重新Rerank评分并进行重排序，文本片段上的评分为Rerank评分。
     - 修改建议：再次进行召回测试时，系统会重新对召回的文本片段进行Rerank评分并重排序，文本片段上的评分即为Rerank评分。

以上是文档的审核结果，希望对您有所帮助。
```

## books/XX平台操作手册/知识库概述/知识库配置/参数设置/参数配置.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现5处英文标点
```
### 语句通顺问题
```markdown
发现1处问题
· ![image-20250123204416448](./assets/image-20250123204416448....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容进行的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - **原文**：点击知识库**设置**，可进行知识库参数的配置调整。
     - **修改建议**：点击知识库**设置**，可以调整知识库参数的配置。
   - **原文**：可调整的配置为：
     - **修改建议**：可调整的配置包括：

3. **不符合技术文档规范的内容**
   - **原文**：检索结果重排开启/关闭
     - **修改建议**：检索结果重排（开启/关闭）
   - **原文**：Score阈值设置
     - **修改建议**：得分阈值设置
   - **原文**：Top K设置
     - **修改建议**：Top K 设置
   - **原文**：具体设置说明详见：[知识库创建](./XX平台操作手册/知识库概述/知识库创建/知识库创建.md)
     - **修改建议**：具体设置说明请参见：[知识库创建](./XX平台操作手册/知识库概述/知识库创建/知识库创建.md)

4. **中英文标点混用的情况**
   - **原文**：检索结果重排开启/关闭
     - **修改建议**：检索结果重排（开启/关闭）
   - **原文**：Score阈值设置
     - **修改建议**：得分阈值设置
   - **原文**：Top K设置
     - **修改建议**：Top K 设置

以上是文档审核的结果，希望对您有所帮助。
```

## books/XX平台操作手册/知识库概述/知识库配置/文档管理/文档管理.md
### Markdown语法问题
```markdown
books/XX平台操作手册/知识库概述/知识库配置/文档管理/文档管理.md:7:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/知识库概述/知识库配置/文档管理/文档管理.md:11:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 2; Style: 1/1/1]
books/XX平台操作手册/知识库概述/知识库配置/文档管理/文档管理.md:13:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/知识库概述/知识库配置/文档管理/文档管理.md:15:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 3; Style: 1/2/3]
books/XX平台操作手册/知识库概述/知识库配置/文档管理/文档管理.md:19:1 MD029/ol-prefix Ordered list item prefix [Expected: 2; Actual: 4; Style: 1/2/3]
books/XX平台操作手册/知识库概述/知识库配置/文档管理/文档管理.md:21:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/知识库概述/知识库配置/文档管理/文档管理.md:23:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/知识库概述/知识库配置/文档管理/文档管理.md:25:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 5; Style: 1/2/3]
books/XX平台操作手册/知识库概述/知识库配置/文档管理/文档管理.md:29:1 MD029/ol-prefix Ordered list item prefix [Expected: 2; Actual: 6; Style: 1/2/3]
books/XX平台操作手册/知识库概述/知识库配置/文档管理/文档管理.md:31:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/知识库概述/知识库配置/文档管理/文档管理.md:33:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 7; Style: 1/1/1]

```
### 英文标点使用
```markdown
发现30处英文标点
```
### 语句通顺问题
```markdown
发现7处问题
· # 文档管理

在知识库的**文档管理**，可对知识库里文档进行管理，包括：

1. **启用/禁用：**

​	点击*...
· ![image-20250123202035859](./assets/image-20250123202035859....
· 3. **重命名**

   点击右侧![image-20250123202316458](./assets/image...
· 4. **调整分段配置，重新索引**

​	点击右侧![image-20250123202525369](./asset...
· 配置详见：[知识库创建](./XX平台操作手册/知识库概述/知识库创建/知识库创建.md)

​	![image-202...
```
### 智能语义审核
```markdown
以下是文档审核结果，按照出现顺序编号，包含原文引用和修改建议：

1. **错别字**
   - 原文：在知识库的**文档管理**，可对知识库里文档进行管理，包括：
   - 修改建议：在知识库的**文档管理**中，可对知识库中的文档进行管理，包括：

2. **语法不通顺的句子**
   - 原文：点击**操作**按钮，可开关文档的启用和禁用。
   - 修改建议：点击**操作**按钮，可以启用或禁用文档。

3. **不符合技术文档规范的内容**
   - 原文：点击**下载**，可下载文档。
   - 修改建议：点击**下载**按钮，可以下载文档。

4. **不符合技术文档规范的内容**
   - 原文：点击右侧![image-20250123202316458](./assets/image-20250123202316458.png)，选择**重命名**，可对文档进行重命名。
   - 修改建议：点击右侧的图标![image-20250123202316458](./assets/image-20250123202316458.png)，选择**重命名**，可以对文档进行重命名。

5. **不符合技术文档规范的内容**
   - 原文：点击右侧![image-20250123202525369](./assets/image-20250123202525369.png)，选择**分段设置**，可重新调整分段配置。
   - 修改建议：点击右侧的图标![image-20250123202525369](./assets/image-20250123202525369.png)，选择**分段设置**，可以重新调整分段配置。

6. **中英文标点混用**
   - 原文：配置详见：[知识库创建](./XX平台操作手册/知识库概述/知识库创建/知识库创建.md)
   - 修改建议：配置详见：[知识库创建](./XX平台操作手册/知识库概述/知识库创建/知识库创建.md)。

7. **不符合技术文档规范的内容**
   - 原文：点击右侧![image-20250123202316458](./assets/image-20250123202316458.png)，选择**归档**，可对文档进行归档，归档的文档不会在检索时召回。
   - 修改建议：点击右侧的图标![image-20250123202316458](./assets/image-20250123202316458.png)，选择**归档**，可以对文档进行归档。归档的文档不会在检索时召回。

8. **不符合技术文档规范的内容**
   - 原文：点击右侧![image-20250123202316458](./assets/image-20250123202316458.png)，选择**删除**，可删除文档。
   - 修改建议：点击右侧的图标![image-20250123202316458](./assets/image-20250123202316458.png)，选择**删除**，可以删除文档。

9. **不符合技术文档规范的内容**
   - 原文：点击**添加文档**，可以添加新文档。
   - 修改建议：点击**添加文档**按钮，可以添加新文档。

10. **中英文标点混用**
    - 原文：![image-20250123203130944](./assets/image-20250123203130944.png)
    - 修改建议：![image-20250123203130944](./assets/image-20250123203130944.png)。

以上是文档审核的详细结果，希望对您有所帮助。
```

## books/XX平台操作手册/开发智能体/开发智能体.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发智能体/开发智能体.md:5 MD036/no-emphasis-as-heading Emphasis used instead of a heading [Context: "编排配置"]
books/XX平台操作手册/开发智能体/开发智能体.md:18 MD036/no-emphasis-as-heading Emphasis used instead of a heading [Context: "友好问答"]
books/XX平台操作手册/开发智能体/开发智能体.md:29 MD036/no-emphasis-as-heading Emphasis used instead of a heading [Context: "智能体运维"]

```
### 语句通顺问题
```markdown
发现5处问题
· | **功能**   | **说明**                                         ...
· 你可以根据不同的问题和应用场景，调试模型参数，直到获得更好的对话效果 |
| 多模型对比 | 多模型对比可让用户一个Pr...
· |
| 编辑变量   | 变量能使提示词中引入用户自行设定的信息                       |
| 工...
· | **功能**                 | **说明**                           ...
· |
| 评估     | 可以在评估中进行批量问题与智能体对话，评估智能体回复的正确率 |
| 监控     | 可在监...
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/开发智能体/智能体运维/智能体运维.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发智能体/智能体运维/智能体运维.md:3 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]
books/XX平台操作手册/开发智能体/智能体运维/智能体运维.md:9 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]
books/XX平台操作手册/开发智能体/智能体运维/智能体运维.md:10 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 3]
books/XX平台操作手册/开发智能体/智能体运维/智能体运维.md:17 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]
books/XX平台操作手册/开发智能体/智能体运维/智能体运维.md:18 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 3]

```
### 英文标点使用
```markdown
发现6处英文标点
```
### 语句通顺问题
```markdown
发现2处问题
· 详情可查看：[AI应用评估](./XX平台操作手册/AI应用评估/AI应用评估.md)



### 智能体监控

可以...
· 详情可查看：[AI应用监控](./XX平台操作手册/AI应用监控/AI应用监控.md)



### 智能体API访问
...
```
### 智能语义审核
```markdown
以下是根据您的要求对文档进行的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - 无明显语法不通顺的句子。

3. **不符合技术文档规范的内容**
   - **原文**：可以通过智能体评估来批量测试智能体的回复效果。
     - **修改建议**：建议改为“通过智能体评估功能，可以批量测试智能体的回复效果。”
   - **原文**：可以通过智能体监控来查看智能体运行的数据。
     - **修改建议**：建议改为“通过智能体监控功能，可以查看智能体运行的数据。”
   - **原文**：详情可查看：[AI应用API访问](./XX平台操作手册/AI应用API访问/AI应用API访问.md)
     - **修改建议**：建议改为“详情请参阅：[AI应用API访问](./XX平台操作手册/AI应用API访问/AI应用API访问.md)”

4. **中英文标点混用的情况**
   - **原文**：详情可查看：[AI应用评估](./XX平台操作手册/AI应用评估/AI应用评估.md)
     - **修改建议**：建议改为“详情可查看：[AI应用评估](./XX平台操作手册/AI应用评估/AI应用评估.md)。”
   - **原文**：详情可查看：[AI应用监控](./XX平台操作手册/AI应用监控/AI应用监控.md)
     - **修改建议**：建议改为“详情可查看：[AI应用监控](./XX平台操作手册/AI应用监控/AI应用监控.md)。”
   - **原文**：详情可查看：[AI应用API访问](./XX平台操作手册/AI应用API访问/AI应用API访问.md)
     - **修改建议**：建议改为“详情请参阅：[AI应用API访问](./XX平台操作手册/AI应用API访问/AI应用API访问.md)。”

以上是文档的审核结果，希望对您有所帮助。
```

## books/XX平台操作手册/开发智能体/智能体编排配置/智能体编排配置.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发智能体/智能体编排配置/智能体编排配置.md:5 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]
books/XX平台操作手册/开发智能体/智能体编排配置/智能体编排配置.md:9:67 MD042/no-empty-links No empty links [Context: "[模型管理]()"]
books/XX平台操作手册/开发智能体/智能体编排配置/智能体编排配置.md:15:8 MD042/no-empty-links No empty links [Context: "[模型参数配置]()"]

```
### 英文标点使用
```markdown
发现57处英文标点
```
### 语句通顺问题
```markdown
发现5处问题
· # 智能体编排配置

在智能体编排配置中可进行一系列设置

### **1.模型选择**

选取合适的模型做为智能体的大...
· 具体可查看：[模型管理]()

![image-20250113174038260-1737454218247-2](....
· 进阶使用详见：[模型参数配置]()

![image-20250113175123240](./assets/image...
· 在输入框输入，可对比多个模型的响应效果

![image-20250114093753532](./assets/ima...
· 关于如何编写提示词，请参考：[提示词编写](./XX平台操作手册/提示词编写/提示词编写.md)

![image-20...
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/XX平台基本介绍/XX平台基本介绍.md
### Markdown语法问题
```markdown
books/XX平台操作手册/XX平台基本介绍/XX平台基本介绍.md:7 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]
books/XX平台操作手册/XX平台基本介绍/XX平台基本介绍.md:19:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/XX平台基本介绍/XX平台基本介绍.md:23:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/XX平台基本介绍/XX平台基本介绍.md:27:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/XX平台基本介绍/XX平台基本介绍.md:29 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]

```
### 英文标点使用
```markdown
发现3处英文标点
```
### 语句通顺问题
```markdown
发现1处问题
· 无论你是否有编程基础，都可以在XX平台上快速搭建基于大模型的各类 AI 应用，并将 AI 应用发布用户使用，也可以通过 ...
```
### 智能语义审核
```markdown
以下是根据您的要求对文档进行的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - **原文**：无论你是否有编程基础，都可以在XX平台上快速搭建基于大模型的各类 AI 应用，并将 AI 应用发布用户使用，也可以通过 API 将 AI 应用集成到你的业务系统中。
     - **修改建议**：无论你是否有编程基础，都可以在XX平台上快速搭建基于大模型的各类 AI 应用，并将这些应用发布给用户使用，也可以通过 API 将 AI 应用集成到你的业务系统中。
   - **原文**：XX平台中搭建的 AI 应用具备完整业务逻辑和可视化用户界面，是一个独立的 AI 项目。
     - **修改建议**：在XX平台中搭建的 AI 应用具备完整的业务逻辑和可视化的用户界面，是一个独立的 AI 项目。
   - **原文**：XX平台的工作流功能可以用来处理逻辑复杂，且有较高稳定性要求的任务流。
     - **修改建议**：XX平台的工作流功能可以用来处理逻辑复杂且有较高稳定性要求的任务流。
   - **原文**：XX平台集成了丰富的工具，极大地拓展智能体的能力边界，你可以直接将这些工具添加到智能体中。
     - **修改建议**：XX平台集成了丰富的工具，极大地拓展了智能体的能力边界，你可以直接将这些工具添加到智能体中。
   - **原文**：XX平台提供了简单易用的知识库功能来管理和存储数据，支持智能体与你自己的数据进行交互。
     - **修改建议**：XX平台提供了简单易用的知识库功能，用于管理和存储数据，支持智能体与你自己的数据进行交互。

3. **不符合技术文档规范的内容**
   - **原文**：智能客服、虚拟女友、个人助理、英语外教都是智能体的典型应用场景。
     - **修改建议**：智能客服、虚拟助手、个人助理、英语教学助手都是智能体的典型应用场景。
   - **原文**：例如创建一个撰写行业研究报告的工作流，让智能体写一份 20 页的报告。
     - **修改建议**：例如，创建一个撰写行业研究报告的工作流，让智能体生成一份 20 页的报告。
   - **原文**：例如使用新闻搜索工具，打造一个可以播报最新时事新闻的 AI 新闻播音员。
     - **修改建议**：例如，使用新闻搜索工具，创建一个可以播报最新时事新闻的 AI 新闻播音员。
   - **原文**：你可以将已有的 API 能力通过参数配置的方式快速创建一个工具让智能体调用。
     - **修改建议**：你可以通过参数配置的方式，将已有的 API 能力快速创建成一个工具，供智能体调用。

4. **中英文标点混用的情况**
   - **原文**：XX平台的工作流功能可以用来处理逻辑复杂，且有较高稳定性要求的任务流。
     - **修改建议**：XX平台的工作流功能可以用来处理逻辑复杂，且有较高稳定性要求的任务流。
   - **原文**：XX平台集成了丰富的工具，极大地拓展智能体的能力边界，你可以直接将这些工具添加到智能体中。
     - **修改建议**：XX平台集成了丰富的工具，极大地拓展了智能体的能力边界，你可以直接将这些工具添加到智能体中。
   - **原文**：XX平台提供了简单易用的知识库功能来管理和存储数据，支持智能体与你自己的数据进行交互。
     - **修改建议**：XX平台提供了简单易用的知识库功能，用于管理和存储数据，支持智能体与你自己的数据进行交互。

以上是文档的审核结果，希望对您有所帮助。
```

## books/XX平台操作手册/AI应用监控/AI应用监控.md
### Markdown语法问题
```markdown
books/XX平台操作手册/AI应用监控/AI应用监控.md:3 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]

```
### 英文标点使用
```markdown
发现18处英文标点
```
### 语句通顺问题
```markdown
发现3处问题
· ![image-20250213135742670](./assets/image-20250213135742670....
· ![image-20250213135904577](./assets/image-20250213135904577....
· ![image-20250213140501184](./assets/image-20250213140501184....
```
### 智能语义审核
```markdown
1. **错别字**
   - 原文：对于AI应用（智能体和AI工作流）XX平台都提供应用监控功能。
     - 错误：XX平台
     - 修改建议：对于AI应用（智能体和AI工作流），平台都提供应用监控功能。
   - 原文：进入到搭建好的智能体，点击上方**监控**，可进入智能体监控界面。
     - 错误：进入到
     - 修改建议：进入搭建好的智能体，点击上方**监控**，可进入智能体监控界面。
   - 原文：进入到搭建好的AI工作流，点击上方**监控**，可进入工作流应用的监控界面。
     - 错误：进入到
     - 修改建议：进入搭建好的AI工作流，点击上方**监控**，可进入工作流应用的监控界面。

2. **语法不通顺的句子**
   - 原文：点击**追踪应用性能**可选择用Langfuse或LangSmith来跟踪应用使用的数据，调试和改进应用。
     - 修改建议：点击**追踪应用性能**，您可以选择使用Langfuse或LangSmith来跟踪应用使用的数据，进行调试和改进。

3. **不符合技术文档规范的内容**
   - 原文：进入到搭建好的智能体，点击上方**监控**，可进入智能体监控界面。
     - 修改建议：进入搭建好的智能体，点击上方的**监控**按钮，可进入智能体监控界面。
   - 原文：进入到搭建好的AI工作流，点击上方**监控**，可进入工作流应用的监控界面。
     - 修改建议：进入搭建好的AI工作流，点击上方的**监控**按钮，可进入工作流应用的监控界面。
   - 原文：点击**追踪应用性能**可选择用Langfuse或LangSmith来跟踪应用使用的数据，调试和改进应用。
     - 修改建议：点击**追踪应用性能**，您可以选择使用Langfuse或LangSmith来跟踪应用使用的数据，进行调试和改进。

4. **中英文标点混用的情况**
   - 原文：对于AI应用（智能体和AI工作流）XX平台都提供应用监控功能。
     - 修改建议：对于AI应用（智能体和AI工作流），平台都提供应用监控功能。
   - 原文：进入到搭建好的智能体，点击上方**监控**，可进入智能体监控界面。
     - 修改建议：进入搭建好的智能体，点击上方的**监控**按钮，可进入智能体监控界面。
   - 原文：进入到搭建好的AI工作流，点击上方**监控**，可进入工作流应用的监控界面。
     - 修改建议：进入搭建好的AI工作流，点击上方的**监控**按钮，可进入工作流应用的监控界面。
   - 原文：点击**追踪应用性能**可选择用Langfuse或LangSmith来跟踪应用使用的数据，调试和改进应用。
     - 修改建议：点击**追踪应用性能**，您可以选择使用Langfuse或LangSmith来跟踪应用使用的数据，进行调试和改进。
```

## books/XX平台操作手册/模型管理/模型管理.md
### Markdown语法问题
```markdown
books/XX平台操作手册/模型管理/模型管理.md:1 MD041/first-line-heading/first-line-h1 First line in a file should be a top-level heading [Context: "- [模型选择与参数配置](./模型选择与参数配置/模型选择..."]

```
### 英文标点使用
```markdown
发现6处英文标点
```
### 语句通顺问题
```markdown
发现1处问题
· - [模型选择与参数配置](./模型选择与参数配置/模型选择与参数配置.md)
- [设置默认模型](./设置默认模型/...
```
### 智能语义审核
```markdown
为了提供更准确的审核，我需要具体的文档内容。请提供上述章节的具体内容，以便我进行详细的检查和标注。
```

## books/XX平台操作手册/模型管理/添加更多模型/添加更多模型.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现20处英文标点
```
### 语句通顺问题
```markdown
发现4处问题
· （XX云添加模型，详情可查看：[快速部署一个开源大语言模型](./XX云操作手册/快速部署一个开源大语言模型/快速部署一...
· ![image-20250210153914051](./assets/image-20250210153914051....
· ![image-20250210154225589](./assets/image-20250210154225589....
· ![image-20250210155825357](./assets/image-20250210155825357....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容进行的审核结果：

1. **错别字**
   - 原文：其中在XX云已经添加了的开源模型，在XX平台会默认已添加。
     - 修改建议：其中在XX云已经添加的开源模型，在XX平台会默认已添加。
   - 原文：如果需要使用其他的未在内置的模型提供商范围之外的在线模型
     - 修改建议：如果需要使用其他未在内置模型提供商范围内的在线模型

2. **语法不通顺的句子**
   - 原文：在XX平台**模型**板块，点击**获取更多模型**，即查看添加的模型，以及添加更多模型。
     - 修改建议：在XX平台的**模型**板块，点击**获取更多模型**，可以查看已添加的模型，并添加更多模型。
   - 原文：点击**XX云-模型广场**下**显示模型**，可查看已经在XX云服务器上传了模型文件的模型。
     - 修改建议：点击**XX云-模型广场**下的**显示模型**，可以查看已在XX云服务器上传模型文件的模型。
   - 原文：其次，XX平台已内置对接了多家模型供应商，在这些模型供应商设置了API Key，即可使用这些供应商提供的在线模型服务。
     - 修改建议：此外，XX平台已内置对接多家模型供应商，设置API Key后，即可使用这些供应商提供的在线模型服务。

3. **不符合技术文档规范的内容**
   - 原文：用户要在XX平台上使用模型，需先在XX平台上添加模型。
     - 修改建议：用户若要在XX平台上使用模型，需先在平台上添加模型。
   - 原文：如果需要使用其他的未在内置的模型提供商范围之外的在线模型，如模型的API接口符合OpenAI规范，则可通过OpenAI-API-compatible进行接口添加。
     - 修改建议：如果需要使用其他未在内置模型提供商范围内的在线模型，且模型的API接口符合OpenAI规范，可通过OpenAI-API-compatible接口进行添加。

4. **中英文标点混用的情况**
   - 原文：XX云添加模型，详情可查看：[快速部署一个开源大语言模型](./XX云操作手册/快速部署一个开源大语言模型/快速部署一个开源大语言模型.md)
     - 修改建议：XX云添加模型，详情可查看：[快速部署一个开源大语言模型](./XX云操作手册/快速部署一个开源大语言模型/快速部署一个开源大语言模型.md)。
   - 原文：如果需要使用其他的未在内置的模型提供商范围之外的在线模型，如模型的API接口符合OpenAI规范，则可通过OpenAI-API-compatible进行接口添加。
     - 修改建议：如果需要使用其他未在内置模型提供商范围内的在线模型，且模型的API接口符合OpenAI规范，则可通过OpenAI-API-compatible接口进行添加。

以上是文档的审核结果，希望对您有所帮助。
```

## books/XX平台操作手册/模型管理/设置默认模型/设置默认模型.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现6处英文标点
```
### 语句通顺问题
```markdown
发现2处问题
· ![image-20250123205433348](./assets/image-20250123205433348....
· ![image-20250123205613954](./assets/image-20250123205613954....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容的审核结果：

1. **错别字**
   - **原文**：在一些场景需要模型能力但未特别指定模型的，会用默认模型进行处理。
     **修改建议**：在一些场景中，当需要模型能力但未特别指定模型时，会使用默认模型进行处理。
   - **原文**：点击左侧**大语言模型**标签，并点击右侧XX云模型广场的模型，即可设置大语言模型的默认模型。
     **修改建议**：点击左侧**大语言模型**标签，并点击右侧“XX云模型广场”中的模型，即可设置大语言模型的默认模型。

2. **语法不通顺的句子**
   - **原文**：在一些场景需要模型能力但未特别指定模型的，会用默认模型进行处理。
     **修改建议**：在一些场景中，当需要模型能力但未特别指定模型时，会使用默认模型进行处理。
   - **原文**：点击**配置**，选择**模型**，可进行模型管理界面。
     **修改建议**：点击**配置**，选择**模型**，即可进入模型管理界面。

3. **不符合技术文档规范的内容**
   - **原文**：比如：知识库文本Q&A模型分段时等。
     **修改建议**：例如，在知识库文本Q&A中进行模型分段时。
   - **原文**：点击**配置**，选择**模型**，可进行模型管理界面。
     **修改建议**：点击**配置**，选择**模型**，即可进入模型管理界面。
   - **原文**：点击左侧**大语言模型**标签，并点击右侧XX云模型广场的模型，即可设置大语言模型的默认模型。
     **修改建议**：点击左侧**大语言模型**标签，并点击右侧“XX云模型广场”中的模型，即可设置大语言模型的默认模型。

4. **中英文标点混用的情况**
   - **原文**：比如：知识库文本Q&A模型分段时等。
     **修改建议**：例如，在知识库文本Q&A中进行模型分段时。
   - **原文**：点击**配置**，选择**模型**，可进行模型管理界面。
     **修改建议**：点击**配置**，选择**模型**，即可进入模型管理界面。
   - **原文**：点击左侧**大语言模型**标签，并点击右侧XX云模型广场的模型，即可设置大语言模型的默认模型。
     **修改建议**：点击左侧**大语言模型**标签，并点击右侧“XX云模型广场”中的模型，即可设置大语言模型的默认模型。

希望以上修改建议对您有所帮助。
```

## books/XX平台操作手册/模型管理/模型选择与参数配置/模型选择与参数配置.md
### Markdown语法问题
```markdown
books/XX平台操作手册/模型管理/模型选择与参数配置/模型选择与参数配置.md:3 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]

```
### 英文标点使用
```markdown
发现15处英文标点
```
### 语句通顺问题
```markdown
发现5处问题
· ![image-20250209161703381](./assets/image-20250209161703381....
· **qwen2.5-32B-instruct**：提供中等的语言理解和推理能力，强于7B但弱于72B，平衡能力与资源占用...
· **qwen2.5-72B-instruct**：提供较强的语言理解和推理能力，占用资源较大...
· 注：智能体和工作流节点的模型选择处，只能选择大语言模型或多模态视觉类模型（如：**Qwen2-VL-7B-Instruc...
· ![image-20250116170415394](./assets/image-20250116170415394....
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/AI应用基础管理/AI应用基础管理.md
### Markdown语法问题
```markdown
books/XX平台操作手册/AI应用基础管理/AI应用基础管理.md:3 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]
books/XX平台操作手册/AI应用基础管理/AI应用基础管理.md:5 MD036/no-emphasis-as-heading Emphasis used instead of a heading [Context: "创建智能体"]
books/XX平台操作手册/AI应用基础管理/AI应用基础管理.md:11 MD036/no-emphasis-as-heading Emphasis used instead of a heading [Context: "创建工作流"]

```
### 英文标点使用
```markdown
发现42处英文标点
```
### 语句通顺问题
```markdown
发现1处问题
· # AI应用基础管理

### 1.AI应用创建

**创建智能体**

在XX平台工作台，点击右上方**新建**按钮，...
```
### 智能语义审核
```markdown
以下是根据您的要求对文档进行的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - 无明显语法不通顺的句子。

3. **不符合技术文档规范的内容**
   - **1.1 创建智能体**
     - 原文：在XX平台工作台，点击右上方**新建**按钮，选择“聊天型”类型，即可创建智能体
     - 修改建议：在XX平台工作台，点击右上方的**新建**按钮，选择“聊天型”类型，即可创建智能体。
   - **2.AI应用导入**
     - 原文：支持从文件和从URL两种方式进行导入
     - 修改建议：支持从文件和URL两种方式进行导入。
   - **5.修改AI应用信息**
     - 原文：1）点击应用卡片上![image-20250115114356562](./assets/image-20250115114356562.png)按钮，选择**编辑信息**，即可修改应用图标、名称、描述
     - 修改建议：1. 点击应用卡片上的![image-20250115114356562](./assets/image-20250115114356562.png)按钮，选择**编辑信息**，即可修改应用的图标、名称和描述。

4. **中英文标点混用的情况**
   - **1.1 创建智能体**
     - 原文：在XX平台工作台，点击右上方**新建**按钮，选择“聊天型”类型，即可创建智能体
     - 修改建议：在XX平台工作台，点击右上方的**新建**按钮，选择“聊天型”类型，即可创建智能体。
   - **2.AI应用导入**
     - 原文：支持从文件和从URL两种方式进行导入
     - 修改建议：支持从文件和URL两种方式进行导入。
   - **5.修改AI应用信息**
     - 原文：1）点击应用卡片上![image-20250115114356562](./assets/image-20250115114356562.png)按钮，选择**编辑信息**，即可修改应用图标、名称、描述
     - 修改建议：1. 点击应用卡片上的![image-20250115114356562](./assets/image-20250115114356562.png)按钮，选择**编辑信息**，即可修改应用的图标、名称和描述。

### 总结
- 文档整体较为规范，但存在少量标点符号使用不当和表述不够严谨的情况。
- 建议统一使用中文标点符号，并确保句子结构完整、逻辑清晰。
- 对于步骤描述，建议使用序号（如1.、2.）而非括号（如1））以保持文档格式的一致性。
```

## books/XX平台操作手册/工具管理/工具管理.md
### Markdown语法问题
```markdown
books/XX平台操作手册/工具管理/工具管理.md:11 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]

```
### 英文标点使用
```markdown
发现6处英文标点
```
### 语句通顺问题
```markdown
发现1处问题
· # 工具管理

XX平台中可以对内置的及自定义工具进行管理

登录XX平台，点击工作台右边**配置**，选择**工具**...
```
### 智能语义审核
```markdown
1. **错别字**
   - 原文: "XX平台中可以对内置的及自定义工具进行管理"
     - 修改建议: "XX平台中可以管理内置的及自定义工具"
   - 原文: "登录XX平台，点击工作台右边**配置**，选择**工具**，进入工具管理界面"
     - 修改建议: 无错别字，但建议将“工作台右边**配置**”改为“工作台右侧的**配置**”以避免歧义。

2. **语法不通顺的句子**
   - 原文: "工具管理页面中，可以查看内置工具和新建自定义工具"
     - 修改建议: "在工具管理页面中，您可以查看内置工具并新建自定义工具"

3. **不符合技术文档规范的内容**
   - 原文: "点击内置工具，可在右侧边栏查看该工具详细信息"
     - 修改建议: "点击内置工具后，您可以在右侧边栏查看该工具的详细信息"

4. **中英文标点混用的情况**
   - 原文: "![image-20250123155556427](./assets/image-20250123155556427.png)"
     - 修改建议: 无中英文标点混用，但建议确保所有图片引用格式一致。
   - 原文: "![image-20250123155913303](./assets/image-20250123155913303.png)"
     - 修改建议: 无中英文标点混用，但建议确保所有图片引用格式一致。

以上是根据您的要求对文档进行的审核和修改建议。希望对您有所帮助。
```

## books/XX平台操作手册/工具管理/工作流工具/工作流工具.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现8处英文标点
```
### 语句通顺问题
```markdown
发现2处问题
· ![image-20250123201150054](./assets/image-20250123201150054....
· ![image-20250123201331236](./assets/image-20250123201331236....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容进行的审核结果：

1. **错别字**
   - **原文**：在**配置**，**工作流**标签中可查看所以已布为工具的工作流。
     - **修改建议**：在**配置**，**工作流**标签中可查看所有已部署为工具的工作流。
   - **原文**：点击具体工作流工具可查看工作流工具详细信息，工具入参，并可以编辑工具入参。
     - **修改建议**：点击具体工作流工具可查看工作流工具的详细信息、工具入参，并可以编辑工具入参。

2. **语法不通顺的句子**
   - **原文**：在**配置**，**工作流**标签中可查看所以已布为工具的工作流。
     - **修改建议**：在**配置**和**工作流**标签中，可以查看所有已部署为工具的工作流。
   - **原文**：点击具体工作流工具可查看工作流工具详细信息，工具入参，并可以编辑工具入参。
     - **修改建议**：点击具体工作流工具，可以查看该工具的详细信息和入参，并可以编辑这些入参。

3. **不符合技术文档规范的内容**
   - **原文**：在**配置**，**工作流**标签中可查看所以已布为工具的工作流。
     - **修改建议**：在**配置**和**工作流**标签中，可以查看所有已部署为工具的工作流。
   - **原文**：点击具体工作流工具可查看工作流工具详细信息，工具入参，并可以编辑工具入参。
     - **修改建议**：点击具体工作流工具，可以查看该工具的详细信息和入参，并可以编辑这些入参。
   - **原文**：编辑工具入参详见：[工具流发布为工具](./XX平台操作手册/开发工作流/工作流发布/工作流发布为工具/工作流发布为工具.md)
     - **修改建议**：编辑工具入参的详细步骤，请参阅：[工具流发布为工具](./XX平台操作手册/开发工作流/工作流发布/工作流发布为工具/工作流发布为工具.md)

4. **中英文标点混用的情况**
   - **原文**：在**配置**，**工作流**标签中可查看所以已布为工具的工作流。
     - **修改建议**：在**配置**和**工作流**标签中，可以查看所有已部署为工具的工作流。
   - **原文**：点击具体工作流工具可查看工作流工具详细信息，工具入参，并可以编辑工具入参。
     - **修改建议**：点击具体工作流工具，可以查看该工具的详细信息和入参，并可以编辑这些入参。
   - **原文**：编辑工具入参详见：[工具流发布为工具](./XX平台操作手册/开发工作流/工作流发布/工作流发布为工具/工作流发布为工具.md)
     - **修改建议**：编辑工具入参的详细步骤，请参阅：[工具流发布为工具](./XX平台操作手册/开发工作流/工作流发布/工作流发布为工具/工作流发布为工具.md)

以上是文档的审核结果，希望对您有所帮助。
```

## books/XX平台操作手册/工具管理/自定义工具/自定义工具.md
### Markdown语法问题
```markdown
books/XX平台操作手册/工具管理/自定义工具/自定义工具.md:19 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]
books/XX平台操作手册/工具管理/自定义工具/自定义工具.md:20 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 3]

```
### 英文标点使用
```markdown
发现10处英文标点
```
### 语句通顺问题
```markdown
发现2处问题
· ![image-20250123173521652](./assets/image-20250123173521652....
· ![image-20250123173643439](./assets/image-20250123173643439....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档进行的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - **原文**: "在Schema区域按例子中的模板编辑，完成后在**可用工具**中会出现此工具。"
     - **修改建议**: "在Schema区域按照示例模板进行编辑，完成后，此工具将出现在**可用工具**列表中。"
   - **原文**: "例子中选择空白模板，在相应位置填入对应内容。"
     - **修改建议**: "例如，选择空白模板，并在相应位置填入对应内容。"

3. **不符合技术文档规范的内容**
   - **原文**: "title: 工具的名称。在智能体中会作为模型判断是否调用工具的参考之一。"
     - **修改建议**: "title: 工具的名称。此名称将作为智能体模型判断是否调用该工具的参考之一。"
   - **原文**: "description：工具的描述。在智能体中会作为模型判断是否调用工具的首要参考。"
     - **修改建议**: "description: 工具的描述。此描述将作为智能体模型判断是否调用该工具的首要参考。"
   - **原文**: "url：工具的API访问地址。"
     - **修改建议**: "url: 工具的API访问地址。"

4. **中英文标点混用的情况**
   - **原文**: "description：工具的描述。"
     - **修改建议**: "description: 工具的描述。"
   - **原文**: "url：工具的API访问地址。"
     - **修改建议**: "url: 工具的API访问地址。"

以上是文档审核的详细结果，希望对您有所帮助。
```

## books/XX平台操作手册/开发工作流/开发工作流.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发工作流/开发工作流.md:7 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]

```
### 英文标点使用
```markdown
发现3处英文标点
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/开发工作流/工作流引入工具/工作流引入工具.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发工作流/工作流引入工具/工作流引入工具.md:37 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]

```
### 英文标点使用
```markdown
发现10处英文标点
```
### 语句通顺问题
```markdown
发现3处问题
· ![image-20250116134313075](./assets/image-20250116134313075....
· - 自定义工具

  用户可自定义需要的工具，添加自定义工具操作详见：[自定义工具](./XX平台操作手册/工具管理/自...
· 工作流发布为工具详见：[工作流工具](./XX平台操作手册/工具管理/工作流工具/工作流工具.md)

选择了具体工具后...
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容进行的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - **原文**：工具节点的输出变量统一设置了三个变量，每个工具会按各自输出数据的类型，在相应的输出变量里输出
     - **修改建议**：工具节点的输出变量统一设置为三个，每个工具将根据其输出数据的类型，在相应的输出变量中输出数据。

3. **不符合技术文档规范的内容**
   - **原文**：工作流发布为工具详见：[工作流工具](./XX平台操作手册/工具管理/工作流工具/工作流工具.md)
     - **修改建议**：有关将工作流发布为工具的详细信息，请参阅：[工作流工具](./XX平台操作手册/工具管理/工作流工具/工作流工具.md)。
   - **原文**：选择了具体工具后，可根据各工具的需要设置输入变量
     - **修改建议**：选择具体工具后，根据各工具的需求设置输入变量。

4. **中英文标点混用的情况**
   - **原文**：text（String类型）：输出工具生成的内容，以字符串类型输出
     - **修改建议**：text（String类型）：输出工具生成的内容，以字符串类型输出。
   - **原文**：files（Array[File]类型）：输出工具生成的文件 ，以文件列表形式输出
     - **修改建议**：files（Array[File]类型）：输出工具生成的文件，以文件列表形式输出。
   - **原文**：json（Array[Object]类型）：输出工具生成的json
     - **修改建议**：json（Array[Object]类型）：输出工具生成的JSON。

以上是文档审核的结果，希望对您有所帮助。
```

## books/XX平台操作手册/开发工作流/工作流画布功能/画布小工具/画布小工具.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发工作流/工作流画布功能/画布小工具/画布小工具.md:7 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]

```
### 英文标点使用
```markdown
发现27处英文标点
```
### 语句通顺问题
```markdown
发现5处问题
· ![image-20250116105411845](./assets/image-20250116105411845....
· ![image-20250116110231684](./assets/image-20250116110231684....
· ![image-20250116110746477](./assets/image-20250116110746477....
· ![image-20250116111049885](./assets/image-20250116111049885....
· ![1736997862224](./assets/1736997862224.png)

![image-202501...
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/开发工作流/工作流画布功能/定时触发/定时触发.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现12处英文标点
```
### 语句通顺问题
```markdown
发现1处问题
· ![image-20250116103513002](./assets/image-20250116103513002....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容进行的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - 无明显语法不通顺的句子。

3. **不符合技术文档规范的内容**
   - **原文**：工作流可以设置定时触发。
     - **修改建议**：建议改为“可以设置工作流的定时触发。”以确保主语明确。
   - **原文**：点击画布右上角的**触发器**按钮，可以设置触发器。
     - **修改建议**：建议改为“点击画布右上角的**触发器**按钮，可以设置触发器选项。”以明确“设置触发器”的具体内容。
   - **原文**：点击**启用**按钮，启用触发器。
     - **修改建议**：建议改为“点击**启用**按钮，以启用触发器。”以确保句子结构更加规范。

4. **中英文标点混用的情况**
   - **原文**：![image-20250116103346305](./assets/image-20250116103346305.png)
     - **修改建议**：图片说明中使用英文标点是正确的，无需修改。
   - **原文**：![image-20250116103422821](./assets/image-20250116103422821.png)
     - **修改建议**：图片说明中使用英文标点是正确的，无需修改。
   - **原文**：![image-20250116103513002](./assets/image-20250116103513002.png)
     - **修改建议**：图片说明中使用英文标点是正确的，无需修改。
   - **原文**：![image-20250116103726646](./assets/image-20250116103726646.png)
     - **修改建议**：图片说明中使用英文标点是正确的，无需修改。

总结：
- 文档整体较为规范，没有明显的错别字和语法错误。
- 建议对部分句子进行结构调整，以确保文档的专业性和清晰度。
- 图片说明中的标点使用正确，无需修改。
```

## books/XX平台操作手册/开发工作流/工作流画布功能/运行历史/运行历史.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现9处英文标点
```
### 绝对路径图片
```markdown
![image-20250116103931564](C:/Users/xxxx/AppData/Roaming/Typora/typora-user-images/image-20250116103931564.png)
```
### 语句通顺问题
```markdown
发现2处问题
· 点击画布右上角![image-20250116103931564](C:/Users/xxxx/AppData/Roam...
· ![image-20250116104030486](./assets/image-20250116104030486....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - **原文**: "工作流运行历史中可查看工作流后台调试的运行记录。"
     - **问题**: 句子结构较为冗长，可以简化。
     - **建议**: "在工作流运行历史中，可以查看后台调试的运行记录。"

3. **不符合技术文档规范的内容**
   - **原文**: "点击画布右上角![image-20250116103931564](C:/Users/xxxx/AppData/Roaming/Typora/typora-user-images/image-20250116103931564.png)图标，选择运行历史，即可查看过往运行的记录。"
     - **问题**: 图片路径为本地路径，不符合技术文档规范，应使用相对路径或在线链接。
     - **建议**: "点击画布右上角的图标，选择运行历史，即可查看过往运行的记录。"（假设图片已上传至文档的 assets 文件夹）
   - **原文**: "即可查看过往运行的记录。"
     - **问题**: "过往"一词在技术文档中不够正式。
     - **建议**: "即可查看之前的运行记录。"

4. **中英文标点混用的情况**
   - **原文**: "点击画布右上角![image-20250116103931564](C:/Users/xxxx/AppData/Roaming/Typora/typora-user-images/image-20250116103931564.png)图标，选择运行历史，即可查看过往运行的记录。"
     - **问题**: 图片路径中的英文标点与中文标点混用。
     - **建议**: 无需修改，但建议统一使用英文标点。

综合以上建议，修改后的文档内容如下：

```markdown
# 运行历史

在工作流运行历史中，可以查看后台调试的运行记录。

点击画布右上角的图标，选择运行历史，即可查看之前的运行记录。

![image-20250116104030486](./assets/image-20250116104030486.png)

![image-20250116104116802](./assets/image-20250116104116802.png)
```
```

## books/XX平台操作手册/开发工作流/工作流画布功能/检查清单/检查清单.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现3处英文标点
```
### 智能语义审核
```markdown
```markdown
1. **错别字**
   - 原文: "检查清单功能，系统会自动将工作流中配置缺失的问题预警提示出来，帮助开发者快速找到工作流配置问题。"
   - 修改建议: "检查清单功能，系统会自动将工作流中配置缺失的问题预警提示出来，帮助开发者快速发现工作流配置问题。"（"找到"改为"发现"，更符合语境）

2. **语法不通顺的句子**
   - 原文: "检查清单功能，系统会自动将工作流中配置缺失的问题预警提示出来，帮助开发者快速找到工作流配置问题。"
   - 修改建议: "检查清单功能，系统会自动提示工作流中配置缺失的问题，帮助开发者快速发现工作流配置问题。"（调整句子结构，使主谓宾更加清晰）

3. **不符合技术文档规范的内容**
   - 原文: "检查清单功能，系统会自动将工作流中配置缺失的问题预警提示出来，帮助开发者快速找到工作流配置问题。"
   - 修改建议: "检查清单功能，系统会自动提示工作流中配置缺失的问题，帮助开发者快速发现并解决工作流配置问题。"（增加“解决”，使表达更加明确）

4. **中英文标点混用**
   - 原文: "检查清单功能，系统会自动将工作流中配置缺失的问题预警提示出来，帮助开发者快速找到工作流配置问题。"
   - 修改建议: "检查清单功能，系统会自动提示工作流中配置缺失的问题，帮助开发者快速发现并解决工作流配置问题。"（原文中未发现中英文标点混用，但建议统一使用中文标点）

5. **图片引用**
   - 原文: "![image-20250116104556341](./assets/image-20250116104556341.png)"
   - 修改建议: "![检查清单示例](./assets/image-20250116104556341.png)"（图片说明应具体，避免使用默认名称）
```

以上是根据您的要求对文档进行的检查和修改建议。希望对您有所帮助！
```

## books/XX平台操作手册/开发工作流/工作流画布功能/环境变量/环境变量.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发工作流/工作流画布功能/环境变量/环境变量.md:19 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]

```
### 英文标点使用
```markdown
发现10处英文标点
```
### 语句通顺问题
```markdown
发现3处问题
· 点击画布右上方**.env环境变量**按钮，可添加环境变量...
· ![image-20250116101027703](./assets/image-20250116101027703....
· ![image-20250116101240988](./assets/image-20250116101240988....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - **原文**: "工作流中可以设置环境变量，环境变量可以在工作流任意可引用变量的节点进行引用。"
     - **修改建议**: "在工作流中可以设置环境变量，这些环境变量可以在工作流中任意可引用变量的节点中使用。"
   - **原文**: "可设置私密信息的环境变量，如密钥等。在导出工作流时会进行询问私密环境变量是否要导出。"
     - **修改建议**: "可以设置包含私密信息的环境变量，例如密钥等。在导出工作流时，系统会询问是否导出私密环境变量。"
   - **原文**: "点击画布右上方**.env环境变量**按钮，可添加环境变量。"
     - **修改建议**: "点击画布右上方的**.env环境变量**按钮，可以添加环境变量。"
   - **原文**: "点击**添加环境变量**可进行环境变量添加。环境变量类型分为String、Number、Secret三种，Secret类型为私密信息。"
     - **修改建议**: "点击**添加环境变量**按钮，可以添加环境变量。环境变量类型包括String、Number和Secret三种，其中Secret类型用于存储私密信息。"
   - **原文**: "环境变量可作为节点的输入使用，也可被引用至模型节点提示词中。"
     - **修改建议**: "环境变量可以作为节点的输入使用，也可以被引用到模型节点的提示词中。"

3. **不符合技术文档规范的内容**
   - **原文**: "点击画布右上方**.env环境变量**按钮，可添加环境变量。"
     - **修改建议**: "点击画布右上方的**.env环境变量**按钮，可以添加环境变量。"（避免口语化表达）
   - **原文**: "点击**添加环境变量**可进行环境变量添加。"
     - **修改建议**: "点击**添加环境变量**按钮，可以添加环境变量。"（避免口语化表达）

4. **中英文标点混用的情况**
   - **原文**: "环境变量类型分为String、Number、Secret三种，Secret类型为私密信息。"
     - **修改建议**: "环境变量类型包括String、Number和Secret三种，其中Secret类型用于存储私密信息。"（将英文逗号统一为中文逗号）
   - **原文**: "环境变量可作为节点的输入使用，也可被引用至模型节点提示词中。"
     - **修改建议**: "环境变量可以作为节点的输入使用，也可以被引用到模型节点的提示词中。"（将英文逗号统一为中文逗号）

希望以上修改建议对您有所帮助。
```

## books/XX平台操作手册/开发工作流/工作流节点/开始节点和结束节点/开始和结束节点.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发工作流/工作流节点/开始节点和结束节点/开始和结束节点.md:5 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]

```
### 英文标点使用
```markdown
发现22处英文标点
```
### 绝对路径图片
```markdown
![image-20250114144649461](C:/Users/xxxx/AppData/Roaming/Typora/typora-user-images/image-20250114144649461.png)
![image-20250115112501599](C:/Users/xxxx/AppData/Roaming/Typora/typora-user-images/image-20250115112501599.png)
```
### 语句通顺问题
```markdown
发现6处问题
· 开始节点有4个默认参数sys.user_id，sys.app_id，sys.workflow_id，sys.workfl...
· ![image-20250114144251526](./assets/image-20250114144251526....
· ![image-20250114144524923](./assets/image-20250114144524923....
· 并且以英文字符开头
- **显示名称：**显示名称默认与变量名称相同，可进行修改，是变量在工作流应用前台显示的名称
- ...
· ![image-20250115112146749](./assets/image-20250115112146749....
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/开发工作流/工作流节点/条件分支节点/条件分支节点.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现6处英文标点
```
### 语句通顺问题
```markdown
发现1处问题
· ![image-20250117140148135](./assets/image-20250117140148135....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容进行的严格检查结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - **原文**：可点击**+ELIF**来添加条件组，不同条件组之间为or的关系。
     - **修改建议**：可点击**+ELIF**来添加条件组，不同条件组之间为“或”关系。
   - **原文**：在条件组内点击**添加条件**，可在条件组内增加条件，并可设置条件是AND还是OR关系。
     - **修改建议**：在条件组内点击**添加条件**，可在条件组内增加条件，并可设置条件之间的关系为“与”（AND）或“或”（OR）。

3. **不符合技术文档规范的内容**
   - **原文**：条件分支节点可以让用户设定不同的条件，按满足的条件走不同的分支流程。
     - **修改建议**：条件分支节点允许用户设定不同的条件，根据满足的条件执行不同的分支流程。
   - **原文**：可点击**+ELIF**来添加条件组，不同条件组之间为or的关系。
     - **修改建议**：用户可以点击**+ELIF**来添加条件组，不同条件组之间为“或”关系。
   - **原文**：在条件组内点击**添加条件**，可在条件组内增加条件，并可设置条件是AND还是OR关系。
     - **修改建议**：在条件组内点击**添加条件**，可在条件组内增加条件，并可设置条件之间的关系为“与”（AND）或“或”（OR）。

4. **中英文标点混用的情况**
   - **原文**：不同条件组之间为or的关系。
     - **修改建议**：不同条件组之间为“或”关系。
   - **原文**：在条件组内点击**添加条件**，可在条件组内增加条件，并可设置条件是AND还是OR关系。
     - **修改建议**：在条件组内点击**添加条件**，可在条件组内增加条件，并可设置条件之间的关系为“与”（AND）或“或”（OR）。

以上是文档的检查结果，希望对您有所帮助。
```

## books/XX平台操作手册/开发工作流/工作流节点/代码节点/代码节点.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现12处英文标点
```
### 语句通顺问题
```markdown
发现4处问题
· ![image-20250207101654218](./assets/image-20250207101654218....
· ![image-20250207101746726](./assets/image-20250207101746726....
· ![image-20250207101939583](./assets/image-20250207101939583....
· ![image-20250207102211174](./assets/image-20250207102211174....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - **原文**：“即可将对应键值在输出变量中输出。”
     - **问题**：句子结构不完整，缺少主语。
     - **建议修改**：“即可将对应的键值输出到输出变量中。”

3. **不符合技术文档规范的内容**
   - **原文**：“代码中main函数的入参名称需与输入变量的名称一致。”
     - **问题**：表达不够明确，建议增加具体操作步骤或示例。
     - **建议修改**：“在代码中，`main`函数的参数名称必须与输入变量的名称一致。例如，如果输入变量名为`input_var`，则`main`函数的参数也应命名为`input_var`。”
   - **原文**：“代码main函数的return一个字典，需要把字典的键名设置到输出变量中，确保名称一致，并且输出变量的类型保持与键值类型一致。”
     - **问题**：句子较长，信息量大，建议拆分。
     - **建议修改**：“`main`函数应返回一个字典。字典的键名需要与输出变量的名称一致，并且输出变量的类型应与字典键值的类型一致。”

4. **中英文标点混用的情况**
   - **原文**：“代码中main函数的入参名称需与输入变量的名称一致。”
     - **问题**：句末使用了中文句号，但建议在代码相关的句子中使用英文句号。
     - **建议修改**：“代码中main函数的入参名称需与输入变量的名称一致.”
   - **原文**：“代码main函数的return一个字典，需要把字典的键名设置到输出变量中，确保名称一致，并且输出变量的类型保持与键值类型一致。”
     - **问题**：句末使用了中文句号，但建议在代码相关的句子中使用英文句号。
     - **建议修改**：“代码main函数的return一个字典，需要把字典的键名设置到输出变量中，确保名称一致，并且输出变量的类型保持与键值类型一致.”

总结：
- 无明显错别字。
- 有部分句子结构不完整或表达不够明确，建议修改。
- 代码相关的句子建议使用英文标点。
```

## books/XX平台操作手册/开发工作流/工作流节点/变量聚合器节点/变量聚合器节点.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发工作流/工作流节点/变量聚合器节点/变量聚合器节点.md:3 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]
books/XX平台操作手册/开发工作流/工作流节点/变量聚合器节点/变量聚合器节点.md:15 MD036/no-emphasis-as-heading Emphasis used instead of a heading [Context: "问题分类后的多分支聚合"]
books/XX平台操作手册/开发工作流/工作流节点/变量聚合器节点/变量聚合器节点.md:39 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]
books/XX平台操作手册/开发工作流/工作流节点/变量聚合器节点/变量聚合器节点.md:40 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 3]
books/XX平台操作手册/开发工作流/工作流节点/变量聚合器节点/变量聚合器节点.md:41 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 4]
books/XX平台操作手册/开发工作流/工作流节点/变量聚合器节点/变量聚合器节点.md:42 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 5]
books/XX平台操作手册/开发工作流/工作流节点/变量聚合器节点/变量聚合器节点.md:43 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 6]
books/XX平台操作手册/开发工作流/工作流节点/变量聚合器节点/变量聚合器节点.md:44 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 7]
books/XX平台操作手册/开发工作流/工作流节点/变量聚合器节点/变量聚合器节点.md:45 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 8]
books/XX平台操作手册/开发工作流/工作流节点/变量聚合器节点/变量聚合器节点.md:46 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 9]
books/XX平台操作手册/开发工作流/工作流节点/变量聚合器节点/变量聚合器节点.md:47 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 10]
books/XX平台操作手册/开发工作流/工作流节点/变量聚合器节点/变量聚合器节点.md:48 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 11]
books/XX平台操作手册/开发工作流/工作流节点/变量聚合器节点/变量聚合器节点.md:49 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 12]

```
### 英文标点使用
```markdown
发现11处英文标点
```
### 语句通顺问题
```markdown
发现3处问题
· ![image-20250209183323724](./assets/image-20250209183323724....
· ![image-20250207121929594](./assets/image-20250207121929594....
· 如下图示例：

变量聚合器将4个分支（模型1，模型2，模型3，模型4）的输出变量，按（模型1、模型2）一组，（模型3、模...
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/开发工作流/工作流节点/迭代节点/迭代节点.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现6处英文标点
```
### 语句通顺问题
```markdown
发现1处问题
· ![image-20250207100558438](./assets/image-20250207100558438....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - **原文**: "迭代节点可实现循环遍历，对于输入的数组的每个元素，执行循环体内部的工作流节点。"
     - **修改建议**: "迭代节点可实现循环遍历，对输入数组的每个元素执行循环体内部的工作流节点。"
   - **原文**: "并且将循环体中节点的输出设置到输出变量中，节点会将每次循环的输出自动加入到输出变量数组中。"
     - **修改建议**: "并且将循环体中节点的输出设置到输出变量中，节点会自动将每次循环的输出添加到输出变量数组中。"

3. **不符合技术文档规范的内容**
   - **原文**: "并且将循环体中节点的输出设置到输出变量中，节点会将每次循环的输出自动加入到输出变量数组中。"
     - **修改建议**: "将循环体中节点的输出设置到输出变量中，节点会自动将每次循环的输出添加到输出变量数组中。"（去掉了“并且”，使句子更加简洁明了）
   - **原文**: "使用迭代节点时，输入变量需要是数组。"
     - **修改建议**: "使用迭代节点时，输入变量必须是数组。"（“需要”改为“必须”，表达更加明确）

4. **中英文标点混用的情况**
   - **原文**: "迭代节点可实现循环遍历，对于输入的数组的每个元素，执行循环体内部的工作流节点。"
     - **修改建议**: "迭代节点可实现循环遍历，对输入数组的每个元素执行循环体内部的工作流节点。"（无中英文标点混用问题）
   - **原文**: "并且将循环体中节点的输出设置到输出变量中，节点会将每次循环的输出自动加入到输出变量数组中。"
     - **修改建议**: "并且将循环体中节点的输出设置到输出变量中，节点会自动将每次循环的输出添加到输出变量数组中。"（无中英文标点混用问题）

总结：
- 文档中的错别字较少，语法和表达方面有少量需要改进的地方。
- 建议按照上述修改建议进行调整，以提高文档的专业性和可读性。
```

## books/XX平台操作手册/开发工作流/工作流节点/知识库节点/知识库节点.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现10处英文标点
```
### 语句通顺问题
```markdown
发现3处问题
· 关于知识库的创建和配置，可查看：[知识库创建](./XX平台操作手册/知识库概述/知识库创建/知识库创建.md)

点击...
· ![image-20250116171427651](./assets/image-20250116171427651....
· ![image-20250116171617462](./assets/image-20250116171617462....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容的审核结果：

1. **错别字**
   - **原文**：关于知识库的创建和配置，可查看：[知识库创建](./XX平台操作手册/知识库概述/知识库创建/知识库创建.md)
     - **修改建议**：无错别字，但“XX平台”可能是特定名称，建议确认是否正确。
   - **原文**：适合多知识库区分较大且知识库数量较少的应用
     - **修改建议**：无错别字，但“区分”建议改为“差异”以更准确表达意思。

2. **语法不通顺的句子**
   - **原文**：点击 **+** 添加知识库。
     - **修改建议**：点击 **+** 按钮添加知识库。
   - **原文**：点击**召回设置**进行设置召回的方式。
     - **修改建议**：点击**召回设置**以设置召回方式。
   - **原文**：添加了多个知识库时，由大模型根据用户意图和知识库的描述，自主判断选择最匹配的知识库进行检索，适合多知识库区分较大且知识库数量较少的应用
     - **修改建议**：当添加了多个知识库时，大模型将根据用户意图和知识库的描述，自主判断并选择最匹配的知识库进行检索。此方式适用于知识库之间差异较大且知识库数量较少的应用。
   - **原文**：同时在所有知识库进行检索，并进行重排序。
     - **修改建议**：同时在所有知识库中进行检索，并进行重排序。
   - **原文**：使用此方式需要选择Rerank模型，并且要在XX云上启动rerank模型
     - **修改建议**：使用此方式时，需要选择Rerank模型，并在XX云上启动rerank模型。

3. **不符合技术文档规范的内容**
   - **原文**：点击 **+** 添加知识库。
     - **修改建议**：点击 **+** 按钮添加知识库。
   - **原文**：点击**召回设置**进行设置召回的方式。
     - **修改建议**：点击**召回设置**以设置召回方式。
   - **原文**：适合多知识库区分较大且知识库数量较少的应用
     - **修改建议**：此方式适用于知识库之间差异较大且知识库数量较少的应用。
   - **原文**：同时在所有知识库进行检索，并进行重排序。
     - **修改建议**：同时在所有知识库中进行检索，并进行重排序。
   - **原文**：使用此方式需要选择Rerank模型，并且要在XX云上启动rerank模型
     - **修改建议**：使用此方式时，需要选择Rerank模型，并在XX云上启动rerank模型。

4. **中英文标点混用的情况**
   - **原文**：关于知识库的创建和配置，可查看：[知识库创建](./XX平台操作手册/知识库概述/知识库创建/知识库创建.md)
     - **修改建议**：关于知识库的创建和配置，可查看：[知识库创建](./XX平台操作手册/知识库概述/知识库创建/知识库创建.md)（保持原样，链接中的斜杠是标准格式）
   - **原文**：1.N选1召回
     - **修改建议**：1. N选1召回
   - **原文**：2.多路召回
     - **修改建议**：2. 多路召回

希望这些修改建议能帮助您改进文档的质量。如果有任何进一步的问题或需要更多帮助，请随时告知。
```

## books/XX平台操作手册/开发工作流/工作流节点/变量赋值节点/变量赋值节点.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发工作流/工作流节点/变量赋值节点/变量赋值节点.md:3 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]
books/XX平台操作手册/开发工作流/工作流节点/变量赋值节点/变量赋值节点.md:16:4 MD037/no-space-in-emphasis Spaces inside emphasis markers [Context: "景 **"]
books/XX平台操作手册/开发工作流/工作流节点/变量赋值节点/变量赋值节点.md:44:46 MD009/no-trailing-spaces Trailing spaces [Expected: 0 or 2; Actual: 1]
books/XX平台操作手册/开发工作流/工作流节点/变量赋值节点/变量赋值节点.md:48:46 MD009/no-trailing-spaces Trailing spaces [Expected: 0 or 2; Actual: 1]
books/XX平台操作手册/开发工作流/工作流节点/变量赋值节点/变量赋值节点.md:54 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]

```
### 英文标点使用
```markdown
发现10处英文标点
```
### 语句通顺问题
```markdown
发现8处问题
· # 变量赋值节点

### 定义

变量赋值器节点用于给**可写变量**赋值，目前支持的可写变量包括：

- 开始节点用...
· 例如：在聊天之前，用户在`language_input输入框中指定了“英语”，这个语言将会被写入到language变量中...
· ![image-20250209190753481](./assets/image-20250209190753481....
· **变量写入/赋值**：在第一轮聊天开始时，如果`language_input`变量为空，则使用 LLM 节点提取用户的...
· ### **指定变量的操作模式**

目标变量的数据类型决定了其操作方式，不同变量类型的操作方式如下：

1. 目标变量...
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/开发工作流/工作流节点/等待用户输入节点/等待用户输入节点.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发工作流/工作流节点/等待用户输入节点/等待用户输入节点.md:7 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]
books/XX平台操作手册/开发工作流/工作流节点/等待用户输入节点/等待用户输入节点.md:21 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]

```
### 英文标点使用
```markdown
发现9处英文标点
```
### 语句通顺问题
```markdown
发现2处问题
· ![image-20250209204217389](./assets/image-20250209204217389....
· ![image-20250209205722667](./assets/image-20250209205722667....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - **原文**：在**向用户展示**添加用户输入时看到的变量信息（可选）。
     - **修改建议**：在**向用户展示**部分，添加用户输入时可见的变量信息（可选）。
   - **原文**：配置了等待用户输入节点后，工作流运行到该节点时，会出现让用户输入的输入框，用户输入后再往下执行。
     - **修改建议**：配置了等待用户输入节点后，当工作流运行到该节点时，会显示一个让用户输入的输入框，用户输入后流程继续执行。

3. **不符合技术文档规范的内容**
   - **原文**：如需在工作流过程中，让用户输入一些额外信息，可以使用等待用户输入节点来实现。
     - **修改建议**：如果需要在工作流过程中让用户输入额外信息，可以使用“等待用户输入”节点来实现。
   - **原文**：在**向用户展示**添加用户输入时看到的变量信息（可选）。
     - **修改建议**：在“向用户展示”部分，添加用户输入时可见的变量信息（可选）。
   - **原文**：在**需要用户输入**设置让用户输入的字段，可设置是否必填。
     - **修改建议**：在“需要用户输入”部分，设置用户需要输入的字段，并可指定是否为必填项。
   - **原文**：配置了等待用户输入节点后，工作流运行到该节点时，会出现让用户输入的输入框，用户输入后再往下执行。
     - **修改建议**：配置了等待用户输入节点后，当工作流运行到该节点时，会显示一个让用户输入的输入框，用户输入后流程继续执行。

4. **中英文标点混用的情况**
   - **原文**：如需在工作流过程中，让用户输入一些额外信息，可以使用等待用户输入节点来实现。
     - **修改建议**：如需在工作流过程中，让用户输入一些额外信息，可以使用等待用户输入节点来实现。
   - **原文**：在**向用户展示**添加用户输入时看到的变量信息（可选）。
     - **修改建议**：在“向用户展示”部分，添加用户输入时可见的变量信息（可选）。
   - **原文**：在**需要用户输入**设置让用户输入的字段，可设置是否必填。
     - **修改建议**：在“需要用户输入”部分，设置用户需要输入的字段，并可指定是否为必填项。
   - **原文**：配置了等待用户输入节点后，工作流运行到该节点时，会出现让用户输入的输入框，用户输入后再往下执行。
     - **修改建议**：配置了等待用户输入节点后，当工作流运行到该节点时，会显示一个让用户输入的输入框，用户输入后流程继续执行。

以上是文档的审核结果，希望对您有所帮助。
```

## books/XX平台操作手册/开发工作流/工作流节点/通过模型分类节点/通过模型分类节点.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现5处英文标点
```
### 语句通顺问题
```markdown
发现2处问题
· 2.在分类中填写分类选项，大模型识别了相应分类后，会走该分类对应的后续节点流程...
· ![image-20250117135500139](./assets/image-20250117135500139....
```
### 智能语义审核
```markdown
1. **错别字**
   - 原文：无明显错别字。

2. **语法不通顺的句子**
   - 原文：通过模型分类节点可使用大语言模型对用户的输入进行分类，多用于用户意图识别的场景。
     - 修改建议：通过模型分类节点，可以使用大语言模型对用户的输入进行分类，主要用于用户意图识别的场景。
   - 原文：使用时先选择大语言模型。
     - 修改建议：使用时，请先选择大语言模型。
   - 原文：在分类中填写分类选项，大模型识别了相应分类后，会走该分类对应的后续节点流程。
     - 修改建议：在分类中填写分类选项，大模型识别相应分类后，将执行该分类对应的后续节点流程。

3. **不符合技术文档规范的内容**
   - 原文：使用时先选择大语言模型。
     - 修改建议：使用时，请先选择大语言模型。
   - 原文：在分类中填写分类选项，大模型识别了相应分类后，会走该分类对应的后续节点流程。
     - 修改建议：在分类中填写分类选项，大模型识别相应分类后，将执行该分类对应的后续节点流程。
   - 原文：开启**视觉**使用多模态模型对输入的图片进行识别分类。
     - 修改建议：开启**视觉**模式，使用多模态模型对输入的图片进行识别分类。

4. **中英文标点混用的情况**
   - 原文：无明显中英文标点混用的情况。
```

## books/XX平台操作手册/开发工作流/工作流节点/模板转换节点/模板转换节点.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发工作流/工作流节点/模板转换节点/模板转换节点.md:41:5 MD033/no-inline-html Inline HTML [Element: li]
books/XX平台操作手册/开发工作流/工作流节点/模板转换节点/模板转换节点.md:49:46 MD033/no-inline-html Inline HTML [Element: li]
books/XX平台操作手册/开发工作流/工作流节点/模板转换节点/模板转换节点.md:49:65 MD033/no-inline-html Inline HTML [Element: li]
books/XX平台操作手册/开发工作流/工作流节点/模板转换节点/模板转换节点.md:49:84 MD033/no-inline-html Inline HTML [Element: li]
books/XX平台操作手册/开发工作流/工作流节点/模板转换节点/模板转换节点.md:49:34 MD033/no-inline-html Inline HTML [Element: ul]

```
### 英文标点使用
```markdown
发现41处英文标点
```
### 语句通顺问题
```markdown
发现3处问题
· ![image-20250207113814027](./assets/image-20250207113814027....
· {% if arg1['is_active'] %}

  我现在有空

  {% else %}

  我现在没空

...
· 我现在有空  这有些东西: <ul>        <li>苹果</li>        <li>香蕉</li>    ...
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容的审核结果：

1. **错别字**
   - 原文：`这有些东西:`
     - 修改建议：`这些是东西:` 或 `这些物品包括:`
   - 原文：`我现在有空`
     - 修改建议：`我当前有空`
   - 原文：`我现在没空`
     - 修改建议：`我当前没空`

2. **语法不通顺的句子**
   - 原文：`使用模板转换节点，可通过Jinja模板设计器将各类Python结构数据转化为string类型文本。`
     - 修改建议：`使用模板转换节点，可以通过Jinja模板设计器将各类Python结构数据转换为字符串类型文本。`
   - 原文：`你好我名叫{{ arg1['name'] }}，我今年{{ arg1['age'] }}岁。`
     - 修改建议：`你好，我名叫{{ arg1['name'] }}，我今年{{ arg1['age'] }}岁。`
   - 原文：`你好我名叫玛丽，我今年30岁。  我现在有空  这有些东西: <ul>        <li>苹果</li>        <li>香蕉</li>        <li>樱桃</li>     </ul>`
     - 修改建议：`你好，我名叫玛丽，我今年30岁。我当前有空。这些物品包括: <ul>        <li>苹果</li>        <li>香蕉</li>        <li>樱桃</li>     </ul>`

3. **不符合技术文档规范的内容**
   - 原文：`使用模板转换节点，可通过Jinja模板设计器将各类Python结构数据转化为string类型文本。`
     - 修改建议：`使用模板转换节点，可以通过Jinja模板设计器将各类Python结构数据转换为字符串类型文本。`（避免口语化表达）
   - 原文：`你好我名叫{{ arg1['name'] }}，我今年{{ arg1['age'] }}岁。`
     - 修改建议：`你好，我名叫{{ arg1['name'] }}，我今年{{ arg1['age'] }}岁。`（避免口语化表达）
   - 原文：`这有些东西:`
     - 修改建议：`这些是东西:` 或 `这些物品包括:`（避免口语化表达）

4. **中英文标点混用的情况**
   - 原文：`使用模板转换节点，可通过Jinja模板设计器将各类Python结构数据转化为string类型文本。`
     - 修改建议：`使用模板转换节点，可以通过Jinja模板设计器将各类Python结构数据转换为字符串类型文本。`（统一使用中文标点）
   - 原文：`你好我名叫{{ arg1['name'] }}，我今年{{ arg1['age'] }}岁。`
     - 修改建议：`你好，我名叫{{ arg1['name'] }}，我今年{{ arg1['age'] }}岁。`（统一使用中文标点）
   - 原文：`你好我名叫玛丽，我今年30岁。  我现在有空  这有些东西: <ul>        <li>苹果</li>        <li>香蕉</li>        <li>樱桃</li>     </ul>`
     - 修改建议：`你好，我名叫玛丽，我今年30岁。我当前有空。这些物品包括: <ul>        <li>苹果</li>        <li>香蕉</li>        <li>樱桃</li>     </ul>`（统一使用中文标点）

希望这些建议能帮助您改进文档的质量。
```

## books/XX平台操作手册/开发工作流/工作流节点/列表过滤节点/列表过滤节点.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发工作流/工作流节点/列表过滤节点/列表过滤节点.md:7 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]
books/XX平台操作手册/开发工作流/工作流节点/列表过滤节点/列表过滤节点.md:15 MD036/no-emphasis-as-heading Emphasis used instead of a heading [Context: "输入变量"]
books/XX平台操作手册/开发工作流/工作流节点/列表过滤节点/列表过滤节点.md:23 MD036/no-emphasis-as-heading Emphasis used instead of a heading [Context: "过滤条件"]
books/XX平台操作手册/开发工作流/工作流节点/列表过滤节点/列表过滤节点.md:39 MD036/no-emphasis-as-heading Emphasis used instead of a heading [Context: "排序"]
books/XX平台操作手册/开发工作流/工作流节点/列表过滤节点/列表过滤节点.md:48 MD036/no-emphasis-as-heading Emphasis used instead of a heading [Context: "取出前 N 个项目"]
books/XX平台操作手册/开发工作流/工作流节点/列表过滤节点/列表过滤节点.md:52 MD036/no-emphasis-as-heading Emphasis used instead of a heading [Context: "输出变量"]
books/XX平台操作手册/开发工作流/工作流节点/列表过滤节点/列表过滤节点.md:73 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]

```
### 英文标点使用
```markdown
发现16处英文标点
```
### 语句通顺问题
```markdown
发现11处问题
· # 列表过滤节点

文件列表变量支持同时上传文档文件、图片、音频、视频等多种文件类型，应用用户上传文件时，所有文件都存放...
· ![image-20250209202405487](./assets/image-20250209202405487....
· 支持提取以下变量：

- type：文件类别，包括图像、文档、音频和视频类型
- size：文件大小
- name：文件...
· - transfer_method：文件上传方式，分为本地上传或者通过URL上传

**排序**

提供对输入变量中的数...
· 对于字母和文本，按字母顺序排序（A - Z）
- 降序（DESC）：从大到小排序，对于字母和文本，按字母表的反向顺序排序...
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/开发工作流/工作流节点/HTTP请求节点/HTTP请求节点.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发工作流/工作流节点/HTTP请求节点/HTTP请求节点.md:3 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]
books/XX平台操作手册/开发工作流/工作流节点/HTTP请求节点/HTTP请求节点.md:22 MD036/no-emphasis-as-heading Emphasis used instead of a heading [Context: "失败时重试"]
books/XX平台操作手册/开发工作流/工作流节点/HTTP请求节点/HTTP请求节点.md:31 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]
books/XX平台操作手册/开发工作流/工作流节点/HTTP请求节点/HTTP请求节点.md:32 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 3]
books/XX平台操作手册/开发工作流/工作流节点/HTTP请求节点/HTTP请求节点.md:33 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 4]
books/XX平台操作手册/开发工作流/工作流节点/HTTP请求节点/HTTP请求节点.md:34 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 5]
books/XX平台操作手册/开发工作流/工作流节点/HTTP请求节点/HTTP请求节点.md:35 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 6]
books/XX平台操作手册/开发工作流/工作流节点/HTTP请求节点/HTTP请求节点.md:36 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 7]
books/XX平台操作手册/开发工作流/工作流节点/HTTP请求节点/HTTP请求节点.md:37 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 8]

```
### 英文标点使用
```markdown
发现6处英文标点
```
### 语句通顺问题
```markdown
发现3处问题
· # HTTP请求节点

### 定义

通过HTTP协议发送服务器请求，适用于获取外部数据、webhook、生成图片、下...
· ![image-20250209180113532](./assets/image-20250209180113532....
· - 最大重试次数为 10
- 最大重试间隔为 5000 毫秒

![image-20250209181919594](....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档进行的详细检查和修改建议：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - **原文**：对于节点发生的一些异常，通常只需再次重试节点即可。
     - **修改建议**：对于节点发生的一些异常，通常只需重新执行节点即可。
   - **原文**：您可以调整最大重试次数以及每次重试的间隔来设置重试策略。
     - **修改建议**：您可以通过调整最大重试次数和每次重试的间隔来设置重试策略。

3. **不符合技术文档规范的内容**
   - **原文**：您可以配置 HTTP 请求的各个方面，包括 URL、请求标头、查询参数、请求正文内容和身份验证信息。
     - **修改建议**：您可以配置 HTTP 请求的各个方面，包括 URL、请求头、查询参数、请求体内容和身份验证信息。
   - **原文**：最大重试次数为 10
     - **修改建议**：最大重试次数为 10 次。
   - **原文**：最大重试间隔为 5000 毫秒
     - **修改建议**：最大重试间隔为 5000 毫秒（5 秒）。

4. **中英文标点混用的情况**
   - **原文**：最大重试次数为 10
     - **修改建议**：最大重试次数为 10 次。
   - **原文**：最大重试间隔为 5000 毫秒
     - **修改建议**：最大重试间隔为 5000 毫秒（5 秒）。

### 修改后的文档

```markdown
# HTTP请求节点

### 定义

通过HTTP协议发送服务器请求，适用于获取外部数据、webhook、生成图片、下载文件等场景，可以向指定网址发送自定义HTTP请求，实现与各种外部服务的对接。

该节点支持常见的HTTP请求方法：

- **GET**：用于请求服务器发送特定资源。
- **POST**：用于向服务器提交数据，通常用于提交表单或上传文件。
- **HEAD**：类似于 GET 请求，但服务器只返回响应头，而不返回资源主体。
- **PATCH**：用于对资源应用部分修改。
- **PUT**：用于将资源上传到服务器，通常用于更新现有资源或创建新资源。
- **DELETE**：用于请求服务器删除指定的资源。

您可以配置 HTTP 请求的各个方面，包括 URL、请求头、查询参数、请求体内容和身份验证信息。

![image-20250209180113532](./assets/image-20250209180113532.png)

### 高级功能

**失败时重试**

对于节点发生的一些异常，通常只需重新执行节点即可。开启错误重试功能后，节点在发生错误时将自动按照预设的策略进行重试。您可以通过调整最大重试次数和每次重试的间隔来设置重试策略。

- 最大重试次数为 10 次
- 最大重试间隔为 5000 毫秒（5 秒）

![image-20250209181919594](./assets/image-20250209181919594.png)
```

希望这些建议对您有所帮助！
```

## books/XX平台操作手册/开发工作流/工作流节点/数据库查询节点/数据库查询节点.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现3处英文标点
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容进行的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - **原文**：使用数据库查询节点可在工作流中进行数据库数据查询。
     - **问题**：句子结构较为冗长，可以简化。
     - **建议**：使用数据库查询节点可在工作流中查询数据库数据。
   - **原文**：添加数据库查询节点并填写相应数据库信息与查询SQL。
     - **问题**：句子结构较为冗长，可以简化。
     - **建议**：添加数据库查询节点并填写数据库信息和查询SQL。

3. **不符合技术文档规范的内容**
   - **原文**：使用数据库查询节点可在工作流中进行数据库数据查询。
     - **问题**：表达不够明确，可以更具体。
     - **建议**：使用数据库查询节点可以在工作流中执行数据库数据查询操作。
   - **原文**：添加数据库查询节点并填写相应数据库信息与查询SQL。
     - **问题**：表达不够明确，可以更具体。
     - **建议**：添加数据库查询节点，并填写数据库连接信息和查询SQL语句。

4. **中英文标点混用的情况**
   - **原文**：![image-20250207095736495](./assets/image-20250207095736495.png)
     - **问题**：图片说明中使用了英文标点，但整体文档为中文，建议统一使用中文标点。
     - **建议**：![图片-20250207095736495](./assets/图片-20250207095736495.png)

总结：
- 无明显错别字。
- 有两处句子结构可以简化。
- 有两处表达可以更具体。
- 图片说明中建议统一使用中文标点。
```

## books/XX平台操作手册/开发工作流/工作流节点/模型节点/模型节点.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发工作流/工作流节点/模型节点/模型节点.md:71 MD012/no-multiple-blanks Multiple consecutive blank lines [Expected: 1; Actual: 2]

```
### 英文标点使用
```markdown
发现36处英文标点
```
### 绝对路径图片
```markdown
![image-20250116162126919](C:/Users/xxxx/AppData/Roaming/Typora/typora-user-images/image-20250116162126919.png)
![image-20250116165001253](C:/Users/xxxx/AppData/Roaming/Typora/typora-user-images/image-20250116165001253.png)
```
### 语句通顺问题
```markdown
发现7处问题
· ![image-20250116161022296](./assets/image-20250116161022296....
· 编写方式可参考：[提示词编写](./XX平台操作手册/提示词编写/提示词编写.md)

编写系统提示词时，可以引用其他节...
· ![image-20250116162126919](C:/Users/xxxx/AppData/Roaming/Typ...
· ![image-20250116162843507](./assets/image-20250116162843507....
· 知识库创建详细参考：[知识库创建](./XX平台操作手册/知识库概述/知识库创建/知识库创建.md)

![image-...
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/开发工作流/工作流节点/参数提取器节点/参数提取器节点.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现10处英文标点
```
### 语句通顺问题
```markdown
发现2处问题
· ![image-20250207184646690](./assets/image-20250207184646690....
· 在指令中，可以输入提示词，指示大模型怎样来提取参数，提示词编写可参考：[提示词编写](./XX平台操作手册/提示词编写/...
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容进行的审核，列出的问题及修改建议如下：

1. **错别字**
   - 原文：使用参数提取器节点，可以使用大模型能力，在文本或图片中提取所需要的参数。
     - 问题：无明显错别字。
   - 原文：在**模型**选择合适的模型，模型选择与模型参数配置可参考：[模型选择与参数配置](./XX平台操作手册/模型管理/模型选择与参数配置/模型选择与参数配置.md)。
     - 问题：无明显错别字。
   - 原文：在**提取参数**中设置想要提取的参数，及参数的描述。参数的名称和描述都是大模型提取参数时的重要参考依据。
     - 问题：无明显错别字。
   - 原文：在指令中，可以输入提示词，指示大模型怎样来提取参数，提示词编写可参考：[提示词编写](./XX平台操作手册/提示词编写/提示词编写.md)。
     - 问题：无明显错别字。
   - 原文：提取的参数将在**输出变量**中输出。
     - 问题：无明显错别字。

2. **语法不通顺的句子**
   - 原文：使用参数提取器节点，可以使用大模型能力，在文本或图片中提取所需要的参数。
     - 问题：句子结构略显冗长，建议简化。
     - 修改建议：使用参数提取器节点，可以利用大模型能力从文本或图片中提取所需参数。
   - 原文：在**提取参数**中设置想要提取的参数，及参数的描述。参数的名称和描述都是大模型提取参数时的重要参考依据。
     - 问题：句子较长，建议拆分。
     - 修改建议：在**提取参数**中设置需要提取的参数及其描述。参数的名称和描述是大模型提取参数时的重要参考依据。

3. **不符合技术文档规范的内容**
   - 原文：使用参数提取器节点，可以使用大模型能力，在文本或图片中提取所需要的参数。
     - 问题：表达略显口语化。
     - 修改建议：使用参数提取器节点，可以利用大模型能力从文本或图片中提取所需参数。
   - 原文：在指令中，可以输入提示词，指示大模型怎样来提取参数，提示词编写可参考：[提示词编写](./XX平台操作手册/提示词编写/提示词编写.md)。
     - 问题：表达略显口语化。
     - 修改建议：在指令中输入提示词，以指导大模型如何提取参数。提示词编写可参考：[提示词编写](./XX平台操作手册/提示词编写/提示词编写.md)。

4. **中英文标点混用的情况**
   - 原文：在**模型**选择合适的模型，模型选择与模型参数配置可参考：[模型选择与参数配置](./XX平台操作手册/模型管理/模型选择与参数配置/模型选择与参数配置.md)。
     - 问题：无明显中英文标点混用。
   - 原文：在**提取参数**中设置想要提取的参数，及参数的描述。参数的名称和描述都是大模型提取参数时的重要参考依据。
     - 问题：无明显中英文标点混用。
   - 原文：在指令中，可以输入提示词，指示大模型怎样来提取参数，提示词编写可参考：[提示词编写](./XX平台操作手册/提示词编写/提示词编写.md)。
     - 问题：无明显中英文标点混用。
   - 原文：提取的参数将在**输出变量**中输出。
     - 问题：无明显中英文标点混用。

以上是文档的审核结果，希望对您有所帮助。
```

## books/XX平台操作手册/开发工作流/工作流节点/文档提取器节点/文档提取器节点.md
### Markdown语法问题
```markdown

```
### 英文标点使用
```markdown
发现6处英文标点
```
### 语句通顺问题
```markdown
发现1处问题
· 支持的文件类型包括：txt、markdown、pdf、html、xlsx、xls、docx、csv、eml、msl、ms...
```
### 智能语义审核
```markdown
1. **错别字**
   - **原文**: 使用文档提取器，可以将各种类型的方件，抽取出其文本内容。
   - **修改建议**: 使用文档提取器，可以将各种类型的文件，抽取出其文本内容。

2. **语法不通顺的句子**
   - **原文**: 使用文档提取器，可以将各种类型的文件，抽取出其文本内容。
   - **修改建议**: 使用文档提取器可以将各种类型的文件中的文本内容抽取出来。

3. **不符合技术文档规范的内容**
   - **原文**: 支持的文件类型包括：txt、markdown、pdf、html、xlsx、xls、docx、csv、eml、msl、msg、pptx、ppt、xml、epub、md、htm
   - **修改建议**: 支持的文件类型包括：txt、Markdown、PDF、HTML、XLSX、XLS、DOCX、CSV、EML、MSG、PPTX、PPT、XML、EPUB、MD、HTM。

4. **中英文标点混用的情况**
   - **原文**: 支持的文件类型包括：txt、markdown、pdf、html、xlsx、xls、docx、csv、eml、msl、msg、pptx、ppt、xml、epub、md、htm
   - **修改建议**: 支持的文件类型包括：txt、Markdown、PDF、HTML、XLSX、XLS、DOCX、CSV、EML、MSG、PPTX、PPT、XML、EPUB、MD、HTM。

5. **不符合技术文档规范的内容**
   - **原文**: 当将文件的列表作为文档提取器输入变量时，输出变量类型自动变为各文档文本的数组。
   - **修改建议**: 当将文件列表作为文档提取器的输入变量时，输出变量类型将自动变为各文档文本的数组。
```

## books/XX平台操作手册/开发工作流/工作流调试/工作流调试.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发工作流/工作流调试/工作流调试.md:17 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]

```
### 英文标点使用
```markdown
发现17处英文标点
```
### 语句通顺问题
```markdown
发现5处问题
· ![image-20250116141851146](./assets/image-20250116141851146....
· ![image-20250116142049661](./assets/image-20250116142049661....
· ![image-20250116142238945](./assets/image-20250116142238945....
· ![image-20250116142448933](./assets/image-20250116142448933....
· ![image-20250116142629491](./assets/image-20250116142629491....
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/开发工作流/工作流创建/工作流基础.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发工作流/工作流创建/工作流基础.md:3 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]

```
### 英文标点使用
```markdown
发现45处英文标点
```
### 绝对路径图片
```markdown
![image-20250115114356562](C:/Users/xxxx/AppData/Roaming/Typora/typora-user-images/image-20250115114356562.png)
![image-20250115114356562](C:/Users/xxxx/AppData/Roaming/Typora/typora-user-images/image-20250115114356562.png)
![image-20250115114356562](C:/Users/xxxx/AppData/Roaming/Typora/typora-user-images/image-20250115114356562.png)
![image-20250115115006511](C:/Users/xxxx/AppData/Roaming/Typora/typora-user-images/image-20250115115006511.png)
![image-20250115114356562](C:/Users/xxxx/AppData/Roaming/Typora/typora-user-images/image-20250115114356562.png)
```
### 语句通顺问题
```markdown
发现1处问题
· # 工作流创建

### 1.创建工作流

在XX平台工作台，点击右上方**新建**按钮，选择“工作流”类型，即可创建工...
```
### 智能审核异常
```markmarkdown
504 Server Error: Gateway Time-out for url: http://192.168.31.52/qwen2-5-72b-instruct-ltgcp/v1/chat/completions
```

## books/XX平台操作手册/开发工作流/工作流发布/工作流发布.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发工作流/工作流发布/工作流发布.md:17 MD001/heading-increment Heading levels should only increment by one level at a time [Expected: h2; Actual: h3]

```
### 英文标点使用
```markdown
发现15处英文标点
```
### 语句通顺问题
```markdown
发现3处问题
· ![image-20250116145432703](./assets/image-20250116145432703....
· ![image-20250116152802644](./assets/image-20250116152802644....
· ![image-20250116153406929](./assets/image-20250116153406929....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档内容进行的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - **原文**：工作流应用开发及调试完成后，可进行正式发布。发布后应用将发布到xxx平台，以供用户使用。
     - **修改建议**：工作流应用开发及调试完成后，可以正式发布。发布后，应用将上线至xxx平台，供用户使用。
   - **原文**：发布的工作流在xxx平台可见。
     - **修改建议**：发布后的工作流将在xxx平台可见。
   - **原文**：工作流应用发布后，可访问应用前台。访问应用前台有2个路径：
     - **修改建议**：工作流应用发布后，可以访问应用前台。访问应用前台有以下两种路径：

3. **不符合技术文档规范的内容**
   - **原文**：点击画布右上角的**发布**按钮，可以发布工作流。
     - **修改建议**：点击画布右上角的“发布”按钮，可以发布工作流。
   - **原文**：每次发布/更新会生成一个新版本号。
     - **修改建议**：每次发布或更新时，系统会生成一个新的版本号。
   - **原文**：1）通过xxx点击应用卡片进入。
     - **修改建议**：1. 通过xxx平台点击应用卡片进入。
   - **原文**：2）在工作流后台，点击**发布**按钮，点击**运行**进入。
     - **修改建议**：2. 在工作流后台，点击“发布”按钮，然后点击“运行”进入。
   - **原文**：可以进行批量运行：
     - **修改建议**：可以进行批量运行操作。

4. **中英文标点混用的情况**
   - **原文**：工作流应用开发及调试完成后，可进行正式发布。发布后应用将发布到xxx平台，以供用户使用。
     - **修改建议**：工作流应用开发及调试完成后，可以正式发布。发布后，应用将上线至xxx平台，供用户使用。
   - **原文**：1）通过xxx点击应用卡片进入。
     - **修改建议**：1. 通过xxx平台点击应用卡片进入。
   - **原文**：2）在工作流后台，点击**发布**按钮，点击**运行**进入。
     - **修改建议**：2. 在工作流后台，点击“发布”按钮，然后点击“运行”进入。

以上是文档审核的详细结果，希望对您有所帮助。
```

## books/XX平台操作手册/开发工作流/工作流发布/工作流发布为工具/工作流发布为工具.md
### Markdown语法问题
```markdown
books/XX平台操作手册/开发工作流/工作流发布/工作流发布为工具/工作流发布为工具.md:9:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 2; Style: 1/1/1]
books/XX平台操作手册/开发工作流/工作流发布/工作流发布为工具/工作流发布为工具.md:15:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/开发工作流/工作流发布/工作流发布为工具/工作流发布为工具.md:17:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/开发工作流/工作流发布/工作流发布为工具/工作流发布为工具.md:19:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/开发工作流/工作流发布/工作流发布为工具/工作流发布为工具.md:21:2 MD010/no-hard-tabs Hard tabs [Column: 2]
books/XX平台操作手册/开发工作流/工作流发布/工作流发布为工具/工作流发布为工具.md:23:1 MD029/ol-prefix Ordered list item prefix [Expected: 1; Actual: 3; Style: 1/1/1]
books/XX平台操作手册/开发工作流/工作流发布/工作流发布为工具/工作流发布为工具.md:29:2 MD010/no-hard-tabs Hard tabs [Column: 2]

```
### 英文标点使用
```markdown
发现18处英文标点
```
### 语句通顺问题
```markdown
发现4处问题
· 1. 工作流画布点击**发布**，选择**发布为工具**...
· ​	c. 在**工具入参**中，工作流的输入变量默认为工具入参...
· 3. 发布为工具后，可在其他工作流中引入该工作流工具...
· ![image-20250123092540739](./assets/image-20250123092540739....
```
### 智能语义审核
```markdown
以下是根据您的要求对文档进行的审核结果：

1. **错别字**
   - 无明显错别字。

2. **语法不通顺的句子**
   - **原文**：工作流画布点击**发布**，选择**发布为工具**。
     - **修改建议**：在工作流画布中点击**发布**，然后选择**发布为工具**。
   - **原文**：LLM填入的方式主要用于在智能体中调用该工具时，由LLM自动填写该入参。（LLM填入暂不支持在工作流引入工具时使用）
     - **修改建议**：LLM填入的方式主要用于在智能体中调用该工具时，由LLM自动填写该入参（LLM填入暂不支持在工作流中引入工具时使用）。
   - **原文**：用户输入方式，在智能体中调用时由用户自行配置该输入。在工作流中调用时在工作流节点中预设填入。
     - **修改建议**：用户输入方式，在智能体中调用时由用户自行配置该输入；在工作流中调用时，在工作流节点中预设填入。

3. **不符合技术文档规范的内容**
   - **原文**：工作流画布点击**发布**，选择**发布为工具**。
     - **修改建议**：在工作流画布中点击**发布**，然后选择**发布为工具**。（避免口语化表达，增加“在...中”以明确操作环境）
   - **原文**：LLM填入的方式主要用于在智能体中调用该工具时，由LLM自动填写该入参。（LLM填入暂不支持在工作流引入工具时使用）
     - **修改建议**：LLM填入的方式主要用于在智能体中调用该工具时，由LLM自动填写该入参（LLM填入暂不支持在工作流中引入工具时使用）。（避免括号内的说明，改为直接说明）
   - **原文**：用户输入方式，在智能体中调用时由用户自行配置该输入。在工作流中调用时在工作流节点中预设填入。
     - **修改建议**：用户输入方式，在智能体中调用时由用户自行配置该输入；在工作流中调用时，在工作流节点中预设填入。（避免分句，使用分号连接两个相关句子，使表达更紧凑）

4. **中英文标点混用的情况**
   - **原文**：LLM填入的方式主要用于在智能体中调用该工具时，由LLM自动填写该入参。（LLM填入暂不支持在工作流引入工具时使用）
     - **修改建议**：LLM填入的方式主要用于在智能体中调用该工具时，由LLM自动填写该入参（LLM填入暂不支持在工作流中引入工具时使用）。（将英文括号改为中文括号）
   - **原文**：用户输入方式，在智能体中调用时由用户自行配置该输入。在工作流中调用时在工作流节点中预设填入。
     - **修改建议**：用户输入方式，在智能体中调用时由用户自行配置该输入；在工作流中调用时，在工作流节点中预设填入。（将英文句号改为中文句号，并使用分号连接两个相关句子）

以上是文档的审核结果，希望对您有所帮助。
```
