# 现代 Unix / CLI 替代工具

把传统 Unix 命令升级成更快、更友好、更适合代码仓库的现代 CLI 工具。

!!! note "维护方式"
    本页是工具百科的一个专题页。新增工具时，请优先补充到对应功能表格中，并保留：核心优势、适合场景、安装方式、官方链接。


## 3. 现代 Unix/CLI 替代工具 {#modern-cli}

| 功能 | 首选 | 替代 | 用途 | 安装 |
| --- | --- | --- | --- | --- |
| `ls` 替代 | eza | lsd | 彩色列表、Git 状态、树形显示 | `brew install eza lsd` |
| `find` 替代 | fd | bfs | 更快更友好的文件查找 | `brew install fd bfs` |
| `grep` 替代 | ripgrep | silversearcher-ag、ack | 代码/日志搜索 | `brew install ripgrep the_silver_searcher ack` |
| `cat` 替代 | bat | glow | 语法高亮查看文件/Markdown | `brew install bat glow` |
| `diff` 增强 | delta | difftastic、diff-so-fancy | Git diff 美化 / 结构化 diff | `brew install git-delta difftastic diff-so-fancy` |
| 文本替换 | sd | perl、gnu-sed | 更直观的替换命令 | `brew install sd gnu-sed` |
| JSON | jq | jless、fx、jid | JSON 查询/浏览/格式化 | `brew install jq jless fx jid` |
| YAML/XML/TOML | yq | dasel | 配置文件处理 | `brew install yq dasel` |
| CSV/TSV | Miller | xsv、qsv | 表格数据处理 | `brew install miller xsv qsv` |
| 日志查看 | lnav | tailspin、ccze | 彩色日志、SQL 查询日志 | `brew install lnav tailspin` |
| 十六进制 | hexyl | xxd、hexdump | 查看二进制文件 | `brew install hexyl` |
| 命令帮助 | tealdeer | tldr | 常用命令示例 | `brew install tealdeer` |
| 代码行数 | tokei | cloc、scc | 统计语言和代码规模 | `brew install tokei cloc scc` |
| 基准测试 | hyperfine | time、bench | 命令耗时对比 | `brew install hyperfine` |

### 结构化代码搜索与重构

| 工具 | 用途 | 适合场景 | 安装 | 官方链接 |
| --- | --- | --- | --- | --- |
| ast-grep | 基于 AST 的代码搜索/重写 | 批量重构、多语言规则 | `brew install ast-grep` | [官网](https://ast-grep.github.io/) |
| Comby | 结构化搜索和替换 | 大规模代码迁移 | `brew install comby` | [官网](https://comby.dev/) |
| semgrep | 静态分析 / 安全规则 | 安全扫描、代码规范 | `brew install semgrep` | [官网](https://semgrep.dev/) |

---
