# 使用说明

本文档说明当前工作区里两个 Read the Docs 文档项目的用途、预览方式、部署方式和后续维护方法。

## 项目目录

当前新增了两个互相独立的文档项目：

```text
mobile-agent-tools-rtd/
  .readthedocs.yaml
  requirements.txt
  README.md
  source/
    conf.py
    index.rst
    _static/custom.css

model-api-gateways-rtd/
  .readthedocs.yaml
  requirements.txt
  README.md
  source/
    conf.py
    index.rst
    _static/custom.css
```

两个项目用途分别是：

- `mobile-agent-tools-rtd/`：手机上操控智能体工具的调研页面。
- `model-api-gateways-rtd/`：一站式多模型 API 平台的调研页面。

根目录下的 `.venv-rtd/` 是本地构建验证用的 Python 虚拟环境，已经被 `.gitignore` 忽略，不需要提交。

## 本地预览

如果已经有根目录的 `.venv-rtd/`，可以直接构建：

```bash
cd /Users/jyxc-dz-0101455/tools

.venv-rtd/bin/sphinx-build -b html mobile-agent-tools-rtd/source mobile-agent-tools-rtd/build/html
.venv-rtd/bin/sphinx-build -b html model-api-gateways-rtd/source model-api-gateways-rtd/build/html
```

构建完成后打开：

- `mobile-agent-tools-rtd/build/html/index.html`
- `model-api-gateways-rtd/build/html/index.html`

如果换了一台机器，没有 `.venv-rtd/`，先创建环境：

```bash
cd /Users/jyxc-dz-0101455/tools

python3 -m venv .venv-rtd
.venv-rtd/bin/pip install -r mobile-agent-tools-rtd/requirements.txt
```

两个项目使用同一套 Sphinx 依赖，所以安装任意一个项目的 `requirements.txt` 即可。

## 严格构建检查

提交前建议用 `-W --keep-going` 检查。这个模式会把 Sphinx 警告当成失败，适合提前发现 RST 表格、标题层级和链接问题。

```bash
cd /Users/jyxc-dz-0101455/tools/mobile-agent-tools-rtd
../.venv-rtd/bin/sphinx-build -W --keep-going -b html source build/html

cd /Users/jyxc-dz-0101455/tools/model-api-gateways-rtd
../.venv-rtd/bin/sphinx-build -W --keep-going -b html source build/html
```

当前两份文档都已经通过过这个检查。

## 部署到 Read the Docs

有两种部署方式。

### 方式一：拆成两个独立仓库

这是最简单、最稳定的方式。

1. 把 `mobile-agent-tools-rtd/` 单独放入一个 Git 仓库。
2. 把 `model-api-gateways-rtd/` 单独放入另一个 Git 仓库。
3. 在 Read the Docs 创建两个项目，分别导入对应仓库。
4. Read the Docs 会自动识别仓库根目录下的 `.readthedocs.yaml`。

适合希望两个页面完全独立管理、独立构建、独立域名的情况。

### 方式二：保留在一个 monorepo

如果要保留当前目录结构，也可以在同一个仓库里建两个 RTD 项目。

1. 提交整个 `tools` 仓库。
2. 在 Read the Docs 创建第一个项目，配置文件路径填写：

   ```text
   mobile-agent-tools-rtd/.readthedocs.yaml
   ```

3. 创建第二个项目，配置文件路径填写：

   ```text
   model-api-gateways-rtd/.readthedocs.yaml
   ```

4. 两个 RTD 项目指向同一个 Git 仓库，但使用不同的配置文件。

适合你还想让另一个 AI 或其他自动化流程继续在同一个仓库里协作。

## 更新内容

主要编辑这两个文件：

```text
mobile-agent-tools-rtd/source/index.rst
model-api-gateways-rtd/source/index.rst
```

常见更新流程：

```bash
cd /Users/jyxc-dz-0101455/tools

# 编辑 RST 文件后构建检查
.venv-rtd/bin/sphinx-build -W --keep-going -b html mobile-agent-tools-rtd/source mobile-agent-tools-rtd/build/html
.venv-rtd/bin/sphinx-build -W --keep-going -b html model-api-gateways-rtd/source model-api-gateways-rtd/build/html

# 查看变更
git status --short
git diff
```

如果只是更新其中一个文档，只构建对应项目即可。

## Git 提交建议

推荐提交这些文件：

```text
.gitignore
USAGE.md
mobile-agent-tools-rtd/
model-api-gateways-rtd/
```

不要提交：

```text
.venv-rtd/
mobile-agent-tools-rtd/build/
model-api-gateways-rtd/build/
```

这三类目录都是本地生成物，已经通过 `.gitignore` 或项目内 `.gitignore` 忽略。

## RST 写作注意事项

- 标题层级要保持一致，例如主标题用 `====`，二级标题也用固定样式。
- 表格内容较多时优先用 `.. list-table::`，不要手写复杂 ASCII 表格。
- 外部链接格式使用：

  ```rst
  `链接文字 <https://example.com/>`_
  ```

- 代码块使用：

  ```rst
  .. code-block:: bash

     echo "hello"
  ```

- 修改后一定跑一次 Sphinx 构建，RST 的缩进和空行错误很常见。

## 常见问题

### Read the Docs 找不到配置文件

检查 RTD 项目里的配置文件路径。

如果是独立仓库，路径通常是：

```text
.readthedocs.yaml
```

如果是当前这种 monorepo，两个项目应分别填写：

```text
mobile-agent-tools-rtd/.readthedocs.yaml
model-api-gateways-rtd/.readthedocs.yaml
```

### 本地没有 Sphinx

使用根目录虚拟环境安装：

```bash
python3 -m venv .venv-rtd
.venv-rtd/bin/pip install -r mobile-agent-tools-rtd/requirements.txt
```

### pip 下载慢或超时

可以提高超时时间重试：

```bash
.venv-rtd/bin/pip install --default-timeout 120 --retries 5 -r mobile-agent-tools-rtd/requirements.txt
```

### 构建时出现链接警告

先确认链接是否仍然有效。调研类文档里很多产品页面和模型页面会变化，必要时更新来源链接和更新时间。

### 页面样式太窄

两个项目都在 `source/_static/custom.css` 中设置了更宽的正文区域：

```css
.wy-nav-content {
  max-width: 1180px;
}
```

如果后续表格更宽，可以适当调大这个值。

## 建议后续动作

1. 先决定是两个独立仓库部署，还是 monorepo 里创建两个 RTD 项目。
2. 提交当前新增文件。
3. 在 Read the Docs 导入项目并触发第一次构建。
4. 发布后把线上链接补回两个项目的 README 或本文档。
