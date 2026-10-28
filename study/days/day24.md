# Day 24 · K8S 基础与 GPU 资源声明

[← Day 23](day23.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 25 →](day25.md)

> 这是任务卡，不是已经实现的完整讲义。当前本地可直接运行的是 Omni 阶段 0 的 Mock 流水线和 C++ 课程中已有的示例；其余内容按固定上游入口阅读，环境具备后再运行。不要把阅读或模拟结果标成真实模型/GPU/集群性能。

## 当天概览

| 项目 | 内容 |
| --- | --- |
| 状态 | `未开始`（初始状态：全部未开始） |
| 目标 | 在理解单机进程之后再理解 Pod 和 GPU 分配。 |
| 计划时间 | **270 分钟**（前 5 天为冲刺目标；测试未通过就顺延） |

## 按序安排

| 顺序 | 分钟 | 任务 |
| ---: | ---: | --- |
| 1 | 120 | 读第1章 Pod、Deployment、Service、探针；将 Omni launcher 的进程边界映射到部署单元。 |
| 2 | 90 | 选第4章驱动、toolkit、device plugin/GPU Operator；只弄清谁提供 GPU 资源，不同时展开 MIG/MPS/DRA。 |
| 3 | 45 | 已有可用测试集群就做最小部署/查询；无集群则读官方示例并画资源表，记录未部署，不占用已有生产集群。 |
| 4 | 15 | 填写统一笔记；把复用证据链接到已有记录，避免复制结论。 |
| **合计** | **270** | **当天学习时间；休息另计** |

## 当天验收证据

- [ ] 进程→容器→Pod→节点关系图
- [ ] 资源与健康检查清单；实测或设计标签

## 与已有工作的复用

复用已完成且有证据的部分；对应主题只读过时仍标阅读，不能抵扣实际实验。

## 原计划映射

| 来源 | 映射 | 用法 |
| --- | --- | --- |
| RL + Inference 原计划 | — | 复用机制、实验或报告；不重复实现已有证据 |
| C++ 10 天 | — | 只在对应日打开本地课程入口 |
| K8S AI Infra 大纲 | K8S-Ch01, K8S-Ch04 | 作为部署/调度/观测的选读映射，先读概念再看环境 |

## C++ 本地入口

- 当天没有 C++ 新课；不要重复打开 C++ 课程。

## 阅读与源码入口

- [K8S AI Infra 19 章大纲（按指定章节选读）](https://my.feishu.cn/wiki/IGekw2vrdiCtS1kQYwIconEBnFb)
- [Kubernetes 基础](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
- [GPU 资源](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/)
- [进程启动](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/serve/launcher.py)

- Omni 上游参考（仅相关日适用）：`870d77446b3fae6e4f4f2a6964f7eae2f75e663a`。

## 当天笔记

- [复制每日笔记模板](../templates/daily-note.md)
- 在仓库根目录运行：`python study/tools/note.py --day 24`
- 生成的填写内容保存在本地 `study/notes/`，不会进入 GitHub 计划文件。

[← Day 23](day23.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 25 →](day25.md)
