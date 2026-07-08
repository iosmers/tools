# 项目计划

## 目标

做一个可以部署到 **Read the Docs** 的网页，集中展示 Mac 程序员常用的现代开发效率工具。不只覆盖终端、CLI、TUI、Shell、Git、文件管理、系统监控、Python 工具链，也覆盖网络抓包、远程连接、窗口桌面、剪贴板、编辑器/IDE、容器、数据库、密码密钥、自动化、笔记文档、截图媒体、Web 调试、AI/LLM 开发等方向。

## 阶段计划

### 阶段 1：调研与筛选

交付物：[`tools.md`](tools.md) 与 [`categories/`](categories/index.md) 下的专题页。

- 收集常见开发者工具：终端模拟器、Shell 增强、现代 Unix 工具、文件管理器、云存储、网络调试、SSH、系统监控、窗口管理、剪贴板、编辑器、Git、容器、数据库、密钥管理、自动化、文档、AI 工具等。
- 按使用场景分类，而不是按语言、公司或实现语言分类。
- 每个功能下至少列出多个同类候选工具，方便比较。
- 每个工具记录：用途、推荐理由、适合人群、安装命令、官方链接。
- 优先选择活跃、安装简单、能显著提升开发效率的工具；CLI/TUI 工具额外关注跨平台和远程服务器可复用性。

### 阶段 2：信息架构

交付物：`docs/` 下的 Markdown 页面。

- 首页：解释项目定位，给新手一个快速入口。
- 快速总览页：只保留选型原则、推荐安装组合、极简选型结论和百科入口。
- 工具百科页：在 `docs/categories/` 下按功能域拆分，例如终端生态、文件存储、网络远程、Mac 系统效率、代码开发核心、基础设施与数据、安全自动化、文档媒体前端 AI 等。
- 项目计划页：维护路线与后续迭代方向。
- 部署指南页：说明如何本地预览、构建、部署到 Read the Docs。

### 阶段 3：网页实现

交付物：`mkdocs.yml`、`requirements.txt`、`.readthedocs.yaml`。

- 使用 MkDocs 把 Markdown 转成静态站点。
- 使用 Material for MkDocs 提供搜索、深色模式、代码复制、导航标签等功能。
- 通过 `.readthedocs.yaml` 告诉 Read the Docs 使用 Python 3.12 安装依赖并执行 MkDocs 构建。

### 阶段 4：本地验证

交付物：本地构建通过。

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
mkdocs build --strict
```

### 阶段 5：部署到 Read the Docs

交付物：公开可访问的文档网站。

1. 把仓库推送到 GitHub。
2. 登录 Read the Docs。
3. 导入 GitHub 仓库。
4. 将 Read the Docs 的配置文件路径设置为 `developer-tools-site/.readthedocs.yaml`。
5. 触发构建并检查构建日志。

## 后续维护建议

- 每月补充 3-5 个新工具。
- 每季度检查一次工具官方链接和安装命令。
- 后续可以把工具信息抽到 `YAML/JSON`，再自动生成 Markdown 表格。
- 总览页只保留结论和入口；新增工具优先补充到 `docs/categories/` 对应专题页。
- 当某个专题页继续变长时，再拆分为二级页面，例如 `network-debugging.md` 可以继续拆成 `api-clients.md`、`proxy-capture.md`、`dns-tunnel.md`。
