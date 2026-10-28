# Day 20 · 量化与推测解码：复用 PA3

[← Day 19](day19.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 21 →](day21.md)

> 这是任务卡，不是已经实现的完整讲义。当前本地可直接运行的是 Omni 阶段 0 的 Mock 流水线和 C++ 课程中已有的示例；其余内容按固定上游入口阅读，环境具备后再运行。不要把阅读或模拟结果标成真实模型/GPU/集群性能。

## 当天概览

| 项目 | 内容 |
| --- | --- |
| 状态 | `未开始`（初始状态：全部未开始） |
| 目标 | 解释优化成立的条件，并避免混淆语音双阶段与推测解码。 |
| 计划时间 | **270 分钟**（前 5 天为冲刺目标；测试未通过就顺延） |

## 按序安排

| 顺序 | 分钟 | 任务 |
| ---: | ---: | --- |
| 1 | 120 | 以 Omni 当前模型路径为例标出精度和阶段边界，不假设所有模型都支持同一种量化或 speculative backend。 |
| 2 | 90 | 复用 PA3 Part3 的 draft/target、接受率与耗时数据；用 RL-D19 的成本模型解释成功与变慢条件。 |
| 3 | 45 | 补位宽/存储量算例；整理 Thinker/Talker 与 draft/target 的区别，不再写一份 speculative pipeline。 |
| 4 | 15 | 填写统一笔记；把复用证据链接到已有记录，避免复制结论。 |
| **合计** | **270** | **当天学习时间；休息另计** |

## 当天验收证据

- [ ] PA3 证据链接或待补项
- [ ] 精度、存储和延迟的条件说明

## 与已有工作的复用

复用已完成且有证据的部分；对应主题只读过时仍标阅读，不能抵扣实际实验。

## 原计划映射

| 来源 | 映射 | 用法 |
| --- | --- | --- |
| RL + Inference 原计划 | RL-D19 | 复用机制、实验或报告；不重复实现已有证据 |
| C++ 10 天 | — | 只在对应日打开本地课程入口 |
| K8S AI Infra 大纲 | K8S-Ch15 | 作为部署/调度/观测的选读映射，先读概念再看环境 |

## C++ 本地入口

- 当天没有 C++ 新课；不要重复打开 C++ 课程。

## 阅读与源码入口

- [PA3](https://github.com/hao-ai-lab/cse-dsc291-s26-pa/blob/b9428ec2466fcf777d79e0ea32501e889e49040c/pa3/README.md)
- [模型数据契约](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/models/qwen3_omni/payload_types.py)
- [原 RL 42 天计划](https://github.com/HlinForest/rl-inference-lab/blob/main/docs/curriculum.md)

- Omni 上游参考（仅相关日适用）：`870d77446b3fae6e4f4f2a6964f7eae2f75e663a`。

## 当天笔记

- [复制每日笔记模板](../templates/daily-note.md)
- 在仓库根目录运行：`python study/tools/note.py --day 20`
- 生成的填写内容保存在本地 `study/notes/`，不会进入 GitHub 计划文件。

[← Day 19](day19.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 21 →](day21.md)
