# 容器、虚拟化、本地开发环境与 Kubernetes

Docker 替代方案、Linux VM、本地 Kubernetes、容器镜像分析和 K8s 工具。

!!! note "维护方式"
    本页是工具百科的一个专题页。新增工具时，请优先补充到对应功能表格中，并保留：核心优势、适合场景、安装方式、官方链接。


## 14. 容器、虚拟化、本地开发环境与 Kubernetes {#containers-kubernetes}

### 容器运行环境

| 工具 | 核心优势 | 适合场景 | 安装/获取 |
| --- | --- | --- | --- |
| Docker Desktop | 官方 Docker 桌面环境、生态完整 | 企业标准、Docker 官方工作流 | `brew install --cask docker` |
| OrbStack | Mac 上运行 Docker/Linux，轻量快速 | Mac 本地容器和 Linux VM | `brew install --cask orbstack` |
| Colima | 基于 Lima 的轻量 Docker 环境 | 免费开源、CLI 用户 | `brew install colima docker` |
| Rancher Desktop | Kubernetes + containerd/Docker | 本地 K8s 开发 | `brew install --cask rancher` |
| Podman Desktop | 无 daemon 容器生态 | Podman/Red Hat 生态 | `brew install --cask podman-desktop` |
| Lima | Linux VM 管理 | 自定义 Linux 开发环境 | `brew install lima` |
| Multipass | Ubuntu VM | 快速起 Ubuntu | `brew install --cask multipass` |

### 虚拟机

| 工具 | 核心优势 | 适合场景 | 获取方式 |
| --- | --- | --- | --- |
| UTM | 免费开源、Apple Virtualization/模拟 | Linux/Windows VM、ARM 设备 | `brew install --cask utm` |
| Parallels Desktop | 商业虚拟机、体验成熟 | Windows on Mac、企业桌面 | 官网 |
| VMware Fusion | 老牌虚拟机 | VMware 用户 | 官网 |
| Tart | macOS/Linux VM 自动化 | CI、自动化构建 | `brew install cirruslabs/cli/tart` |
| Vagrant | VM 开发环境描述 | 老项目/团队一致环境 | `brew install vagrant` |

### Kubernetes / 容器运维

| 工具 | 用途 | 安装 |
| --- | --- | --- |
| kubectl | Kubernetes 标准 CLI | `brew install kubectl` |
| k9s | Kubernetes TUI | `brew install k9s` |
| kubectx / kubens | context/namespace 切换 | `brew install kubectx` |
| Helm | K8s 包管理 | `brew install helm` |
| Kustomize | YAML overlay | `brew install kustomize` |
| stern | 多 Pod 日志聚合 | `brew install stern` |
| Lens / OpenLens | K8s GUI | 官网/GitHub |
| kind | 本地 K8s 集群 | `brew install kind` |
| minikube | 本地 K8s | `brew install minikube` |
| Tilt | 本地 K8s 开发循环 | `brew install tilt` |
| Skaffold | K8s 开发部署流水线 | `brew install skaffold` |
| lazydocker | Docker TUI | `brew install lazydocker` |
| dive | Docker 镜像层分析 | `brew install dive` |
| trivy | 容器/依赖漏洞扫描 | `brew install trivy` |

---
