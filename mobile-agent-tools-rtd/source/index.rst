================================================
手机可操控智能体工具调研
================================================

.. admonition:: 调研口径
   :class: note

   更新时间：2026-07-08。这里的“手机操纵”按四类理解：手机原生 App、手机浏览器/PWA、手机远程控制桌面或服务器上的 agent、手机 SSH/云终端直接运行 agent。目标场景是用对话方式让 agent 在夜间处理服务器或代码任务。

结论先行
========

如果目标是“晚上让它帮我干活”，最实用的不是把生产服务器完全交出去，而是搭一个受限的 agent 工作面：

* **优先路线**：OpenAI Codex 移动端、Claude Code Remote Control、Omnara 这类“手机控制电脑/服务器上 agent”的工具。它们保留审批、diff、终端输出和上下文，适合长任务中途从手机介入。
* **PR/Issue 路线**：GitHub Copilot cloud agent、Cursor Cloud Agents。适合明确的代码任务，agent 在云环境里开分支、跑测试、提 PR，不适合直接登录生产机。
* **自托管路线**：OpenHands 或手机 SSH/云终端加 Codex CLI、Claude Code、Gemini CLI、Aider。适合你要真正接入自己的服务器，但安全边界必须自己设计。
* **原型路线**：Replit Agent。手机上直接构建、预览、发布 Web App 很顺，但不是“接管你的服务器”的工具。

手机控制能力矩阵
================

.. list-table::
   :header-rows: 1
   :widths: 18 20 20 24 18

   * - 工具
     - 手机入口
     - 工作运行位置
     - 适合服务器/夜间任务吗
     - 资料来源
   * - OpenAI Codex in ChatGPT mobile
     - ChatGPT iOS/Android 内的 Codex 移动体验，可监控、转向、审批任务。
     - 连接到正在运行 Codex 的电脑、devbox 或托管远程环境。
     - **推荐**。适合把 agent 跑在专门的远程开发机，再用手机审批和改方向。
     - `OpenAI Codex mobile <https://openai.com/index/work-with-codex-from-anywhere/>`_, `Codex Cloud <https://developers.openai.com/codex/cloud>`_
   * - Claude Code Remote Control / Claude Code on web
     - Claude mobile app、浏览器、``claude.ai/code``。
     - 可远程接管本地 Claude Code 会话，也可使用云端/隔离环境会话。
     - **推荐**。适合手机继续本地或远程 coding session，Team/Enterprise 默认需要管理员开启远程控制。
     - `Remote Control 文档 <https://docs.anthropic.com/en/docs/claude-code/remote-control>`_, `Claude Code on web <https://www.anthropic.com/news/claude-code-on-the-web>`_, `Claude release notes <https://support.claude.com/en/articles/12138966-release-notes>`_
   * - Omnara
     - Web、桌面、移动端，官方页面也提到 Apple Watch。
     - 控制运行在笔记本、云机器或服务器上的 Claude Code、Codex 等 session。
     - **推荐**。它更像 agent 控制台，适合手机查看进度、审核 diff、回复 agent 问题。
     - `Omnara 官网 <https://www.omnara.com/>`_, `Omnara quickstart <https://docs.omnara.com/quickstart>`_, `Omnara GitHub <https://github.com/omnara-ai/omnara>`_
   * - Cursor Cloud Agents
     - Cursor Web 和移动浏览器/PWA，Slack 也可触发。
     - Cursor 云工作区，通常基于 GitHub 仓库。
     - **适合代码 PR，不适合直接运维**。适合让 agent 开分支、改代码、给 PR。
     - `Cursor on web and mobile <https://cursor.com/blog/agent-web>`_, `Cloud Agents Docs <https://cursor.com/docs/cloud-agent>`_
   * - GitHub Copilot cloud agent
     - GitHub 网站、GitHub Mobile、Issues/PRs、Copilot Chat。
     - GitHub Actions 驱动的云环境。
     - **适合明确 Issue**。强项是开分支、改代码、跑 CI、提 PR；不应直接给生产 SSH。
     - `GitHub Copilot cloud agent <https://docs.github.com/copilot/concepts/agents/cloud-agent/about-cloud-agent>`_, `Start sessions <https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/start-copilot-sessions>`_
   * - Replit Agent
     - Replit 移动 App、移动 Web。
     - Replit 工作区和 Replit 部署环境。
     - **适合原型和小应用**。手机上 prompt、预览、发布方便，但不是接管已有服务器的工具。
     - `Replit mobile <https://replit.com/mobile>`_, `Replit Agent docs <https://docs.replit.com/references/agent/overview>`_
   * - OpenHands / Agent Canvas
     - 浏览器 UI，可自托管后通过 VPN 或内网访问。
     - 本机、Docker/Kubernetes sandbox、OpenHands Cloud。
     - **适合自托管**。能编辑文件、跑命令、接工具，但需要你自己负责暴露方式、鉴权和沙箱。
     - `OpenHands 官网 <https://www.openhands.dev/>`_, `Agent Canvas Docs <https://docs.openhands.dev/openhands/usage/agent-canvas/overview>`_, `OpenHands SDK <https://docs.openhands.dev/sdk/getting-started>`_
   * - Cosyra
     - iOS/Android 原生云终端。
     - 持久 Ubuntu 云容器，内置多种 CLI agent。
     - **适合移动终端派**。它直接把手机变成带 agent 的云 Linux 终端，适合试用，但要评估供应商可靠性和密钥托管方式。
     - `Cosyra mobile guide <https://cosyra.com/guides/ai-coding-agents-mobile.html>`_
   * - 手机 SSH/Termux/Blink/Termius + tmux + CLI agent
     - SSH 客户端或 Android Termux。
     - 你的服务器或跳板机。
     - **控制力最高，风险也最高**。适合熟悉 Linux、tmux、sudo 限权、日志和回滚的人。
     - 本方案主要依赖通用 SSH/tmux 能力，具体 agent 可选 Codex CLI、Claude Code、Aider、OpenHands CLI 等。
   * - Slack/Discord/Telegram ChatOps bot
     - 手机聊天工具。
     - 你部署的 bot 和任务 runner。
     - **适合团队自动化**。适合“跑健康检查、生成报告、开 PR”，不适合把任意 shell 暴露到群聊。
     - 可结合 Omnara、Cursor Slack、GitHub Issue flow 或自研 webhook。

推荐架构
========

用于服务器和代码任务时，建议按下面的边界设计：

.. code-block:: text

   手机
     -> Codex / Claude / Omnara / SSH / ChatOps
     -> agent host: 专用非 root 用户
     -> repo 或 worktree: 独立分支，禁止直接改主分支
     -> CI/test: 自动验证
     -> PR 或变更单: 人工合并
     -> deploy script: 仅允许白名单脚本
     -> 通知: 成功、失败、需要审批

关键原则：

* 不把生产服务器 root shell 直接交给 agent。
* 给 agent 单独用户，例如 ``agent-runner``，默认没有 ``sudo``。
* 如果必须执行运维动作，用 ``sudoers`` 只放行具体脚本，不放行通配命令。
* 工作目录和生产目录分开，agent 只在 repo/worktree、临时目录、日志目录内写入。
* 所有夜间任务必须有“完成定义”：测试命令、回滚命令、不可触碰范围、汇报格式。
* 密钥放在 secret manager 或受限环境变量里，不让 agent 读取云主账号、支付账号、数据库管理员凭据。

夜间任务模板
============

可以给 agent 的任务说明使用这个模板：

.. code-block:: text

   目标：
   - 修复/实现什么，必须交付什么结果。

   范围：
   - 允许修改哪些目录。
   - 禁止修改哪些目录、配置、生产数据。

   命令：
   - 允许运行：npm test, pytest, make lint, docker compose up -d test-db
   - 禁止运行：rm -rf, sudo su, 直接操作生产数据库, 变更云 IAM。

   验收：
   - 必须通过哪些测试。
   - 必须生成 diff、测试日志、风险说明。

   中断条件：
   - 需要 sudo、需要新密钥、测试不稳定、迁移涉及生产数据时立即停止并通知我。

工具选择建议
============

.. list-table::
   :header-rows: 1
   :widths: 28 36 36

   * - 场景
     - 首选
     - 原因
   * - 手机审批长时间 coding task
     - OpenAI Codex mobile、Claude Code Remote Control、Omnara
     - 手机端能看到 live state、审批点、diff 和 agent 问题，适合夜间不断电的任务流。
   * - GitHub Issue 交给 agent 改代码
     - GitHub Copilot cloud agent、Cursor Cloud Agents
     - 云环境执行，天然走分支和 PR，权限面比生产 SSH 小。
   * - 从手机做 Web/App 原型
     - Replit Agent
     - 移动 App 和 Web 工作流完整，预览和部署路径短。
   * - 自己控制模型、沙箱、内网
     - OpenHands、LiteLLM/New API 网关、VPN 内访问
     - 适合私有部署，但需要工程化和安全投入。
   * - 真的要操作服务器
     - SSH + tmux + CLI agent，或 OpenHands 自托管
     - 控制力强，必须配合最小权限、日志、回滚和手动审批。

落地清单
========

1. 准备一台 agent host，不要直接使用生产机。
2. 建立 ``agent-runner`` 用户，只给 repo、测试环境、临时目录权限。
3. 选择一种手机控制面：Codex mobile、Claude Remote Control、Omnara，或 SSH/云终端。
4. 所有任务通过 Git 分支或 PR 交付，不让 agent 直接修改主分支。
5. 给夜间任务加预算限制、最长运行时间、日志保存和通知。
6. 生产变更必须走白名单部署脚本和人工确认。

来源汇总
========

* OpenAI Codex mobile: https://openai.com/index/work-with-codex-from-anywhere/
* OpenAI Codex Cloud: https://developers.openai.com/codex/cloud
* OpenAI Codex safety: https://openai.com/index/running-codex-safely/
* Claude Code Remote Control: https://docs.anthropic.com/en/docs/claude-code/remote-control
* Claude Code on web: https://www.anthropic.com/news/claude-code-on-the-web
* Claude release notes: https://support.claude.com/en/articles/12138966-release-notes
* Omnara: https://www.omnara.com/
* Cursor Web/Mobile Agents: https://cursor.com/blog/agent-web
* GitHub Copilot cloud agent: https://docs.github.com/copilot/concepts/agents/cloud-agent/about-cloud-agent
* Replit mobile: https://replit.com/mobile
* Replit Agent: https://docs.replit.com/references/agent/overview
* OpenHands: https://www.openhands.dev/
* OpenHands Agent Canvas: https://docs.openhands.dev/openhands/usage/agent-canvas/overview
* Cosyra guide: https://cosyra.com/guides/ai-coding-agents-mobile.html
