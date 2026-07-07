import requests
import time
import warnings
from typing import List, Dict, Tuple, Optional

# 屏蔽 LibreSSL / urllib3 版本警告
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", message="urllib3 v2 only supports OpenSSL*")

# 镜像列表：国内源 + 国外源分开
MIRRORS = [
    # ========== 国内源 ==========
    {"name": "清华源(国内)", "url": "https://pypi.tuna.tsinghua.edu.cn/simple"},
    {"name": "阿里云源(国内)", "url": "https://mirrors.aliyun.com/pypi/simple/"},
    {"name": "中科大源(国内)", "url": "https://pypi.mirrors.ustc.edu.cn/simple/"},
    {"name": "腾讯云源(国内)", "url": "https://mirrors.cloud.tencent.com/pypi/simple/"},
    {"name": "华为云源(国内)", "url": "https://repo.huaweicloud.com/repository/pypi/simple/"},
    {"name": "上海交大源(国内)", "url": "https://mirrors.sjtug.sjtu.edu.cn/pypi/web/simple/"},
    {"name": "豆瓣源(国内HTTP)", "url": "http://pypi.douban.com/simple/"},

    # ========== 国外源对比 ==========
    {"name": "PyPI官方源(US)", "url": "https://pypi.org/simple"},
    {"name": "PyPI Fastly CDN", "url": "https://files.pythonhosted.org/simple"},
    {"name": "Google PyPI镜像", "url": "https://pypi-gcp.withgoogle.com/simple/"},
    {"name": "阿里云国际版", "url": "https://mirrors.aliyun.com/pypi-global/simple/"},
    {"name": "清华海外镜像", "url": "https://mirrors.tuna.tsinghua.edu.cn/pypi-global/simple/"},
]

TEST_ROUND = 3       # 每个源测试3轮取平均
TIMEOUT_SEC = 10     # 单次请求超时阈值
HEADERS = {
    "User-Agent": "pip-test-latency/1.0 python-requests"
}

def test_single_mirror(url: str) -> Optional[float]:
    """单次测试单个源，返回延迟ms，失败返回None"""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT_SEC)
        delay_ms = resp.elapsed.total_seconds() * 1000
        return delay_ms
    except requests.exceptions.Timeout:
        print(f"  [超时] {url} 单次请求超过{TIMEOUT_SEC}s")
        return None
    except Exception as e:
        print(f"  [失败] {url} 异常: {str(e)[:60]}")
        return None

def benchmark_mirror(item: Dict) -> Tuple[str, str, Optional[float]]:
    """对一个镜像执行多轮测速，计算平均延迟"""
    name = item["name"]
    url = item["url"]
    print(f"\n正在测速 {name}: {url}")
    delays = []
    for i in range(TEST_ROUND):
        d = test_single_mirror(url)
        if d is not None:
            delays.append(d)
        time.sleep(0.2)  # 间隔防限流
    if not delays:
        return (name, url, None)
    avg_delay = sum(delays) / len(delays)
    print(f"  {TEST_ROUND}轮平均延迟: {avg_delay:.2f} ms")
    return (name, url, avg_delay)

def main():
    print("=" * 80)
    print(f"PIP镜像延迟测速工具 | 国内+国外源对比 | 每源{TEST_ROUND}次，超时{TIMEOUT_SEC}秒")
    print("=" * 80)
    results = []
    for mirror in MIRRORS:
        res = benchmark_mirror(mirror)
        results.append(res)

    # 排序：连通成功的按延迟升序，失败放最后
    success = [r for r in results if r[2] is not None]
    fail = [r for r in results if r[2] is None]
    success.sort(key=lambda x: x[2])
    final = success + fail

    # 汇总表格输出
    print("\n" + "=" * 80)
    print(f"{'排名':<4}{'镜像名称':<16}{'平均延迟(ms)':<16}{'源地址'}")
    print("-" * 80)
    for idx, (name, url, delay) in enumerate(final, start=1):
        delay_str = f"{delay:.2f}" if delay is not None else "连接失败"
        print(f"{idx:<4}{name:<16}{delay_str:<16}{url}")
    print("=" * 80)

    # 最优源推荐
    if success:
        best_name, best_url, best_delay = success[0]
        print(f"\n✅ 当前网络最优镜像：{best_name}，平均延迟 {best_delay:.2f} ms")
        print(f"👉 临时安装使用：pip install xxx -i {best_url} --timeout 120")
        print(f"👉 永久设为默认：pip config set global.index-url {best_url}")

if __name__ == "__main__":
    try:
        import requests
    except ImportError:
        print("未安装requests，请先执行：pip install requests")
        exit(1)
    main()
