# 原计划如何合并

总 D 表示本套整合计划，RL-D 表示原 RL + Inference 的章节编号，C++-D 表示 C++ 原课程编号。资料出现过不等于已完成；只有同一目标的正确性、输入输出和实验条件得到验证，才可抵扣。

## 不重复做的五件事

| 重叠 | 本轮唯一主要证据 | 后面怎样用 |
| --- | --- | --- |
| GPU MatMul/tiling | CSE291 PA2 | RL-D3–D5复用；C++只研究CPU内存，不再复制GPU作业 |
| Collective/TP/MoE | PA2/PA3 | RL-D10/D12复用，D21补ZeRO/PP与训练显存差异 |
| Speculative decoding | PA3 Part3 | 总D20解释成本与失败条件，不写第二套实现 |
| 推理请求/缓存/调度 | SGLang-Omni固定版本及所接SGLang引擎 | K8S中的vLLM章节作概念对照，不另建vLLM课程 |
| Benchmark/日志 | 一套负载配置与证据索引 | Omni、K8S可观测性复用指标口径；真实GPU、CPU与Mock分开 |

## 原 RL 42 个主题的去向

这是主题和最小验证的整合，不是再额外执行原计划的84–126小时。原后续实验多数仍待逐课建设；本计划没有把任务卡冒充已交付的实验代码。

| 原日 | 主题 | 整合日 | 本轮处理 |
| --- | --- | --- | --- |
| RL-D01 | Tensor/storage/stride | D06 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D02 | Vector add 与尾块 | D16 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D03 | MatMul 索引 | D02、D16 | 复用CSE证据，补缺口；未过测试不抵扣 |
| RL-D04 | Shared-memory tiling | D02、D16 | 复用CSE证据，补缺口；未过测试不抵扣 |
| RL-D05 | 配置与计时 | D05、D16、D23 | 复用CSE证据，补缺口；未过测试不抵扣 |
| RL-D06 | Reduction | D16 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D07 | GPU 基础复盘 | D05、D07、D16 | 复用CSE证据，补缺口；未过测试不抵扣 |
| RL-D08 | 显存组成 | D01、D13、D21 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D09 | 梯度累积与 checkpoint | D21 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D10 | Collectives | D03、D14、D21 | 复用CSE证据，补缺口；未过测试不抵扣 |
| RL-D11 | DP 与 ZeRO | D21 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D12 | TP | D03、D21 | 复用CSE证据，补缺口；未过测试不抵扣 |
| RL-D13 | PP 与通信重叠 | D21 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D14 | 并行复盘 | D21 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D15 | Prefill/decode 与基线 | D17 | 用Omni/SGLang替代vLLM主实践；GPU结果按环境验证 |
| RL-D16 | KV 预算与回收 | D18 | 用Omni/SGLang替代vLLM主实践；GPU结果按环境验证 |
| RL-D17 | Continuous batching | D17、D19 | 用Omni/SGLang替代vLLM主实践；GPU结果按环境验证 |
| RL-D18 | Prefix cache/chunked prefill | D18、D19 | 用Omni/SGLang替代vLLM主实践；GPU结果按环境验证 |
| RL-D19 | 量化与推测解码 | D04、D05、D20 | 复用CSE证据，补缺口；未过测试不抵扣 |
| RL-D20 | Benchmark | D22、D23 | 用Omni/SGLang替代vLLM主实践；GPU结果按环境验证 |
| RL-D21 | 推理报告 | D23、D26 | 用Omni/SGLang替代vLLM主实践；GPU结果按环境验证 |
| RL-D22 | 样本与概率契约 | D27 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D23 | REINFORCE | D28 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D24 | PPO clipped objective | D29 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D25 | GRPO-style | D29 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D26 | KL/mask/aggregation | D30 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D27 | 评估与多 seed | D30、D41 | 评估合并到D41；各3 seed，未运行保留待测 |
| RL-D28 | 同步 RL 闭环 | D31 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D29 | Ray actor | D32 | 保留最小actor实验；先核验Ray环境 |
| RL-D30 | 有界 buffer | D33 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D31 | Sampler/learner 编排 | D32 | 保留最小actor实验；先核验Ray环境 |
| RL-D32 | Staleness | D34 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D33 | Timeout/去重 | D34 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D34 | 权重快照版本 | D35 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D35 | 同步/异步比较 | D36 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D36 | Batch invariance | D37 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D37 | IS/TIS | D38 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D38 | Pack/unpack | D39 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D39 | 原子发布与故障 | D39 | 保留核心机制与最小验证，按日程合并阅读 |
| RL-D40 | 异构采样案例 | D40 | 案例选读，后置大型集群复现 |
| RL-D41 | 三 seed 总比较 | D41 | 评估合并到D41；各3 seed，未运行保留待测 |
| RL-D42 | 复现与总结 | D42 | 保留核心机制与最小验证，按日程合并阅读 |

## 10 天 C++

总 D06–D15 对应 C++-D01–D10，按现有工程顺序学习，合计约12.5小时。VS Code 的“C++ 10天”文件夹保留示例、练习、参考实现与构建/调试任务。学习笔记集中在本仓库 study/notes；旧课程的 notes.md 不要求再写一遍。

## K8S 19 章的去向

仅核验过飞书课程大纲，未核验全部课程视频、课时或练习。缺完整课件时按本计划源码与官方文档学习，不把未读课标成完成。

| 章 | 主题 | 安排 |
| --- | --- | --- |
| 1 | K8S核心/Pod | D24核心选读；部署按测试集群条件 |
| 2 | Operator/CRD | 后置，暂不开发控制器 |
| 3 | 生产集群/高可用 | 后置 |
| 4 | GPU资源栈 | D24选驱动/toolkit/device plugin；MIG/MPS/DRA后置 |
| 5 | 调度 | D25选资源、亲和/污点；gang/拓扑高级策略后置 |
| 6 | vLLM请求路径 | D17改用Omni/SGLang源码，概念对照 |
| 7 | Prefix/KV路由 | D18；不假设同名组件/API |
| 8 | KV offload/connector | 后续缓存深入路线；本轮只知道职责 |
| 9 | LoRA管理 | 后置 |
| 10 | Pause/resume | 后置 |
| 11 | 冷启动 | D25选读 |
| 12 | 并行策略 | D21复用PA2/PA3与RL并行基础 |
| 13 | 多节点/MP/Ray/LWS | K8S多节点后置；D32仅Ray本机语义 |
| 14 | P/D分离 | 后续架构选读，不新建分离集群 |
| 15 | 推理调优 | D19/D20，迁移问题而非照抄vLLM开关 |
| 16 | HPA/KEDA | D25概念与前提；自动扩缩集群后置 |
| 17 | 可观测性 | D22/D23，加入音频TTFA和stage指标 |
| 18 | eBPF/perf | 后置 |
| 19 | Profiler/Nsight | D23按硬件选用 |

## 后续长期路线

完整模型族、真实流式音频、CUDA Graph、Rust Router、NIXL/Mooncake、多节点部署和完整1:1复刻继续沿COURSE.md推进。42天结束标志是一轮可追溯的学习与有限实验，不是上游功能全部实现。
