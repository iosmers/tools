# RDMA 通信网络确认方法

本文档记录如何确认一台机器是否具备 RDMA 通信网络，以及如何判断它是原生 InfiniBand 还是 RoCE（RDMA over Ethernet）。

---

## 结论判断依据

确认 RDMA 通信网络时，主要通过以下几类信息交叉判断：

1. RDMA link 是否存在并且处于 `ACTIVE / LINK_UP`
2. `ibv_devinfo` 是否能识别到 HCA 设备
3. `/sys/class/infiniband` 下是否存在 RDMA 设备
4. PCI 设备中是否存在 Mellanox / NVIDIA ConnectX 网卡
5. 网卡接口是否 UP，并且链路速率正常
6. RDMA 相关内核模块是否加载
7. GID 类型是否包含 `RoCE v2`

---

## 1. 最直接确认：查看 RDMA link

```bash
rdma link show
```

示例输出：

```text
link mlx5_0/1 state ACTIVE physical_state LINK_UP netdev brainpf0
link mlx5_1/1 state ACTIVE physical_state LINK_UP netdev brainpf1
link mlx5_bond_0/1 state ACTIVE physical_state LINK_UP netdev ens1f0np0
link mlx5_2/1 state ACTIVE physical_state LINK_UP netdev brainvf0
link mlx5_3/1 state ACTIVE physical_state LINK_UP netdev brainvf1
```

判断依据：

- `state ACTIVE`：RDMA 端口已激活
- `physical_state LINK_UP`：物理链路已连通
- `mlx5_*`：Mellanox / NVIDIA ConnectX 系列 RDMA 设备
- `netdev brainpf0` 等：该 RDMA 设备绑定到具体网卡接口

---

## 2. 查看 RDMA HCA 设备详情

```bash
ibv_devinfo
```

关键看这些字段：

```text
hca_id: mlx5_0
    transport: InfiniBand
    port: 1
        state: PORT_ACTIVE
        link_layer: Ethernet
```

判断依据：

- 出现 `hca_id: mlx5_0` / `mlx5_1` / `mlx5_bond_0` 等，说明系统识别到了 RDMA HCA
- `state: PORT_ACTIVE` 表示 RDMA 端口可用
- `link_layer: Ethernet` 表示这是 **RoCE**，即 RDMA over Ethernet
- 如果是原生 InfiniBand，通常会显示 `link_layer: InfiniBand`

---

## 3. 查看系统 RDMA 设备目录

```bash
ls -l /sys/class/infiniband
```

示例输出：

```text
mlx5_0
mlx5_1
mlx5_2
mlx5_3
mlx5_bond_0
```

说明内核已经注册了 RDMA 设备。

进一步查看每个端口状态：

```bash
for d in /sys/class/infiniband/*; do
  [ -e "$d" ] || continue
  echo "===== $(basename "$d") ====="
  cat "$d/node_type" 2>/dev/null
  cat "$d/fw_ver" 2>/dev/null

  for p in "$d"/ports/*; do
    echo "--- port $(basename "$p") ---"
    echo -n "state: "
    cat "$p/state" 2>/dev/null
    echo -n "phys_state: "
    cat "$p/phys_state" 2>/dev/null
    echo -n "link_layer: "
    cat "$p/link_layer" 2>/dev/null
    echo -n "rate: "
    cat "$p/rate" 2>/dev/null
  done
done
```

关键输出类似：

```text
mlx5_0
state: 4: ACTIVE
phys_state: 5: LinkUp
link_layer: Ethernet
rate: 200 Gb/sec
```

---

## 4. 确认是否有 Mellanox / ConnectX 网卡

```bash
lspci -nn | egrep -i 'infiniband|mellanox|nvidia|connectx|roce|ethernet controller'
```

示例输出：

```text
27:00.0 Ethernet controller: Mellanox Technologies MT28908 Family [ConnectX-6]
27:00.1 Ethernet controller: Mellanox Technologies MT28908 Family [ConnectX-6 Virtual Function]
60:00.0 Ethernet controller: Mellanox Technologies MT28908 Family [ConnectX-6]
60:00.1 Ethernet controller: Mellanox Technologies MT28908 Family [ConnectX-6 Virtual Function]
ca:00.0 Ethernet controller: Mellanox Technologies MT2892 Family [ConnectX-6 Dx]
ca:00.1 Ethernet controller: Mellanox Technologies MT2892 Family [ConnectX-6 Dx]
```

判断依据：

- `Mellanox`
- `ConnectX-6`
- `ConnectX-6 Dx`

这些都是常见 RDMA / RoCE 网卡。

---

## 5. 查看 RDMA 网卡 IP 和链路速率

```bash
ip -br addr show
```

示例输出：

```text
brainpf0 UP 10.201.194.55/23
brainpf1 UP 10.201.192.58/23
bond0    UP 10.201.48.68/24
```

再看链路状态和速率：

```bash
for i in brainpf0 brainpf1 brainvf0 brainvf1 ens1f0np0 ens1f1np1 bond0; do
  echo "===== $i ====="
  echo -n "operstate: "
  cat /sys/class/net/$i/operstate 2>/dev/null
  echo -n "carrier: "
  cat /sys/class/net/$i/carrier 2>/dev/null
  echo -n "speed: "
  cat /sys/class/net/$i/speed 2>/dev/null
done
```

关键结果：

```text
brainpf0
operstate: up
carrier: 1
speed: 200000
```

说明：

- `operstate: up`：网卡接口 up
- `carrier: 1`：物理链路有载波
- `speed: 200000`：200000 Mb/s，即 200 Gb/s

---

## 6. 查看 RDMA 内核模块

```bash
lsmod | egrep 'mlx5|ib_core|rdma|ib_uverbs'
```

示例输出：

```text
rdma_ucm
rdma_cm
mlx5_ib
ib_uverbs
ib_core
mlx5_core
```

判断依据：

- `mlx5_core`：Mellanox mlx5 网卡核心驱动
- `mlx5_ib`：Mellanox RDMA / IB 驱动
- `ib_uverbs`：用户态 RDMA verbs 接口
- `rdma_cm`：RDMA connection manager

---

## 7. 查看 RoCE GID，确认是否是 RoCE v2

```bash
for d in /sys/class/infiniband/*; do
  [ -e "$d" ] || continue
  dev=$(basename "$d")
  echo "===== $dev valid GIDs ====="

  for g in "$d"/ports/1/gids/*; do
    [ -e "$g" ] || continue
    val=$(cat "$g" 2>/dev/null)

    [ "$val" = "0000:0000:0000:0000:0000:0000:0000:0000" ] && continue

    idx=$(basename "$g")
    ndev=$(cat "$d/ports/1/gid_attrs/ndevs/$idx" 2>/dev/null)
    type=$(cat "$d/ports/1/gid_attrs/types/$idx" 2>/dev/null)

    echo "gid_idx=$idx gid=$val ndev=$ndev type=$type"
  done
done
```

关键结果类似：

```text
mlx5_0 valid GIDs
gid_idx=1 ... ndev=brainpf0 type=RoCE v2
gid_idx=3 ... ndev=brainpf0 type=RoCE v2

mlx5_1 valid GIDs
gid_idx=1 ... ndev=brainpf1 type=RoCE v2
gid_idx=3 ... ndev=brainpf1 type=RoCE v2

mlx5_bond_0 valid GIDs
gid_idx=1 ... ndev=bond0 type=RoCE v2
gid_idx=3 ... ndev=bond0 type=RoCE v2
```

这个是确认它是 **RoCE v2** 的重要依据。

---

# 一键检查脚本

可以保存成脚本：

```bash
cat > check_rdma.sh <<'SCRIPT'
#!/usr/bin/env bash
set -o pipefail

if [ -n "$BASH_VERSION" ]; then
  shopt -s nullglob
fi

echo "=== Hostname ==="
hostname

echo
echo "=== 1. rdma link show ==="
if command -v rdma >/dev/null 2>&1; then
  rdma link show
else
  echo "rdma command not found"
fi

echo
echo "=== 2. rdma dev show ==="
if command -v rdma >/dev/null 2>&1; then
  rdma dev show
else
  echo "rdma command not found"
fi

echo
echo "=== 3. ibv_devinfo ==="
if command -v ibv_devinfo >/dev/null 2>&1; then
  ibv_devinfo
else
  echo "ibv_devinfo command not found"
fi

echo
echo "=== 4. /sys/class/infiniband ==="
ls -la /sys/class/infiniband 2>&1 || true

echo
echo "=== 5. RDMA port details from sysfs ==="
for d in /sys/class/infiniband/*; do
  [ -e "$d" ] || continue
  echo "===== $(basename "$d") ====="

  echo -n "node_type: "
  cat "$d/node_type" 2>/dev/null || true

  echo -n "fw_ver: "
  cat "$d/fw_ver" 2>/dev/null || true

  for p in "$d"/ports/*; do
    [ -e "$p" ] || continue
    echo "--- port $(basename "$p") ---"

    echo -n "state: "
    cat "$p/state" 2>/dev/null || true

    echo -n "phys_state: "
    cat "$p/phys_state" 2>/dev/null || true

    echo -n "link_layer: "
    cat "$p/link_layer" 2>/dev/null || true

    echo -n "rate: "
    cat "$p/rate" 2>/dev/null || true
  done
done

echo
echo "=== 6. PCI devices, Mellanox/NVIDIA/ConnectX candidates ==="
if command -v lspci >/dev/null 2>&1; then
  lspci -nn | egrep -i 'infiniband|mellanox|nvidia|connectx|roce|ethernet controller'
else
  echo "lspci command not found"
fi

echo
echo "=== 7. Network links ==="
ip -br link 2>/dev/null || true

echo
echo "=== 8. Network addresses ==="
ip -br addr 2>/dev/null || true

echo
echo "=== 9. RDMA-related kernel modules ==="
lsmod | egrep 'mlx5|ib_core|rdma|ib_uverbs' || true

echo
echo "=== 10. Valid GIDs / RoCE type ==="
for d in /sys/class/infiniband/*; do
  [ -e "$d" ] || continue
  dev=$(basename "$d")
  echo "===== $dev valid GIDs ====="

  for g in "$d"/ports/1/gids/*; do
    [ -e "$g" ] || continue
    val=$(cat "$g" 2>/dev/null)

    [ "$val" = "0000:0000:0000:0000:0000:0000:0000:0000" ] && continue

    idx=$(basename "$g")
    ndev=$(cat "$d/ports/1/gid_attrs/ndevs/$idx" 2>/dev/null)
    type=$(cat "$d/ports/1/gid_attrs/types/$idx" 2>/dev/null)

    echo "gid_idx=$idx gid=$val ndev=$ndev type=$type"
  done
done

echo
echo "=== Summary hint ==="
echo "If you see RDMA links with state ACTIVE and physical_state LINK_UP, RDMA device exists and link is up."
echo "If link_layer is Ethernet and GID type has RoCE v2, it is RoCE/RDMA over Ethernet."
echo "If link_layer is InfiniBand, it is native InfiniBand."
SCRIPT

chmod +x check_rdma.sh
./check_rdma.sh
```

---

## 最小判断命令

如果只想快速判断，跑这三个就够了：

```bash
rdma link show
ibv_devinfo
ls -l /sys/class/infiniband
```

看到类似下面就可以确认有 RDMA：

```text
state ACTIVE physical_state LINK_UP
```

以及：

```text
hca_id: mlx5_0
state: PORT_ACTIVE
link_layer: Ethernet
```

这里的 `Ethernet` 说明是 **RoCE**。

---

## 备注

本地检查可以确认本机侧 RDMA 设备和链路是否存在、是否 active。  
如果要进一步确认“能否和另一台机器实际 RDMA 通信”，需要有对端节点一起跑以下工具之一：

```bash
ib_send_bw
ib_write_bw
ib_read_bw
```

或者使用 NCCL / RDMA 测试程序进行端到端验证。
