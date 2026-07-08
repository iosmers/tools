# 网络调试、抓包、代理与隧道

HTTP/API 调试、HTTPS 抓包、网络诊断、端口扫描、本地隧道和代理规则管理。

!!! note "维护方式"
    本页是工具百科的一个专题页。新增工具时，请优先补充到对应功能表格中，并保留：核心优势、适合场景、安装方式、官方链接。


## 7. 网络调试、抓包、代理与隧道 {#network-debugging}

### HTTP/API 客户端 {#api-clients}

| 工具 | 核心优势 | 适合场景 | 安装 | 官方链接 |
| --- | --- | --- | --- | --- |
| HTTPie | 语法友好的 HTTP CLI | API 调试、演示 | `brew install httpie` | [官网](https://httpie.io/) |
| xh | Rust HTTP CLI | 快速、语法类似 HTTPie | `brew install xh` | [GitHub](https://github.com/ducaale/xh) |
| hurl | HTTP 测试文件 | API 测试、CI 集成 | `brew install hurl` | [官网](https://hurl.dev/) |
| curl | 标准 HTTP 工具 | 脚本、系统通用 | 系统自带/`brew install curl` | [官网](https://curl.se/) |
| Postman | API 协作平台 | 团队接口管理、文档、Mock | `brew install --cask postman` | [官网](https://www.postman.com/) |
| Bruno | 本地文件化 API 客户端 | Git 管理 API Collection | `brew install --cask bruno` | [官网](https://www.usebruno.com/) |
| Insomnia | API/GraphQL/gRPC 客户端 | 轻量图形 API 调试 | `brew install --cask insomnia` | [官网](https://insomnia.rest/) |
| Hoppscotch | Web API 调试 | 浏览器内快速测试 | Web/自托管 | [官网](https://hoppscotch.io/) |
| Kreya | gRPC/REST 客户端 | gRPC、团队接口测试 | 官网 | [官网](https://kreya.app/) |
| grpcurl | gRPC CLI | 命令行调 gRPC | `brew install grpcurl` | [GitHub](https://github.com/fullstorydev/grpcurl) |

### 抓包 / 代理 / 安全测试

| 工具 | 核心优势 | 适合场景 | 安装 | 官方链接 |
| --- | --- | --- | --- | --- |
| Proxyman | Mac 原生 HTTP/HTTPS 抓包、断点、Map Local | iOS/Android/Web API 调试 | `brew install --cask proxyman` | [官网](https://proxyman.com/) |
| Charles | 经典跨平台 HTTP/HTTPS 代理 | 老牌抓包、弱网、移动端调试 | `brew install --cask charles` | [官网](https://www.charlesproxy.com/) |
| mitmproxy | CLI/TUI/Web 抓包代理，可脚本化 | 自动化测试、可编程抓包 | `brew install mitmproxy` | [官网](https://mitmproxy.org/) |
| Wireshark | 底层网络包分析 | TCP/UDP/协议排障 | `brew install --cask wireshark` | [官网](https://www.wireshark.org/) |
| HTTP Toolkit | 开源 HTTP 调试 | Web/Node/Android 抓包 | 官网 | [官网](https://httptoolkit.com/) |
| Burp Suite | Web 安全测试 | 安全测试、渗透测试 | `brew install --cask burp-suite` | [官网](https://portswigger.net/burp) |
| OWASP ZAP | 开源 Web 安全代理 | 安全扫描学习/CI | `brew install --cask owasp-zap` | [官网](https://www.zaproxy.org/) |

### DNS、测速、端口和隧道

| 功能 | 工具 | 用途 | 安装 |
| --- | --- | --- | --- |
| DNS 查询 | doggo、dog、dig | DNS 排障 | `brew install doggo dog bind` |
| 路由追踪 | mtr、traceroute | 网络路径/丢包 | `brew install mtr` |
| 带宽测试 | iperf3 | 内网/服务器吞吐测试 | `brew install iperf3` |
| 端口扫描 | nmap、rustscan | 端口发现 | `brew install nmap rustscan` |
| 本地隧道 | ngrok、cloudflared、localtunnel | 本地服务暴露给外网 | `brew install ngrok cloudflared localtunnel` |
| 内网穿透 | frp、Tailscale、ZeroTier | 远程访问内网机器 | `brew install frpc tailscale zerotier-one` |
| Hosts 管理 | SwitchHosts | 多环境 hosts 切换 | `brew install --cask switchhosts` |
| 代理规则 | Clash Verge Rev、Surge、Mihomo Party | 本地代理规则管理 | 官网/Homebrew Cask |

---
