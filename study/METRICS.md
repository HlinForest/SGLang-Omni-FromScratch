# 性能笔记的统一口径

每份结果先声明：真实模型 / Mock、CPU / GPU / 集群、代码commit、模型revision、设备、依赖、dtype、shape、采样参数、输入输出长度、并发或到达率、预热、样本数、失败率和计时边界。

| 指标 | 本计划的记录定义 | 注意 |
| --- | --- | --- |
| TTFT | 请求起点到第一个有效文本token | 写清客户端发起还是服务端接收；排除空控制事件 |
| TTFA | 请求起点到第一个可用于播放的非空音频块 | 要写清首次字节、完整chunk或客户端可解码之间的差异 |
| Stage queue time | 输入可调度到真正开始执行 | 上游传输等待与队列等待不要重复累计 |
| Stage execution time | 定义好的执行开始到结束 | 异步GPU操作需正确同步/事件计时；CPU提交耗时不等于kernel耗时 |
| Stage hop time | 定义的上游交出到下游收到 | 包含哪些编码/搬运/等待步骤必须声明 |
| E2E | 请求起点到定义的最终输出完成 | 文本终点与音频终点分别记录；多终点请求注明完成条件 |
| TPOT | (最终token时刻－首token时刻)/(输出token数－1) | 至少2个token才有定义；平均值会掩盖抖动 |
| 音频chunk间隔 | 连续音频块到达时刻之差 | 同时记录每块音频时长；不直接等同播放器卡顿 |
| RTF | 指定生成墙钟时长/生成音频总秒数 | 本报告选择是否包含排队/传输并注明；音频时长为0则不适用 |
| 吞吐 | 指定窗口的完成请求/token/音频秒数除以窗口秒数 | 单位明确；错误和丢弃不能悄悄剔除 |

计时的定义是本计划的报告约定，不保证等同每个上游工具的同名字段。对照[固定版事件记录器](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/profiler/event_recorder.py)与[指标视图](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/sglang_omni/profiler/views.py)，以实际事件含义核对。

输出平均值与p50/p95时保留样本数及原始日志。并发固定的闭环测量、到达率固定的开环测量分开；每次只改一个变量。没有硬件时可以留下实验设计，但实测字段填写“待测”。

CPU MatMul、PA2 GPU fused MatMul、Omni模型端到端任务具有不同计算与I/O边界。分别报告，不据此直接宣布CPU/GPU速度倍数。模拟等待只验证调度现象，不证明模型加速。
