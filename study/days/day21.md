# Day 21 · 训练显存与并行机制补齐

[← Day 20](day20.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 22 →](day22.md)

> 这是任务卡，不是已经实现的完整讲义。当前本地可直接运行的是 Omni 阶段 0 的 Mock 流水线和 C++ 课程中已有的示例；其余内容按固定上游入口阅读，环境具备后再运行。不要把阅读或模拟结果标成真实模型/GPU/集群性能。

## 当天概览

| 项目 | 内容 |
| --- | --- |
| 状态 | `未开始`（初始状态：全部未开始） |
| 目标 | 用 PA1/PA2/PA3 的证据补全训练侧机制，避免与推理调度混淆。 |
| 计划时间 | **270 分钟**（前 5 天为冲刺目标；测试未通过就顺延） |

## 按序安排

| 顺序 | 分钟 | 任务 |
| ---: | ---: | --- |
| 1 | 120 | 复用 PA1 小模型：整 batch 与梯度累积比较；检查 loss 缩放、dropout，阅读/运行现成 checkpoint 对照。 |
| 2 | 90 | 复用 PA2/PA3 的 TP、DP、collective；补 ZeRO 状态分片表和 2-stage/4-microbatch PP 时间线。 |
| 3 | 45 | 对照 Omni placement：训练 PP、Omni stage 图和 K8S 调度解决不同层的问题；只读 K8S 第12章对应部分。 |
| 4 | 15 | 填写统一笔记；把复用证据链接到已有记录，避免复制结论。 |
| **合计** | **270** | **当天学习时间；休息另计** |

## 当天验收证据

- [ ] 梯度一致性或未验证说明
- [ ] DP/ZeRO/TP/PP 的切分、通信、代价表

## 与已有工作的复用

复用已完成且有证据的部分；对应主题只读过时仍标阅读，不能抵扣实际实验。

## 原计划映射

| 来源 | 映射 | 用法 |
| --- | --- | --- |
| RL + Inference 原计划 | RL-D08, RL-D09, RL-D10, RL-D11, RL-D12, RL-D13, RL-D14 | 复用机制、实验或报告；不重复实现已有证据 |
| C++ 10 天 | — | 只在对应日打开本地课程入口 |
| K8S AI Infra 大纲 | K8S-Ch12 | 作为部署/调度/观测的选读映射，先读概念再看环境 |

## C++ 本地入口

- 当天没有 C++ 新课；不要重复打开 C++ 课程。

## 阅读与源码入口

- [PA1](https://github.com/hao-ai-lab/cse-dsc291-s26-pa/blob/b9428ec2466fcf777d79e0ea32501e889e49040c/pa1/CSE291-S26-PA1.ipynb)
- [PA2](https://github.com/hao-ai-lab/cse-dsc291-s26-pa/blob/b9428ec2466fcf777d79e0ea32501e889e49040c/pa2/README.md)
- [K8S AI Infra 19 章大纲（按指定章节选读）](https://my.feishu.cn/wiki/IGekw2vrdiCtS1kQYwIconEBnFb)
- [原 RL 42 天计划](https://github.com/HlinForest/rl-inference-lab/blob/main/docs/curriculum.md)

- Omni 上游参考（仅相关日适用）：`870d77446b3fae6e4f4f2a6964f7eae2f75e663a`。

## 当天笔记

- [复制每日笔记模板](../templates/daily-note.md)
- 在仓库根目录运行：`python study/tools/note.py --day 21`
- 生成的填写内容保存在本地 `study/notes/`，不会进入 GitHub 计划文件。

[← Day 20](day20.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 22 →](day22.md)
