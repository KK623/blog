# 复数神经网络（CVNN）深度调研报告

## 综述类论文

### 1. Complex-valued Neural Networks -- Theory and Analysis
- **arXiv链接**: https://arxiv.org/abs/2312.06087
- **作者**: Rayyan Abdalla
- **机构**: 信息未提供
- **发表年份**: 2023
- **核心方法**: 该论文全面综述了CVNN的不同结构和分类，详细阐述了复数激活函数的理论基础、复数可微性的影响以及CVNN输出层的特殊激活函数。论文还讨论了CVNN的学习和优化算法，包括基于梯度和非梯度的方法。使用Wirtinger微积分解释了复数反向传播和复数链式法则。此外，还讨论了构建CVNN模型的特殊模块，如复数批归一化和复数随机初始化。
- **主要实验结果**: 该论文是理论综述性质，主要提供了CVNN的理论框架和未来方向的讨论，未提供具体实验数据集和性能指标。

### 2. A Survey of Complex-Valued Neural Networks
- **arXiv链接**: https://arxiv.org/abs/2101.12249
- **作者**: Joshua Bassey, Lijun Qian, Xianfang Li
- **机构**: Texas A&M University
- **发表年份**: 2021
- **核心方法**: 系统性地综述了CVNN的最新发展，详细回顾了各种CVNN在激活函数、学习和优化、输入输出表示方面的研究，以及在信号处理和计算机视觉任务中的应用。
- **主要实验结果**: 综述性质论文，涵盖了对现有CVNN方法的全面回顾，讨论了相关挑战和未来研究方向。

### 3. Theory and Implementation of Complex-Valued Neural Networks
- **arXiv链接**: https://arxiv.org/abs/2302.08286
- **作者**: Jose Agustin Barrachina, Chengfang Ren, Gilles Vieillard, Christele Morisseau, Jean-Philippe Ovarlez
- **机构**: 法国研究机构
- **发表年份**: 2023
- **核心方法**: 详细解释了CVNN的理论基础，包括Wirtinger微积分、复数反向传播以及基本模块（复数层、复数激活函数、复数权重初始化）的实现。论文还展示了使用cvnn工具包在Python中实现这些模块的方法，并通过Hilbert变换将实值数据转换到复数域进行验证。
- **主要实验结果**: 在实值数据上进行了仿真实验，通过Hilbert变换将数据映射到复数域，验证了CVNN对非复数数据的潜在应用价值。

### 4. On the Computational Complexities of Complex-valued Neural Networks
- **arXiv链接**: https://arxiv.org/abs/2310.13075
- **DOI**: 10.1109/LATINCOM59467.2023.10361866
- **作者**: Kayol Soares Mayer, Jonathan Aguiar Soares, Ariadne Arrais Cruz, Dalton Soares Arantes
- **机构**: 巴西研究机构
- **发表年份**: 2023
- **核心方法**: 从定量和渐近两个角度分析了CVNN的计算复杂度，以实值乘法次数描述数学运算。论文调查了文献中讨论的CVNN的计算复杂度，为在低功耗系统中选择算法提供了重要工具。
- **主要实验结果**: 提供了CVNN计算复杂度的定量分析方法，可用于估计浮点运算次数。

### 5. Spectral Complexity-scaled Generalization Bound of Complex-valued Neural Networks
- **arXiv链接**: https://arxiv.org/abs/2112.03467
- **作者**: Haowen Chen, Fengxiang He, Shiye Lei, Dacheng Tao
- **机构**: 悉尼大学
- **发表年份**: 2021
- **核心方法**: 首次证明了CVNN的泛化界，该界与谱复杂度相关，主要因素是权重矩阵的谱范数乘积。论文还提供了序列训练数据情况下CVNN的泛化界，通过Maurey稀疏化引理和Dudley熵积分进行理论推导。
- **主要实验结果**: 在MNIST、FashionMNIST、CIFAR-10、CIFAR-100、Tiny ImageNet和IMDB数据集上训练复数卷积神经网络，Spearman秩相关系数表明谱复杂度与泛化能力之间存在统计显著相关性。

---

## 复数卷积神经网络（Complex CNN）

### 6. Evaluation of Complex-Valued Neural Networks on Real-Valued Classification Tasks
- **arXiv链接**: https://arxiv.org/abs/1811.12351
- **作者**: Nils Mönning, Suresh Manandhar
- **机构**: University of York
- **发表年份**: 2018
- **核心方法**: 研究了在实值分类任务上CVNN与实值神经网络（RVNN）的性能比较。发现在相似容量下，复数模型与实值模型性能相当或略差。但当处理复平面上的噪声时，复数网络具有优势。
- **主要实验结果**: 在多个实值分类任务上进行比较，发现复数权重初始化仍是重要问题，复数网络的虚部权重会跟随实部。

### 7. Complex-valued Neural Networks with Non-parametric Activation Functions
- **arXiv链接**: https://arxiv.org/abs/1802.08026
- **作者**: Simone Scardapane, Steven Van Vaerenbergh, Amir Hussain, Aurelio Uncini
- **机构**: 意大利研究机构
- **发表年份**: 2018
- **核心方法**: 提出了第一个完全复数、非参数化的激活函数，基于核展开和固定字典，可在向量化硬件上高效实现。利用核激活函数（KAFs）和复数核设计的最新进展。
- **主要实验结果**: 在预测和信道均衡等常见用例上进行了验证，与实值神经网络和固定激活函数的CVNN相比显示出优势。

### 8. High-Capacity Complex Convolutional Neural Networks For I/Q Modulation Classification
- **arXiv链接**: https://arxiv.org/abs/2010.10717
- **作者**: Jakob Krzyston, Rajib Bhattacharjea, Andrew Stark
- **机构**: Georgia Tech Research Institute
- **发表年份**: 2020
- **核心方法**: 提出了高容量架构，包含残差和/或密集连接的复数卷积，用于I/Q调制分类。将样本视为复值信号，在深度学习框架中计算复值卷积。
- **主要实验结果**: 在RadioML 2016.10a数据集上达到92.4%的峰值分类准确率，与可比参数数量和速度的架构相比，复数卷积模型性能提升超过10%。

### 9. DeepcomplexMRI: Exploiting deep residual network for fast parallel MR imaging with complex convolution
- **arXiv链接**: https://arxiv.org/abs/1906.04359
- **作者**: Shanshan Wang, Huitao Cheng, Leslie Ying, Taohui Xiao, Ziwen Ke, Xin Liu, Hairong Zheng, Dong Liang
- **机构**: 中国科学院
- **发表年份**: 2019
- **核心方法**: 提出了DeepcomplexMRI，使用残差复数卷积神经网络加速并行MR成像。利用现有的多通道真实图像作为标记数据离线训练深度残差卷积神经网络。特别提出了复数卷积网络来考虑MR图像实部和虚部之间的相关性，并在网络层之间反复强制执行k空间数据一致性。
- **主要实验结果**: 在体内数据集上的评估表明，该方法能够恢复期望的多通道图像，与最先进的方法相比能够更准确地重建MR图像。

### 10. Analysis of Deep Complex-Valued Convolutional Neural Networks for MRI Reconstruction
- **arXiv链接**: https://arxiv.org/abs/2004.01738
- **作者**: Elizabeth K. Cole, Joseph Y. Cheng, John M. Pauly, Shreyas S. Vasanawala
- **机构**: Stanford University
- **发表年份**: 2020
- **核心方法**: 研究了端到端复数卷积神经网络用于MRI图像重建，替代双通道实值网络。测试了各种有前景的复数激活函数。
- **主要实验结果**: 发现具有复数卷积的复数CNN在各种网络架构和数据集上，与相同可训练参数数量的实数卷积相比，提供更优越的重建质量。

### 11. Complex Convolutional Neural Networks for Ultrafast Ultrasound Image Reconstruction from In-Phase/Quadrature Signal
- **arXiv链接**: https://arxiv.org/abs/2009.11536
- **作者**: Jingfeng Lu, Fabien Millioz, Damien Garcia, Sebastien Salles, Dong Ye, Denis Friboulet
- **机构**: 法国研究机构
- **发表年份**: 2020
- **核心方法**: 使用复数卷积神经网络从I/Q信号重建超声图像。提出了Complex-valued Inception for Diverging-wave Network (CID-Net)，在I/Q数据上操作。
- **主要实验结果**: 实验证据表明，仅使用三张I/Q图像，CID-Net就能产生可与31张RF图像相干复合获得的高质量图像相媲美的高质量图像。

### 12. Complex-valued Convolutional Neural Networks for Enhanced Radar Signal Denoising and Interference Mitigation
- **arXiv链接**: https://arxiv.org/abs/2105.00929
- **作者**: Alexander Fuchs, Johanna Rock, Mate Toth, Paul Meissner, Franz Pernkopf
- **机构**: Graz University of Technology
- **发表年份**: 2021
- **核心方法**: 提出了复数卷积神经网络（CVCNNs）来解决雷达传感器之间的相互干扰问题。将先前开发的方法扩展到复数域，以根据雷达数据的物理特性处理雷达数据。
- **主要实验结果**: 使用CVCNN提高了数据效率，加快了网络训练速度，并大幅改善了干扰去除过程中相位信息的保存。

---

## 复数循环神经网络（Complex RNN/LSTM）

### 13. Binaural Speech Enhancement Using Complex Convolutional Recurrent Networks
- **arXiv链接**: https://arxiv.org/abs/2507.20023
- **作者**: Vikas Tokala, Eric Grinstein, Mike Brookes, Simon Doclo, Jesper Jensen, Patrick A. Naylor
- **机构**: Imperial College London等
- **发表年份**: 2025
- **核心方法**: 提出了端到端双耳语音增强方法，使用具有编码器-解码器架构的复数循环卷积网络，在编码器和解码器之间放置复数LSTM循环块。引入了关注空间信息保留以及语音清晰度改善和噪声抑制的损失函数。
- **主要实验结果**: 在单目标说话人和各向同性噪声的声学场景中，与基线算法相比，该方法显著改善了估计的语音清晰度并减少了噪声，同时保留了双耳信号的空间信息。

### 14. Complex Unitary Recurrent Neural Networks using Scaled Cayley Transform
- **arXiv链接**: https://arxiv.org/abs/1811.04142
- **作者**: Kehelwala D. G. Maduranga, Kyle E. Helfrich, Qiang Ye
- **机构**: University of Kentucky
- **发表年份**: 2018
- **核心方法**: 开发了基于复数缩放Cayley变换的单元RNN架构。与实数正交情况不同，该变换使用由复数单位圆上的条目组成的对角缩放矩阵，可以使用梯度下降进行优化，不再需要调整超参数。
- **主要实验结果**: 在多个实验中，缩放Cayley单元循环神经网络（scuRNN）在固定缩放矩阵的情况下，达到了与scoRNN和其他单元RNN相当或更好的结果。

### 15. Gated Orthogonal Recurrent Units: On Learning to Forget
- **arXiv链接**: https://arxiv.org/abs/1706.02761
- **作者**: Li Jing, Caglar Gulcehre, John Peurifoy, Yichen Shen, Max Tegmark, Marin Soljačić, Yoshua Bengio
- **机构**: MIT, Google Brain
- **发表年份**: 2017
- **核心方法**: 提出了一种新的基于RNN的模型，结合了单元RNN的记忆能力和门控RNN有效遗忘冗余/不相关信息的能力。通过扩展单元RNN与门控机制实现。
- **主要实验结果**: 在多个长期依赖基准任务上优于LSTM、GRU和单元RNN，包括bAbI问答、TIMIT语音频谱预测、Penn TreeBank以及算法、括号、去噪和复制等合成任务。

### 16. Tunable Efficient Unitary Neural Networks (EUNN) and their application to RNNs
- **arXiv链接**: https://arxiv.org/abs/1612.05231
- **作者**: Li Jing, Yichen Shen, Tena Dubček, John Peurifoy, Scott Skirlo, Yann LeCun, Max Tegmark, Marin Soljačić
- **机构**: MIT
- **发表年份**: 2016
- **核心方法**: 提出了高效单元神经网络（EUNN）的新架构。单元空间的表示能力完全可调，从SU(N)的子空间到整个单元空间。每个参数的训练计算复杂度仅为O(1)。
- **主要实验结果**: 在标准复制任务、像素置换MNIST数字识别基准以及语音预测测试（TIMIT）上，EUNN在最终性能和/或挂钟训练速度方面显著优于其他最先进的单元RNN和LSTM架构。

### 17. Orthogonal Recurrent Neural Networks with Scaled Cayley Transform
- **arXiv链接**: https://arxiv.org/abs/1707.09520
- **作者**: Kyle Helfrich, Devin Willmott, Qiang Ye
- **机构**: University of Kentucky
- **发表年份**: 2017
- **核心方法**: 提出了一种更简单的新更新方案，使用Cayley变换和斜对称矩阵参数化来保持正交循环权重矩阵，而不使用复数值矩阵。通过由1和-1组成的对角缩放矩阵来克服表示负一特征值矩阵的限制。
- **主要实验结果**: 在多个实验中，缩放Cayley正交循环神经网络（scoRNN）以比其他单元RNN更少的可训练参数获得了优越的结果。

### 18. Eigenvalue Normalized Recurrent Neural Networks for Short Term Memory
- **arXiv链接**: https://arxiv.org/abs/1911.07964
- **作者**: Kyle Helfrich, Qiang Ye
- **机构**: University of Kentucky
- **发表年份**: 2019
- **核心方法**: 提出了一种架构，扩展了正交/单元RNN，其状态由特征值在单位圆盘内的循环矩阵生成。任何对该状态的输入都会随时间消散，并被新输入替代，模拟短期记忆。
- **主要实验结果**: 在多个实验中，特征值归一化RNN（ENRNN）表现出高度竞争力。

---

## 复数Transformer和注意力机制

### 19. Building Blocks for a Complex-Valued Transformer Architecture
- **arXiv链接**: https://arxiv.org/abs/2306.09827
- **DOI**: 10.1109/ICASSP49357.2023.10095349
- **作者**: Florian Eilers, Xiaoyi Jiang
- **机构**: University of Münster
- **发表年份**: 2023
- **核心方法**: 提出了将Transformer架构转移到复数域的构建块。提出了复数缩放点积注意力机制的多个版本以及复数层归一化。
- **主要实验结果**: 在MusicNet数据集上的分类和序列生成任务中测试，显示出改善的过拟合鲁棒性，同时与实值Transformer架构保持相当的性能。

### 20. Binaural Speech Enhancement Using Deep Complex Convolutional Transformer Networks
- **arXiv链接**: https://arxiv.org/abs/2403.05393
- **作者**: Vikas Tokala, Eric Grinstein, Mike Brookes, Simon Doclo, Jesper Jensen, Patrick A. Naylor
- **机构**: Imperial College London等
- **发表年份**: 2024
- **核心方法**: 提出了双耳语音增强方法，使用具有编码器-解码器架构的复数卷积神经网络和复数多头注意力Transformer。模型训练用于估计双耳 hearing device左右耳通道的时频域中的单独复数比率掩码。
- **主要实验结果**: 在单目标说话人和各向同性噪声的声学场景中，与几个基线算法相比，所提出的方法改善了估计的双耳语音清晰度并更好地保留了双耳线索。

### 21. Efficient Complex-Valued Vision Transformers for MRI Classification Directly from k-Space
- **arXiv链接**: https://arxiv.org/abs/2601.18392
- **作者**: Moritz Rempe, Lukas T. Rotkopf, Marco Schlimbach, Helmut Becker, Fabian Hörst, Johannes Haubold, Philipp Dammann, Kevin Kröninger, Jens Kleesiek
- **机构**: RWTH Aachen University
- **发表年份**: 2026
- **核心方法**: 提出了复数视觉Transformer（kViT），设计用于直接对k空间数据进行分类。引入了径向k空间分块策略，尊重频域数据的频谱能量分布。
- **主要实验结果**: 在fastMRI和内部数据集上的广泛实验表明，该方法实现了与最先进的图像域基线（ResNet、EfficientNet、ViT）相当的分类性能。kViT对高加速因子表现出卓越的鲁棒性，训练期间VRAM消耗减少高达68倍。

---

## 四元数神经网络（Quaternion Neural Networks）

### 22. 3D-Rotation-Equivariant Quaternion Neural Networks
- **arXiv链接**: https://arxiv.org/abs/1911.09040
- **作者**: Wen Shen, Binbin Zhang, Shikun Huang, Zhihua Wei, Quanshi Zhang
- **机构**: Shanghai Jiao Tong University
- **发表年份**: 2019
- **核心方法**: 提出了一套规则来修订用于3D点云处理的各种神经网络，使其成为旋转等变四元数神经网络（REQNNs）。发现当神经网络在某些条件下使用四元数特征时，网络特征自然具有旋转等变性。
- **主要实验结果**: 与原始神经网络相比，REQNN表现出更高的旋转鲁棒性。

### 23. Speech recognition with quaternion neural networks
- **arXiv链接**: https://arxiv.org/abs/1811.09678
- **作者**: Titouan Parcollet, Mirco Ravanelli, Mohamed Morchid, Georges Linarès, Renato De Mori
- **机构**: Avignon University
- **发表年份**: 2018
- **核心方法**: 研究了现代四元数模型（如卷积和循环四元数神经网络）在语音识别中的应用。四元数代数以Hamilton积替换标准点积，提供了一种简单而优雅的方式来建模元素之间的依赖关系。
- **主要实验结果**: 在TIMIT数据集上，QNN始终优于等效的实值模型，使用更少的自由参数，实现了更有效、紧凑和富有表现力的信息表示。

### 24. Quaternion Neural Networks for Multi-channel Distant Speech Recognition
- **arXiv链接**: https://arxiv.org/abs/2005.08566
- **作者**: Xinchi Qiu, Titouan Parcollet, Mirco Ravanelli, Nicholas Lane, Mohamed Morchid
- **机构**: University of Cambridge
- **发表年份**: 2020
- **核心方法**: 提出使用四元数神经网络捕获多通道音频录音中的内部关系，将多个信号作为整体四元数实体联合处理。四元数层与循环神经网络耦合，可以在时域中学习长期依赖关系。
- **主要实验结果**: 在多个通道远距离语音识别任务上，使用连接的多通道语音信号训练的四元数长短时记忆神经网络（QLSTM）优于等效的实值LSTM。

### 25. Compressing deep quaternion neural networks with targeted regularization
- **arXiv链接**: https://arxiv.org/abs/1907.11546
- **DOI**: 10.1049/trit.2020.0020
- **作者**: Riccardo Vecchi, Simone Scardapane, Danilo Comminiello, Aurelio Uncini
- **机构**: Sapienza University of Rome
- **发表年份**: 2019
- **核心方法**: 展示了如何通过设计有针对性的正则化策略来解决四元数神经网络（QVNNs）的正则化和/或稀疏化问题。研究了l1和结构化正则化到四元数域的两种扩展。
- **主要实验结果**: 实验评估表明，这些定制策略显著优于经典的（实值）正则化方法，产生了特别适合低功耗和实时应用的小型网络。

### 26. Improving Quaternion Neural Networks with Quaternionic Activation Functions
- **arXiv链接**: https://arxiv.org/abs/2406.16481
- **作者**: Johannes Pöppelbaum, Andreas Schwung
- **机构**: South Westphalia University of Applied Sciences
- **发表年份**: 2024
- **核心方法**: 提出了新颖的四元数激活函数，通过修改四元数幅度或相位，替代常用的分割激活函数。所有四元数分量都用于计算所有输出分量，将Hamilton积的好处带到激活函数。
- **主要实验结果**: 在CIFAR-10和SVHN数据集上的图像分类任务中，所提出的激活函数一致优于分割ReLU和分割Tanh，特别是影响相位的四元数激活函数在基本上整个输入范围内都敏感。

---

## 复数生成对抗网络（Complex GAN）

### 27. Co-VeGAN: Complex-Valued Generative Adversarial Network for Compressive Sensing MR Image Reconstruction
- **arXiv链接**: https://arxiv.org/abs/2002.10523
- **作者**: Bhavya Vasudeva, Puneesh Deora, Saumik Bhattacharya, Pyari Mohan Pradhan
- **机构**: Indian Institute of Technology
- **发表年份**: 2020
- **核心方法**: 提出了基于复数生成对抗网络（Co-VeGAN）的新框架。模型可以处理复值输入，能够执行CS-MR图像的高质量重建。考虑到相位是复值实体的关键组成部分，提出了一种对输入相位敏感的新复数激活函数。
- **主要实验结果**: 在不同数据集上使用各种采样掩码对所提出的方法进行了广泛评估，证明该模型在峰值信噪比和结构相似性指数方面显著优于现有的CS-MRI重建技术，使用的可训练参数显著少于基于实值的深度学习方法。

---

## 复数神经网络在医学成像（MRI）中的应用

### 28. Better than Real: Complex-valued Neural Nets for MRI Fingerprinting
- **arXiv链接**: https://arxiv.org/abs/1707.00070
- **作者**: Patrick Virtue, Stella X. Yu, Michael Lustig
- **机构**: UC Berkeley
- **发表年份**: 2017
- **核心方法**: 将深度学习用作高效的非线性逆映射方法进行MRI指纹识别。从MRI模拟器生成合成（组织、MRI）数据，并使用它们训练深度网络直接将MRI信号映射到组织参数。开发了具有新的心形激活函数的复数神经网络。
- **主要实验结果**: 结果表明，复数神经网络在复值MRI指纹识别方面比实值神经网络准确得多。

### 29. PhaseGen: A Diffusion-Based Approach for Complex-Valued MRI Data Generation
- **arXiv链接**: https://arxiv.org/abs/2504.07560
- **作者**: Moritz Rempe, Fabian Hörst, Helmut Becker, Marco Schlimbach, Lukas Rotkopf, Kevin Kröninger, Jens Kleesiek
- **机构**: RWTH Aachen University
- **发表年份**: 2025
- **核心方法**: 提出了PhaseGen，一种基于扩散的新颖复值模型，用于生成以临床常用的幅度图像为条件的合成MRI原始数据。这使得能够创建需要k空间信息的模型的人工复值原始数据预训练。
- **主要实验结果**: 在两个任务上评估了PhaseGen：直接在k空间进行颅骨剥离和MRI重建。结果表明，使用合成相位数据进行训练显著改善了真实世界数据的颅骨剥离泛化，分割准确率从41.1%提高到80.1%。

### 30. Complex-valued Federated Learning with Differential Privacy and MRI Applications
- **arXiv链接**: https://arxiv.org/abs/2110.03478
- **作者**: Anneliese Riess, Alexander Ziller, Stefan Kolek, Daniel Rueckert, Julia Schnabel, Georgios Kaissis
- **机构**: Technical University of Munich
- **发表年份**: 2021
- **核心方法**: 从理论上引入了复数高斯机制，在f-DP、(ε,δ)-DP和Rényi-DP方面表征其行为。将DP随机梯度下降的基本算法推广到复数神经网络，并提出了与DP兼容的新复数神经网络原语。
- **主要实验结果**: 通过在真实任务（k空间中的MRI脉冲序列分类）上使用DP训练联邦复数神经网络，展示了概念验证，产生了出色的效用和隐私。

---

## 复数神经网络在其他领域的应用

### 31. Room Transfer Function Reconstruction Using Complex-valued Neural Networks and Irregularly Distributed Microphones
- **arXiv链接**: https://arxiv.org/abs/2402.04866
- **作者**: Francesca Ronchini, Luca Comanducci, Mirco Pezzoli, Fabio Antonacci, Augusto Sarti
- **机构**: Politecnico di Milano
- **发表年份**: 2024
- **核心方法**: 首次使用复数神经网络来估计房间传递函数。分析了将复数优化应用于所考虑任务的好处，与最先进的基于核的信号处理方法进行了比较。
- **主要实验结果**: 结果表明，所提出的技术在相位精度和重建声场的整体质量方面表现出相关优势。

### 32. Complex-valued neural networks for voice anti-spoofing
- **arXiv链接**: https://arxiv.org/abs/2308.11800
- **作者**: Nicolas M. Müller, Philip Sperl, Konstantin Böttinger
- **机构**: Fraunhofer AISEC
- **发表年份**: 2023
- **核心方法**: 提出了一种新方法，通过使用复数神经网络处理输入音频的复值CQT频域表示来结合两种方法的优点。这种方法保留了相位信息并允许使用可解释的AI方法。
- **主要实验结果**: 在"In-the-Wild"反欺骗数据集上，该方法优于先前的方法，并通过可解释的AI实现了结果的解释。消融研究证实模型已经学会使用相位信息来检测语音欺骗。

### 33. DeepCSHAP: Utilizing Shapley Values to Explain Deep Complex-Valued Neural Networks
- **arXiv链接**: https://arxiv.org/abs/2403.08428
- **作者**: Florian Eilers, Xiaoyi Jiang
- **机构**: University of Münster
- **发表年份**: 2024
- **核心方法**: 将广泛使用的DeepSHAP算法适应到复数域，还提出了适用于复数神经网络的四种基于梯度的解释方法版本。
- **主要实验结果**: 评估了所有呈现算法的解释质量，并提供了所有方法作为开源库，可适应于大多数最新的复数神经网络架构。

### 34. Quantitative approximation results for complex-valued neural networks
- **arXiv链接**: https://arxiv.org/abs/2102.13092
- **作者**: A. Caragea, D. G. Lee, J. Maly, G. Pfander, F. Voigtlaender
- **机构**: Technical University of Munich等
- **发表年份**: 2021
- **核心方法**: 分析了复数网络的表达能力，提供了使用modReLU激活函数（σ(z) = ReLU(|z| - 1) · sgn(z)）的复数神经网络在C^d的紧子集上近似C^n函数的显式定量误差界。
- **主要实验结果**: 证明推导的近似率在具有适度增长的权重的modReLU网络类中是最优的（最多相差对数因子）。

---

## 总结

本次调研共收集了**34篇**高质量的复数神经网络（CVNN）相关论文，涵盖了以下主要方向：

1. **理论基础与综述** (5篇): CVNN的理论分析、综述、实现和计算复杂度研究
2. **复数CNN** (7篇): 复数卷积神经网络在MRI、雷达、调制识别等领域的应用
3. **复数RNN/LSTM** (6篇): 单元RNN、正交RNN、门控机制等循环神经网络变体
4. **复数Transformer** (3篇): 复数注意力机制和Vision Transformer
5. **四元数神经网络** (5篇): 3D旋转等变、语音识别、多通道处理等应用
6. **复数GAN** (1篇): 复数生成对抗网络用于MRI重建
7. **医学成像应用** (3篇): MRI指纹识别、数据生成、联邦学习
8. **其他应用** (4篇): 房间声学、语音反欺骗、可解释性、近似理论

这些论文展示了CVNN在信号处理、医学成像、无线通信、语音处理等领域的广泛应用前景，特别是在处理固有复值数据（如MRI、雷达、通信信号）时的显著优势。
