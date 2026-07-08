# 手机可操控智能体工具调研

这是一个独立的 Read the Docs/Sphinx 文档项目，目录和配置与其他项目隔离。

本地预览：

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
sphinx-build -b html source build/html
```

部署到 Read the Docs：

1. 把本目录提交到一个 Git 仓库，或作为仓库中的独立子目录。
2. 在 Read the Docs 中导入该仓库。
3. 如果仓库根目录不是本目录，需要在 RTD 项目设置中把配置文件路径指向 `mobile-agent-tools-rtd/.readthedocs.yaml`，或把本目录拆成独立仓库。
4. 构建完成后入口页是 `index.html`。
