# Shell、提示符、补全与历史

围绕 Shell 本身、提示符、命令历史、目录跳转、补全和终端复用器的效率工具。

!!! note "维护方式"
    本页是工具百科的一个专题页。新增工具时，请优先补充到对应功能表格中，并保留：核心优势、适合场景、安装方式、官方链接。


## 2. Shell、提示符、补全与历史 {#shell}

| 工具 | 类型 | 核心优势 | 适合人群 | 安装 | 官方链接 |
| --- | --- | --- | --- | --- | --- |
| Zsh | Shell | macOS 默认 Shell，生态成熟 | 大多数 Mac 用户 | 系统自带 | [官网](https://www.zsh.org/) |
| Fish | Shell | 默认补全和高亮体验好，配置成本低 | 新手、交互优先用户 | `brew install fish` | [官网](https://fishshell.com/) |
| Nushell | 结构化 Shell | 管道传递结构化数据，适合表格/JSON | 数据处理、喜欢新范式的人 | `brew install nushell` | [官网](https://www.nushell.sh/) |
| Oh My Zsh | Zsh 框架 | 插件和主题丰富，上手快 | Zsh 用户 | 脚本安装 | [官网](https://ohmyz.sh/) |
| zinit | Zsh 插件管理 | 快速、灵活、延迟加载 | 重度 Zsh 配置用户 | 脚本安装 | [GitHub](https://github.com/zdharma-continuum/zinit) |
| Powerlevel10k | Zsh 主题 | 高颜值、高信息密度、向导配置 | 注重提示符美观 | Git 安装 | [GitHub](https://github.com/romkatv/powerlevel10k) |
| Starship | 跨 Shell 提示符 | Rust 实现、跨 Shell、配置简单 | 多 Shell/多语言开发者 | `brew install starship` | [官网](https://starship.rs/) |
| Atuin | Shell 历史 | 可搜索、可同步、上下文丰富 | 多机器、经常查历史命令 | `brew install atuin` | [官网](https://atuin.sh/) |
| zoxide | 智能 cd | 根据访问频率跳转目录 | 多项目切换 | `brew install zoxide` | [GitHub](https://github.com/ajeetdsouza/zoxide) |
| fzf | 模糊搜索 | 文件、历史、分支、进程都能接入 | 所有终端用户 | `brew install fzf` | [GitHub](https://github.com/junegunn/fzf) |
| direnv | 环境变量加载 | 进入目录自动加载 `.envrc` | 多项目环境变量管理 | `brew install direnv` | [官网](https://direnv.net/) |
| Carapace | 命令补全 | 多 Shell 命令补全生成器 | CLI 重度用户 | `brew install carapace` | [官网](https://carapace-sh.github.io/carapace-bin/) |
| tmux | 终端复用器 | 会话保持、分屏、远程服务器必备 | SSH/服务器用户 | `brew install tmux` | [GitHub](https://github.com/tmux/tmux) |
| Zellij | 现代终端工作区 | 默认布局友好、TUI 体验现代 | 想替代 tmux 的用户 | `brew install zellij` | [官网](https://zellij.dev/) |

---
