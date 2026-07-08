================================================
一站式多模型 API 平台调研
================================================

.. admonition:: 调研口径
   :class: note

   更新时间：2026-07-08。这里的“一站式 token 调所有模型”不是字面上的所有模型，而是指：一个 API key、一个 base URL、统一计费或统一路由，尽量接入 OpenAI、Anthropic、Google、DeepSeek、Qwen、Meta、Mistral、xAI、图片、语音、视频等多类模型。

结论先行
========

* **最快上手、国际模型覆盖广**：OpenRouter、Vercel AI Gateway、AI/ML API、Eden AI。
* **要自托管、自己管理多个供应商 key**：New API、LiteLLM Proxy、Portkey Gateway。
* **要中国大陆网络和国产模型优先**：302.AI、SiliconFlow、阿里云百炼、火山方舟、ModelScope。
* **企业合规和云账号统一治理**：AWS Bedrock、Azure AI Foundry Models、Google Model Garden。

最适合“给服务器 agent 配一个统一 token”的组合通常是：

1. 个人或小团队：OpenRouter 或 302.AI 做托管入口。
2. 自己管密钥和预算：LiteLLM 或 New API 自托管。
3. 企业环境：Portkey、Vercel AI Gateway 或云厂商模型平台。

平台对比矩阵
============

.. list-table::
   :header-rows: 1
   :widths: 18 16 26 24 16

   * - 平台
     - 类型
     - 覆盖与接口
     - 适合场景
     - 资料来源
   * - OpenRouter
     - 托管聚合 API
     - OpenAI-compatible，一套 ``/api/v1/chat/completions``，聚合主流 LLM 和路由能力。
     - 个人开发、agent、快速试模型、按模型 fallback。
     - `OpenRouter quickstart <https://openrouter.ai/docs/quickstart>`_, `OpenRouter FAQ <https://openrouter.ai/docs/faq>`_
   * - Vercel AI Gateway
     - 托管 AI Gateway
     - 官方称一个 endpoint 访问数百模型，支持预算、监控、负载均衡和 fallback；也提供 OpenAI Chat Completions 兼容端点。
     - 已经用 Vercel/AI SDK 的团队，或需要前端和 agent 统一模型路由。
     - `Vercel AI Gateway docs <https://vercel.com/docs/ai-gateway>`_, `OpenAI Chat compatible endpoint <https://vercel.com/docs/ai-gateway/sdks-and-apis/openai-chat-completions>`_
   * - AI/ML API
     - 托管聚合 API
     - 官方页面宣称 1000+ AI models，覆盖文本、推理、图像、视频、音频、搜索等，OpenAI-compatible。
     - 想用一个账单覆盖多模态模型，尤其是需要图片/视频模型时。
     - `AI/ML API 官网 <https://aimlapi.com/>`_
   * - Eden AI
     - 托管聚合 API
     - 官方称 500+ LLM 和专家模型，支持成本、性能、区域路由与 fallback。
     - 除 LLM 外还要 OCR、语音、翻译、图像等传统 AI API 的团队。
     - `Eden AI 官网 <https://www.edenai.co/>`_
   * - 302.AI
     - 托管聚合 API
     - 文档说明与 OpenAI API Reference 对齐，替换 base URL 即可迁移；同一账号 API key 调用多类 302.AI API。
     - 国内用户接入国际/多模型资源，常见工具替换 base URL。
     - `302.AI API docs <https://doc-en.302.ai/>`_, `API migration guide <https://doc-en.302.ai/5030894m0>`_
   * - New API
     - 开源自托管网关
     - AI API gateway 和用量管理系统，支持把 OpenAI、Anthropic、Gemini、DeepSeek、Midjourney、Suno 等服务统一到 OpenAI/Claude/Gemini 兼容格式。
     - 想自己部署“类 New API”面板、渠道、额度、用户 token、模型映射。
     - `New API docs <https://docs.newapi.pro/en/docs/guide/wiki/basic-concepts/project-introduction>`_, `New API GitHub <https://github.com/QuantumNous/new-api>`_
   * - LiteLLM Proxy
     - 开源自托管网关
     - OpenAI-compatible proxy，官方文档称可用统一接口调用 100+ LLM，并支持虚拟 key、预算、用量追踪。
     - 团队内部标准网关、agent 统一出口、按用户限额、供应商 fallback。
     - `LiteLLM docs <https://docs.litellm.ai/docs/>`_, `LiteLLM proxy <https://docs.litellm.ai/docs/simple_proxy>`_
   * - Portkey Gateway
     - 开源/托管企业网关
     - 统一 API、观测、重试、fallback、guardrails、预算；GitHub 项目称可路由 250+ LLM 和 1600+ 多模态模型。
     - 生产环境治理、多团队、多供应商、审计和可靠性要求高。
     - `Portkey Gateway GitHub <https://github.com/Portkey-AI/gateway>`_, `Portkey AI Gateway <https://portkey.ai/features/ai-gateway>`_
   * - SiliconFlow
     - 模型服务平台
     - 官方称 200+ 优化 LLM 和多模态模型，OpenAI-compatible，一套 API 调用多模型。
     - 国内网络、国产开源模型、DeepSeek/Qwen/Llama 等推理。
     - `SiliconFlow docs <https://docs.siliconflow.com/en/api-reference/chat-completions/chat-completions>`_, `SiliconFlow 官网 <https://www.siliconflow.com/>`_
   * - 阿里云百炼
     - 云厂商模型平台
     - 一站式大模型开发与应用平台，集成千问及主流第三方模型；提供 OpenAI 兼容 API。
     - 阿里云账号体系、企业合规、国内模型和应用构建。
     - `百炼概览 <https://help.aliyun.com/zh/model-studio/what-is-model-studio>`_, `OpenAI 兼容 <https://help.aliyun.com/zh/model-studio/compatibility-of-openai-with-dashscope>`_
   * - 火山方舟
     - 云厂商模型平台
     - 方舟模型 API 尽可能兼容 OpenAI API，修改 base URL、model、api_key 等即可接入。
     - 字节/火山生态、豆包、国内模型、企业部署。
     - `火山方舟 OpenAI 兼容 <https://www.volcengine.com/docs/82379/1330626>`_
   * - ModelScope API Inference
     - 模型社区/服务平台
     - 文档说明 LLM API Inference 提供 OpenAI API-compatible 接口。
     - 模型社区试用、国产/开源模型实验、评测任务。
     - `ModelScope API Inference <https://modelscope.ai/docs/model-service/API-Inference/intro>`_
   * - AWS Bedrock
     - 云厂商模型平台
     - AWS 文档称 Bedrock 支持 100+ foundation models，并通过 Converse/InvokeModel 等 API 调用。
     - AWS 企业账号、IAM、私有网络、合规审计。
     - `Bedrock overview <https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html>`_, `Model access <https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html>`_
   * - Azure AI Foundry Models
     - 云厂商模型平台
     - 模型目录包含 Microsoft/OpenAI/Anthropic/DeepSeek/xAI/Hugging Face/Meta/Mistral/Cohere 等模型。
     - Azure 企业账号、Microsoft 生态、区域与合规管理。
     - `Azure Foundry Models <https://azure.microsoft.com/en-us/products/ai-foundry/models>`_
   * - Google Model Garden
     - 云厂商模型平台
     - Google Cloud 文档称 Model Garden 是发现、测试、定制、部署 Google 与合作伙伴模型的一站式目录。
     - Google Cloud 账号、Gemini 与合作伙伴模型、云端 MLOps。
     - `Google Model Garden <https://cloud.google.com/model-garden>`_, `Model Garden docs <https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models>`_

怎么选
======

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - 目标
     - 推荐
     - 理由
   * - 快速给 agent 一个统一 API key
     - OpenRouter、302.AI、Vercel AI Gateway
     - 少改代码，替换 ``base_url`` 和 ``model`` 就能试很多模型。
   * - 自己控制用户、额度、渠道和密钥
     - New API、LiteLLM Proxy
     - 自托管后可给每个 agent 发虚拟 key，限制预算和模型范围。
   * - 生产治理和审计
     - Portkey、Vercel AI Gateway、AWS Bedrock、Azure AI Foundry
     - 有观测、预算、fallback、团队管理或云厂商 IAM。
   * - 国内网络和人民币结算
     - 302.AI、SiliconFlow、阿里云百炼、火山方舟、ModelScope
     - 国内访问、国内模型覆盖和云合规路径更直接。
   * - 多模态模型多
     - AI/ML API、Eden AI、Portkey、OpenRouter
     - 图片、视频、音频、OCR、语音等非纯文本模型覆盖更广。

给服务器 agent 的基线配置
=========================

无论选择哪个平台，都建议这样接：

.. code-block:: text

   agent process
     -> 内部统一 base_url
     -> 网关层: New API / LiteLLM / Portkey / OpenRouter / 302.AI
     -> 多模型供应商

   每个 agent:
     - 单独 virtual key
     - 单独预算
     - 单独可用模型列表
     - 单独日志和 trace id

配置原则：

* 不把主账号 key 写进 agent 的环境变量，只给虚拟 key。
* 给夜间任务设置每日预算、RPM/TPM 限制和最长运行时间。
* 低风险任务用便宜模型，复杂代码修改再升级到强模型。
* 为常用模型设置 fallback，例如主模型失败时切换到同能力层级备选模型。
* 对生产操作类 agent 关闭自动提权和任意工具调用，保留审批点。
* 记录请求 ID、模型、成本、输入输出 token、失败原因，便于第二天审计。

OpenAI-compatible 示例
======================

多数网关可以用 OpenAI SDK 或兼容请求格式，只替换 ``base_url`` 和 key。示例仅说明形态，不包含真实密钥：

.. code-block:: python

   from openai import OpenAI

   client = OpenAI(
       api_key="YOUR_GATEWAY_KEY",
       base_url="https://YOUR_GATEWAY_BASE_URL/v1",
   )

   response = client.chat.completions.create(
       model="provider/model-name",
       messages=[
           {"role": "user", "content": "Summarize this incident log."}
       ],
   )

   print(response.choices[0].message.content)

注意事项
========

* “OpenAI-compatible”通常覆盖 Chat Completions，但并不保证所有参数、工具调用、Responses API、音视频、文件、批处理都完全一致。
* 模型名、价格、上下文长度、区域可用性会频繁变化，应以平台模型列表和官方价格为准。
* 国际聚合平台可能涉及跨境数据和供应商条款，企业或敏感数据必须先做合规评审。
* 中国大陆平台不等于能调用所有国际模型，国际平台也不等于在大陆网络稳定。
* 自托管 New API/LiteLLM/Portkey 时，网关本身也会成为生产基础设施，需要备份数据库、监控、限流和升级策略。

落地清单
========

1. 先选一个托管平台快速验证模型效果，例如 OpenRouter、302.AI 或 Vercel AI Gateway。
2. 如果要给多个 agent 长期使用，再上 New API 或 LiteLLM 自托管。
3. 为每个 agent 创建独立 key，并设置预算、模型 allowlist、最大上下文和速率限制。
4. 在网关层做日志和成本看板，第二天能复盘每个夜间任务花了多少 token。
5. 为核心模型配置至少一个 fallback。
6. 把网关 base URL 抽成环境变量，避免业务代码写死供应商。

来源汇总
========

* OpenRouter: https://openrouter.ai/docs/quickstart
* LiteLLM: https://docs.litellm.ai/docs/
* LiteLLM Proxy: https://docs.litellm.ai/docs/simple_proxy
* Portkey Gateway: https://github.com/Portkey-AI/gateway
* Vercel AI Gateway: https://vercel.com/docs/ai-gateway
* Eden AI: https://www.edenai.co/
* AI/ML API: https://aimlapi.com/
* New API docs: https://docs.newapi.pro/en/docs/guide/wiki/basic-concepts/project-introduction
* New API GitHub: https://github.com/QuantumNous/new-api
* 302.AI API docs: https://doc-en.302.ai/
* SiliconFlow: https://www.siliconflow.com/
* 阿里云百炼: https://help.aliyun.com/zh/model-studio/what-is-model-studio
* 火山方舟: https://www.volcengine.com/docs/82379/1330626
* ModelScope API Inference: https://modelscope.ai/docs/model-service/API-Inference/intro
* AWS Bedrock: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html
* Azure AI Foundry Models: https://azure.microsoft.com/en-us/products/ai-foundry/models
* Google Model Garden: https://cloud.google.com/model-garden
