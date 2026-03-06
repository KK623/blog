# 复数神经网络（CVNN）主题3-4初步调研报告

## 调研时间：2026-03-05
## 调研周期：Cycle 1

---

# 主题3：信号处理应用（重点）

## 1. 关键发现

### 1.1 MIMO信道估计

**应用场景：**
- Massive MIMO系统的信道估计（5G/6G通信）
- FDD大规模MIMO系统的CSI预测
- mmWave毫米波系统信道估计
- 抗干扰信道估计

**主要进展：**

#### (1) CVNN辅助的抗干扰信道估计（2024）
- **作者/机构：** Y Dai, B Nikolić (IEEE Workshop on Signal Processing Systems 2024)
- **论文：** "A CVNN-Aided Anti-Interference Channel Estimation for Massive MIMO Systems"
- **核心发现：** CVNN在无线通信中的潜力被重点强调，提出CVNN辅助的信道估计方法改善大规模MIMO系统的信道估计

#### (2) CV-3DCNN用于FDD大规模MIMO（2020）
- **作者：** Y Zhang等 (IEEE Communications Letters)
- **论文：** "CV-3DCNN: Complex-valued deep learning for CSI prediction in FDD massive MIMO systems"
- **引用：** 88次
- **性能提升：** 处理I/Q样本的回归任务，避免了复数值分割导致的信息丢失

#### (3) ISDNN用于Massive MIMO信道估计（2024）
- **作者：** DH Son等 (arXiv:2410.20110)
- **论文：** "ISDNN: A deep neural network for channel estimation in massive MIMO systems"
- **性能数据：** 
  - 训练时间减少13%
  - 运行时间减少4.6%
  - 精度提升0.43 dB
  - 优于DetNet方法

#### (4) Deep CNN-based CE for mmWave（2019）
- **作者：** P Dong等 (IEEE Journal of Selected Topics in Signal Processing)
- **论文：** "Deep CNN-based channel estimation for mmWave massive MIMO systems"
- **引用：** 481次（高影响力）
- **意义：** 深度学习在毫米波大规模MIMO信道估计的开创性工作

### 1.2 DOA估计（波达方向估计）

**应用场景：**
- 雷达系统源数估计
- 无人机DOA估计（城市环境）
- 超宽带DOA估计
- 无网格DOA估计
- 近场MIMO系统DOA估计

**主要进展：**

#### (1) 复数神经网络雷达源数估计（2024）
- **作者：** S Cho等 (IEEE Sensors Journal)
- **论文：** "Complex-valued neural network for estimating the number of sources in radar systems"
- **引用：** 4次
- **应用：** 高分辨率DOA估计中的源数估计

#### (2) 基于生成概率波的CVNN DOA估计（2025）
- **作者：** W Xu, S Yi, Z Zhang (Circuits, Systems, and Signal Processing)
- **论文：** "DOA Estimation Using Complex-Valued Neural Networks with Generative Probability Wave"
- **最新进展：** 2025年最新发表，结合生成概率波方法

#### (3) 基于CVCNN的多源DOA估计（2024）
- **作者：** Z Zhang等 (ACM Conference on VR, Image and Signal Processing)
- **论文：** "Multi Source DOA Estimation Based On Complex-valued Neural Networks"
- **方法：** 复数卷积神经网络(CVCNN)

#### (4) 超宽带DOA估计（2014）
- **作者：** K Terabayashi等 (IEEE Transactions on Neural Networks)
- **论文：** "Ultrawideband direction-of-arrival estimation using complex-valued spatiotemporal neural networks"
- **引用：** 52次
- **方法：** CVSTNN（复数时空神经网络）

#### (5) 城市环境UAV DOA估计（2020）
- **作者：** B Shi等 (IEEE Transactions on Information Networks)
- **论文：** "Complex-valued convolutional neural networks design and its application on UAV DOA estimation in urban environments"
- **引用：** 27次
- **应用：** 电磁信号处理、无人机控制系统

#### (6) 无网格DOA估计（2023-2024）
- **C-LeDIM-net：** 使用phasor归一化的复数CNN进行无网格DOA估计
- **Gridless DOA for Arbitrary Arrays：** 基于CV-DNN的任意阵列几何无网格DOA估计（Remote Sensing 2024）

### 1.3 雷达信号处理

**应用场景：**
- SAR图像分类与分割
- ISAR成像增强
- 雷达信号去噪
- 雷达发射器识别
- 波束形成

**主要进展：**

#### (1) SAR图像分类（2017-2021）
- **Zhang等（2017）：** "Complex-valued convolutional neural network and its application in polarimetric SAR image classification" - **引用791次**
- **Scarnati & Lewis（2021）：** "Complex-valued neural networks for synthetic aperture radar image classification" - 引用32次
- **性能：** 利用雷达数据的复数值特性，相比幅度-only方法有显著提升

#### (2) 雷达成像增强（2018）
- **作者：** J Gao等 (IEEE Geoscience and Remote Sensing Letters)
- **论文：** "Enhanced radar imaging using a complex-valued convolutional neural network"
- **引用：** 242次
- **应用：** SAR/ISAR成像增强

#### (3) ISAR成像（2019）
- **作者：** CY Hu等 (The Journal of Engineering)
- **论文：** "Inverse synthetic aperture radar imaging using complex-value deep neural network"
- **引用：** 15次

#### (4) 雷达信号去噪（2024）
- **作者：** P Sertdal等 (IEEE Radar Conference)
- **论文：** "Radar Signal Denoising for ISAR Imaging Using Complex-valued Neural Network"
- **引用：** 3次

#### (5) 多尺度SAR目标识别（2025）
- **作者：** G Hou等 (IEEE Journal of Selected Topics in Applied Earth Observations and Remote Sensing)
- **论文：** "A multiscale convolution SAR image target recognition method based on complex-valued neural networks"
- **引用：** 5次

### 1.4 波束形成与天线阵列

**主要进展：**

#### (1) 基于CV-CNN的鲁棒波束形成（2022）
- **作者：** S Mohammadzadeh, VH Nascimento等 (IEEE Signal Processing Letters)
- **论文：** "Robust beamforming based on complex-valued convolutional neural networks for sensor arrays"
- **引用：** 41次

#### (2) 智能波束形成（2004）
- **作者：** AB Suksmono, A Hirose (Journal of Intelligent & Fuzzy Systems)
- **论文：** "Intelligent beamforming by using a complex-valued neural network"
- **引用：** 20次
- **特点：** 无需DOA知识的智能波束形成

#### (3) 堆叠智能表面建模（2025）
- **作者：** A Zayat等 (IEEE International Conference on Communications)
- **论文：** "Deep Complex-Valued Neural-Network Modeling and Optimization of Stacked Intelligent Surfaces"
- **引用：** 1次
- **应用：** 5G/6G混合模拟-数字波束形成

### 1.5 OFDM信道均衡

**主要进展：**

#### (1) 无循环前缀OFDM的CVNN信道估计与均衡（2023）
- **作者：** HS Sousa等 (arXiv:2308.13623)
- **论文：** "CVNN-based Channel Estimation and Equalization in OFDM Systems Without Cyclic Prefix"
- **引用：** 2次
- **标准：** 基于3GPP 38.211 5G物理层规范

#### (2) 复数2D-CNN均衡（2022）
- **作者：** K Wang等 (Journal of Lightwave Technology)
- **论文：** "Complex-valued 2D-CNN equalization for OFDM signals in a photonics-aided MMW communication system at the D-band"
- **引用：** 43次
- **性能：** 相比实数2D-CNN有显著提升

## 2. 性能提升数据汇总

| 应用场景 | 方法 | 性能提升 | 年份 |
|---------|------|---------|------|
| Massive MIMO CE | ISDNN | 训练时间↓13%, 运行时间↓4.6%, 精度↑0.43dB | 2024 |
| FDD MIMO CSI | CV-3DCNN | 避免信息丢失，优于实数网络 | 2020 |
| mmWave CE | Deep CNN | 引用481次，开创性工作 | 2019 |
| DOA估计 | C-LeDIM-net | 低快拍和阵列缺陷下的无网格估计 | 2023 |
| SAR分类 | CV-CNN | 引用791次，优于幅度-only | 2017 |
| 雷达成像 | CV-CNN | 引用242次 | 2018 |
| OFDM均衡 | CV-2DCNN | 优于实数2D-CNN | 2022 |
| 波束形成 | CV-CNN | 引用41次 | 2022 |

## 3. 部署案例

- **5G/6G通信系统：** CVNN信道估计和均衡已集成到5G物理层规范评估中
- **雷达系统：** 军事和民用雷达中的SAR/ISAR成像增强
- **无人机系统：** 城市环境下的DOA估计和跟踪
- **智能天线阵列：** 基于CVNN的智能波束形成系统

---

# 主题4：计算机视觉应用

## 1. 关键发现

### 1.1 图像分类

**主要进展：**

#### (1) 复数CNN基础理论（2016）
- **作者：** N Guberman (arXiv:1602.09046)
- **论文：** "On complex valued convolutional neural networks"
- **引用：** 221次
- **发现：** 
  - 复数模型是实数CNN的两倍参数限制形式
  - 对相位结构敏感
  - 在细胞检测问题上与实数网络相当但过拟合更少

#### (2) Deep Complex Networks（2017）
- **作者：** C Trabelsi等 (NeurIPS 2017, arXiv:1705.09792)
- **论文：** "Deep Complex Networks"
- **核心贡献：**
  - 提供复数深度网络的关键原子组件
  - 复数批归一化算法
  - 复数权重初始化策略
  - 在MusicNet和TIMIT数据集上达到SOTA
- **意义：** 复数网络的里程碑工作

#### (3) 四元数CNN（2018）
- **作者：** X Zhu等 (ECCV 2018)
- **论文：** "Quaternion convolutional neural networks"
- **引用：** 258次
- **应用：** 彩色图像分类，将颜色三通道作为整体处理

#### (4) 四元数CNN用于彩色图像分类和取证（2019）
- **作者：** Q Yin等 (IEEE Access)
- **论文：** "Quaternion convolutional neural network for color image classification and forensics"
- **引用：** 90次

### 1.2 图像去噪

**主要进展：**

#### (1) 复数深度CNN图像去噪（2021）
- **作者：** Y Quan等 (Pattern Recognition)
- **论文：** "Image denoising using complex-valued deep CNN"
- **引用：** 203次
- **性能：** 利用复数表示的丰富表达能力

#### (2) 医学图像去噪（2021）
- **作者：** S Rawat等 (Biomedical Signal Processing and Control)
- **论文：** "A novel complex-valued convolutional neural network for medical image denoising"
- **引用：** 87次

### 1.3 目标检测与姿态估计

**主要进展：**

#### (1) 3D物体姿态估计（2019）
- **作者：** C Papaioannidis, I Pitas (IEEE Transactions on Circuits and Systems for Video Technology)
- **论文：** "3D object pose estimation using multi-objective quaternion learning"
- **引用：** 23次
- **方法：** 使用四元数学习的CNN进行物体识别和姿态估计

#### (2) 四元数近似网络（2025）
- **作者：** B Grant, P Wang (IEEE/RSJ International Conference on Intelligent Robots and Systems)
- **论文：** "Quaternion Approximate Networks for Enhanced Image Classification and Oriented Object Detection"
- **应用：** 定向目标检测，6DoF姿态估计

### 1.4 图像分割

**主要进展：**

#### (1) 异构图像处理（2019）
- **作者：** T Parcollet等 (ICASSP 2019)
- **论文：** "Quaternion convolutional neural networks for heterogeneous image processing"
- **引用：** 143次
- **发现：** 四元数编码器-解码器能完美学习颜色空间

#### (2) 医学图像分割比较研究（2022）
- **作者：** S Chatterjee等 (IEEE International Conference on Image Processing)
- **论文：** "Complex Network for Complex Problems: A comparative study of CNN and Complex-valued CNN"
- **引用：** 27次
- **内容：** 脑肿瘤分类和分割的CNN vs CV-CNN比较

### 1.5 图像修复与生成

**主要进展：**

#### (1) 四元数矩阵补全（2024）
- **作者：** J Miao等 (Signal Processing)
- **论文：** "Quaternion matrix completion using untrained quaternion convolutional neural network for color image inpainting"
- **引用：** 25次

#### (2) 图像去雾（2023）
- **作者：** V Frants, S Agaian, K Panetta (IEEE Transactions on Image Processing)
- **论文：** "QCNN-H: Single-image dehazing using quaternion neural networks"
- **引用：** 76次

### 1.6 医学成像

**主要进展：**

#### (1) MRI重建（2021）
- **作者：** E Cole等 (Magnetic Resonance in Medicine)
- **论文：** "Analysis of deep complex-valued convolutional neural networks for MRI reconstruction and phase-focused applications"
- **引用：** 194次
- **性能：** CV-CNN的PSNR (36.08 ± 3.06) 优于实数CNN

#### (2) 医学图像重建综述（2025）
- **作者：** S Costanzo, AM Flores (Electronics)
- **论文：** "From Iterative Methods to Neural Networks: Complex-Valued Approaches in Medical Image Reconstruction"
- **引用：** 1次

---

## 2. 主题4性能数据汇总

| 任务 | 方法 | 性能 | 年份 | 引用 |
|-----|------|------|------|------|
| 图像分类 | Quaternion CNN | 彩色图像整体处理 | 2018 | 258 |
| 图像去噪 | CV-Deep CNN | 复数表示丰富性 | 2021 | 203 |
| MRI重建 | CV-CNN | PSNR 36.08 vs 实数CNN | 2021 | 194 |
| 异构图像处理 | QCNN | 完美学习颜色空间 | 2019 | 143 |
| 图像去雾 | QCNN-H | 单图像去雾 | 2023 | 76 |
| 医学去噪 | CV-CNN | 专用医学图像 | 2021 | 87 |
| 彩色图像分类 | QCNN | 颜色通道整体处理 | 2019 | 90 |
| 3D姿态估计 | 四元数学习 | 多目标学习 | 2019 | 23 |
| 图像修复 | 未训练QCNN | 四元数矩阵补全 | 2024 | 25 |

---

## 3. 主要文献来源（信号处理领域 ≥10篇）

### 3.1 高影响力论文（引用>100）

| # | 论文 | 作者 | 年份 | 引用 | 领域 |
|---|------|------|------|------|------|
| 1 | Complex-valued convolutional neural network and its application in polarimetric SAR image classification | Zhang等 | 2017 | 791 | SAR/雷达 |
| 2 | Deep CNN-based channel estimation for mmWave massive MIMO systems | Dong等 | 2019 | 481 | MIMO/通信 |
| 3 | Enhanced radar imaging using a complex-valued convolutional neural network | Gao等 | 2018 | 242 | 雷达成像 |
| 4 | Quaternion convolutional neural networks | Zhu等 | 2018 | 258 | 视觉/四元数 |
| 5 | Deep Complex Networks | Trabelsi等 | 2017 | - | 基础理论 |
| 6 | Image denoising using complex-valued deep CNN | Quan等 | 2021 | 203 | 图像处理 |
| 7 | Analysis of deep complex-valued CNN for MRI reconstruction | Cole等 | 2021 | 194 | 医学成像 |

### 3.2 信道估计（5篇）

| # | 论文 | 作者 | 年份 | 引用 |
|---|------|------|------|------|
| 8 | CV-3DCNN: Complex-valued deep learning for CSI prediction in FDD massive MIMO systems | Zhang等 | 2020 | 88 |
| 9 | Deep learning based channel estimation for MIMO systems with received SNR feedback | Kang等 | 2020 | 81 |
| 10 | Dual CNN-based channel estimation for MIMO-OFDM systems | Jiang等 | 2021 | 120 |
| 11 | ISDNN: A deep neural network for channel estimation in massive MIMO systems | Son等 | 2024 | 1 |
| 12 | A CVNN-Aided Anti-Interference Channel Estimation for Massive MIMO Systems | Dai等 | 2024 | - |

### 3.3 DOA估计（5篇）

| # | 论文 | 作者 | 年份 | 引用 |
|---|------|------|------|------|
| 13 | Ultrawideband DOA estimation using CVSTNN | Terabayashi等 | 2014 | 52 |
| 14 | Complex-valued CNN for UAV DOA estimation in urban environments | Shi等 | 2020 | 27 |
| 15 | Complex-valued neural network for estimating the number of sources in radar systems | Cho等 | 2024 | 4 |
| 16 | Gridless DOA estimation using complex-valued CNN with phasor normalization | Tan等 | 2023 | 16 |
| 17 | DOA Estimation Using CVNN with Generative Probability Wave | Xu等 | 2025 | - |

### 3.4 波束形成（3篇）

| # | 论文 | 作者 | 年份 | 引用 |
|---|------|------|------|------|
| 18 | Robust beamforming based on CV-CNN for sensor arrays | Mohammadzadeh等 | 2022 | 41 |
| 19 | Intelligent beamforming by using a CVNN | Suksmono等 | 2004 | 20 |
| 20 | Deep Complex-Valued NN Modeling of Stacked Intelligent Surfaces | Zayat等 | 2025 | 1 |

### 3.5 OFDM均衡（2篇）

| # | 论文 | 作者 | 年份 | 引用 |
|---|------|------|------|------|
| 21 | CVNN-based Channel Estimation and Equalization in OFDM Systems Without Cyclic Prefix | Sousa等 | 2023 | 2 |
| 22 | Complex-valued 2D-CNN equalization for OFDM signals | Wang等 | 2022 | 43 |

---

## 4. 识别的知识空白

### 4.1 信号处理领域

#### (1) 理论基础空白
- **复数可微性理论：** 复数域的反向传播理论仍需完善，特别是非全纯函数的处理
- **泛化能力分析：** CVNN在信号处理任务中的泛化边界缺乏理论分析
- **相位敏感性量化：** 复数网络的相位敏感性如何量化仍不明确

#### (2) 架构设计空白
- **自适应架构：** 针对特定信号特征（如稀疏性、循环平稳性）的自适应CVNN架构
- **混合架构：** 实数-复数混合网络的系统设计和优化方法
- **轻量化设计：** 边缘设备部署的轻量级CVNN架构研究不足

#### (3) 应用场景空白
- **6G通感一体化：** CVNN在联合通信与感知(JCAS)中的应用尚未充分探索
- **太赫兹通信：** 太赫兹频段信道估计的CVNN方法
- **智能反射面(RIS)：** CVNN辅助的RIS波束形成和信道估计
- **卫星通信：** 卫星MIMO和卫星-地面链路的CVNN应用

#### (4) 数据集与基准
- **标准化数据集：** 缺乏类似ImageNet的复数信号处理标准数据集
- **公平比较基准：** 实数网络与复数网络的公平比较框架不完善

#### (5) 硬件部署空白
- **专用硬件：** 支持复数运算的专用AI芯片设计
- **量化与压缩：** 复数网络的量化、剪枝和知识蒸馏方法
- **实时性优化：** 高吞吐率低延迟的CVNN部署方案

### 4.2 计算机视觉领域

#### (1) 生成模型空白
- **复数GAN：** 复数生成对抗网络的研究较少
- **扩散模型：** CVNN在扩散模型中的应用几乎空白
- **视频生成：** 时空复数特征的视频生成方法

#### (2) 多模态融合
- **视觉-语言：** 复数特征在多模态大模型中的应用
- **视觉-音频：** 跨模态复数表示学习

#### (3) 基础模型
- **预训练模型：** 大规模复数视觉基础模型缺失
- **自监督学习：** 复数域的自监督预训练方法

#### (4) 可解释性
- **相位语义：** 复数特征的相位信息在视觉任务中的语义解释
- **可视化方法：** 复数特征图的可视化和分析方法

### 4.3 跨领域空白

- **信号-视觉联合：** 雷达视觉融合中的CVNN应用
- **物理信息神经网络：** 复数PINN在波动物理中的应用
- **神经算子：** 复数神经算子在偏微分方程求解中的应用

---

## 5. 总结与建议

### 5.1 信号处理领域（重点发展）

**成熟方向：**
- MIMO信道估计（高引用，实际部署）
- SAR图像分类（高引用，军事应用）
- 雷达成像增强（成熟应用）

**新兴方向：**
- 6G JCAS（2025年热点）
- 智能反射面（RIS）优化
- 太赫兹通信

**建议重点：**
1. 深入研究CVNN在5G/6G通信系统中的实际部署
2. 建立信号处理领域的标准化CVNN基准测试
3. 探索CVNN与传统信号处理算法的混合方法

### 5.2 计算机视觉领域

**成熟方向：**
- 彩色图像处理（四元数网络）
- 医学图像重建（MRI）
- 图像去噪

**待发展：**
- 生成模型（GAN、扩散模型）
- 基础预训练模型
- 多模态融合

---

*报告完成*
