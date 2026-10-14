# 参考源码

## 固定版本

本课程对照 [SGLang-Omni](https://github.com/sgl-project/sglang-omni) 的 `v0.1.8`，固定提交为：

```text
870d77446b3fae6e4f4f2a6964f7eae2f75e663a
```

`main` 会继续变化；课程引用以这个固定提交为准。未来升级参考版本时，同时更新启动文件、课程引用和 [CREDITS.md](../CREDITS.md)。

## 获取只读参考副本

在本仓库根目录运行：

```bash
git clone --depth 1 --branch v0.1.8 https://github.com/sgl-project/sglang-omni.git sglang-omni
git -C sglang-omni rev-parse HEAD
```

第二条命令的输出应与上面的固定提交一致。如果不一致，先核对 tag 和来源，再开始引用。这里的 clone 只下载源码，不安装依赖或模型权重。

`sglang-omni/` 作为只读参考，由 `.gitignore` 排除。课程实现使用不同的目录 `sglang_omni/`。只读是本项目的操作约定，不是操作系统权限设置。

## 源码入口

| 主题 | 固定版本中的路径 |
| --- | --- |
| CLI 与引擎入口 | `sglang_omni/cli/` |
| 拓扑与配置契约 | `sglang_omni/config/schema.py` |
| 请求协调 | `sglang_omni/pipeline/coordinator.py` |
| 进程启动 | `sglang_omni/serve/launcher.py` |
| 控制面与数据面 | `docs/developer_reference/communication.md`、`sglang_omni/relay/` |
| 模型族数据契约 | 对应模型目录下的 `payload_types.py` |

## 依赖与运行环境

固定版本的默认 [pyproject.toml](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/pyproject.toml) 声明 Python `>=3.10,<3.13`、`torch==2.13.0`，并包含按平台选择的依赖。其他硬件配置应查阅相应的 `pyproject_*.toml` 和上游安装说明。

这些是上游参考环境的信息，并不是当前空白教学仓库的安装要求。阶段 0 计划从标准库模拟流水线开始；进入 GPU 与模型阶段时，再记录实际验证过的操作系统、设备、驱动和依赖版本。
