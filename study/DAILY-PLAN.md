# SGLang-Omni / CSE291 / C++ / RL + Inference / K8S · 42 天总表

> 主线顺序：**D01–D05 先完成 CSE291 → D06 起以 SGLang-Omni 为主线，C++ 在 D06–D15 集中完成 → D16–D26 补推理、K8S 与观测 → D27–D42 完成 RL 闭环、异步系统和一致性分析。**

## 使用边界

这些页面是每天的任务卡，不是全套已实现讲义。当前本地可直接运行的是 Omni 阶段 0 的 Mock Pipeline 和 C++ 10 天课程已有的可运行例子；其余 Omni、RL、推理和 K8S 内容按固定上游入口读代码、读文档、记录环境，具备 GPU/MPI/多进程/集群条件后再运行。

- 日程更新：`2026-10-28`；编号规则：逻辑学习日；未完成则顺延，不绑定日历日期。
- 时间口径：前5天300分钟，其余270分钟；休息另计，可在240–300分钟内缩减选读；本表合计 **11490 分钟**，休息另计。
- 起始状态：PA1/PA2/PA3均未完成；学习状态全部未开始；当前 42 行状态全部为 **未开始**。
- 前 5 天是 CSE291 PA1/PA2/PA3 的冲刺目标，不把“运行 local_check”当成整份作业完成；测试或必交项未通过就顺延，插入 CSE 补完日，D06 及以后整体顺延。
- 已有证据只复用一次：同一份 MatMul、MPI、推测解码或 benchmark 不为换教材再次重做；后续记录它被复用到哪个 RL/Omni/K8S 概念。
- SGLang-Omni 上游参考固定 commit：`870d77446b3fae6e4f4f2a6964f7eae2f75e663a`；上游目录只读。

## 每天任务

| 日 | 主线 | 分钟 | RL / C++ / K8S 映射 | 状态 |
| ---: | --- | ---: | --- | --- |
| [D01](days/day01.md) | CSE291 · PA1 自动微分与 Transformer 起步 | 300 | RL-D08 / — / — | 未开始 |
| [D02](days/day02.md) | CSE291 · PA1 收尾 → PA2 Triton | 300 | RL-D03, RL-D04 / — / — | 未开始 |
| [D03](days/day03.md) | CSE291 · PA2 MPI → PA3 MoE | 300 | RL-D10, RL-D12 / — / — | 未开始 |
| [D04](days/day04.md) | CSE291 · PA3 MoE、成本与推测解码 | 300 | RL-D19 / — / — | 未开始 |
| [D05](days/day05.md) | CSE291 · PA3 收尾与三份作业验收 | 300 | RL-D05, RL-D07, RL-D19 / — / — | 未开始 |
| [D06](days/day06.md) | Omni · Omni 任务与一份输入的变化 / C++ 1 | 270 | RL-D01 / C++-Day01 / — | 未开始 |
| [D07](days/day07.md) | Omni · Stage、队列与串行/流水线 / C++ 2 | 270 | RL-D07 / C++-Day02 / — | 未开始 |
| [D08](days/day08.md) | Omni · Payload 与所有权 / C++ 3 | 270 | — / C++-Day03 / — | 未开始 |
| [D09](days/day09.md) | Omni · 声明式配置与拓扑 / C++ 4 | 270 | — / C++-Day04 / — | 未开始 |
| [D10](days/day10.md) | Omni · Coordinator 请求生命周期 / C++ 5 | 270 | — / C++-Day05 / — | 未开始 |
| [D11](days/day11.md) | Omni · Fan-in、动态路由与多终点 / C++ 6 | 270 | — / C++-Day06 / — | 未开始 |
| [D12](days/day12.md) | Omni · 请求内流式输出 / C++ 7 | 270 | — / C++-Day07 / — | 未开始 |
| [D13](days/day13.md) | Omni · 进程放置与内存预算 / C++ 8 | 270 | RL-D08 / C++-Day08 / — | 未开始 |
| [D14](days/day14.md) | Omni · Relay：控制消息与张量数据 / C++ 9 | 270 | RL-D10 / C++-Day09 / — | 未开始 |
| [D15](days/day15.md) | Omni · 调度、背压与 C++ 总结 / C++ 10 | 270 | — / C++-Day10 / — | 未开始 |
| [D16](days/day16.md) | GPU 基础查漏与 Omni 数据路径复盘 | 270 | RL-D02, RL-D03, RL-D04, RL-D05, RL-D06, RL-D07 / — / — | 未开始 |
| [D17](days/day17.md) | SGLang AR 引擎桥接与请求路径 | 270 | RL-D15, RL-D17 / — / K8S-Ch06 | 未开始 |
| [D18](days/day18.md) | KV Cache、Prefix Cache 与失效边界 | 270 | RL-D16, RL-D18 / — / K8S-Ch07 | 未开始 |
| [D19](days/day19.md) | Continuous Batching 与 Chunked Prefill | 270 | RL-D17, RL-D18 / — / K8S-Ch15 | 未开始 |
| [D20](days/day20.md) | 量化与推测解码：复用 PA3 | 270 | RL-D19 / — / K8S-Ch15 | 未开始 |
| [D21](days/day21.md) | 训练显存与并行机制补齐 | 270 | RL-D08, RL-D09, RL-D10, RL-D11, RL-D12, RL-D13, RL-D14 / — / K8S-Ch12 | 未开始 |
| [D22](days/day22.md) | 服务入口、SSE/PCM 与延迟指标 | 270 | RL-D20 / — / K8S-Ch17 | 未开始 |
| [D23](days/day23.md) | Request-level Profiling 与可信性能报告 | 270 | RL-D05, RL-D20, RL-D21 / — / K8S-Ch17, K8S-Ch19 | 未开始 |
| [D24](days/day24.md) | K8S 基础与 GPU 资源声明 | 270 | — / — / K8S-Ch01, K8S-Ch04 | 未开始 |
| [D25](days/day25.md) | K8S 调度、冷启动与扩缩容 | 270 | — / — / K8S-Ch05, K8S-Ch11, K8S-Ch16 | 未开始 |
| [D26](days/day26.md) | Omni 阶段复盘与部署边界 | 270 | RL-D21 / — / — | 未开始 |
| [D27](days/day27.md) | RL 样本契约与 Omni 请求契约 | 270 | RL-D22 / — / — | 未开始 |
| [D28](days/day28.md) | REINFORCE 与可枚举基准 | 270 | RL-D23 / — / — | 未开始 |
| [D29](days/day29.md) | PPO Clip 与 GRPO-style | 270 | RL-D24, RL-D25 / — / — | 未开始 |
| [D30](days/day30.md) | KL、Mask 与评估 | 270 | RL-D26, RL-D27 / — / — | 未开始 |
| [D31](days/day31.md) | 同步 RL 闭环与模型服务边界 | 270 | RL-D28 / — / — | 未开始 |
| [D32](days/day32.md) | Ray Actor 与 Omni 多进程 | 270 | RL-D29, RL-D31 / — / — | 未开始 |
| [D33](days/day33.md) | 有界 Buffer 与背压 | 270 | RL-D30 / — / — | 未开始 |
| [D34](days/day34.md) | Staleness、超时与去重 | 270 | RL-D32, RL-D33 / — / — | 未开始 |
| [D35](days/day35.md) | 完整权重快照与缓存版本 | 270 | RL-D34 / — / — | 未开始 |
| [D36](days/day36.md) | 同步/异步对照与系统复盘 | 270 | RL-D35 / — / — | 未开始 |
| [D37](days/day37.md) | 数值差异与 Batch Invariance | 270 | RL-D36 / — / — | 未开始 |
| [D38](days/day38.md) | IS / TIS 与三种概率 | 270 | RL-D37 / — / — | 未开始 |
| [D39](days/day39.md) | Pack/Unpack 与原子发布 | 270 | RL-D38, RL-D39 / — / — | 未开始 |
| [D40](days/day40.md) | 异构采样案例与 Omni 后续路线 | 270 | RL-D40 / — / — | 未开始 |
| [D41](days/day41.md) | 三组种子与最终测量补齐 | 270 | RL-D27, RL-D41 / — / — | 未开始 |
| [D42](days/day42.md) | 整理成果、复现与下一阶段 | 270 | RL-D42 / — / — | 未开始 |

## 每天的固定收尾

1. 打开当天页面，先回答目标问题，再按顺序执行 blocks。
2. 勾选证据；将观察到的事实和自己的解释分开写。
3. 在仓库根目录运行 `python study/tools/note.py --day N`，填写本地笔记；不把 CSE291 解答代码或机器私有日志提交到 GitHub。
4. 如果测试失败，保留失败证据并顺延；不要为了日历上的 Day 编号把状态改成已完成。

## 目录

- C++ 10 天课程（工作区路径：`../../cpp-ai-systems-10days/README.md`）
- [RL + Inference 原始 42 天计划](https://github.com/HlinForest/rl-inference-lab/blob/main/docs/curriculum.md)
- [K8S AI Infra 衔接说明](MAPPING.md)
- [每日笔记模板](templates/daily-note.md)
