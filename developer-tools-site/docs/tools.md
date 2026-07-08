# 全维度工具总览

本页是工具百科站的快速入口：先看选型原则、推荐安装组合和极简选型结论；需要完整说明时，再进入对应专题页。

## 选型原则

- **先按功能选，不按名气选**：例如“HTTP 抓包”下比较 Proxyman、Charles、mitmproxy，而不是只列一个。
- **优先官方/活跃项目**：优先收录维护活跃、文档完整、社区使用多的工具。
- **Mac 体验优先，但不排斥跨平台**：GUI 工具看 macOS 原生体验；CLI/TUI 工具看 SSH、Linux、CI 场景可复用性。
- **开发效率优先**：能显著提升查文件、写代码、调 API、管理 Git、连接服务器、容器调试、数据库操作、文档沉淀的工具优先。
- **安全默认谨慎**：密码、证书、SSH Key、抓包代理、代理工具必须理解权限和信任边界。

## 快速推荐组合

### 新 Mac 开发机基础套装

```bash
brew install git gh ripgrep fd fzf zoxide eza bat jq yq git-delta lazygit starship atuin direnv mise just uv ruff btop bottom duf dust hyperfine tokei tldr
brew install --cask ghostty wezterm visual-studio-code raycast rectangle maccy stats tableplus orbstack proxyman shottr obsidian
```

### 远程服务器 / 运维套装

```bash
brew install openssh mosh autossh tmux zellij k9s kubectx helm stern lazydocker dive htop btop procs glances doggo mtr iperf3 rclone restic age sops
```

### Python / AI 开发套装

```bash
brew install uv ruff mise direnv just hyperfine tokei jq yq graphviz ffmpeg imagemagick git-lfs pre-commit
```

### 前端 / API / Web 调试套装

```bash
brew install node pnpm bun deno httpie xh hurl jq yq mkcert ngrok cloudflared oha k6 playwright
brew install --cask google-chrome firefox@developer-edition proxyman bruno insomnia postman responsively-app imageoptim
```

---

## 0. 极简选型结论

| 场景 | 首选 | 替代 / 进阶 | 说明 |
| --- | --- | --- | --- |
| 现代终端 | Ghostty | WezTerm、Warp、iTerm2、Alacritty、Kitty | Ghostty 偏原生和性能；WezTerm 可编程；Warp 偏 AI/块状工作流 |
| Shell 效率 | zoxide + fzf + atuin | fish、nushell、direnv、starship | 先改善跳转、搜索、历史，再考虑换 shell |
| 文件搜索 | ripgrep + fd | ast-grep、silversearcher-ag | 文本搜索用 rg，结构化代码搜索用 ast-grep |
| 终端文件管理 | Yazi | nnn、ranger、lf、vifm、broot | Yazi 适合现代 TUI，nnn 适合极轻量 |
| GUI 文件管理 | ForkLift | Path Finder、Commander One、Marta、QSpace | 双栏、SFTP、云盘、批量操作比 Finder 强 |
| Git TUI | lazygit | gitui、tig、Fork、Tower、GitKraken | 命令行用户先试 lazygit |
| API 调试 | Bruno / HTTPie | Postman、Insomnia、xh、hurl | 团队协作看 Postman；本地文件化看 Bruno |
| HTTP 抓包 | Proxyman | Charles、mitmproxy、HTTP Toolkit、Burp Suite | Mac 原生体验 Proxyman 好；CLI 自动化用 mitmproxy |
| 容器 | OrbStack | Docker Desktop、Colima、Rancher Desktop、Podman Desktop | Mac 轻量体验优先 OrbStack/Colima；企业标准常用 Docker Desktop |
| Kubernetes | k9s | Lens/OpenLens、kubectl、kubectx、stern | 终端排障 k9s；图形管理 Lens 类工具 |
| 数据库 GUI | TablePlus | DBeaver、DataGrip、Beekeeper Studio、Sequel Ace | 轻量好看选 TablePlus；全数据库覆盖选 DBeaver |
| 系统监控 | Stats + btop | iStat Menus、Activity Monitor、asitop、Little Snitch | 免费菜单栏 Stats，终端 btop |
| 窗口管理 | Rectangle | Raycast、Moom、Magnet、yabai、AeroSpace | 普通用户 Rectangle；键盘流/平铺用 AeroSpace/yabai |
| 启动器 | Raycast | Alfred、LaunchBar、Spotlight | Raycast 插件生态强；Alfred 工作流成熟 |
| 剪贴板 | Maccy | Paste、Raycast Clipboard、CopyQ、Flycut | 开源轻量选 Maccy；全功能历史库选 Paste |
| 密码/SSH Key | 1Password | Bitwarden、KeePassXC、Secretive、YubiKey | 团队协作和 SSH Agent 选 1Password；开源/自托管看 Bitwarden/KeePassXC |
| 笔记知识库 | Obsidian | Logseq、Joplin、Notion、Zettlr | 本地 Markdown 首选 Obsidian；大纲/日志流选 Logseq |
| 截图/OCR | Shottr | CleanShot X、Snagit、macOS Screenshot | 轻量 OCR/贴图选 Shottr；专业工作流 CleanShot X |

---


## 百科分类导航

| 分类 | 覆盖范围 | 页面 |
| --- | --- | --- |
| 终端生态 | GUI 终端、Shell、现代 CLI、TUI 文件管理 | [GUI 终端模拟器](categories/terminal-emulators.md)、[Shell、提示符、补全与历史](categories/shell.md)、[现代 Unix / CLI 替代工具](categories/modern-cli.md)、[终端文件管理器](categories/tui-file-managers.md) |
| 文件、存储与磁盘 | Finder 增强、云存储、远程挂载、压缩、磁盘清理、备份 | [GUI 文件管理器与同步](categories/files-storage.md)、[压缩、磁盘清理、备份](categories/disk-backup.md) |
| 网络、远程与云 | API 调试、抓包代理、隧道、SSH、云服务器、IaC | [网络调试、抓包、代理与隧道](categories/network-debugging.md)、[SSH、远程连接与云服务器](categories/ssh-cloud.md) |
| Mac 系统效率 | 系统监控、窗口桌面、剪贴板、系统维护 | [系统资源监控与安全排障](categories/system-monitoring.md)、[窗口、桌面、启动器](categories/window-desktop.md)、[剪贴板与输入增强](categories/clipboard-input.md)、[Mac 系统维护](categories/mac-maintenance.md) |
| 代码开发核心 | 编辑器、IDE、Git、代码质量、测试与安全扫描 | [编辑器、IDE 与 AI 编程](categories/editors-ide-ai.md)、[Git、代码评审与版本控制](categories/git-review.md)、[代码质量、测试、性能与安全扫描](categories/code-quality.md) |
| 基础设施与数据 | 容器、虚拟化、Kubernetes、数据库、缓存 | [容器、虚拟化与 Kubernetes](categories/containers-kubernetes.md)、[数据库、缓存和数据客户端](categories/databases.md) |
| 安全、自动化与环境 | 密码密钥、证书、系统自动化、包管理和语言版本 | [密码、密钥、证书与安全](categories/secrets-security.md)、[自动化、脚本和工作流](categories/automation.md)、[包管理、语言版本与项目环境](categories/package-env.md) |
| 文档、媒体、前端与 AI | 笔记知识库、截图媒体、Web 调试、本地 LLM | [笔记、文档、知识库与图表](categories/docs-knowledge.md)、[截图、录屏、图片和媒体处理](categories/media.md)、[前端、浏览器与 Web 调试](categories/web-frontend.md)、[AI / LLM 本地开发](categories/ai-llm.md) |
| 角色与维护 | 按角色快速选型，以及后续维护路线 | [按角色推荐](categories/roles.md)、[维护路线与候选方向](categories/maintenance.md) |

## 按角色快速入口

- [后端 / 前端 / AI 数据 / DevOps / 远程服务器用户推荐](categories/roles.md)
- [维护路线与后续候选方向](categories/maintenance.md)

!!! tip "后续维护建议"
    总览页只放结论和入口；新增工具时，请优先补充到 `docs/categories/` 下对应专题页，避免总览页重新变成超长单页。
