# Day 02 · CSE291 · PA1 收尾 → PA2 Triton

[← Day 01](day01.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 03 →](day03.md)

> 这是任务卡，不是已经实现的完整讲义。当前本地可直接运行的是 Omni 阶段 0 的 Mock 流水线和 C++ 课程中已有的示例；其余内容按固定上游入口阅读，环境具备后再运行。不要把阅读或模拟结果标成真实模型/GPU/集群性能。

## 当天概览

| 项目 | 内容 |
| --- | --- |
| 状态 | `未开始`（初始状态：全部未开始） |
| 目标 | 完成 PA1 必做链路，随后把 PA2 fused MatMul 做到正确。 |
| 计划时间 | **300 分钟**（前 5 天为冲刺目标；测试未通过就顺延） |

## 按序安排

| 顺序 | 分钟 | 任务 |
| ---: | ---: | --- |
| 1 | 75 | 完成 PA1 训练、SGD、generation，检查 weights.pt 与官方必交项；若 PA1 未过测试，先修复再转 PA2。 |
| 2 | 120 | PA2 Part 1：读取接口和参考语义，补齐 tile 索引、边界 mask、累加与 fused epilogue。 |
| 3 | 45 | 运行正确性检查；核对远程 A10 grader 返回记录。先正确，再比较配置。 |
| 4 | 45 | 准备 MPI 环境并运行官方通信示例，检查进程数和退出。 |
| 5 | 15 | 记录 PA1 状态、kernel 配置和真实硬件来源。 |
| **合计** | **300** | **当天学习时间；休息另计** |

## 当天验收证据

- [ ] PA1 必交项清单与训练/生成记录
- [ ] PA2 kernel 正确性结果；有权限时保留官方 grader 结果

## 与已有工作的复用

此处 MatMul 是 RL-D3/D4 的主要 GPU 实践，后面只补本作业没有覆盖的边界。

## 原计划映射

| 来源 | 映射 | 用法 |
| --- | --- | --- |
| RL + Inference 原计划 | RL-D03, RL-D04 | 复用机制、实验或报告；不重复实现已有证据 |
| C++ 10 天 | — | 只在对应日打开本地课程入口 |
| K8S AI Infra 大纲 | — | 作为部署/调度/观测的选读映射，先读概念再看环境 |

## C++ 本地入口

- 当天没有 C++ 新课；不要重复打开 C++ 课程。

## 阅读与源码入口

- [PA1 notebook](https://github.com/hao-ai-lab/cse-dsc291-s26-pa/blob/b9428ec2466fcf777d79e0ea32501e889e49040c/pa1/CSE291-S26-PA1.ipynb)
- [PA2 说明](https://github.com/hao-ai-lab/cse-dsc291-s26-pa/blob/b9428ec2466fcf777d79e0ea32501e889e49040c/pa2/README.md)

- Omni 上游参考（仅相关日适用）：`870d77446b3fae6e4f4f2a6964f7eae2f75e663a`。

## 当天笔记

- [复制每日笔记模板](../templates/daily-note.md)
- 在仓库根目录运行：`python study/tools/note.py --day 2`
- 生成的填写内容保存在本地 `study/notes/`，不会进入 GitHub 计划文件。

[← Day 01](day01.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 03 →](day03.md)
