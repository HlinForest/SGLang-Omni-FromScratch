# Credits 与来源说明

感谢以下项目的作者、维护者与贡献者。本页区分教学方法的来源、主要复刻对象和底层技术来源，避免把上游工作表述为本项目原创。

## OpenCodeFromScratch：教学方法与启动文件结构

- 项目：[hong-kailin/OpenCodeFromScratch](https://github.com/hong-kailin/OpenCodeFromScratch)
- 用户指定的参考：[video 分支 / AGENTS.md](https://github.com/hong-kailin/OpenCodeFromScratch/blob/video/AGENTS.md)
- 初始化时核对的固定版本：[998819165d8380aebb03017942cdb1d917b572ca / AGENTS.md](https://github.com/hong-kailin/OpenCodeFromScratch/blob/998819165d8380aebb03017942cdb1d917b572ca/AGENTS.md)

本项目采用的渐进式复刻路线、读代码与理解设计决策的学习方式、代码配文档、按需引入概念，以及 AI 助手教学约定，参考了该项目。用户提供的 SGLang-Omni 启动文件沿用了这套组织方式，并将学习对象和系统工程内容改为 SGLang-Omni。

初始化时未在所参考的 `video` 分支根目录发现仓库级 `LICENSE` 文件，GitHub 仓库元数据也未标明许可证。本页记录来源，不为其材料另行指定许可证。本仓库没有复制该项目的课程正文或实现代码。

## SGLang-Omni：主要学习与复刻对象

- 项目：[sgl-project/sglang-omni](https://github.com/sgl-project/sglang-omni)
- 参考 tag：[`v0.1.8`](https://github.com/sgl-project/sglang-omni/tree/v0.1.8)
- 固定提交：[`870d77446b3fae6e4f4f2a6964f7eae2f75e663a`](https://github.com/sgl-project/sglang-omni/tree/870d77446b3fae6e4f4f2a6964f7eae2f75e663a)
- 仓库级许可证：[Apache License 2.0](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/LICENSE)

多阶段流水线、阶段生命周期、拓扑编排、Relay 数据面、模型集成和流式服务等设计的技术来源是 SGLang-Omni。未来引用、移植或改写其代码时，需要在对应文件或课程中记录来源路径与版本，并保留适用的原始版权和许可证说明；模型目录中另附的第三方许可也要逐项保留。

## SGLang：底层自回归推理引擎

- 项目：[sgl-project/sglang](https://github.com/sgl-project/sglang)
- 仓库级许可证：[Apache License 2.0](https://github.com/sgl-project/sglang/blob/main/LICENSE)
- 版本关系：[SGLang-Omni v0.1.8 的 pyproject.toml](https://github.com/sgl-project/sglang-omni/blob/870d77446b3fae6e4f4f2a6964f7eae2f75e663a/pyproject.toml) 在相应平台依赖条件下固定 `sglang==0.5.21`。

RadixAttention、Continuous Batching 和相关自回归执行能力来自 SGLang。课程将研究如何桥接与复用这些能力，相关贡献归原作者和贡献者所有。

## 本仓库的材料与后续记录

本次初始化包含用户提供并经版本信息校准的 `AGENTS.md`，以及新编写的 README、路线图、导航和来源说明；未导入上游实现代码、模型权重、音频数据或图片。根目录暂未为全部材料统一指定分发许可证，上游许可证也不会因此自动适用于本仓库的全部文档。

后续实际引入 PyTorch、通信库、模型实现或示例数据时，按文件和课程补充直接来源、具体版本及适用许可，避免把计划采用的组件误列为已经集成。

本项目为独立教学与学习项目，不代表 OpenCodeFromScratch、SGLang-Omni 或 SGLang 官方。
