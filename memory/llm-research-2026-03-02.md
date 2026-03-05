# LLM量化/部署/低精度/蒸馏技术调研报告

**调研日期**: 2026-03-02  
**调研人**: Subagent

---

## 摘要

本报告聚焦于2026年2月下旬至3月初发布的大语言模型（LLM）量化、部署、低精度及蒸馏相关最新论文昨日已发布经典文献调研，本次主要关注过去24小时的新发表成果及近期热点方向。涵盖了包括高效量化方法、边缘部署、模型压缩框架等前沿研究。

---

## 一、量化技术最新进展

### 1.1 高效低比特量化

#### pQuant: Decoupled Linear Quantization-Aware Training
- **作者**: Wenzheng Zhang, Bingzheng Liu, Yang Hu 等
- **arXiv**: 2602.23351
- **摘要**: 提出解耦线性量化感知训练方法，用于构建高效的低比特语言模型
- **亮点**: 从 scratch 进行 QAT 的新范式

#### NanoQuant: Efficient Sub-1-Bit Quantization
- **作者**: Hyochan Chong, Dongkyu Kim, Changdong Kim, Minseop Choi
- **arXiv**: 提交于 2026年2月6日
- **摘要**: 针对 LLM 的亚1比特量化的高效方法
- **亮点**: 突破 1 比特限制的量化技术

#### Quecto-V1: 8-bit Quantized Small Language Models
- **作者**: Subrit Dikshit
- **arXiv**: 提交于 2026年2月18日
- **摘要**: 8比特量化小型语言模型在设备端法律检索中的实证分析
- **应用场景**: 资源受限环境的法律智能系统

#### TernaryLM: Native 1-Bit Quantization
- **作者**: Nisharg Nargund, Priyesh Shukla
- **arXiv**: 提交于 2026年2月7日
- **摘要**: 通过自适应层缩放实现原生1比特量化的内存高效语言建模
- **亮点**: 1比特原生量化 + 自适应层缩放

#### RaBiT: Residual-Aware Binarization Training
- **作者**: Youngcheon You, Banseok Lee, Minseop Choi 等
- **arXiv**: 提交于 2026年2月5日
- **摘要**: 用于准确高效 LLM 的残差感知二值化训练
- **技术**: 二值化(±1)层 + 硬件友好的 matmul-free 推理

#### BPDQ: Bit-Plane Decomposition Quantization
- **作者**: Junyu Chen, Jungang Li, Jing Xiong 等
- **arXiv**: 提交于 2026年2月3日
- **摘要**: 面向 LLM 的位平面分解量化，灵活位宽
- **亮点**: 可变网格上的量化方法

### 1.2 量化与推理优化

#### QTALE: Quantization-Robust Token-Adaptive Layer Execution
- **作者**: Kanghyun Noh, Jinheon Choi, Yulhwa Kim
- **arXiv**: 2602.22207
- **摘要**: 量化鲁棒的 Token 自适应层执行技术
- **亮点**: 针对量化的鲁棒性优化

#### Astro: Activation-guided Structured Regularization
- **作者**: Xi Chen, Ming Li, Junxi Li 等
- **arXiv**: 提交于 2026年2月7日
- **摘要**: 用于异常值鲁棒 LLM 后训练量化的激活引导结构化正则化
- **核心**: 解决量化中的异常值问题

#### D²Quant: Accurate Low-bit Post-Training Weight Quantization
- **作者**: Xianglong Yan, ChengZhu Bao 等
- **arXiv**: 提交于 2026年2月3日
- **摘要**: 准确的后训练权重量化方法

#### MatGPTQ: Matryoshka Quantization
- **作者**: Maximilian Kleinegger, Elvir Crnčević, Dan Alistarh
- **arXiv**: 提交于 2026年2月3日
- **摘要**: 精确高效的 Matryoshka 后训练量化
- **亮点**: 多粒度量化技术

#### MoBiQuant: Mixture-of-Bits Quantization
- **作者**: Dongwei Wang, Jinhee Kim, Seokho Han 等
- **arXiv**: 提交于 2026年2月21日
- **摘要**: Token 自适应弹性 LLM 的混合位量化
- **创新**: 不同 token 使用不同位宽

#### Regularized Calibration with Successive Rounding
- **作者**: Seohyeon Cha, Huancheng Chen, Dongjun Kim 等
- **arXiv**: 提交于 2026年2月5日
- **摘要**: 后训练量化的正则化校准与连续舍入技术

### 1.3 量化与隐私/安全

#### Quantization-Robust LLM Unlearning via LoRA
- **作者**: João Vitor Boer Abitante, Joana Meneguzzo Pasquali 等
- **arXiv**: 提交于 2026年2月13日
- **摘要**: 通过低秩适应实现量化鲁棒的 LLM 遗忘学习
- **应用**: 在量化模型中移除特定知识

#### Differential Privacy + Split Inference
- **作者**: Yujie Gu, Richeng Jin, Xiaoyu Ji 等
- **arXiv**: 提交于 2026年2月11日
- **摘要**: 差分隐私与通信高效 LLM 分割推理
- **技术**: 随机量化 + 软提示

---

## 二、部署与推理优化

### 2.1 边缘端部署

#### TOM: Ternary Read-only Memory Accelerator
- **作者**: Hongyi Guan, Yijia Zhang, Wenqiang Wang 等
- **arXiv**: 提交于 2026年2月24日
- **摘要**: LLM 边缘智能的三元只读存储器加速器
- **应用场景**: 边缘设备部署

#### Compact LLM Deployment in Mobile Edge Computing
- **作者**: Ruichen Zhang, Xiaofeng Luo, Jiayi He 等
- **arXiv**: 提交于 2026年2月14日
- **摘要**: 移动边缘计算中的紧凑 LLM 部署与世界模型辅助卸载
- **亮点**: 边缘端部署 + 推理卸载

#### Mapping Gemma3 onto Edge Dataflow Architecture
- **作者**: Shouyu Du, Miaoxiang Yu, Zhenyu Xu 等
- **arXiv**: 提交于 2026年2月24日
- **摘要**: Gemma3 在 AMD Ryzen AI NPU 上的端到端部署
- **技术**: 高效解量化引擎、FlowQKV

### 2.2 高效推理架构

#### Scaling State-Space Models with Tensor Parallelism
- **作者**: Anurag Dutt, Nimit Shah, Hazem Masarani, Anshul Gandhi
- **arXiv**: 提交于 2026年2月24日
- **摘要**: 多 GPU 分布式推理的状态空间模型张量并行
- **目标**: 突破单 GPU 内存/带宽限制

#### SpeContext: Speculative Context Sparsity
- **作者**: Jiaming Xu, Jiayi Pan, Hanzhen Wang 等
- **arXiv**: 提交于 2025年11月29日
- **摘要**: 长上下文推理的投机上下文稀疏化
- **应用**: 高效长上下文处理

---

## 三、模型压缩与蒸馏

### 3.1 统一压缩框架

#### UniComp: Unified Evaluation of LLM Compression
- **arXiv**: 提交于 2026年2月11日
- **摘要**: 通过剪枝、量化和蒸馏对 LLM 压缩的统一评估
- **亮点**: 统一评估框架

#### SPQ: SVD-Pruning-Quantization Ensemble
- **arXiv**: 提交于 2026年2月20日
- **摘要**: 大语言模型压缩的集成技术

### 3.2 剪枝技术

#### GradPruner: Gradient-Guided Layer Pruning
- **作者**: Wei Huang, Anda Cheng, Yinggui Wang
- **arXiv**: 提交于 2026年1月27日
- **摘要**: 梯度引导的层剪枝，实现 LLM 高效微调和推理

#### FineScope: Precision Pruning with SAE
- **arXiv**: 提交于 2025年
- **摘要**: 使用 SAE 引导自数据培育的领域专用 LLM 精确剪枝

### 3.3 蒸馏与压缩

#### SlimMoE: Expert Slimming and Distillation
- **作者**: Zichong Li, Chen Liang, Zixuan Zhang 等
- **arXiv**: 提交于 2025年6月23日
- **摘要**: 通过专家精简和蒸馏对大型 MoE 模型进行结构化压缩

#### daDPO: Distribution-Aware DPO
- **作者**: Zhengze Zhang, Shiqi Wang, Yiqun Shen 等
- **arXiv**: 提交于 2025年6月2日
- **摘要**: 用于蒸馏对话能力的分布感知 DPO

#### EPiC: Edge-Preserving CoT Condensation
- **作者**: Jinghan Jia, Hadi Reisizadeh, Chongyu Fan 等
- **arXiv**: 提交于 2025年6月4日
- **摘要**: 通过边沿保留的思维链压缩实现推理训练无损加速

---

## 四、视觉-语言-动作模型量化

#### QVLA: Vision-Language-Action Model Quantization
- **作者**: Yuhao Xu, Yantai Yang, Zhenyang Fan 等
- **arXiv**: 提交于 2026年2月3日
- **摘要**: VLA 模型量化中并非所有通道都同等重要
- **应用**: 机器人平台部署

#### AdaTSQ: Temporal-Sensitivity Quantization for DiT
- **作者**: Shaoqiu Zhang, Zizhong Ding, Kaicheng Yang 等
- **arXiv**: 提交于 2026年2月10日
- **摘要**: Diffusion Transformer 的时序敏感量化
- **目标**: 高效图像/视频生成

---

## 五、理论研究与分析

#### Price of Universality in Vector Quantization
- **作者**: Alina Harbuzova, Or Ordentlich, Yury Polyanskiy
- **arXiv**: 提交于 2026年2月5日
- **摘要**: 矢量量化的通用性代价不超过 0.11 比特
- **亮点**: 信息论角度的分析

#### Rethinking Perplexity: Input Length Impact
- **作者**: Letian Cheng, Junyan Wang, Yan Gao 等
- **arXiv**: 提交于 2026年2月3日
- **摘要**: 重新思考困惑度：输入长度对 LLM 困惑度评估的影响

---

## 六、总结与趋势分析

### 6.1 当前研究热点

1. **超低比特量化**: 1-bit、2-bit 量化技术持续突破，RaBiT、 TernaryLM 等工作推动极端压缩边界
2. **Token 自适应量化**: MoBiQuant、QTALE 等工作根据 token 重要性动态调整量化精度
3. **硬件感知优化**: 边缘端部署成为热点，Gemma3 在 NPU 上的部署工作展示硬件协同设计
4. **量化鲁棒性**: Astro、Quantization-Robust Unlearning 等关注量化对模型行为的影响
5. **多模态量化**: VLA 模型、Diffusion Transformer 的量化需求增长

### 6.2 技术路线对比

| 方向 | 代表工作 | 优势 | 局限 |
|-----|---------|-----|-----|
| 1-bit 量化 | TernaryLM, RaBiT | 极致压缩 | 精度损失大 |
| 混合位量化 | MoBiQuant | 灵活性高 | 复杂度增加 |
| 后训练量化 | D²Quant, MatGPTQ | 无需再训练 | 精度依赖校准 |
| 硬件部署 | TOM, Gemma3 NPU | 实际可用 | 硬件依赖 |

### 6.3 下一步方向建议

- 关注 **1-bit 量化** 在实际部署中的可行性
- **Token 级量化** 与推理系统的深度整合
- **MoE 模型** 的压缩与部署
- **长上下文** 场景下的效率优化

---

## 参考文献

1. pQuant: Towards Effective Low-Bit Language Models via Decoupled Linear Quantization-Aware Training (arXiv:2602.23351)
2. Scaling State-Space Models on Multiple GPUs with Tensor Parallelism (arXiv:2026)
3. TOM: A Ternary Read-only Memory Accelerator for LLM-powered Edge Intelligence (arXiv:2026)
4. MoBiQuant: Mixture-of-Bits Quantization for Token-Adaptive Elastic LLMs (arXiv:2026)
5. SPQ: An Ensemble Technique for Large Language Model Compression (arXiv:2026)
6. Quecto-V1: Empirical Analysis of 8-bit Quantized Small Language Models (arXiv:2026)
7. Compact LLM Deployment and World Model Assisted Offloading in Mobile Edge Computing (arXiv:2026)
8. Quantization-Robust LLM Unlearning via Low-Rank Adaptation (arXiv:2026)
9. QTALE: Quantization-Robust Token-Adaptive Layer Execution for LLMs (arXiv:2602.22207)
10. NanoQuant: Efficient Sub-1-Bit Quantization of Large Language Models (arXiv:2026)
11. Astro: Activation-guided Structured Regularization for Outlier-Robust LLM Quantization (arXiv:2026)
12. TernaryLM: Memory-Efficient Language Modeling via Native 1-Bit Quantization (arXiv:2026)
13. MatGPTQ: Accurate and Efficient Post-Training Matryoshka Quantization (arXiv:2026)
14. D²Quant: Accurate Low-bit Post-Training Weight Quantization for LLMs (arXiv:2026)
15. RaBiT: Residual-Aware Binarization Training for Accurate and Efficient LLMs (arXiv:2026)
16. Mapping Gemma3 onto an Edge Dataflow Architecture (arXiv:2026)
17. Regularized Calibration with Successive Rounding for Post-Training Quantization (arXiv:2026)
18. BPDQ: Bit-Plane Decomposition Quantization on a Variable Grid (arXiv:2026)
19. QVLA: Not All Channels Are Equal in Vision-Language-Action Model's Quantization (arXiv:2026)
20. UniComp: A Unified Evaluation of LLM Compression via Pruning, Quantization and Distillation (arXiv:2026)
21. GradPruner: Gradient-Guided Layer Pruning for LLMs (arXiv:2026)
22. Price of universality in vector quantization is at most 0.11 bit (arXiv:2026)
23. Differentially Private and Communication Efficient LLM Split Inference (arXiv:2026)
24. KBVQ-MoE: KLT-guided SVD with Bias-Corrected Vector Quantization for MoE (arXiv:2026)

---

*本报告由 Subagent 自动生成*
*调研时间: 2026-03-02 07:00 (GMT+8)*
