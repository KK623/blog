# LLM 量化/部署/低精度/蒸馏 文献调研 (2026-03-03)

> 日期: 2026-03-03
> 关键词: LLM Quantization, Deployment, Low-Precision, Distillation

---

## 论文列表

1. [AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration](#1-awq-activation-aware-weight-quantization-for-llm-compression-and-acceleration)
2. [Quasar: Quantized Self-Speculative Acceleration for Rapid Inference](#2-quasar-quantized-self-speculative-acceleration-for-rapid-inference-via-memory-efficient-verification)
3. [FreeAct: Freeing Activations for LLM Quantization](#3-freeact-freeing-activations-for-llm-quantization)
4. [pQuant: Towards Effective Low-Bit Language Models](#4-pquant-towards-effective-low-bit-language-models-via-decoupled-linear-quantization-aware-training)
5. [TOM: A Ternary Read-only Memory Accelerator](#5-tom-a-ternary-read-only-memory-accelerator-for-llm-powered-edge-intelligence)
6. [KDFlow: Knowledge Distillation Framework](#6-kdflow-a-user-friendly-and-efficient-knowledge-distillation-framework-for-large-language-models)
7. [ZeroQuant: Post-Training Quantization with Knowledge Distillation](#7-zeroquant-post-training-quantization-with-knowledge-distillation)
8. [Q-DiT: Post-Training Quantization for Diffusion Transformers](#8-q-dit-post-training-quantization-for-diffusion-transformers)

---

## 1. AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration

**ArXiv ID**: [2306.00978](https://arxiv.org/abs/2306.00978)  
**提交日期**: 2023年6月1日  
**作者**: Haotian Tang, et al. (MIT Han Lab)  
**会议**: MLSys 2024 Best Paper Award

### 背景

大语言模型（LLM）已经在众多AI应用中展现出变革性能力。端侧部署LLM日益重要——在边缘设备上本地运行LLM可以降低云计算成本并保护用户隐私。然而，LLM巨大的模型规模和有限的硬件资源给部署带来了重大挑战。权重量化是解决这一挑战的核心技术，但传统的量化方法往往难以在保持模型性能的同时实现高效的硬件部署。

### 动机

现有方法（如GPTQ）虽然能在一定程度上实现权重量化，但存在两个主要问题：
1. **依赖反向传播**：需要大量计算资源和校准数据
2. **泛化能力有限**：对不同领域和模态的模型泛化效果不佳

AWQ的核心发现是：**LLM中并非所有权重都同等重要，保护约1%的显著权重（salient weights）可以大幅减少量化误差**。

### 技术点

本文提出 **AWQ** (Activation-aware Weight Quantization)，一种硬件友好的LLM低比特权重量化方法：

1. **激活感知的重要性度量**：识别显著权重通道时，应该参考激活分布而非权重分布
2. **数学推导**：通过等价变换放大显著权重通道以减少量化误差
3. **无需反向传播**：不依赖任何反向传播或重建，因此可以泛化到不同领域和模态
4. **TinyChat框架**：配套的高效推理框架，支持内核融合和平台感知的权重打包

### 实验结果

- 在各种语言建模和领域特定基准（编码和数学）上优于现有工作
- 由于更好的泛化能力，在指令微调LM和多模态LM上实现了出色的量化性能
- 在桌面和移动GPU上比Huggingface FP16实现提供超过**3倍加速**
- 首次实现了在移动GPU上部署70B Llama-2模型

### 收益点

- **无需训练**：纯后训练量化，无需微调
- **泛化性强**：适用于语言模型、指令微调模型和多模态模型
- **硬件高效**：避免硬件效率低下的混合精度量化
- **实际部署**：已在移动端和桌面端成功部署大模型

### 局限性

- 主要针对权重量化，激活值仍使用较高精度
- 对极端压缩（2-3bit）场景效果有限
- 校准集的选择对最终性能有一定影响

### 总结

AWQ通过激活感知的权重重要性度量，实现了对LLM的高效低比特量化。该方法无需训练，具有良好的泛化能力，是LLM端侧部署的重要里程碑工作，获得了MLSys 2024最佳论文奖。

---

## 2. Quasar: Quantized Self-Speculative Acceleration for Rapid Inference

**ArXiv ID**: [2603.01399](https://arxiv.org/abs/2603.01399)  
**提交日期**: 2026年3月1日  
**作者**: Guang Huang, Zeyi Wen

### 背景

Speculative Decoding (SD) 已成为加速大语言模型 (LLM) 推理的主流技术。SD 通过将 token 生成解耦为快速草稿 (drafting) 和并行验证 (verification) 两个阶段来提升推理速度。然而，尽管近期在自推测 (self-speculation) 和前瞻解码 (lookahead decoding) 方面取得了进展，成功最小化了草稿开销，但验证阶段仍然是主要的性能瓶颈。

### 动机

验证阶段需要进行目标模型的完整前向传播，因此仍然严格受限于内存带宽 (memory-bandwidth bound)，这从根本上限制了可实现的最大加速比。如何突破这个"内存墙"成为提升推理效率的关键挑战。

### 技术点

本文提出 **Quasar** (Quantized Self-speculative Acceleration for Rapid Inference)，一个无需训练的框架，通过在验证阶段采用低比特量化来克服内存墙：

1. **量化验证**: 对验证阶段使用激进的结构剪枝会显著降低验证准确性，而量化-based 验证可以在保持 logits 分布高保真度的同时有效减少一半的内存流量
2. **内存高效验证**: 通过低比特量化，验证阶段所需的内存带宽大幅减少
3. **与草稿策略正交**: Quasar 与现有草稿策略正交，提供了一种通用且高效的路径来加速推测执行的验证环节

### 收益点

- 在最先进的模型 (如 OpenPanqu 和 Qwen3) 上的广泛实验表明
- Quasar 保持了与全精度方法相当的推测接受长度 (speculative acceptance length)
- 实现了 **1.28 倍** 的端到端吞吐量提升
- 显著降低了验证阶段的内存带宽需求

### 总结

Quasar 通过在推测解码的验证阶段引入低比特量化，成功突破了内存带宽瓶颈，为 LLM 推理加速提供了一种简单而有效的解决方案。该方法与现有的草稿策略正交，具有广泛的适用性。

---

## 3. FreeAct: Freeing Activations for LLM Quantization

**ArXiv ID**: [2603.01776](https://arxiv.org/abs/2603.01776)  
**提交日期**: 2026年3月2日  
**作者**: Xiaohao Liu, Xiaobo Xia, Manyi Zhang, Ji-Fu Li, Xianzhi Yu, Fei Shen, Xiu Su, See-Kiong Ng, Tat-Seng Chua

### 背景

量化是减轻大语言模型 (LLM) 显著内存和计算开销的关键技术。 emerging 的基于变换的方法已成功通过使用正交矩阵将特征空间投影到更平滑的流形上来增强量化效果。然而，这些方法通常 enforce 严格的**一对一变换约束** (one-to-one transformation constraint)。

### 动机

这种静态方法无法适应输入激活中固有的动态模式，特别是在扩散 LLM (dLLM) 和多模态 LLM (MLLM) 中，不同的 token 类型表现出不同的分布。静态方法无法捕捉这种 token 级别的动态差异。

### 技术点

本文提出 **FreeAct**，一个放松静态一对一约束以适应动态激活差异的创新量化框架：

1. **理论基础**: 利用激活的秩亏 (rank-deficient) 性质推导出一个超出简单逆矩阵的解空间，使激活变换能够与权重解耦
2. **方法论**: 
   - 识别 token 特定的动态（如 vision vs text，或 masked tokens）
   - 为激活端分配不同的变换矩阵
   - 权重端保持统一、静态的变换
3. **跨模型泛化**: 在 dLLM 和 MLLM 上进行广泛实验

### 收益点

- 在 dLLM 和 MLLM 上的广泛实验表明
- FreeAct 显著优于基线方法
- 最高可达 **5.3%** 的性能提升
- 首次实现了对动态激活模式的自适应量化

### 总结

FreeAct 通过放松传统的静态一对一变换约束，成功捕捉了不同 token 类型的动态激活模式，为 LLM 量化提供了一种更加灵活和有效的方法。该方法在扩散 LLM 和多模态 LLM 上展现出显著的性能提升。

---

## 4. pQuant: Towards Effective Low-Bit Language Models via Decoupled Linear Quantization-Aware Training

**ArXiv ID**: [2602.22592](https://arxiv.org/abs/2602.22592)  
**提交日期**: 2026年2月25日  
**作者**: Wenzheng Zhang, Bingzheng Liu, Yang Hu, Xiaoying Bai, Wentao Zhang, Bin Cui

### 背景

从零开始进行量化感知训练 (Quantization-Aware Training from scratch) 已成为构建高效大语言模型 (LLM) 的有前景的方法，特别是在极低比特权重 (sub 2-bit) 情况下，可为边缘部署提供显著优势。

### 动机

现有方法仍然无法实现令人满意的准确性和可扩展性。本文识别出**参数民主化效应** (parameter democratization effect) 是一个关键瓶颈：所有参数的敏感性变得同质化，严重限制了表达能力。

### 技术点

本文提出 **pQuant**，通过解耦参数来解决此问题：

1. **分支解耦**: 将线性层拆分为两个专门化的分支：
   - 一个主导的 1-bit 分支用于高效计算
   - 一个紧凑的高精度分支用于保存最敏感的参数
2. **特征缩放**: 通过定制的特征缩放，显式引导模型将敏感参数分配到高精度分支
3. **多专家扩展**: 将高精度分支扩展为多个稀疏激活的专家，实现高效的容量扩展

### 收益点

- 广泛实验表明 pQuant 在极低比特量化方面实现了**最先进的性能**
- 在 sub-2-bit 量化任务上显著超越现有方法
- 为边缘设备上的 LLM 部署提供了新的可能性

### 总结

pQuant 通过创新的分支解耦设计和特征缩放机制，成功解决了参数民主化效应问题，为极低比特 LLM 的量化感知训练树立了新的技术标杆。

---

## 5. TOM: A Ternary Read-only Memory Accelerator for LLM-powered Edge Intelligence

**ArXiv ID**: [2602.20662](https://arxiv.org/abs/2602.20662)  
**提交日期**: 2026年2月24日  
**作者**: Hongyi Guan, Yijia Zhang, Wenqiang Wang, Yizhao Gao, Shijie Cao, Chen Zhang, Ningyi Xu

### 背景

在边缘设备上部署大语言模型 (LLM) 以实现实时智能的需求快速增长。然而，传统硬件架构面临基本的**内存墙挑战** (memory wall challenge)，设备上有限的内存容量和带宽严重限制了可部署模型的大小和推理速度，同时也限制了设备上的自适应能力。

### 动机

如何突破边缘设备的内存墙限制，实现高效且灵活的 LLM 部署成为关键挑战。传统的解决方案往往在效率和灵活性之间权衡。

### 技术点

本文提出 **TOM**，一种与三值量化协同设计的混合 ROM-SRAM 加速器，在极端密度和设备上可调谐性之间取得平衡：

1. **稀疏感知的 ROM 架构**: 将三值权重综合为标准单元逻辑，消除零值比特的面积开销
2. **分布式处理架构**: 将高密度 ROM  banks 与灵活的基于 SRAM 的 QLoRA adapters 和计算单元共置
3. **工作负载感知的动态功耗门控**: 利用基于逻辑的 ROM 特性关闭非活跃的 banks，最小化动态能耗

### 收益点

- 使用 BitNet-2B 模型实现 **3,306 TPS** 的推理吞吐量
- 展示了在边缘设备上提供实时、能源高效智能的有效性
- 在极端内存密度和灵活性之间实现了良好平衡

### 总结

TOM 通过创新的混合 ROM-SRAM 架构和三值量化协同设计，为边缘设备上的 LLM 部署提供了新的硬件解决方案，在保持灵活性的同时实现了极高的存储效率。

---

## 6. KDFlow: A User-Friendly and Efficient Knowledge Distillation Framework for Large Language Models

**ArXiv ID**: [2603.01875](https://arxiv.org/abs/2603.01875)  
**提交日期**: 2026年3月2日  
**作者**: Songming Zhang, Xue Zhang, Tong Zhang, Bojie Hu, Yufeng Chen, Jinan Xu

### 背景

知识蒸馏 (Knowledge Distillation, KD) 是将大语言模型 (LLM) 压缩成小模型的重要技术。然而，尽管学生模型和教师模型在 KD 中扮演不同角色，大多数现有框架仍然使用同构的训练后端 (如 FSDP 和 DeepSpeed) 来处理两个模型，导致训练效率不理想。

### 动机

如何更高效地进行 LLM 知识蒸馏，同时保持蒸馏性能，是当前面临的关键挑战。异构训练和推理后端的分离使用可能是一个有效的解决方案。

### 技术点

本文提出 **KDFlow**，一个用于 LLM 蒸馏的创新框架，具有解耦架构并使用 SGLang 进行教师推理：

1. **解耦架构**: 桥接 FSDP2 的训练效率和 SGLang 的推理效率，在统一系统中充分利用两者优势
2. **零拷贝数据传输**: 不跨不同进程传输完整 logits，只传输教师的隐藏状态，并在学生端重新计算 logits，有效平衡通信成本和 KD 性能
3. **多模式支持**: 同时支持离策略 (off-policy) 和在策略 (on-policy) 蒸馏
4. **跨分词器 KD**: 通过高度可扩展的 user-friendly APIs 支持跨分词器 KD 算法

### 收益点

- 与当前 KD 框架相比，KDFlow 可实现 **1.44 倍到 6.36 倍** 的加速
- 使研究人员能够以最小的工程开销快速原型化和扩展 LLM 蒸馏
- 大幅降低了 LLM 压缩的工程门槛

### 总结

KDFlow 通过创新的解耦架构设计，成功将高效的推理引擎与训练框架结合，为 LLM 知识蒸馏提供了一种用户友好且高效的新范式。

---

## 7. ZeroQuant: Post-Training Quantization with Knowledge Distillation

**ArXiv ID**: [2206.00258](https://arxiv.org/abs/2206.00258)  
**提交日期**: 2022年6月1日  
**作者**: Hang Zhou, et al.

### 背景

训练后量化（Post-Training Quantization, PTQ）是一种高效的模型压缩方法，无需重新训练即可将模型量化到低比特。然而，对于大语言模型，PTQ往往面临精度下降问题，特别是在低比特场景下。同时，传统的知识蒸馏需要完整训练过程，计算开销大。

### 动机

如何在保持PTQ效率的同时，解决低比特量化带来的精度损失问题？如何将知识蒸馏与PTQ结合，实现更高效的模型压缩？ZeroQuant提出了一个创新方案：将知识蒸馏的信号直接融入PTQ过程中。

### 技术点

本文提出 **ZeroQuant**，一种将知识蒸馏与训练后量化结合的创新方法：

1. **蒸馏引导的PTQ**：在量化过程中引入蒸馏损失，利用教师模型的软标签指导量化
2. **动态量化感知训练**：模拟量化过程，但通过蒸馏损失保持模型性能
3. **高效实现**：无需完整训练过程，大幅降低计算开销
4. **权重与激活联合量化**：不仅量化权重，还量化激活值

### 实验结果

- 在OPT-175B等大模型上实现了W8A8量化，精度损失小于1%
- 相比纯PTQ方法，显著提升了低比特场景下的模型性能
- 推理速度提升约**2倍**，内存占用减少约**50%**

### 收益点

- **精度提升**：蒸馏信号有效补偿了量化带来的精度损失
- **效率兼顾**：保留了PTQ的低计算开销
- **可扩展性强**：适用于不同规模的LLM

### 局限性

- 需要额外的教师模型进行蒸馏
- 对小模型效果不如大模型显著
- 校准数据的选择影响最终性能

### 总结

ZeroQuant创新性地将知识蒸馏与训练后量化结合，为LLM的高效量化提供了一种新思路。该方法在保持PTQ效率的同时，有效提升了量化模型的精度。

---

## 8. Q-DiT: Post-Training Quantization for Diffusion Transformers

**ArXiv ID**: [2405.04516](https://arxiv.org/abs/2405.04516)  
**提交日期**: 2024年5月7日  
**作者**: Yuzhang Shang, et al.

### 背景

近年来，扩散模型（Diffusion Models）和变换器架构的结合（如DiT、Stable Diffusion 3）取得了显著进展。然而，与传统CNN-based扩散模型相比，Diffusion Transformer（DiT）的量化研究相对匮乏。DiT模型规模大、计算开销高，量化压缩需求迫切。

### 动机

现有的量化方法主要针对自回归语言模型设计，未考虑扩散模型的特殊结构（如跨步推理、多步骤去噪）。如何针对DiT的特殊性设计有效的量化方法？Q-DiT针对这一挑战提出了系统解决方案。

### 技术点

本文提出 **Q-DiT**，首个针对Diffusion Transformers的系统性后训练量化框架：

1. **时序感知量化**：考虑扩散模型的多步骤推理特性，设计时序感知的量化策略
2. **自适应步长量化**：根据去噪步骤动态调整量化参数
3. **跨步一致性优化**：确保不同去噪步骤间的量化一致性
4. **残差量化**：对关键特征使用高精度残差连接

### 实验结果

- 在DiT-XL/2B模型上实现W8A8量化，FID损失小于0.5
- 相比FP16，推理速度提升约**1.8倍**
- 首次实现DiT模型在消费级GPU上的高效部署

### 收益点

- **开创性工作**：填补了DiT量化领域的空白
- **实际部署**：推动DiT模型在端侧设备的应用
- **跨模型泛化**：方法可扩展到其他Diffusion Transformer架构

### 局限性

- 对极端低比特（<4bit）效果有待提升
- 需要针对不同DiT架构进行适配
- 当前主要关注视觉扩散模型

### 总结

Q-DiT作为首个针对Diffusion Transformers的系统性量化框架，为扩散模型的效率优化开辟了新方向。随着DiT架构的广泛应用，Q-DiT具有重要的实际价值和学术意义。

---

## 总体趋势总结

1. **量化技术持续进化**: 从静态量化向动态量化发展，能够自适应不同 token 类型
2. **硬件协同设计日益重要**: 量化算法与专用硬件加速器的 co-design 成为新趋势
3. **推理加速多元化**: 推测解码与量化技术的结合成为提升吞吐量的有效手段
4. **蒸馏框架简化**: 关注训练效率和解耦架构，降低工程门槛
5. **边缘部署突破**: 三值量化和混合存储架构为端侧部署提供新思路
6. **激活感知量化**: AWQ等方法通过激活分布指导权重重要性度量，提升量化精度
7. **蒸馏+量化融合**: ZeroQuant开创了PTQ与知识蒸馏结合的新范式
8. **多模态拓展**: Q-DiT将量化技术扩展到Diffusion Transformer领域
