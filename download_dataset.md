# MMMU / MMMU_Pro 数据集完整下载指南
## 目录
1. 前置依赖安装
2. 方式一：Hugging Face 镜像加载（推荐，macOS 无兼容坑）
   2.1 Python datasets 库自动下载
   2.2 Git LFS 完整克隆离线文件
   2.3 huggingface-cli 命令行下载
3. 方式二：阿里 ModelScope 国内镜像下载（无需外网）
   3.1 Python 代码下载（修复导入错误版）
   3.2 终端命令行下载
4. 官方配套脚本下载
5. 国内加速关键配置
6. 报错问题修复
7. 数据集区别简要说明
8. 论文引用

## 1. 前置依赖安装
```bash
pip install datasets huggingface_hub pillow -i https://pypi.tuna.tsinghua.edu.cn/simple
# ModelScope 额外依赖（国内镜像专用）
pip install modelscope --upgrade -i https://pypi.tuna.tsinghua.edu.cn/simple
# Git LFS（克隆完整仓库必需）
# Mac
brew install git-lfs
# Ubuntu
apt install git-lfs
# 初始化lfs
git lfs install
```

## 2. 方式一：Hugging Face 国内镜像（hf-mirror）
### 2.1 Python datasets 库一键加载（自动缓存图片）
终端先配置镜像（每次终端生效，可写入 ~/.zshrc 永久生效）
```bash
export HF_ENDPOINT=https://hf-mirror.com
```
```python
from datasets import load_dataset

# 1. 原版 MMMU
ds_mmmu = load_dataset("MMMU/MMMU", cache_dir="./mmmu_cache")
print(ds_mmmu["test"][0])

# 2. MMMU_Pro 多配置选择
# 10高干扰选项标准版
ds_pro_10 = load_dataset("MMMU/MMMU_Pro", "standard (10 options)", cache_dir="./mmmu_pro_cache")
# 仅视觉子集（题干在图片内）
ds_pro_vision = load_dataset("MMMU/MMMU_Pro", "vision_only", cache_dir="./mmmu_pro_cache")
print(ds_pro_10["test"][0])
```
流式加载不占内存（超大数据集推荐）
```python
ds_stream = load_dataset("MMMU/MMMU", streaming=True)
```

### 2.2 Git LFS 完整克隆离线文件
```bash
# MMMU 原版
git clone https://hf-mirror.com/datasets/MMMU/MMMU
# MMMU_Pro
git clone https://hf-mirror.com/datasets/MMMU/MMMU_Pro
```

### 2.3 huggingface-cli 命令行下载
```bash
# MMMU
huggingface-cli download MMMU/MMMU --local-dir ./mmmu
# MMMU_Pro
huggingface-cli download MMMU/MMMU_Pro --local-dir ./mmmu_pro
```

## 3. 方式二：ModelScope 国内镜像（无外网）
### 3.1 Python 代码（修复导入错误：使用 dataset_snapshot_download）
```python
# 错误写法：from modelscope import snapshot_dataset
# 正确导入
from modelscope import dataset_snapshot_download

# 下载 MMMU
mmmu_path = dataset_snapshot_download(
    "AI-ModelScope/MMMU",
    local_dir="./mmmu"
)
print("MMMU 本地路径：", mmmu_path)

# 下载 MMMU_Pro
mmmu_pro_path = dataset_snapshot_download(
    "AI-ModelScope/MMMU_Pro",
    local_dir="./mmmu_pro"
)
print("MMMU_Pro 本地路径：", mmmu_pro_path)
```

### 3.2 终端命令行下载
```bash
# MMMU
modelscope download --dataset AI-ModelScope/MMMU --local_dir ./mmmu
# MMMU_Pro
modelscope download --dataset AI-ModelScope/MMMU_Pro --local_dir ./mmmu_pro
```

## 4. 官方评测仓库内置下载脚本
```bash
# 拉取官方代码
git clone https://github.com/MMMU-Benchmark/MMMU.git
cd MMMU
pip install -r requirements.txt

# 下载原版MMMU
python download_dataset.py --dataset_name MMMU/MMMU
# 下载MMMU_Pro
python download_dataset.py --dataset_name MMMU/MMMU_Pro
```

## 5. 国内加速永久配置
### Mac/Linux 永久生效
```bash
echo 'export HF_ENDPOINT=https://hf-mirror.com' >> ~/.zshrc
source ~/.zshrc
```
### Windows CMD 临时
```cmd
set HF_ENDPOINT=https://hf-mirror.com
```

## 6. 常见报错修复
### 6.1 ImportError: cannot import name 'snapshot_dataset'
原因：函数名错误，数据集下载函数为 `dataset_snapshot_download`，模型下载才是`snapshot_download`
解决：使用上方3.1正确代码，并升级modelscope
```bash
pip install --upgrade modelscope
```

### 6.2 urllib3 LibreSSL 版本警告（Mac）
警告不影响下载，可选修复：
```bash
brew install openssl
pip install urllib3==1.26.18
```

### 6.3 git lfs not found
先执行安装并初始化
```bash
brew install git-lfs
git lfs install
```

### 6.4 下载超时/速度慢
配置 `HF_ENDPOINT=https://hf-mirror.com` 镜像

## 7. 数据集区分说明
| 数据集 | 规模 | 特点 |
|--------|------|------|
| MMMU（原版） | 11500题 | 6大学科30科目，4选项单选，基础多模态推理，分train/val/test |
| MMMU_Pro | 3460题 | 1730标准题(4/10选项)+1730 vision-only；10选项大幅降低随机正确率，vision-only需OCR提取图片内题干，难度更高 |

## 8. 论文引用
- MMMU：https://arxiv.org/abs/2311.16502
- MMMU_Pro：https://arxiv.org/abs/2409.02813
