# Day 04 · CSE291 · PA3 MoE、成本与推测解码

[← Day 03](day03.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 05 →](day05.md)

> 这是任务卡，不是已经实现的完整讲义。当前本地可直接运行的是 Omni 阶段 0 的 Mock 流水线和 C++ 课程中已有的示例；其余内容按固定上游入口阅读，环境具备后再运行。不要把阅读或模拟结果标成真实模型/GPU/集群性能。

## 当天概览

| 项目 | 内容 |
| --- | --- |
| 状态 | `未开始`（初始状态：全部未开始） |
| 目标 | 把 PA3 三个技术部分串起来；只做必做项，暂缓 bonus。 |
| 计划时间 | **300 分钟**（前 5 天为冲刺目标；测试未通过就顺延） |

## 按序安排

| 顺序 | 分钟 | 任务 |
| ---: | ---: | --- |
| 1 | 75 | 完成 MoE 的 TP/EP 正确性、benchmark 和解释，保留 all-to-all 路由证据。 |
| 2 | 60 | 完成训练成本与固定预算模型设计，逐项核对假设、单位和最终答案。 |
| 3 | 120 | PA3 Part 3：沿 draft → target verification → accept/reject → update 阅读并完成 notebook。 |
| 4 | 30 | 跑最小正确性和接受率检查；真实 GPU 上再测 latency，CPU 仅验证逻辑。 |
| 5 | 15 | 记录推测解码中 target 与 draft 的区别。 |
| **合计** | **300** | **当天学习时间；休息另计** |

## 当天验收证据

- [ ] PA3 Part 1/2 已完成项与未完成项
- [ ] 推测解码最小结果、模型配置与硬件记录

## 与已有工作的复用

RL-D19 复用 PA3 推测解码证据；Omni 的 Thinker/Talker 不是 speculative draft/target。

## 原计划映射

| 来源 | 映射 | 用法 |
| --- | --- | --- |
| RL + Inference 原计划 | RL-D19 | 复用机制、实验或报告；不重复实现已有证据 |
| C++ 10 天 | — | 只在对应日打开本地课程入口 |
| K8S AI Infra 大纲 | — | 作为部署/调度/观测的选读映射，先读概念再看环境 |

## C++ 本地入口

- 当天没有 C++ 新课；不要重复打开 C++ 课程。

## 阅读与源码入口

- [PA3 说明](https://github.com/hao-ai-lab/cse-dsc291-s26-pa/blob/b9428ec2466fcf777d79e0ea32501e889e49040c/pa3/README.md)

- Omni 上游参考（仅相关日适用）：`870d77446b3fae6e4f4f2a6964f7eae2f75e663a`。

## 当天笔记

- [复制每日笔记模板](../templates/daily-note.md)
- 在仓库根目录运行：`python study/tools/note.py --day 4`
- 生成的填写内容保存在本地 `study/notes/`，不会进入 GitHub 计划文件。

[← Day 03](day03.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 05 →](day05.md)
