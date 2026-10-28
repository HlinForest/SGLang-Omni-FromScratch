# Day 03 · CSE291 · PA2 MPI → PA3 MoE

[← Day 02](day02.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 04 →](day04.md)

> 这是任务卡，不是已经实现的完整讲义。当前本地可直接运行的是 Omni 阶段 0 的 Mock 流水线和 C++ 课程中已有的示例；其余内容按固定上游入口阅读，环境具备后再运行。不要把阅读或模拟结果标成真实模型/GPU/集群性能。

## 当天概览

| 项目 | 内容 |
| --- | --- |
| 状态 | `未开始`（初始状态：全部未开始） |
| 目标 | 先理解并完成通信语义，再把同类通信用于专家路由。 |
| 计划时间 | **300 分钟**（前 5 天为冲刺目标；测试未通过就顺延） |

## 按序安排

| 顺序 | 分钟 | 任务 |
| ---: | ---: | --- |
| 1 | 135 | PA2 Part 2：myAllreduce/myAlltoall、data split、DP/TP group、forward/backward helper；按官方限制使用通信原语并测试。 |
| 2 | 90 | PA3 Part 1：在 PA2 通信基础上追踪 TP-MoE、EP-MoE、token 路由和输出恢复。 |
| 3 | 45 | PA3 Part 2：列出参数、FLOPs、显存公式及单位，先做 Llama-3 8B 必做分析。 |
| 4 | 15 | 归档 PA2 已过/未过测试与配置；记录 MPI rank 和运行环境。 |
| 5 | 15 | 填笔记，写出通信输入与输出。 |
| **合计** | **300** | **当天学习时间；休息另计** |

## 当天验收证据

- [ ] PA2 通信测试及失败项
- [ ] MoE token→expert→token 顺序图；成本公式草稿

## 与已有工作的复用

复用同一套 collective 语义，RL-D10/D12 不再重建通信程序。

## 原计划映射

| 来源 | 映射 | 用法 |
| --- | --- | --- |
| RL + Inference 原计划 | RL-D10, RL-D12 | 复用机制、实验或报告；不重复实现已有证据 |
| C++ 10 天 | — | 只在对应日打开本地课程入口 |
| K8S AI Infra 大纲 | — | 作为部署/调度/观测的选读映射，先读概念再看环境 |

## C++ 本地入口

- 当天没有 C++ 新课；不要重复打开 C++ 课程。

## 阅读与源码入口

- [PA2 说明](https://github.com/hao-ai-lab/cse-dsc291-s26-pa/blob/b9428ec2466fcf777d79e0ea32501e889e49040c/pa2/README.md)
- [PA3 说明](https://github.com/hao-ai-lab/cse-dsc291-s26-pa/blob/b9428ec2466fcf777d79e0ea32501e889e49040c/pa3/README.md)

- Omni 上游参考（仅相关日适用）：`870d77446b3fae6e4f4f2a6964f7eae2f75e663a`。

## 当天笔记

- [复制每日笔记模板](../templates/daily-note.md)
- 在仓库根目录运行：`python study/tools/note.py --day 3`
- 生成的填写内容保存在本地 `study/notes/`，不会进入 GitHub 计划文件。

[← Day 02](day02.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 04 →](day04.md)
