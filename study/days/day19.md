# Day 19 · Continuous Batching 与 Chunked Prefill

[← Day 18](day18.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 20 →](day20.md)

> 这是任务卡，不是已经实现的完整讲义。当前本地可直接运行的是 Omni 阶段 0 的 Mock 流水线和 C++ 课程中已有的示例；其余内容按固定上游入口阅读，环境具备后再运行。不要把阅读或模拟结果标成真实模型/GPU/集群性能。

## 当天概览

| 项目 | 内容 |
| --- | --- |
| 状态 | `未开始`（初始状态：全部未开始） |
| 目标 | 理解长短请求如何竞争计算和 KV 资源。 |
| 计划时间 | **270 分钟**（前 5 天为冲刺目标；测试未通过就顺延） |

## 按序安排

| 顺序 | 分钟 | 任务 |
| ---: | ---: | --- |
| 1 | 120 | 读调度与流式输出代码：短请求结束后如何释放位置，下游 stage 是否同一调度策略。 |
| 2 | 90 | K8S 第15章与 RL-D17/D18 合并；固定长短负载，每次只改变一个调度开关。 |
| 3 | 45 | 记录 TTFT、输出长度、吞吐与错误率；无真实 GPU 时画时间线，性能栏填待测。 |
| 4 | 15 | 填写统一笔记；把复用证据链接到已有记录，避免复制结论。 |
| **合计** | **270** | **当天学习时间；休息另计** |

## 当天验收证据

- [ ] 固定负载和单变量对照设计
- [ ] AR 与非 AR 阶段的批处理差异

## 与已有工作的复用

复用已完成且有证据的部分；对应主题只读过时仍标阅读，不能抵扣实际实验。

## 原计划映射

| 来源 | 映射 | 用法 |
| --- | --- | --- |
| RL + Inference 原计划 | RL-D17, RL-D18 | 复用机制、实验或报告；不重复实现已有证据 |
| C++ 10 天 | — | 只在对应日打开本地课程入口 |
| K8S AI Infra 大纲 | K8S-Ch15 | 作为部署/调度/观测的选读映射，先读概念再看环境 |

## C++ 本地入口

- 当天没有 C++ 新课；不要重复打开 C++ 课程。

## 阅读与源码入口

- [OmniScheduler](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/scheduling/omni_scheduler.py)
- [SimpleScheduler](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/scheduling/simple_scheduler.py)
- [K8S AI Infra 19 章大纲（按指定章节选读）](https://my.feishu.cn/wiki/IGekw2vrdiCtS1kQYwIconEBnFb)
- [原 RL 42 天计划](https://github.com/HlinForest/rl-inference-lab/blob/main/docs/curriculum.md)

- Omni 上游参考（仅相关日适用）：`870d77446b3fae6e4f4f2a6964f7eae2f75e663a`。

## 当天笔记

- [复制每日笔记模板](../templates/daily-note.md)
- 在仓库根目录运行：`python study/tools/note.py --day 19`
- 生成的填写内容保存在本地 `study/notes/`，不会进入 GitHub 计划文件。

[← Day 18](day18.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 20 →](day20.md)
