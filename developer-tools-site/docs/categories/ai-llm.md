# AI / LLM 本地开发与辅助工具

本地模型运行、LLM Web UI、AI 编程 CLI、模型 API 网关和本地推理工具。

!!! note "维护方式"
    本页是工具百科的一个专题页。新增工具时，请优先补充到对应功能表格中，并保留：核心优势、适合场景、安装方式、官方链接。


## 23. AI / LLM 本地开发与辅助工具 {#ai-llm}

| 工具 | 类型 | 核心优势 | 适合场景 | 安装/获取 |
| --- | --- | --- | --- | --- |
| Ollama | 本地模型运行 | 一条命令运行本地 LLM | 本地实验、离线测试 | `brew install ollama` |
| LM Studio | 本地模型 GUI | 下载/运行/聊天/本地 API | 非 CLI 用户、本地模型评估 | 官网 |
| llama.cpp | 推理引擎 | GGUF、本地 CPU/GPU 推理 | 深度调参/研究 | `brew install llama.cpp` |
| Open WebUI | LLM Web UI | 连接 Ollama/OpenAI 兼容 API | 内部聊天界面 | Docker/pip |
| Continue | IDE AI 助手 | 连接本地/云模型 | VS Code/JetBrains AI | 扩展 |
| Aider | AI 结对编程 CLI | Git-aware 代码修改 | 终端 AI 编程 | `pipx install aider-chat` |
| Fabric | Prompt/AI 工作流 | 命令行总结/提取模式 | 文档和命令行 AI | GitHub |
| Simon Willison `llm` | LLM CLI | 多模型 CLI、插件 | 脚本化 LLM 调用 | `brew install llm` |
| vLLM | 高吞吐推理服务 | Linux/服务器推理 | GPU 服务端部署 | pip/Docker |
| LiteLLM | LLM API 网关 | 多模型统一 API | 团队模型网关 | pip/Docker |

> 注意：AI 编程工具会读取代码上下文。公司项目、密钥、客户数据、未公开代码要遵守团队安全规范。

---
