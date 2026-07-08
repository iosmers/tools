# Mac 开发效率工具箱

一个面向 Mac 程序员的全维度开发效率工具百科站，不只收录终端工具，也覆盖 **文件、存储、网络、远程连接、系统监控、窗口桌面、剪贴板、编辑器、Git、容器、数据库、密码密钥、自动化、笔记文档、截图媒体、Web 调试、AI/LLM 开发** 等高频场景。

[快速总览](tools.md){ .md-button .md-button--primary }
[进入工具百科](categories/index.md){ .md-button }
[部署指南](deploy.md){ .md-button }

<div class="tool-hero" markdown>

## 为什么做这个站？

很多优秀的开发工具分散在 GitHub、官方文档、博客、包管理器和商业软件官网中。这个项目把它们整理成一个可搜索、可维护、可部署到 Read the Docs 的网页：

- **从工具链全局看效率**：不只看终端，还看窗口、剪贴板、抓包、数据库、容器、云服务器、文档、AI 编程等环节。
- **按功能组织同类工具**：每个功能下列多个候选工具，方便横向比较。
- **多页面百科结构**：总览页只放结论；完整工具说明拆到专题页，便于扩展和维护。
- **保留 Markdown 源文件**：方便持续补充，也方便以后自动生成排行榜、标签页、安装脚本。

</div>

## 推荐从这 18 个入口开始

| 场景 | 入口 | 一句话说明 |
| --- | --- | --- |
| 终端 | [Ghostty / WezTerm / Warp](categories/terminal-emulators.md) | 现代 GUI 终端模拟器 |
| Shell 效率 | [zoxide + fzf + Atuin](categories/shell.md) | 目录跳转、模糊搜索、命令历史 |
| 文件搜索 | [ripgrep + fd + bat](categories/modern-cli.md) | 快速查代码、查文件、看内容 |
| 文件管理 | [Yazi / nnn / ranger](categories/tui-file-managers.md) | 终端文件导航和批量操作 |
| GUI 文件管理 | [ForkLift / Path Finder](categories/files-storage.md) | Finder 增强、远程文件、双栏管理 |
| 网络调试 | [Proxyman / Charles / mitmproxy](categories/network-debugging.md) | HTTP/HTTPS 抓包和接口排障 |
| API 客户端 | [Bruno / Postman / HTTPie](categories/network-debugging.md#api-clients) | 调试 REST、GraphQL、gRPC |
| 远程连接 | [OpenSSH / mosh / Termius](categories/ssh-cloud.md) | SSH、SFTP、服务器连接管理 |
| 系统监控 | [Stats + btop](categories/system-monitoring.md) | 菜单栏和终端资源监控 |
| 窗口管理 | [Rectangle / Raycast / AeroSpace](categories/window-desktop.md) | 分屏、启动器、平铺窗口 |
| 剪贴板 | [Maccy / Paste](categories/clipboard-input.md) | 剪贴板历史和代码片段 |
| 编辑器 | [VS Code / JetBrains / Zed / Neovim](categories/editors-ide-ai.md) | GUI IDE 与终端编辑器 |
| Git | [lazygit / gh / delta](categories/git-review.md) | 终端 Git、PR、diff 阅读 |
| 容器 | [OrbStack / Docker Desktop / Colima](categories/containers-kubernetes.md) | 本地容器和 Linux VM |
| 数据库 | [TablePlus / DBeaver / DataGrip](categories/databases.md) | SQL/NoSQL 图形客户端 |
| 密钥安全 | [1Password / Bitwarden / Secretive](categories/secrets-security.md) | 密码、SSH Key、证书 |
| 自动化 | [Hammerspoon / Keyboard Maestro / just](categories/automation.md) | 系统自动化和项目命令 |
| AI/LLM | [Ollama / LM Studio / Aider](categories/ai-llm.md) | 本地模型和 AI 编程辅助 |

## 百科结构

| 一级分组 | 专题页面 |
| --- | --- |
| 终端生态 | [GUI 终端](categories/terminal-emulators.md)、[Shell 增强](categories/shell.md)、[现代 CLI](categories/modern-cli.md)、[TUI 文件管理](categories/tui-file-managers.md) |
| 文件、存储与磁盘 | [GUI 文件管理与同步](categories/files-storage.md)、[压缩/磁盘/备份](categories/disk-backup.md) |
| 网络、远程与云 | [网络调试/抓包/隧道](categories/network-debugging.md)、[SSH/远程/云服务器](categories/ssh-cloud.md) |
| Mac 系统效率 | [系统监控](categories/system-monitoring.md)、[窗口桌面](categories/window-desktop.md)、[剪贴板输入](categories/clipboard-input.md)、[系统维护](categories/mac-maintenance.md) |
| 代码开发核心 | [编辑器 IDE](categories/editors-ide-ai.md)、[Git 评审](categories/git-review.md)、[代码质量测试](categories/code-quality.md) |
| 基础设施与数据 | [容器/Kubernetes](categories/containers-kubernetes.md)、[数据库/缓存](categories/databases.md) |
| 安全、自动化与环境 | [密码密钥安全](categories/secrets-security.md)、[自动化工作流](categories/automation.md)、[包管理环境](categories/package-env.md) |
| 文档、媒体、前端与 AI | [笔记文档图表](categories/docs-knowledge.md)、[截图媒体](categories/media.md)、[Web 调试](categories/web-frontend.md)、[AI/LLM](categories/ai-llm.md) |
| 角色与维护 | [按角色推荐](categories/roles.md)、[维护路线](categories/maintenance.md) |

## 站点结构

```text
.
└── developer-tools-site/
    ├── .readthedocs.yaml      # Read the Docs 构建配置
    ├── mkdocs.yml             # MkDocs 站点配置与多级导航
    ├── requirements.txt       # Python 构建依赖
    └── docs/
        ├── index.md           # 首页
        ├── tools.md           # 快速总览
        ├── categories/        # 工具百科专题页
        │   ├── index.md       # 百科索引
        │   ├── terminal-emulators.md
        │   ├── shell.md
        │   └── ...
        ├── plan.md            # 项目计划
        └── deploy.md          # 部署指南
```

## 下一步可迭代方向

- 给每个工具增加截图、图标或 GIF。
- 给每个专题页增加“首选 / 免费 / 开源 / 商业 / 团队协作 / 远程服务器”标签。
- 增加“安装脚本生成器”：按类别勾选后生成 Homebrew / apt / cargo / pipx 命令。
- 后续把工具信息抽到 YAML/JSON，再自动生成 Markdown 表格和筛选页。
