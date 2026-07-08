# Mac 开发效率工具箱

这是一个准备用于部署到 Read the Docs 的 MkDocs 文档站点，内容是 Mac 程序员常用的全维度开发效率工具百科，覆盖终端、Shell、文件、存储、网络、远程连接、系统监控、窗口管理、剪贴板、编辑器、Git、容器、数据库、密码密钥、自动化、文档、截图媒体、Web 调试、AI/LLM 开发等方向。

> 本站点放在仓库的 `developer-tools-site/` 子目录中，避免和仓库根目录的其他脚本或其他 AI 的工作产生冲突。

## 本地预览

```bash
cd developer-tools-site
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

浏览器打开 `http://127.0.0.1:8000/` 即可预览。

## 本地构建检查

```bash
cd developer-tools-site
mkdocs build --strict
```

构建产物会生成到 `site/`，该目录已加入 `.gitignore`。

## Read the Docs 部署

仓库根目录已包含：

- `developer-tools-site/.readthedocs.yaml`：Read the Docs 构建配置。
- `developer-tools-site/requirements.txt`：MkDocs 与 Material for MkDocs 依赖。
- `developer-tools-site/mkdocs.yml`：站点导航、主题、Markdown 扩展配置。
- `developer-tools-site/docs/`：Markdown 页面源码。

其中：

- `docs/tools.md`：快速总览和百科入口。
- `docs/categories/`：按功能拆分后的工具百科专题页。

把仓库推送到 GitHub 后，在 Read the Docs 导入该仓库，并把配置文件路径设置为 `developer-tools-site/.readthedocs.yaml` 即可构建。详细步骤见 [`docs/deploy.md`](docs/deploy.md)。
