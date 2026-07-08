# 自动化、脚本、任务运行与工作流

macOS 系统自动化、键盘/窗口自动化、项目命令运行器和文件变化监听。

!!! note "维护方式"
    本页是工具百科的一个专题页。新增工具时，请优先补充到对应功能表格中，并保留：核心优势、适合场景、安装方式、官方链接。


## 17. 自动化、脚本、任务运行与工作流 {#automation}

| 工具 | 类型 | 核心优势 | 适合场景 | 安装/获取 |
| --- | --- | --- | --- | --- |
| Shortcuts | 系统自动化 | macOS/iOS 统一自动化 | 简单自动化 | 系统自带 |
| Automator | 系统自动化 | 批量文件/服务菜单 | 老式工作流 | 系统自带 |
| Hammerspoon | Lua 自动化 | 窗口、快捷键、系统事件 | 程序员自动化 | `brew install --cask hammerspoon` |
| Keyboard Maestro | GUI 自动化 | 录制、宏、复杂流程 | 非程序员/重度效率 | 官网 |
| BetterTouchTool | 触控板/键盘/窗口自动化 | 手势、快捷动作 | Mac 高级用户 | 官网/Setapp |
| Karabiner-Elements | 键盘改键 | CapsLock、Hyper Key、复杂映射 | 键盘流 | `brew install --cask karabiner-elements` |
| Hazel | 文件夹自动整理 | 下载目录/归档自动化 | 文件整理 | 官网 |
| launchd | 定时/守护任务 | macOS 原生服务 | 后台任务 | 系统自带 |
| just | 命令运行器 | `justfile` 管理项目命令 | 项目脚本入口 | `brew install just` |
| Task | YAML 任务运行器 | 跨平台任务定义 | DevOps/团队 | `brew install go-task` |
| Make | 经典构建工具 | 老项目/通用任务 | 构建脚本 | 系统自带/`brew install make` |
| watchexec | 文件变化执行命令 | 自动测试/重启 | 开发循环 | `brew install watchexec` |
| entr | 文件变化触发 | 简单 UNIX 工作流 | Shell 用户 | `brew install entr` |
| fswatch | 文件系统事件 | 监听文件变化 | 脚本自动化 | `brew install fswatch` |
| cron | 定时任务 | 简单定时脚本 | 传统 Unix | 系统自带 |

---
