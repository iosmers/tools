# 代码质量、测试、性能与安全扫描

Lint、format、类型检查、压测、漏洞扫描、Secret 扫描、SBOM 和签名。

!!! note "维护方式"
    本页是工具百科的一个专题页。新增工具时，请优先补充到对应功能表格中，并保留：核心优势、适合场景、安装方式、官方链接。


## 19. 代码质量、测试、性能与安全扫描

| 方向 | 工具 | 用途 | 安装 |
| --- | --- | --- | --- |
| Python lint/format | ruff | Python 检查/格式化 | `brew install ruff` |
| Python 类型 | pyright、mypy | 类型检查 | `brew install pyright mypy` |
| JS/TS lint | eslint、biome | 前端 lint/format | `brew install eslint biome` |
| Shell | shellcheck、shfmt | Shell 检查/格式化 | `brew install shellcheck shfmt` |
| Dockerfile | hadolint | Dockerfile lint | `brew install hadolint` |
| YAML | yamllint、yamlfmt | YAML 检查/格式化 | `brew install yamllint yamlfmt` |
| GitHub Actions | actionlint | Workflow 检查 | `brew install actionlint` |
| 拼写 | typos、codespell | 代码拼写检查 | `brew install typos-cli codespell` |
| 文档风格 | vale | 文档 lint | `brew install vale` |
| 负载测试 | k6、wrk、oha、hey | HTTP 压测 | `brew install k6 wrk oha hey` |
| Python 压测 | locust | 场景化压测 | `brew install locust` |
| 漏洞扫描 | trivy、grype、osv-scanner | 依赖/镜像漏洞 | `brew install trivy grype osv-scanner` |
| Secret 扫描 | gitleaks、detect-secrets | 防止密钥提交 | `brew install gitleaks detect-secrets` |
| SBOM | syft | 软件物料清单 | `brew install syft` |
| 签名 | cosign | 容器/制品签名 | `brew install cosign` |
| 许可证 | licensee、scancode-toolkit | 许可证识别 | `brew install licensee` |

---
