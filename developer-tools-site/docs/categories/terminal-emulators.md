# GUI 终端模拟器

Mac 开发者的终端入口选型：原生性能、AI 交互、可编程配置、远程 SSH 和视觉体验。

!!! note "维护方式"
    本页是工具百科的一个专题页。新增工具时，请优先补充到对应功能表格中，并保留：核心优势、适合场景、安装方式、官方链接。


## 1. GUI 终端模拟器 {#terminal-emulators}

| 工具 | 类型 | 核心优势 | 适合人群 | 安装 | 官方链接 |
| --- | --- | --- | --- | --- | --- |
| Ghostty | 原生终端模拟器 | GPU 加速、平台原生 UI、配置简洁、性能好 | 追求原生体验、长时间看日志、SSH 用户 | `brew install --cask ghostty` | [官网](https://ghostty.org/) |
| Warp | 现代终端 / AI 终端 | 命令输出分块、AI 命令辅助、团队 runbook、上手简单 | 新手、AI 编程、团队协作 | `brew install --cask warp` | [官网](https://www.warp.dev/) |
| WezTerm | 终端模拟器 + 复用器 | Lua 配置、跨平台、内置 tabs/panes/mux、可编程能力强 | 深度自定义、跨平台用户 | `brew install --cask wezterm` | [官网](https://wezterm.org/) |
| iTerm2 | 经典 Mac 终端 | Profile、触发器、热键窗口、长期稳定 | 传统 Mac 开发者、Zsh/Tmux 用户 | `brew install --cask iterm2` | [官网](https://iterm2.com/) |
| Alacritty | 极简 GPU 终端 | OpenGL 渲染、轻量、配置简单、不内置复杂 UI | 极简党、tmux/yabai 用户 | `brew install --cask alacritty` | [GitHub](https://github.com/alacritty/alacritty) |
| Kitty | GPU 终端 | 图片协议、远程控制、布局、性能好 | 需要图像预览、终端图形能力的人 | `brew install --cask kitty` | [官网](https://sw.kovidgoyal.net/kitty/) |
| Tabby | 跨平台终端/SSH | SSH 分组、SFTP、跨平台 UI | 多服务器管理、Windows/Mac 双平台 | `brew install --cask tabby` | [官网](https://tabby.sh/) |
| Hyper | Electron 终端 | CSS/JS 插件生态，界面可玩性强 | 前端开发者、视觉定制 | `brew install --cask hyper` | [官网](https://hyper.is/) |
| Rio | Rust 终端 | WebGPU/现代渲染、配置简洁 | 想尝鲜新终端的人 | `brew install --cask rio` | [官网](https://raphamorim.io/rio/) |

**建议**：

- 想少折腾：Ghostty / iTerm2。
- 想 AI 命令和现代交互：Warp。
- 想高度可编程：WezTerm。
- 已经重度使用 tmux：Alacritty / Ghostty / Kitty 都可以。

---
