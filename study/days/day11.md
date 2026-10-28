# Day 11 · Omni · Fan-in、动态路由与多终点 / C++ 6

[← Day 10](day10.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 12 →](day12.md)

> 这是任务卡，不是已经实现的完整讲义。当前本地可直接运行的是 Omni 阶段 0 的 Mock 流水线和 C++ 课程中已有的示例；其余内容按固定上游入口阅读，环境具备后再运行。不要把阅读或模拟结果标成真实模型/GPU/集群性能。

## 当天概览

| 项目 | 内容 |
| --- | --- |
| 状态 | `未开始`（初始状态：全部未开始） |
| 目标 | 理解什么时候能继续、什么时候才算整个请求完成。 |
| 计划时间 | **270 分钟**（前 5 天为冲刺目标；测试未通过就顺延） |

## 按序安排

| 顺序 | 分钟 | 任务 |
| ---: | ---: | --- |
| 1 | 135 | 读 AggregatedInput、路由和 terminal 完成逻辑；对比单输入、多模态汇聚与只返回文本。 |
| 2 | 75 | C++ 第 6 天：连续内存与转置。打开 C++ 文件夹 days/day06/README.md，运行示例；现有练习按自身进度选做，参考实现可直接跟读。 |
| 3 | 45 | 结合连续内存解释聚合元数据和搬运张量的区别；不假定所有模型都使用同一阶段图。 |
| 4 | 15 | 填写当天笔记，记录已运行与只读源码的边界。 |
| **合计** | **270** | **当天学习时间；休息另计** |

## 当天验收证据

- [ ] 两条分支汇合的事件表
- [ ] early end 与正常全部终点完成的区别

## 与已有工作的复用

C++ 只占这一段固定时间；Omni 后续课未实现时以固定源码/测试阅读推进，不声称已跑通。

## 原计划映射

| 来源 | 映射 | 用法 |
| --- | --- | --- |
| RL + Inference 原计划 | — | 复用机制、实验或报告；不重复实现已有证据 |
| C++ 10 天 | C++-Day06 | 只在对应日打开本地课程入口 |
| K8S AI Infra 大纲 | — | 作为部署/调度/观测的选读映射，先读概念再看环境 |

## C++ 本地入口

- C++ Day 06 工作区路径：`../../../cpp-ai-systems-10days/days/day06/README.md`（本地已有工程入口，不把课程代码重复发布到本计划仓库）

## 阅读与源码入口

- [输入汇聚](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/pipeline/stage/input.py)
- [协调器](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/pipeline/coordinator.py)

- Omni 上游参考（仅相关日适用）：`870d77446b3fae6e4f4f2a6964f7eae2f75e663a`。

## 当天笔记

- [复制每日笔记模板](../templates/daily-note.md)
- 在仓库根目录运行：`python study/tools/note.py --day 11`
- 生成的填写内容保存在本地 `study/notes/`，不会进入 GitHub 计划文件。

[← Day 10](day10.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 12 →](day12.md)
