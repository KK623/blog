# 博客命名规范与目录结构

## 📁 目录结构

```
blog/
├── index.html                    # 主页
├── posts/
│   ├── index.html               # 博客列表页
│   ├── mwc2026/                 # 专栏目录
│   │   └── index.html          # MWC2026 专栏页
│   └── 2026/                    # 年份
│       └── 03/                  # 月份
│           └── 04/              # 日期
│               ├── llm-research-2026-03-04.html
│               ├── cvnn-research-2026-03-04.html
│               ├── huawei-mwc-2026-report.html
│               ├── zte-mwc-2026-report.html
│               └── nvidia-blackwell-vs-rubin.html
├── skills/                       # Skill 目录
└── assets/                       # 静态资源
```

## 📝 文件命名规范

### 1. 文章文件命名
格式: `{category}-{title}-{date}.html`

| 类型 | 示例 |
|------|------|
| LLM 调研 | `llm-research-YYYY-MM-DD.html` |
| CVNN 调研 | `cvnn-research-YYYY-MM-DD.html` |
| MWC 报告 | `{vendor}-mwc-2026-report.html` |
| 芯片分析 | `{topic}-analysis.html` |

### 2. 专栏页面
- 路径: `posts/{column}/index.html`
- 示例: `posts/mwc2026/index.html`

### 3. 图片目录
- 文章图片: `posts/YYYY/MM/DD/images/{article-name}/`
- 示例: `posts/2026/03/04/images/huawei-mwc-2026-report/`

## 🔗 链接规则

### 主页 (index.html)
- 指向文章: `posts/YYYY/MM/DD/{filename}.html`
- 指向专栏: `posts/{column}/`

### 博客列表页 (posts/index.html)
- 指向文章: `YYYY/MM/DD/{filename}.html` (相对路径)
- 指向专栏: `{column}/` (相对路径)

### 文章页
- 返回首页: `../../index.html` 或 `/`
- 返回博客列表: `../index.html`
- 专栏链接: `../{column}/index.html`

## 🗑️ 清理规则

1. 删除重复文件 (保留最新版本)
2. 删除测试文件
3. 统一使用 `.html` 格式 (不再使用 `.md` 直接展示)

## ⏰ 定时任务规范

新增文章时:
1. 按日期创建目录: `posts/YYYY/MM/DD/`
2. 按规范命名文件
3. 更新 `posts/index.html` 添加链接
4. 如需要,更新主页 `index.html`
