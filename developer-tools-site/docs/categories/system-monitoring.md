# 系统资源监控、安全与进程排障

菜单栏监控、终端进程监控、网络权限、安全持久化项检查和性能排障。

!!! note "维护方式"
    本页是工具百科的一个专题页。新增工具时，请优先补充到对应功能表格中，并保留：核心优势、适合场景、安装方式、官方链接。


## 9. 系统资源监控、安全与进程排障 {#system-monitoring}

### 菜单栏 / GUI 监控

| 工具 | 核心优势 | 适合场景 | 获取方式 |
| --- | --- | --- | --- |
| Stats | 开源菜单栏 CPU/内存/网络/温度 | 免费菜单栏监控 | `brew install --cask stats` |
| iStat Menus | 商业全维度系统监控 | 需要传感器、温度、历史图表 | 官网/Setapp |
| Activity Monitor | 系统自带 | 快速查看进程/能耗 | 系统自带 |
| MenuMeters | 轻量菜单栏监控 | 极简用户 | 官网/GitHub |
| Sensei | 系统监控/磁盘健康 | 商业 Mac 维护 | 官网 |

### 终端监控

| 工具 | 用途 | 适合场景 | 安装 |
| --- | --- | --- | --- |
| btop | 现代资源监控 TUI | 本地/服务器监控 | `brew install btop` |
| bottom | 跨平台系统监控 | 长时间观察资源 | `brew install bottom` |
| htop | 经典进程监控 | 服务器常见 | `brew install htop` |
| procs | 现代 `ps` 替代 | 查进程 | `brew install procs` |
| glances | 全局系统监控 | 服务器/远程 Web 模式 | `brew install glances` |
| asitop | Apple Silicon 性能监控 | M 系列芯片观察 | `pipx install asitop` |
| powermetrics | macOS 底层功耗/频率 | 深度性能分析 | 系统自带，需要 sudo |
| lsof | 文件/端口占用 | “谁占了端口/文件” | 系统自带 |
| bandwhich | 按进程看带宽 | 网络占用排查 | `brew install bandwhich` |

### 网络权限 / 安全监控

| 工具 | 用途 | 适合场景 | 获取方式 |
| --- | --- | --- | --- |
| Little Snitch | 出站网络防火墙 | 管控软件联网 | 官网 |
| LuLu | 开源出站防火墙 | 免费替代 Little Snitch | [Objective-See](https://objective-see.org/products/lulu.html) |
| KnockKnock | 持久化项检查 | 排查可疑启动项 | Objective-See |
| BlockBlock | 持久化防护 | 监控新增持久化项 | Objective-See |
| ReiKey | 键盘事件监控检查 | 检查键盘监听权限 | Objective-See |

---
