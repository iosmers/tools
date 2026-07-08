# SSH、远程连接与云服务器管理

SSH、远程桌面、云厂商 CLI、IaC、服务器访问审计和团队远程管理。

!!! note "维护方式"
    本页是工具百科的一个专题页。新增工具时，请优先补充到对应功能表格中，并保留：核心优势、适合场景、安装方式、官方链接。


## 8. SSH、远程连接与云服务器管理 {#ssh-remote-cloud}

| 工具 | 类型 | 核心优势 | 适合场景 | 安装/获取 |
| --- | --- | --- | --- | --- |
| OpenSSH | CLI | 标准 SSH 客户端/服务端 | 所有远程连接 | 系统自带 |
| mosh | CLI | 移动网络更稳、断线恢复体验好 | 网络不稳定、跨地区 SSH | `brew install mosh` |
| autossh | CLI | 自动重连 SSH 隧道 | 长连接/隧道守护 | `brew install autossh` |
| Termius | GUI SSH | 跨端同步、SFTP、端口转发 | 多设备 SSH 管理 | 官网 |
| Royal TSX | GUI 远程管理 | SSH/RDP/VNC/团队连接管理 | 企业运维、多协议 | 官网 |
| Tabby | GUI 终端/SSH | SSH 分组、SFTP、跨平台 | 多服务器日常管理 | `brew install --cask tabby` |
| SecureCRT | 企业 SSH | 稳定、脚本自动化、企业功能 | 企业/网络设备管理 | 官网 |
| VS Code Remote SSH | 编辑器远程 | 远程服务器上直接开发 | 远程开发 | VS Code 扩展 |
| Tailscale SSH | 零信任 SSH | 基于 WireGuard 的私网访问 | 多机器内网互联 | `brew install tailscale` |
| Teleport | 访问平面 | 审计、短期证书、团队访问控制 | 企业服务器/K8s 访问 | `brew install teleport` |
| Microsoft Remote Desktop / Windows App | RDP | 连接 Windows 机器 | Windows 远程桌面 | App Store |
| RealVNC / Jump Desktop | VNC/RDP | 图形远程桌面 | 跨平台桌面远程 | 官网/App Store |

### 云服务器与 IaC

| 工具 | 用途 | 安装 |
| --- | --- | --- |
| AWS CLI | AWS 资源管理 | `brew install awscli` |
| gcloud CLI | Google Cloud 管理 | `brew install --cask google-cloud-sdk` |
| Azure CLI | Azure 管理 | `brew install azure-cli` |
| doctl | DigitalOcean CLI | `brew install doctl` |
| flyctl | Fly.io CLI | `brew install flyctl` |
| Vercel CLI | 前端部署 | `brew install vercel-cli` |
| Netlify CLI | 前端部署 | `brew install netlify-cli` |
| Terraform | 基础设施即代码 | `brew install terraform` |
| OpenTofu | Terraform 开源替代 | `brew install opentofu` |
| Pulumi | 多语言 IaC | `brew install pulumi` |
| Ansible | 自动化运维 | `brew install ansible` |

---
