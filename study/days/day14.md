# Day 14 · Omni · Relay：控制消息与张量数据 / C++ 9

[← Day 13](day13.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 15 →](day15.md)

> 这是任务卡，不是已经实现的完整讲义。当前本地可直接运行的是 Omni 阶段 0 的 Mock 流水线和 C++ 课程中已有的示例；其余内容按固定上游入口阅读，环境具备后再运行。不要把阅读或模拟结果标成真实模型/GPU/集群性能。

## 当天概览

| 项目 | 内容 |
| --- | --- |
| 状态 | `未开始`（初始状态：全部未开始） |
| 目标 | 沿一个张量说明数据为什么不能总随控制消息传输。 |
| 计划时间 | **270 分钟**（前 5 天为冲刺目标；测试未通过就顺延） |

## 按序安排

| 顺序 | 分钟 | 任务 |
| ---: | ---: | --- |
| 1 | 135 | 读 communication.md、DataRef、Relay 接口与 SHM；只追踪同进程引用→跨进程描述符→释放。 |
| 2 | 90 | C++ 第 9 天：Tiling 与边界处理。打开 C++ 文件夹 days/day09/README.md，运行示例；现有练习按自身进度选做，参考实现可直接跟读。 |
| 3 | 30 | 复用 PA2 collective 输入输出；SHM、CUDA IPC、NIXL 各有环境条件，不笼统称全部零拷贝。 |
| 4 | 15 | 填写当天笔记，记录已运行与只读源码的边界。 |
| **合计** | **270** | **当天学习时间；休息另计** |

## 当天验收证据

- [ ] 控制面/数据面图
- [ ] C++ tiled MatMul 非整块尺寸结果

## 与已有工作的复用

C++ 只占这一段固定时间；Omni 后续课未实现时以固定源码/测试阅读推进，不声称已跑通。

## 原计划映射

| 来源 | 映射 | 用法 |
| --- | --- | --- |
| RL + Inference 原计划 | RL-D10 | 复用机制、实验或报告；不重复实现已有证据 |
| C++ 10 天 | C++-Day09 | 只在对应日打开本地课程入口 |
| K8S AI Infra 大纲 | — | 作为部署/调度/观测的选读映射，先读概念再看环境 |

## C++ 本地入口

- C++ Day 09 工作区路径：`../../../cpp-ai-systems-10days/days/day09/README.md`（本地已有工程入口，不把课程代码重复发布到本计划仓库）

## 阅读与源码入口

- [通信设计](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/docs/developer_reference/communication.md)
- [Relay 接口](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/relay/base.py)
- [SHM 后端](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/relay/shm.py)

- Omni 上游参考（仅相关日适用）：`870d77446b3fae6e4f4f2a6964f7eae2f75e663a`。

## 当天笔记

- [复制每日笔记模板](../templates/daily-note.md)
- 在仓库根目录运行：`python study/tools/note.py --day 14`
- 生成的填写内容保存在本地 `study/notes/`，不会进入 GitHub 计划文件。

[← Day 13](day13.md) · [返回 42 天总表](../DAILY-PLAN.md) · [Day 15 →](day15.md)
