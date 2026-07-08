# 压缩、磁盘清理、备份与恢复

压缩解压、磁盘空间分析、重复文件清理、加密去重备份和系统备份。

!!! note "维护方式"
    本页是工具百科的一个专题页。新增工具时，请优先补充到对应功能表格中，并保留：核心优势、适合场景、安装方式、官方链接。


## 6. 压缩、磁盘清理、备份与恢复

### 压缩/解压

| 工具 | 用途 | 适合场景 | 安装 |
| --- | --- | --- | --- |
| Keka | 7z/zip/rar 等压缩解压 | 免费、简洁、日常压缩 | `brew install --cask keka` |
| The Unarchiver | 解压大量格式 | 只想补强系统解压 | `brew install --cask the-unarchiver` |
| BetterZip | 压缩包预览/编辑/批量 | 高级压缩包操作 | `brew install --cask betterzip` |
| 7zip | CLI 压缩工具 | 脚本/服务器复用 | `brew install sevenzip` |
| ouch | 统一压缩/解压 CLI | 不想记 tar/zip/7z 参数 | `brew install ouch` |
| zstd / brotli | 高性能压缩 | 构建产物、日志压缩 | `brew install zstd brotli` |

### 磁盘空间与重复文件

| 工具 | 用途 | 适合场景 | 安装/获取 |
| --- | --- | --- | --- |
| DaisyDisk | 磁盘可视化分析 | 快速找大文件 | 官网/App Store |
| GrandPerspective | 开源磁盘 Treemap | 免费可视化 | `brew install --cask grandperspective` |
| OmniDiskSweeper | 按目录大小排序 | 快速清理 | 官网 |
| Disk Inventory X | 经典磁盘可视化 | 免费替代 | 官网 |
| dust | 终端磁盘占用 | CLI 快速定位大目录 | `brew install dust` |
| duf | 终端磁盘分区展示 | 替代 `df` | `brew install duf` |
| dua-cli | 交互式磁盘分析 | 删除大目录 | `brew install dua-cli` |
| ncdu | 经典 TUI 磁盘分析 | 服务器清理 | `brew install ncdu` |
| Czkawka | 重复文件/相似图片 | 清理重复文件 | `brew install --cask czkawka` |
| rmlint | 重复/垃圾文件 CLI | 脚本化清理 | `brew install rmlint` |

### 备份

| 工具 | 用途 | 适合场景 | 安装 |
| --- | --- | --- | --- |
| Time Machine | 系统自带备份 | Mac 全盘备份 | 系统自带 |
| restic | 加密去重备份 | 服务器/本地/云备份 | `brew install restic` |
| Kopia | GUI+CLI 去重备份 | 想要可视化备份管理 | `brew install --cask kopiaui` |
| BorgBackup | 去重压缩备份 | Linux/服务器用户 | `brew install borgbackup` |
| Arq Backup | 商业云备份 | 想要 GUI+多云备份 | 官网 |

---
