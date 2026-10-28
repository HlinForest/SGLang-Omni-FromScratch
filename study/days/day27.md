# Day 27 · RL 样本契约与 Omni 请求契约

[← Day 26](day26.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 28 →](day28.md)

> 这是任务卡，不是已经实现的完整讲义。当前本地可直接运行的是 Omni 阶段 0 的 Mock 流水线和 C++ 课程中已有的示例；其余内容按固定上游入口阅读，环境具备后再运行。不要把阅读或模拟结果标成真实模型/GPU/集群性能。

## 当天概览

| 项目 | 内容 |
| --- | --- |
| 状态 | `未开始`（初始状态：全部未开始） |
| 目标 | 为后面的概率与版本讨论先明确记录的含义。 |
| 计划时间 | **270 分钟**（前 5 天为冲刺目标；测试未通过就顺延） |

## 按序安排

| 顺序 | 分钟 | 任务 |
| ---: | ---: | --- |
| 1 | 120 | 读 RL-D22 与 RLHF Training Overview，建立4-action contextual bandit 的样本结构；区分行为 q、固定 old learner 与当前 learner 的 logprob。 |
| 2 | 90 | 回看 Omni payload、request_id 和 finish_reason；比较推理请求完成与训练样本可用的条件，learner 保持独立于 Omni stage。 |
| 3 | 45 | 检查 sample_id、context/action/reward、采样配置和版本字段，记录固定评估输入。 |
| 4 | 15 | 填写笔记：事实、解释、限制、明日起点。 |
| **合计** | **270** | **当天学习时间；休息另计** |

## 当天验收证据

- [ ] 样本字段表与三种 logprob 定义
- [ ] Omni 请求/训练样本职责对照

## 与已有工作的复用

沿用同一小型 RL 闭环和 Omni 项目；RL 是机制补充，不把训练逻辑加入推理 stage。

## 原计划映射

| 来源 | 映射 | 用法 |
| --- | --- | --- |
| RL + Inference 原计划 | RL-D22 | 复用机制、实验或报告；不重复实现已有证据 |
| C++ 10 天 | — | 只在对应日打开本地课程入口 |
| K8S AI Infra 大纲 | — | 作为部署/调度/观测的选读映射，先读概念再看环境 |

## C++ 本地入口

- 当天没有 C++ 新课；不要重复打开 C++ 课程。

## 阅读与源码入口

- [模型 payload](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/models/qwen3_omni/payload_types.py)
- [原 RL 42 天计划](https://github.com/HlinForest/rl-inference-lab/blob/main/docs/curriculum.md)

- Omni 上游参考（仅相关日适用）：`870d77446b3fae6e4f4f2a6964f7eae2f75e663a`。

## 当天笔记

- [复制每日笔记模板](../templates/daily-note.md)
- 在仓库根目录运行：`python study/tools/note.py --day 27`
- 生成的填写内容保存在本地 `study/notes/`，不会进入 GitHub 计划文件。

[← Day 26](day26.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 28 →](day28.md)
