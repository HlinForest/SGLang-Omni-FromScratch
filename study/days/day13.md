# Day 13 · Omni · 进程放置与内存预算 / C++ 8

[← Day 12](day12.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 14 →](day14.md)

> 这是任务卡，不是已经实现的完整讲义。当前本地可直接运行的是 Omni 阶段 0 的 Mock 流水线和 C++ 课程中已有的示例；其余内容按固定上游入口阅读，环境具备后再运行。不要把阅读或模拟结果标成真实模型/GPU/集群性能。

## 当天概览

| 项目 | 内容 |
| --- | --- |
| 状态 | `未开始`（初始状态：全部未开始） |
| 目标 | 理解阶段共置或隔离会改变什么。 |
| 计划时间 | **270 分钟**（前 5 天为冲刺目标；测试未通过就顺延） |

## 按序安排

| 顺序 | 分钟 | 任务 |
| ---: | ---: | --- |
| 1 | 135 | 读 StagePlacementPlanner 和 build_process_topology_plan；标出每个进程、设备、显存份额和共享资源。 |
| 2 | 75 | C++ 第 8 天：循环次序与可靠计时。打开 C++ 文件夹 days/day08/README.md，运行示例；现有练习按自身进度选做，参考实现可直接跟读。 |
| 3 | 45 | 复用 PA1/PA3 内存分析；训练状态、推理 KV 和激活必须分项，估算与实测分开。 |
| 4 | 15 | 填写当天笔记，记录已运行与只读源码的边界。 |
| **合计** | **270** | **当天学习时间；休息另计** |

## 当天验收证据

- [ ] 进程/设备/资源表
- [ ] C++ 计时边界和预热记录

## 与已有工作的复用

C++ 只占这一段固定时间；Omni 后续课未实现时以固定源码/测试阅读推进，不声称已跑通。

## 原计划映射

| 来源 | 映射 | 用法 |
| --- | --- | --- |
| RL + Inference 原计划 | RL-D08 | 复用机制、实验或报告；不重复实现已有证据 |
| C++ 10 天 | C++-Day08 | 只在对应日打开本地课程入口 |
| K8S AI Infra 大纲 | — | 作为部署/调度/观测的选读映射，先读概念再看环境 |

## C++ 本地入口

- C++ Day 08 工作区路径：`../../../cpp-ai-systems-10days/days/day08/README.md`（本地已有工程入口，不把课程代码重复发布到本计划仓库）

## 阅读与源码入口

- [Placement](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/config/placement.py)
- [Topology](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/config/topology.py)

- Omni 上游参考（仅相关日适用）：`870d77446b3fae6e4f4f2a6964f7eae2f75e663a`。

## 当天笔记

- [复制每日笔记模板](../templates/daily-note.md)
- 在仓库根目录运行：`python study/tools/note.py --day 13`
- 生成的填写内容保存在本地 `study/notes/`，不会进入 GitHub 计划文件。

[← Day 12](day12.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 14 →](day14.md)
