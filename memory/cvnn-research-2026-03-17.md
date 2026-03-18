# CVNN Research Daily - 2026-03-17

## 搜索时间范围
本报告搜索了arXiv过去30天内发表的论文（2026-02-17 至 2026-03-17），主要关注复数神经网络(CVNN)、Complex Transformer及其在信号处理中的应用。

## 论文列表

| 序号 | 论文标题 | arXiv ID | 方向 |
|------|----------|----------|------|
| 1 | Toward Complex-Valued Neural Networks for Waveform Generation | 2603.11589 | CVNN语音合成 |
| 2 | Complex-Valued Unitary Representations as Classification Heads | 2602.15283 | CVNN分类/不确定性量化 |
| 3 | Near-Field Multiuser Beam Training for XL-MIMO | 2603.11959 | Complex Transformer通信 |
| 4 | Indirect and Direct Multiuser Hybrid Beamforming | 2603.11918 | CVNN无线通信 |
| 5 | Perturbing the Phase: Analyzing Adversarial Robustness of CVNNs | 2602.06577 | CVNN鲁棒性分析 |

---

## 论文详解

### 1. Toward Complex-Valued Neural Networks for Waveform Generation

**论文基本信息**
- **arXiv链接**: https://arxiv.org/abs/2603.11589
- **完整标题**: Toward Complex-Valued Neural Networks for Waveform Generation
- **作者**: Hyung-Seok Oh, Deok-Hyeon Cho, Seung-Bin Kim, Seong-Whan Lee
- **机构**: 韩国科学技术院（KAIST）
- **发表时间**: 2026-03-12
- **会议**: ICLR 2026 (已接收)

**背景**
神经声码器在近年来推动了波形生成的进步，产生了自然且富有表现力的音频。其中，基于iSTFT的声码器通过预测复值频谱图并通过iSTFT合成波形，避免了学习上采样阶段带来的计算成本增加。然而，当前的方法使用实值网络独立处理实部和虚部，这种分离限制了它们捕捉复数频谱图内在结构的能力。

**动机**
复值频谱图具有内在的幅相结构，而实值网络将其视为两个独立的通道无法充分利用这一结构。如何设计原生支持复数运算的神经网络架构，以更好地建模复值频谱图的特性，是本研究的核心问题。

**技术点**
- **原生复数运算**: ComVo的生成器和判别器都使用原生复数算术，而非分离的实部和虚部处理
- **相位量化**: 引入相位量化技术，将相位值离散化并以结构化方式引导相位变换
- **对抗训练框架**: 在复数表示空间中提供结构化反馈的对抗训练框架
- **块矩阵计算方案**: 提出块矩阵计算方案，通过减少冗余操作提高训练效率

**收益点**
- **合成质量提升**: 相比可比较的实值基线，ComVo实现了更高的合成质量
- **训练效率**: 块矩阵方案减少了25%的训练时间
- **参数效率**: 复数表示允许更紧凑的模型参数化
- **结构化相位建模**: 相位量化提供了更稳定的相位学习和更好的音频质量

**总结**
ComVo是首个在神经声码器中全面采用复数运算的工作，通过原生复数运算、相位量化和块矩阵计算，在语音合成质量上超越了实值基线，同时提高了训练效率。这项工作为复数神经网络在语音和音频处理领域的应用开辟了新方向。

---

### 2. Complex-Valued Unitary Representations as Classification Heads for Improved Uncertainty Quantification in Deep Neural Networks

**论文基本信息**
- **arXiv链接**: https://arxiv.org/abs/2602.15283
- **完整标题**: Complex-Valued Unitary Representations as Classification Heads for Improved Uncertainty Quantification in Deep Neural Networks
- **作者**: Akbar Anbar Jafari, Cagri Ozcinar, Gholamreza Anbarjafari
- **机构**: 爱沙尼亚塔尔图大学、东地中海大学等
- **发表时间**: 2026-02-17

**背景**
现代深度神经网络虽然预测准确率高，但校准性差：它们的置信度分数不能可靠地反映真实的正确概率。不确定性量化对于安全关键应用至关重要，但现有方法往往在精度和校准之间难以平衡。

**动机**
量子力学中的复值希尔伯特空间和酉变换提供了保范数的演化，这一特性可能有助于改善神经网络的校准。本研究探索将量子启发的复值酉表示应用于分类头，以提高模型的不确定性量化能力。

**技术点**
- **复值希尔伯特空间投影**: 将主干网络特征投影到复值希尔伯特空间
- **Cayley参数化酉变换**: 使用Cayley映射参数化学习的酉变换，保持特征范数
- **混合实验设计**: 训练共享主干并比较可互换的轻量级头部，隔离复值表示的影响
- **酉幅度头**: 复值特征在Cayley酉演化下通过幅度读出和softmax进行分类
- **Born规则测量层**: 探索量子力学启发的测量方法

**收益点**
- **显著校准改善**: 在CIFAR-10上，酉幅度头的ECE为0.0146，比标准softmax头(0.0355)提升2.4倍，比温度缩放(0.0510)提升3.5倍
- **更好的人类不确定性对齐**: 在CIFAR-10H基准上，波函数头实现最低的KL散度(0.336)，表明复值表示更好地捕捉人类感知歧义的结构
- **理论分析**: 提供了连接保范数酉动力学到特征空间几何校准的理论分析
- **可解释性**: 酉变换提供了几何上可解释的特征演化

**总结**
这项工作创新性地将量子启发的复值酉表示应用于神经网络分类头，显著改善了模型的校准和不确定性量化能力。研究还发现直接使用Born规则测量反而会降低校准，这一反直觉的发现为复值神经网络的设计提供了重要指导。

---

### 3. Near-Field Multiuser Beam Training for XL-MIMO: An End-to-End Interference-Aware Approach with Pilot Limitations

**论文基本信息**
- **arXiv链接**: https://arxiv.org/abs/2603.11959
- **完整标题**: Near-Field Multiuser Beam Training for XL-MIMO: An End-to-End Interference-Aware Approach with Pilot Limitations
- **作者**: Xinyang Li, Songjie Yang, Xiang Ling, Jianhui Song, Yibo Wang, Hua Chen
- **发表时间**: 2026-03-12

**背景**
超大规模MIMO(XL-MIMO)中的近场传播通过引入额外的距离维度扩大了波束训练搜索空间，使得传统的基于码本的波束扫描在导频资源受限时变得不可行，特别是在多用户子连接混合架构中。

**动机**
如何在有限的导频资源下高效地进行多用户波束训练？本研究提出一种深度学习的干扰感知多用户波束训练框架，直接从少量上行感知测量中预测模拟波束索引。

**技术点**
- **子阵级近似**: 利用子阵级近似，采用远场码本表示每个子阵响应，失配可忽略不计
- **变体MSE替代损失**: 通过KKT条件的闭式MMSE解消除数字预编码器，隐式考虑多用户干扰
- **复值感知前端**: 网络集成复值感知前端处理上行测量
- **复值编码器**: 共享复值编码器提取用户特征
- **Transformer多用户预测器**: 基于Transformer的多用户预测器
- **Gumbel-Softmax波束选择头**: 可扩展的Gumbel-Softmax波束选择头

**收益点**
- **近最优性能**: DL-IABT实现接近最优的和速率性能
- **高有效吞吐量**: 在导频开销限制下提供显著更高的有效吞吐量
- **端到端学习**: 完整的端到端训练，无需分阶段优化
- **干扰感知**: 通过损失函数设计隐式考虑多用户干扰

**总结**
这项工作为XL-MIMO系统的近场多用户波束训练提供了一个高效的深度学习解决方案。通过复值感知前端和端到端学习，在导频受限条件下实现了接近最优的性能，为下一代无线通信系统的波束管理提供了新思路。

---

### 4. Indirect and Direct Multiuser Hybrid Beamforming for Far-Field and Near-Field Communications: A Deep Learning Approach

**论文基本信息**
- **arXiv链接**: https://arxiv.org/abs/2603.11918
- **完整标题**: Indirect and Direct Multiuser Hybrid Beamforming for Far-Field and Near-Field Communications: A Deep Learning Approach
- **作者**: Xinyang Li, Songjie Yang, Boyu Ning, Zongmiao He, Xiang Ling, Chau Yuen
- **发表时间**: 2026-03-12

**背景**
XL-MIMO系统的混合波束赋形在近场中面临挑战，因为信道同时依赖于角度和距离，且多用户干扰(MUI)很强。现有的深度学习方法要么采用解耦设计而不显式考虑MUI，要么采用端到端联合模拟-数字优化但在非凸约束下不稳定。

**动机**
如何设计一个既能处理远场又能处理近场通信的统一深度学习框架，同时保持训练稳定性和高性能？本研究提出基于变体MMSE准则的复值端到端框架。

**技术点**
- **变体MMSE准则**: 通过KKT条件以闭式形式消除数字预编码器，使模拟学习具有稳定目标
- **分组复数卷积感知前端**: 用于上行测量的分组复数卷积感知前端
- **共享复数MLP**: 用于每用户特征提取的共享复数多层感知器
- **合并恒模头**: 输出模拟预编码器的合并恒模头
- **间接模式**: 从估计的信道状态信息(CSI)设计混合波束赋形器
- **直接模式**: 在显式CSI不可用时，从短导频学习感知算子和模拟映射

**收益点**
- **复杂度降低**: 间接模式接近迭代变体MMSE优化性能，复杂度降低与天线数量成正比
- **频谱效率提升**: 在相同导频预算下，直接模式比稀疏恢复流程和近期深度学习基线提高频谱效率
- **双模式灵活**: 支持CSI可用和不可用两种场景
- **稳定训练**: 变体MMSE准则确保训练稳定性

**总结**
这项工作提出了一个统一的复值深度学习框架，同时支持远场和近场多用户混合波束赋形。通过变体MMSE准则和复数运算，实现了稳定的端到端训练和优异的性能，为XL-MIMO系统的实际部署提供了实用解决方案。

---

### 5. Perturbing the Phase: Analyzing Adversarial Robustness of Complex-Valued Neural Networks

**论文基本信息**
- **arXiv链接**: https://arxiv.org/abs/2602.06577
- **完整标题**: Perturbing the Phase: Analyzing Adversarial Robustness of Complex-Valued Neural Networks
- **作者**: Florian Eilers, Christof Duhme, Xiaoyi Jiang
- **发表时间**: 2026-02-06

**背景**
复数神经网络(CVNN)在各类应用中日益流行。为了在实践中安全使用CVNN，分析其对异常值的鲁棒性至关重要。对抗攻击是理解深度神经网络行为的一种著名技术，可视为最坏情况下的最小扰动。

**动机**
CVNN与实值神经网络(RVNN)在对抗鲁棒性方面有何差异？相位信息对CVNN的脆弱性有何影响？本研究设计针对复值输入相位信息的专门攻击，并评估CVNN的鲁棒性。

**技术点**
- **相位攻击(Phase Attacks)**: 专门针对复值输入相位信息的攻击方法
- **复数对抗攻击**: 推导常用对抗攻击的复数版本
- **对比分析**: 在相同设置下比较CVNN和RVNN的鲁棒性
- **幅相分离分析**: 分别评估对相位和幅度扰动的敏感性

**收益点**
- **CVNN更鲁棒**: 在某些场景下CVNN比RVNN更鲁棒
- **相位脆弱性**: CVNN和RVNN都对相位变化非常敏感
- **相位攻击更有效**: 相位攻击比同等强度的常规攻击（可同时攻击相位和幅度）更能降低模型性能
- **安全指导**: 为CVNN在安全关键应用中的部署提供了鲁棒性评估框架

**总结**
这项工作首次系统性地分析了CVNN的对抗鲁棒性，发现尽管CVNN在某些场景下比RVNN更鲁棒，但两者都对相位扰动高度敏感。相位攻击的有效性提醒我们在设计CVNN时需要特别关注相位信息的保护。

---

## 研究趋势洞察

1. **CVNN在语音合成领域的突破**: ComVo代表了CVNN在神经声码器中的首次全面应用，通过原生复数运算实现了超越实值基线的性能，为语音和音频处理开辟了新方向。

2. **复数表示改善不确定性量化**: 复值酉表示在分类头中的应用显著改善了神经网络的校准，这一发现可能对安全关键应用产生重要影响。

3. **Complex Transformer在通信领域的广泛应用**: XL-MIMO波束赋形和波束训练中越来越多地采用复值感知前端和Complex Transformer架构，充分利用了无线信道的复数特性。

4. **CVNN鲁棒性研究起步**: 对CVNN对抗鲁棒性的系统性研究刚刚起步，相位信息的脆弱性是一个值得关注的安全问题。

5. **量子启发方法的探索**: 将量子力学中的概念（如酉变换、Born规则）应用于CVNN，为神经网络设计提供了新的理论视角。

## 关键指标汇总

| 论文 | 核心技术 | 主要收益 |
|------|----------|----------|
| ComVo | 原生复数运算+相位量化 | 更高合成质量，25%训练时间减少 |
| Unitary Classification Head | Cayley参数化酉变换 | 2.4x校准改善，更好的人类不确定性对齐 |
| DL-IABT | Complex Transformer+Gumbel-Softmax | 近最优和速率，高有效吞吐量 |
| Hybrid Beamforming | 变体MMSE+复数MLP | 复杂度与天线数成正比降低 |
| Phase Attacks | 相位特异性对抗攻击 | 发现CVNN相位脆弱性 |

---

*报告生成时间：2026-03-17 09:25 GMT+8*
