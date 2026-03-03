# LLM 量化/部署/低精度/蒸馏文献调研 (2026-03-03)

## 今日关注论文

### 1. QLoRA: Efficient Finetuning of LLMs
- **作者**: Tim Dettmers等
- **arXiv**: 2305.14314
- **主要贡献**: 结合4-bit量化和LoRA微调，单卡微调65B模型
- **为什么值得关注**: 开创性降低LLM微调显存需求

### 2. GPTQ: Accurate Post-Training Quantization for LLMs
- **作者**: Elias Frantar等
- **arXiv**: 2210.17323
- **主要贡献**: 基于近似二阶信息的GPTQ算法，单GPU量化175B模型
- **为什么值得关注**: LLM量化基础方法

### 3. AWQ: Activation-aware Weight Quantization
- **作者**: Lin等
- **arXiv**: 2306.00978
- **主要贡献**: 保护1%显著权重实现4-bit量化
- **为什么值得关注**: 比GPTQ更好困惑度，推理更快

### 4. SmoothQuant: Accurate INT8 Quantization
- **作者**: Xiao等
- **arXiv**: 2311.02683
- **主要贡献**: 迁移量化难度，解决激活值outlier问题
- **为什么值得关注**: 实现更均衡的INT8量化

### 5. GGUF: GPT-Generated Unified Format
- **主要贡献**: 支持多种精度(Q2-Q8)，llama.cpp广泛采用
- **为什么值得关注**: 消费级CPU也能运行大模型

---

*调研时间: 2026-03-03*
