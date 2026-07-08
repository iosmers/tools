# 部署指南

本项目使用 **MkDocs + Material for MkDocs + Read the Docs**。Markdown 写在 `developer-tools-site/docs/` 目录中，站点配置写在 `developer-tools-site/mkdocs.yml`，Read the Docs 构建配置写在 `developer-tools-site/.readthedocs.yaml`。

> 注意：为了避免和仓库根目录中的其他文件、其他 AI 的工作产生冲突，本项目不是放在仓库根目录，而是放在 `developer-tools-site/` 子目录。

## 1. 本地预览

```bash
cd developer-tools-site
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

然后访问：

```text
http://127.0.0.1:8000/
```

## 2. 本地构建检查

```bash
cd developer-tools-site
mkdocs build --strict
```

如果构建成功，会生成：

```text
site/
```

`site/` 是静态网页产物，不需要提交到 Git。

## 3. 推送到 GitHub

```bash
git status
git add developer-tools-site
git commit -m "Add developer tools documentation site"
git push origin main
```

## 4. 在 Read the Docs 导入项目

1. 打开 Read the Docs 控制台。
2. 选择 **Import a Project**。
3. 选择 GitHub 仓库 `iosmers/tools`。
4. 保持默认分支为 `main`。
5. 进入项目设置，找到 **Build configuration file** / **配置文件路径**。
6. 设置为：

```text
developer-tools-site/.readthedocs.yaml
```

7. 点击构建。

## 5. 当前构建配置说明

`developer-tools-site/.readthedocs.yaml`：

```yaml
version: 2

build:
  os: ubuntu-24.04
  tools:
    python: "3.12"

python:
  install:
    - requirements: developer-tools-site/requirements.txt

mkdocs:
  configuration: developer-tools-site/mkdocs.yml
```

含义：

- 使用 Read the Docs 配置文件版本 2。
- 使用 Ubuntu 24.04 构建环境。
- 使用 Python 3.12。
- 安装 `developer-tools-site/requirements.txt` 中的 MkDocs 依赖。
- 使用 `developer-tools-site/mkdocs.yml` 构建网站。

Read the Docs 对子目录配置有一个容易踩坑的点：即使 `.readthedocs.yaml` 放在子目录里，配置文件中的路径仍然要相对于仓库根目录填写，所以这里写的是 `developer-tools-site/requirements.txt` 和 `developer-tools-site/mkdocs.yml`，而不是单独写 `requirements.txt` 和 `mkdocs.yml`。

## 6. 常见问题

### 构建日志提示找不到 mkdocs

检查 `requirements.txt` 是否包含：

```text
mkdocs
mkdocs-material
```

### 构建日志提示找不到页面

检查 `mkdocs.yml` 的 `nav` 路径是否和 `docs/` 下的文件名一致。

### 想改网站标题

修改 `developer-tools-site/mkdocs.yml`：

```yaml
site_name: 程序员终端工具箱
```

### 想新增工具

直接编辑 [`tools.md`](tools.md)，增加一个新的工具小节即可。
