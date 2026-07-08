# 密码、密钥、证书与开发者安全

密码管理、SSH Key、硬件密钥、证书、本地加密、团队 Secrets 和云凭据。

!!! note "维护方式"
    本页是工具百科的一个专题页。新增工具时，请优先补充到对应功能表格中，并保留：核心优势、适合场景、安装方式、官方链接。


## 16. 密码、密钥、证书与开发者安全 {#secrets-security}

| 工具 | 类型 | 核心优势 | 适合场景 | 安装/获取 |
| --- | --- | --- | --- | --- |
| 1Password | 密码/SSH Key/Secrets | SSH Agent、团队共享、跨端 | 团队和个人密码管理 | 官网 |
| Bitwarden | 开源密码管理 | 开源、可自托管、性价比高 | 个人/团队/自托管 | `brew install --cask bitwarden` |
| KeePassXC | 本地密码库 | 离线、开源、文件自管 | 不想上云 | `brew install --cask keepassxc` |
| macOS Keychain Access | 系统钥匙串 | 系统证书/密码管理 | 证书、系统凭据 | 系统自带 |
| Secretive | SSH Agent | Secure Enclave 存 SSH Key | 本地高安全 SSH | `brew install --cask secretive` |
| YubiKey Manager | 硬件密钥管理 | FIDO2/PIV/OTP | 硬件 2FA、SSH/GPG | `brew install --cask yubico-yubikey-manager` |
| GnuPG / GPG Suite | GPG 签名加密 | Git commit 签名、邮件加密 | 开源签名流程 | `brew install gnupg` |
| age | 简单文件加密 | 替代复杂 GPG 场景 | 配置/文件加密 | `brew install age` |
| sops | Secrets 加密 YAML/JSON | GitOps/K8s secrets | 团队密钥文件 | `brew install sops` |
| gopass / pass | CLI 密码管理 | Unix 哲学、Git 同步 | 终端用户 | `brew install gopass pass` |
| HashiCorp Vault | Secrets 管理 | 企业动态密钥 | 平台工程 | `brew install vault` |
| Doppler | Secrets 平台 | 环境变量/多环境配置 | SaaS 团队 | `brew install dopplerhq/cli/doppler` |
| AWS Vault | AWS 凭据隔离 | 多 AWS 账号 | 云开发 | `brew install aws-vault` |
| mkcert | 本地 HTTPS 证书 | 本地开发 HTTPS | `brew install mkcert` |
| certbot | Let's Encrypt 证书 | 服务器证书自动化 | `brew install certbot` |
| step CLI | 私有 CA/证书 | 内部证书体系 | `brew install step` |

---
