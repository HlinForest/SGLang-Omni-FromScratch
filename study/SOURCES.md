# 资料与源码导航

核对日期：2026-10-28。学习以原作者资料为准；本仓库只做安排与索引，不复制整套课程正文或课程解答。

## CSE291

- [课程主页](https://haoailab.com/cse291-s26/)与[作业页](https://haoailab.com/cse291-s26/assignments/)。作业页的列表目前落后于官方仓库。
- [官方作业仓库](https://github.com/hao-ai-lab/cse-dsc291-s26-pa)已包含PA1/PA2/PA3；具体必交项以对应说明为准。
- [PA1 notebook](https://github.com/hao-ai-lab/cse-dsc291-s26-pa/blob/b9428ec2466fcf777d79e0ea32501e889e49040c/pa1/CSE291-S26-PA1.ipynb)：autodiff、Transformer、训练与生成。
- [PA2 README](https://github.com/hao-ai-lab/cse-dsc291-s26-pa/blob/b9428ec2466fcf777d79e0ea32501e889e49040c/pa2/README.md)：Triton fused MatMul及MPI并行通信；远程grader需要课程提供的访问条件。
- [PA3 README](https://github.com/hao-ai-lab/cse-dsc291-s26-pa/blob/b9428ec2466fcf777d79e0ea32501e889e49040c/pa3/README.md)：MoE、训练成本、speculative decoding与个人论述；CPU逻辑验证不能替代GPU速度结论。

本机已下载官方起始代码，固定commit为 `b9428ec2466fcf777d79e0ea32501e889e49040c`，入口是工作区“CSE291作业”。本文件与日程已固定到该快照；以后更新作业说明时重新记录版本。日程不代替评分规则，不包含答案；五天未完成则顺延。

## SGLang-Omni

本地上游副本HEAD已核验为v0.1.8，commit：

    870d77446b3fae6e4f4f2a6964f7eae2f75e663a

以下链接全部固定到该提交。本地路径需加前缀sglang-omni/；教学实现sglang_omni/与它不是同一个目录。获取方法见[参考说明](../docs/REFERENCE.md)。

| 顺序/主题 | 固定源码入口 | 重点符号/问题 |
| --- | --- | --- |
| 1 数据契约 | [sglang_omni/models/qwen3_omni/payload_types.py](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/models/qwen3_omni/payload_types.py) | PromptInputs、ThinkerOutput、Qwen3OmniPipelineState |
| 2 配置 | [sglang_omni/config/schema.py](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/config/schema.py) | PipelineConfig、StageConfig |
| 3 Stage运行 | [sglang_omni/pipeline/stage/runtime.py](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/pipeline/stage/runtime.py) | Stage.run、execute、route_result |
| 4 输入汇聚 | [sglang_omni/pipeline/stage/input.py](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/pipeline/stage/input.py) | DirectInput、AggregatedInput |
| 5 请求协调 | [sglang_omni/pipeline/coordinator.py](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/pipeline/coordinator.py) | submit、stream、abort、handle_completion |
| 6 分块与结束 | [sglang_omni/pipeline/stage/stream_queue.py](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/pipeline/stage/stream_queue.py) | put、put_done、get_with_source |
| 7 进程放置 | [sglang_omni/config/placement.py](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/config/placement.py) | StagePlacementPlanner |
| 8 进程拓扑 | [sglang_omni/config/topology.py](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/config/topology.py) | build_process_topology_plan |
| 9 通信设计 | [docs/developer_reference/communication.md](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/docs/developer_reference/communication.md) | 控制消息、数据引用、后端条件 |
| 10 Relay | [sglang_omni/relay/base.py](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/relay/base.py) | Relay、RelayOperation |
| 11 CPU共享内存 | [sglang_omni/relay/shm.py](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/relay/shm.py) | 生命周期与释放 |
| 12 非AR调度 | [sglang_omni/scheduling/simple_scheduler.py](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/scheduling/simple_scheduler.py) | collect_batch、run_batch |
| 13 流式调度 | [sglang_omni/scheduling/streaming_simple_scheduler.py](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/scheduling/streaming_simple_scheduler.py) | on_stream_chunk、run_ready_step |
| 14 AR桥接 | [sglang_omni/scheduling/omni_scheduler.py](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/scheduling/omni_scheduler.py) | get_next_batch_to_run、emit_stream_output |
| 15 启动 | [sglang_omni/serve/launcher.py](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/serve/launcher.py) | launch_server |
| 16 服务API | [sglang_omni/serve/openai_api.py](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/serve/openai_api.py) | create_app、chat_completions、create_speech |
| 17 请求追踪 | [sglang_omni/profiler/event_recorder.py](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/profiler/event_recorder.py) | 事件时间线 |
| 18 指标视图 | [sglang_omni/profiler/views.py](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/profiler/views.py) | 从事件到指标 |

不需要从头顺序读完所有文件；当天只沿一个请求找相关部分。测试是行为说明和对照材料，不意味着当前Windows环境可以直接运行整套上游测试。

## 已有课程和辅助资料

- C++现有本地工程：工作区“C++ 10天”，入口README.md；D01–D10保持原顺序。语言查阅用[LearnCpp](https://www.learncpp.com/)、[C++ Core Guidelines](https://github.com/isocpp/CppCoreGuidelines)、[cppreference](https://en.cppreference.com/w/cpp)。构建参考[CMake Tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/)，性能测试参考[Google Benchmark](https://github.com/google/benchmark)；先使用课程现有计时工具，不为换工具重做项目。
- [原RL42天计划](https://github.com/HlinForest/rl-inference-lab/blob/main/docs/curriculum.md)和[原资料登记](https://github.com/HlinForest/rl-inference-lab/blob/main/docs/resources.md)：PMPP第4版、Ultra-Scale Playbook、Inference Engineering、RLHF Book及补充文章保留原出处与致谢。版本以原登记和当天实际运行记录为准。
- RLHF主阅读按[book/v0.12固定版](https://github.com/natolambert/rlhf-book/releases/tag/book/v0.12)，先用可枚举小任务验证概率和梯度，再讨论LLM。
- [程治玮《K8S AI Infra课程大纲》](https://my.feishu.cn/wiki/IGekw2vrdiCtS1kQYwIconEBnFb)：只核验过19章大纲。主选6/7/12/15/17/19，后接1/4/5；其余处置见[MAPPING](MAPPING.md)。
- [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/)、[GPU调度](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/)、[Scheduling](https://kubernetes.io/docs/concepts/scheduling-eviction/)作为概念和环境前提参考。
- [VS Code多文件夹工作区](https://code.visualstudio.com/docs/editing/workspaces/multi-root-workspaces)是统一入口的配置依据。

## 现有可运行内容与未实现内容

本机已有Omni阶段0标准库Mock、C++10天工程和RL-D01材料；不代表学习已经完成。Omni后续小课、真实引擎桥接、后续RL实验、GPU和K8S部署仍需逐课准备与验证。计划卡只约定目标、资料和证据。无对应环境就标为阅读/设计/待测，不将模拟当成真实性能。
