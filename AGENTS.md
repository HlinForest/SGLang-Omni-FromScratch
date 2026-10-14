# SGLang-Omni From Scratch 启动文件

> 本文件基于仓库创建者提供的启动文本整理；教学方法与组织结构参考 [hong-kailin/OpenCodeFromScratch 的 AGENTS.md](https://github.com/hong-kailin/OpenCodeFromScratch/blob/video/AGENTS.md)。系统实现的学习对象是 [SGLang-Omni](https://github.com/sgl-project/sglang-omni)，底层 AR 引擎来自 [SGLang](https://github.com/sgl-project/sglang)。详细来源见 [CREDITS.md](CREDITS.md)。
> 当前仅完成仓库初始化，以下架构描述指向上游参考系统，课程实现尚未开始。

## 项目概述
本项目是一个教学项目：从零开始、一步一步重新实现 **SGLang-Omni**——SGLang 生态下专为全模态（Omni）、语音识别（ASR）、语音合成（TTS）与音乐生成模型打造的高性能多阶段推理服务框架。源码参考位于 `./sglang-omni/`（只读，不修改）。
参考版本：`sglang-omni` tag `v0.1.8`，固定 commit `870d77446b3fae6e4f4f2a6964f7eae2f75e663a`（仓库 `https://github.com/sgl-project/sglang-omni.git`）。复刻以此提交为准，不跟随滚动的 `main`。本地参考源码需按 [docs/REFERENCE.md](docs/REFERENCE.md) 单独获取。

`sglang-omni` 是一个以 Python（PyTorch + SGLang + FastAPI + 分布式通信层）为核心、辅以 Rust 路由器和原生硬件扩展的推理系统工程。它的核心设计目标是 **Multi-Stage Decoding（异构多阶段解耦推理）**：不同于单一 LLM 只需在一个自回归引擎里循环，Omni 与语音模型的单次生成往往跨越多个计算特性截然不同的阶段——预处理（Preprocessing）、多模态编码器（Vision/Audio Encoders）、特征汇聚（Fan-in Aggregator）、自回归思考主干（Thinker / AR Engine）、声学生成器（Talker AR / CFM 流匹配）以及流式声码器（Vocoder / Code2Wav）。
`sglang-omni` 负责管控 **流水线拓扑图（Pipeline Topology）、阶段生命周期（Stage Lifecycle）、跨阶段张量传输（Relay Data Plane）、模型族集成层（Model Integration）以及兼容 OpenAI 的流式 API 服务面**，同时在自回归阶段无缝复用上游 `SGLang` 的 RadixAttention、Continuous Batching 与 TP（张量并行）能力。

**我们的最终目标是 1:1 复刻 `sglang-omni` 的完整代码。** 我们相信每一行代码都有它存在的意义，因此不会跳过或省略任何部分。但 `sglang-omni` 涉及多进程拓扑编排、零拷贝张量中继、异构调度器与十余种复杂模型结构，一次性照搬无法理解其设计意图。所以我们的策略是：**从最简化的能跑版本起步，逐步演进到完整版**——先在单进程内用纯 Python `asyncio.Queue` 跑通一个“预处理 → AR 生成 → Vocoder 解码”的三阶段最小流水线，理解多阶段解耦解决什么问题，再逐步引入跨进程拓扑、Shared Memory / NIXL / Mooncake 零拷贝中继、SGLang 引擎桥接与多模态 Fan-in 汇聚，最终补全到与 `sglang-omni` 源码一致。遇到大量重复或模型定义样板代码时可以直接从源码复制，但复制前必须读懂它在做什么。最终产物是 `sglang-omni` 的完整 1:1 复刻。

## 用户画像
- 算法工程师，Python 与 PyTorch 基础扎实，熟悉常见深度学习模型结构与基础算法
- 擅长单卡模型训练与前向推理脚本，但对 **高性能推理系统工程（Inference Systems）** 不熟悉：如多进程拓扑与显存预算划分、控制面与数据面分离（IPC / 共享内存 / RDMA 零拷贝）、异构 Stage 调度器、CUDA Graph 静态图捕获重放、流式音频码本（RVQ Codebook / Delay Pattern）与实时 PCM 流式传输等，这些都需要从零教起
- 学习动机：多模态 Omni 与实时语音交互太火了，想彻底搞懂工业级多阶段推理引擎的内部原理，跨越“能写模型脚本”到“能造推理引擎”的鸿沟
- 学习方式：读代码 + 理解系统设计决策（trade-off），不是被布置作业

## 核心价值
读一万篇推理系统与多模态架构文章，不如亲手写一个多阶段推理运行时。

---

## SGLang-Omni 架构全景
理解我们要构建什么，先看真实的 `sglang-omni` 是怎么组织的。

### 模块分层
依赖方向：上 → 下（下层运行时与通信原语不知道具体模型与上层 HTTP 路由的存在）：

```
┌──────────────────────────────────────────────────────────────────────┐
│  sglang_omni/cli/ & sglang_omni/serve/ & sglang_omni_router/       │
│  入口与网关层（sgl-omni CLI、FastAPI OpenAI 兼容端点、SSE 与         │
│  audio/pcm 流式响应、Rust 多 Worker 路由与故障无缝迁移）             │
├──────────────────────────────────────────────────────────────────────┤
│  sglang_omni/models/                                                 │
│  模型族声明与组件层（Qwen3-Omni、Ming-Omni、MiniCPM-o、Higgs-TTS、   │
│  Qwen3-TTS、MOSS-TTS、Fish-S2、Qwen3-ASR、Whisper、MiniMax-Music 等）│
├──────────────────────────────────────────────────────────────────────┤
│  sglang_omni/pipeline/ & sglang_omni/config/                         │
│  流水线控制面与拓扑规划层（PipelineConfig / StageConfig 拓扑声明、   │
│  显存预算与进程组 Placement 校验、Coordinator 全局编排、Stage 封装） │
├──────────────────────────────────────────────────────────────────────┤
│  sglang_omni/engines/                       │
│  异构阶段调度与执行引擎层（SGLang AR Engine 桥接、SimpleScheduler    │
│  轻量批处理循环、TpModelWorker 编码器并行、LogitsProcessor、CUDA 图）│
├──────────────────────────────────────────────────────────────────────┤
│  sglang_omni/relay/ & sglang_omni/client/                            │
│  跨阶段数据面中继层（Control Notification + Relay Data Plane：       │
│  Shared Memory、NCCL、NIXL、Mooncake 零拷贝传输与 typed_tensor 编码）│
└──────────────────────────────────────────────────────────────────────┘
```


### 核心概念（对照真实源码）

| 概念 | 真实位置 | 说明 |
| :--- | :--- | :--- |
| **PipelineConfig & StageConfig** | `sglang_omni/config/schema.py` | 声明式流水线契约：定义 Stage 节点、路由边（Routing）、多路汇聚（Fan-in）、流式边（Streaming Edges）、多终点（Terminals）以及进程与显存拓扑（`stage.process`、`gpu_memory_fraction`） |
| **Coordinator** | `sglang_omni/pipeline/coordinator.py` | 流水线控制面大脑：维护每个请求的生命周期（`RequestInfo`），处理动态路由、Fan-in 同步等待、提前退出（Early End，如纯文本响应跳过语音模块）与多终点汇聚 |
| **Stage** | `sglang_omni/pipeline/` | 单个推理阶段的运行时容器：遵循 `Inbox → Scheduler → Executor/ModelRunner → Outbox` 模型，支持多 Stage 同进程共置（Colocation）或跨进程/跨卡隔离（Isolation） |
| **Stage-Specialized Scheduler** | `sglang_omni/engines/` | 匹配工作负载特征的专属调度器：AR 主干阶段复用 SGLang 的 Continuous Batching 调度器；非 AR 阶段（预处理、Encoder、CFM 采样、Vocoder）使用轻量级 `SimpleScheduler` 或流式循环 |
| **StagePayload** | `sglang_omni/models/.../payload_types.py` | 跨阶段流转的数据载体：封装请求元数据、控制信号（如 `finish_reason`）与张量字典，跨进程时通过 `typed_tensor` 协议与数据面中继配合传输 |
| **Control Plane vs Relay Data Plane** | `sglang_omni/relay/`、`docs/developer_reference/communication.md` | **控制面与数据面解耦**：控制面仅传递轻量级描述符（Descriptor）与就绪通知；笨重的中间态 Tensor（如视觉特征、Latent、音频波形）由 Relay 数据面通过共享内存（SHM）、NCCL、NIXL 或 Mooncake 零拷贝拉取 |
| **Thinker–Talker & Code2Wav** | `sglang_omni/models/` | Omni 与 TTS 的经典解耦范式：Thinker（大模型）负责跨模态推理并吐出文本与隐状态；Talker（小 AR 或 CFM/DiT）通过分段器（Segmenter）流式接收并生成声学 Token/Latent；Vocoder（Code2Wav）将其合成为实时 PCM 音频块 |
| **Placement & Topology Planner** | `sglang_omni/config/`、`sglang_omni/serve/launcher.py` | 启动期拓扑规划器：校验每个进程组的 GPU 绑定、汇总各 Stage 的 `gpu_memory_fraction`，并将 AR 阶段的显存预算精确折算为 SGLang 的 KV Cache 静态比例（`mem_fraction_static`） |

### Multi-Stage Pipeline 简化流程（以 Omni 多模态输入 + 文本/语音双流输出为例）

```
客户端请求 (/v1/chat/completions 或 /v1/audio/speech)
    │
    ▼
Coordinator 创建 RequestInfo，按 PipelineConfig 注入首阶段 Inbox
    │
    ▼
[Stage 1: Preprocessing] 解析多模态输入，动态决定激活哪些下游 Encoder
    │
    ├──(有图像/视频)──→ [Stage 2a: Vision Encoder (ViT/TP)] ──┐
    └──(有音频/参考音)─→ [Stage 2b: Audio Encoder (Whisper)] ──┤ (Relay 零拷贝传输 Tensor)
                                                               ▼
                       [Stage 3: mm_aggregate (Fan-in)] 等待当前请求所需的全部模态特征就绪
                                                               │
                                                               ▼
                       [Stage 4: Thinker (SGLang AR Engine)] 连续批处理自回归生成
                                    │                                    │
                  (流式吐出 Text Delta: Terminal 1)        (经 Segmenter 分段流式喂给下游)
                                    │                                    ▼
                                    │             ┌─→ [Stage 5: Talker (AR / CFM-DiT)]
                                    │             │        生成离散 Codebook 或连续 Latent
                                    │             │                      │
                                    │             │                      ▼
                                    │             └── [Stage 6: Vocoder / Code2Wav]
                                    │                      流式合成 PCM 音频 Chunk (Terminal 2)
                                    ▼                                    │
                       ┌────────────────────────┐                        │
                       │ 是否仅需文本 (Early End)│◄───────────────────────┘
                       └────────────┬───────────┘
                                    ▼
              HTTP 层实时流式推送 SSE 文本块 / audio/pcm 字节流，全部 Terminal 完成后回收请求
```


---

## 技术栈

| 技术 | 作用 | 对应算法工程师熟悉的 Python/DL 概念 |
| :--- | :--- | :--- |
| **uv + pyproject.toml (多硬件分支)** | 环境与包管理（支持 CUDA / XPU / ROCm / MUSA / NPU / CPU / MLX） | `conda` / `pip`，但用多套 `pyproject_*.toml` 管理异构算力依赖 |
| **PyTorch（默认配置 2.13.0）+ CUDA Graph** | 模型执行与静态计算图捕获/重放（加速 Talker CFM ODE 与 Decoder） | 常规 `nn.Module.forward()` vs 把多步循环录制成单次 GPU Kernel 发射 |
| **SGLang (`sglang.srt`)** | 自回归阶段的底层引擎（RadixAttention、Continuous Batching、TP） | 类似把 `model.generate()` 升级为支持前缀缓存与动态拼 Batch 的工业级服务引擎 |
| **Multiprocessing + ZMQ + Asyncio** | 多进程 Stage 隔离、控制面异步信令通知与协程事件循环 | 单机 `torch.multiprocessing` + 异步消息队列编排 |
| **SHM / NCCL / NIXL / Mooncake** | Relay 数据面：跨进程/跨机零拷贝 Tensor 传输后端 | 避免 `pickle` 序列化大 Tensor：只传内存地址/描述符，下游直接 DMA 读取 |
| **FastAPI + StreamingResponse** | OpenAI 兼容 API 服务面，支持 SSE 与原生二进制 `audio/pcm` 流 | 标准 Web 服务，但重点在于低首包延迟（TTFA）的服务端流式 Chunk 吐出 |
| **Pydantic / Dataclasses** | `PipelineConfig`、`StageConfig` 与 `StagePayload` 强类型拓扑契约 | 结构化配置校验，在服务启动前拦截拓扑冲突与显存超限 |

**“控制面与数据面分离的多阶段图调度（Stage Graph + Relay）”以及“与 SGLang SRT 引擎的无缝嵌合”是 `sglang-omni` 的灵魂。** 我们会渐进式引入：先用单进程 `asyncio` + 内存引用跑通多阶段流转，等感受到“GIL 与 GPU 争抢导致 Vocoder 阻塞 AR 解码”、“跨进程 Pickle 序列化大 Tensor 延迟爆炸”的痛点时，再引入多进程 Placement 隔离与 Relay 零拷贝中继。

---

## 学习路线图
详细的课程内容见 `COURSE.md`。核心原则：**每个阶段产出一个能跑、能测延迟/吞吐的东西。** 从阶段 0（开发环境与最小单进程三阶段 Pipeline 原型）到阶段 10（全模态 Omni 模型 Thinker-Talker 流式协同、CUDA Graph 优化与 Rust Router 多实例路由），共 11 个阶段，每个阶段先实现简化版，再逐步补全到与 `sglang-omni` 源码一致。
注意：`COURSE.md` 是活文档。进入每个阶段前细化具体课程内容，不提前规划过细。

---

## 开发约定

### 代码风格
学习 `sglang-omni`（及根目录下 `AGENTS.md`）的真实系统工程约定，但根据学习阶段渐进采用：
- **何时用 Omni 的边界纪律**：只有当请求本身包含“需独立调度的多阶段、动态路由、Fan-in 汇聚、阶段间流式传递或多终点完成”时才建 Stage；绝不把外部业务逻辑硬塞进推理 Stage 图
- **显式拓扑与配置唯一真源**：进程拓扑统一由 `StageConfig.process` 声明，显存预算由 `gpu_memory_fraction` 声明；启动期必须先过 Placement 与 Topology Planner 静态校验，拒绝隐式兜底或冲突覆写
- **控制面与数据面严格分离**：控制面消息只传轻量级元数据与 Tensor 描述符（Descriptor），大张量必须走 Relay 数据面或 `typed_tensor` 编码，禁止在控制信道直接 `pickle` 大尺寸 GPU/CPU Tensor
- **复用上游 SGLang 而非重复造轮子**：凡是上游 `sglang` 已有的能力（AR 模型定义、原生 TP 进程组、RadixCache、Continuous Batching），通过稳定的版本化契约面（如 `TpModelWorker` 或 SGLang Backend）桥接复用，不在 `sglang-omni` 内维护分叉副本
- **类型标注与契约**：全量使用 Python Type Hints（`dataclass` / `TypedDict` / `Protocol`）；跨 Stage 传递的数据必须在 `payload_types.py` 中明确定义字段与终止原因（`finish_reason`），避免用无约束的裸 `dict` 传状态
- **控制流与可读性**：优先使用 early return 消除深层嵌套；异步控制流（`asyncio`）与底层阻塞计算/GPU Kernel 严格解耦；注释解释“为什么这样设计（尤其是性能与显存 trade-off）”而非重复代码字面意思

### Git 规范
- Conventional Commits：`feat:` / `fix:` / `docs:` / `refactor:` / `perf:` / `test:`
- commit message 用中文（type 前缀保留英文，描述用中文，如 `docs: 添加项目启动文件`）
- **不要自动提交 commit**：完成工作后告知用户，等用户确认后再提交，不要自己执行 `git commit`
- 每个阶段完成后打 tag：`v0.1.0`、`v0.2.0` ...
- 分支：`main` 保持稳定，每个阶段独立分支开发
- 分支名：最多三个词，连字符分隔，如 `stage-graph`、`relay-shm`、`sglang-bridge`

### 文件组织
- **项目代码**：采用与 `sglang-omni` 一致的包结构，核心代码写在 `sglang_omni/` 下（包含 `config/`、`pipeline/`、`relay/`、`engines/`、`serve/`、`models/`、`client/` 等子模块）。渐进式起步——前期阶段只建当前用到的核心子包，随着课程推进逐步生长出完整的目录树
- **课程文档**：每个阶段在 `docs/` 下创建编号文件夹（如 `docs/00-minimal-pipeline/`），阶段内每节小课再创建子文件夹（如 `docs/00-minimal-pipeline/01-stage-inbox-outbox/`）
- **源码参考**：`./sglang-omni/` 目录只读，不修改，用于对照学习

### 文档拆分
**原则：一个文件只讲一件事。** 内容堆在一起会让人望而生畏，拆开读才轻松。
- 每节小课有独立文件夹，文件夹内放该课的文档（`.md`）和其他必要文件（架构图、测试音频样本、教学代码、Benchmark 脚本等）
- 一节课只讲一个知识点时，直接用 `README.md` 承载正文
- 一节课涉及多个概念时，拆成多个 `.md` 文件，`README.md` 只做目录导航（列出文件清单和阅读顺序），不承载正文
- 按序号编号：小课文件夹和拆出的文件都用数字前缀排序，如 `docs/01-process-topology/01-placement-planner/`、`docs/01-process-topology/02-gpu-memory-budget/`
- 判断拆分时机：一个 `README.md` 超过约 150 行，或出现“接下来讲……”这种明显的话题切换时，就该拆

### 教学代码
**原则：不布置作业，把代码讲透。** 通过读懂代码和观察系统指标学习，而不是被要求自己填空。
- **不设置动手作业**：课程文档不要出现“动手做：请自己实现一个 XX Stage”这类需要用户从零写代码的环节。用户的时间花在「读懂源码设计」与「观察运行现象」上，不是「被考」上
- **代码即教材**：文档里出现的每一段代码，都要有对应的、可直接打开阅读并运行的 `.py` 代码文件，让用户能进代码里学习，而不是只看文档里的代码片段
- **代码配文档**：每份教学代码配套一份说明文档，讲清这份代码解决什么系统瓶颈、关键设计点、怎么跑起来（含无大卡环境下的 Dummy/Mock Tensor 轻量运行模式与真实 GPU 模式）
- **详细注释**：教学代码要有详细注释。和项目代码“注释聚焦 Why”不同，教学代码的注释可以也应当解释「这段异步通信/张量中继/CUDA Graph 代码在做什么」「为什么这样写」，因为目的是让算法背景的读者看懂底层系统机制。修改代码时必须同步更新注释，不允许注释与代码不匹配
- **教 Debug 与 Profiling**：用户熟悉单进程训练调试，但对多进程推理服务调试不熟。课程要教具体的系统 debug 与性能剖析手法：多进程日志染色与追踪、跨进程死锁/队列积压排查、共享内存泄漏清理、CUDA Graph 捕获失败（动态 shape / CPU 同步点）如何定位、以及使用 Request-level Profiler 分析各 Stage 的排队与执行耗时（TTFT / TTFA / RTF）。不能只给“正确答案”代码，要演示“流水线卡死或显存 OOM 时怎么定位问题”

### 概念引入节奏
**原则：用到再讲，讲到再展开。** 不要提前透支后续课程的概念。
- **不提前引入**：课程文档不要提前介绍后续课程才讲到的概念。即使当前代码里不得不出现它，也只用一句话标注“后续 XX 课会讲”，不展开解释
- **在需要时才引入**：一个概念应当在它被真正需要、能解决一个具体系统瓶颈（如延迟抖动、显存冲突、吞吐受限）时才引入，而不是“顺便提一下”
- **先动手后概念**：一节课的内部顺序，优先「先跑通看输出与耗时对比、再回头看为什么」。系统概念没有实操指标打底就是空的——先让读者看到屏幕上流式吐出的数据或吞吐变化，再解释背后的架构原理
- **避免前向依赖**：写当前课程时，不要假设读者已经懂后续课程的内容；只能假设读者懂前面课程已讲过的东西

---

## 给 AI 助手的指令
当你在本项目的新 session 中工作时，请遵循以下原则：
1. **奥卡姆剃刀原则**：如无必要，勿增实体。能用简单方案解决的，不要引入额外的抽象、库或复杂度。先问“这个真的需要吗？”，而不是“这样做更优雅”。但记住最终目标是 1:1 复刻，简化只是过渡手段，不是终点
2. **教推理系统工程思维，不教基础 Python/DL 语法**：用户是算法工程师，Python 与深度学习基础扎实。重点是系统设计决策、多阶段解耦架构、控制面与数据面分离、显存与延迟 trade-off 分析，不是“什么是 PyTorch Tensor”或“什么是 Attention”。同时对多进程 IPC、零拷贝 Relay、SGLang SRT 内部桥接、流式音频工程等系统知识要从零讲透
3. **渐进式复杂度**：从最简单的实现开始，逐步引入系统抽象和优化。让用户亲眼看到“为什么需要这个抽象”的性能动机，而不是直接给最终方案。例如：先用单进程串行跑通三阶段推理，观察到 Vocoder 拖慢 AR 生成后再拆多进程；先用普通队列传 Tensor，观察到序列化开销后再引入 Shared Memory / NIXL Relay。但每个简化版最终都要补全到与 `sglang-omni` 源码一致
4. **关联已有算法知识**：解释新系统概念时，尽量关联用户熟悉的算法与 PyTorch 概念。比如用“PyTorch `DataLoader` 的 `pin_memory` 与 `num_workers` 共享内存队列”类比“`sglang-omni` 的 Relay Data Plane”，用“计算图算子融合（Operator Fusion）”类比“Talker 阶段的 CUDA Graph 多步 ODE 捕获”
5. **先问后做**：遇到系统设计决策（如 Stage 进程共置还是隔离、流式分块窗口大小 trade-off）时，给出选项和各自的延迟/吞吐/显存权衡，让用户选择。这是培养推理系统判断力的关键
6. **对照真实源码**：每个阶段实现简化版后，带用户看 `sglang-omni` 对应的真实源码（`./sglang-omni/` 目录），理解真实版为了支持多模型、多硬件与高并发为什么更复杂，再逐步把简化版补全到与源码一致。引用真实源码时使用 `sglang-omni/sglang_omni/...` 路径
7. **阶段验收**：每个阶段完成后，帮用户总结“这个阶段你掌握了什么推理系统工程思维”，而不是“你调了哪些 API”
8. **代码是思维的载体**：每段代码都应该能回答“为什么这样设计”。如果一段代码只是“源码里这么写的”，那就需要剖析它背后的硬件特性或并发原因
9. **中文为主，术语保留英文**：解释用中文，核心技术术语保留英文（如 `Coordinator`、`StagePayload`、`Relay Data Plane`、`Fan-in`、`Thinker-Talker`、`Continuous Batching`、`CUDA Graph`、`trade-off`）

## 当前状态
见 `COURSE.md` 的“当前状态”部分。
下一步：从阶段 0 开始。进入前先细化 `COURSE.md` 中阶段 0 的具体课程内容。
