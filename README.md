# SGLang-Omni From Scratch

> 每天4–5小时的整合安排：[统一学习入口](LEARNING.md) · [42天日程](study/DAILY-PLAN.md) · [每日笔记模板](study/templates/daily-note.md)

从一个能跑的三阶段流水线开始，逐步读懂并重新实现 SGLang-Omni。

面向熟悉 Python 与 PyTorch、希望深入推理系统工程的算法工程师。先运行、看输出与耗时，再理解系统设计，最后对照上游源码补全实现。课程以中文讲解，保留英文技术术语。

> **当前进度：仓库初始化完成，阶段 0 尚未开始。** 本仓库目前提供项目启动文件、课程路线与来源说明；尚无可运行的推理引擎或已完成的课程。

## 学什么

一次全模态或语音生成，可能需要多个计算特性不同的阶段协同。我们从下面这个简化模型出发：

```text
请求 → Preprocessing → AR Generation → Vocoder → 流式输出
```

逐步学习 Stage 生命周期、拓扑与 Fan-in、进程隔离、控制面与数据面、张量 Relay、异构调度、SGLang 引擎集成，以及流式 API、调试和性能分析。起步阶段使用单进程 `asyncio.Queue` 和模拟数据，后续按课程需要接入真实模型与硬件。

长期目标是对照固定版本的 SGLang-Omni 完整复刻。每个阶段先交付可运行、可观察的简化实现，再解释上游设计并补全；这个目标不代表当前已经实现相同功能或性能。

## 从哪里开始

| 文件 | 用途 |
| --- | --- |
| [AGENTS.md](AGENTS.md) | 项目定位、读者背景、架构全景、教学与开发约定 |
| [COURSE.md](COURSE.md) | 11 个阶段的路线及当前进度 |
| [docs/README.md](docs/README.md) | 课程文档入口 |
| [docs/REFERENCE.md](docs/REFERENCE.md) | 固定参考版本、获取源码的方法与依赖边界 |
| [CREDITS.md](CREDITS.md) | 教学灵感、技术来源及许可证信息 |

克隆本仓库后，先读 `AGENTS.md` 与 `COURSE.md`。下一步是细化阶段 0，再实现最小流水线。暂不需要安装完整 GPU 推理环境。

```bash
git clone https://github.com/HlinForest/SGLang-Omni-FromScratch.git
cd SGLang-Omni-FromScratch
```

## 学习方式

- 读代码、运行示例、观察系统行为，不设置填空式作业。
- 教学代码配套说明、注释与调试方法；每节课聚焦一个问题。
- 在可测量的瓶颈出现时引入抽象与优化，记录延迟、吞吐和资源开销。
- 后续项目代码逐步放入 `sglang_omni/`；上游参考源码放在只读的 `sglang-omni/`，不提交到本仓库。

## Credits

- **[hong-kailin/OpenCodeFromScratch](https://github.com/hong-kailin/OpenCodeFromScratch)**：本项目的教学方法、启动文件组织和渐进式学习约定参考其 [`video` 分支的 AGENTS.md](https://github.com/hong-kailin/OpenCodeFromScratch/blob/video/AGENTS.md)。感谢原作者分享用 AI 辅助阅读和重建复杂项目的方法。
- **[sgl-project/sglang-omni](https://github.com/sgl-project/sglang-omni)**：本项目的主要学习与复刻对象。多阶段运行时及相关系统设计来自其作者与贡献者；参考版本固定为 `v0.1.8`。
- **[sgl-project/sglang](https://github.com/sgl-project/sglang)**：SGLang-Omni 自回归推理阶段使用的基础引擎，也是后续引擎桥接部分的学习来源。

本仓库是独立教学项目，与上述项目不存在官方隶属或背书关系。具体来源、固定提交与许可说明见 [CREDITS.md](CREDITS.md)。
