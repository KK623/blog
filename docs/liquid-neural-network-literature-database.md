# Liquid Neural Network 文献数据库
# 创建时间: 2026-03-06
# 调研阶段: 第二阶段 - 系统性搜索完成

## 📊 文献统计

| 类别 | 数量 | 说明 |
|------|------|------|
| 核心开创性论文 | 3篇 | LTC奠基、闭式解、综述 |
| 应用论文 - 自动驾驶 | 8+篇 | 无人机导航、车辆控制 |
| 应用论文 - 机器人 | 10+篇 | 机械臂控制、逆运动学 |
| 应用论文 - 时序预测 | 6+篇 | 股价预测、时间序列 |
| 对比研究 | 3+篇 | vs RNN/LSTM/Transformer |
| 开源实现/教程 | 10+篇 | GitHub项目、教程 |
| **总计** | **40+篇** | 覆盖理论、应用、代码 |

---

## 🔬 核心开创性论文 (必读)

### 1. Liquid Time-constant Networks (LTC)
- **标题**: Liquid Time-constant Networks
- **作者**: Ramin Hasani, Mathias Lechner, Alexander Amini, Daniela Rus
- **发表**: AAAI 2021
- **arXiv**: https://arxiv.org/abs/2006.04439
- **引用**: 高引用
- **核心贡献**: 提出LTC网络，用ODE描述连续时间动态
- **分类**: 🧠理论基础 / 🏗️架构设计

### 2. Closed-form Continuous-time Neural Models
- **标题**: Closed-form Continuous-time Neural Networks
- **作者**: Ramin Hasani et al.
- **发表**: Nature Machine Intelligence 2022
- **arXiv**: https://arxiv.org/abs/2106.13898
- **核心贡献**: 闭式解突破，大幅提升计算效率
- **分类**: 🧠理论基础 / ⚡优化算法

### 3. Neural Differential Equations Survey
- **标题**: Differential Equations for Continuous-Time Deep Learning
- **作者**: (多位作者)
- **发表**: arXiv 2024
- **链接**: https://arxiv.org/abs/2401.03965
- **核心贡献**: 综述连续时间深度学习方法
- **分类**: 📚综述 / 🧠理论基础

---

## 🚗 应用 - 自动驾驶与无人机

### 导航与路径规划
1. **Robust flight navigation out of distribution with liquid neural networks**
   - MIT CSAIL
   - 无人机在未知环境中鲁棒导航
   - 链接: https://cap.csail.mit.edu/sites/default/files/research-pdfs/Robust%20flight%20navigation...

2. **Liquid Dino: A Multi-Task Neural Network towards Autonomous Driving**
   - OpenReview
   - 驾驶员行为分类和上下文感知
   - 链接: https://openreview.net/forum?id=0qfIhtel8N

3. **MIT uses liquid neural networks to teach drones navigation skills**
   - The Robot Report
   - 视觉引导的飞行目标追踪
   - 链接: https://www.therobotreport.com/mit-uses-liquid-neural-networks-to-teach-drones...

4. **Autonomous Vehicle Control with Liquid Time Constant Networks**
   - ResearchGate
   - 自动驾驶车辆控制综合评估
   - 链接: https://www.researchgate.net/publication/393897318...

---

## 🤖 应用 - 机器人控制

### 机械臂与逆运动学
1. **Invertible liquid neural network-based learning of inverse kinematics and dynamics for robotic manipulators**
   - Nature Scientific Reports 2025
   - 可逆LNN学习逆运动学和动力学
   - 链接: https://www.nature.com/articles/s41598-025-22825-2

2. **Tracking control of humanoid manipulator using sliding mode**
   - Nature Scientific Reports
   - 仿人机械臂的滑模跟踪控制

3. **Inverse Kinematics for Robotic Manipulators via Deep Neural Networks**
   - Applied Sciences (MDPI)
   - DNN解决逆运动学问题

### 无人机控制
4. **Robust flight navigation out of distribution**
   - MIT CSAIL
   - 分布外鲁棒飞行导航

---

## 📈 应用 - 时间序列预测

### 股价预测与金融
1. **Liquid Neural Networks in Stock Market Prediction**
   - GitHub: HusseinJammal/Liquid-Neural-Networks-in-Stock-Market-Prediction
   - Tesla和Apple股价预测
   - 链接: https://github.com/HusseinJammal/Liquid-Neural-Networks-in-Stock-Market-Prediction

2. **Combining the Power of Liquid Neural Networks: A Hybrid Approach with LSTM**
   - AI Mind
   - LNN+LSTM混合预测

3. **Liquid Neural Networks: Classification and Time Series Forecasting**
   - Semantic Scholar
   - MNIST分类 + Yahoo Finance时序分析

4. **Liquid Neural Networks - Classification and Time Series**
   - GitHub: flaviagiammarino/lnn-sagemaker
   - AWS SageMaker实现

---

## ⚖️ 对比研究

### LNN vs 其他架构
1. **A Comparative Study on Liquid Neural Networks and Recurrent Neural Networks**
   - arXiv 2025
   - 准确性、内存效率、泛化能力对比
   - 链接: https://arxiv.org/html/2510.07578v1

2. **Liquid Neural Networks vs RNNs: A Deep Learning Approach to Time Series Forecasting**
   - LIACS Thesis Repository
   - 时序预测对比研究

3. **Liquid Neural Networks Overview**
   - Emergent Mind
   - 紧凑参数化、低延迟、增强鲁棒性

---

## 💻 开源实现与教程

### 官方实现
1. **官方GitHub: liquid_time_constant_networks**
   - 作者: Ramin Hasani
   - 链接: https://github.com/raminmh/liquid_time_constant_networks
   - ⭐ 高星标，官方实现

### 社区实现
2. **LTCtutorial - 从零实现LTC**
   - 作者: KPEKEP
   - 链接: https://github.com/KPEKEP/LTCtutorial/
   - ⭐ 44 stars, 详细教程

3. **LNN - Liquid Neural Network**
   - 作者: MMatulenko
   - 链接: https://github.com/MMatulenko/LNN
   - ⭐ 31 stars, 股价预测和异常检测

4. **liquid-neural-networks**
   - 作者: babycommando
   - 链接: https://github.com/babycommando/liquid-neural-networks
   - 包含liquidMNIST.ipynb

5. **Liquid Neural Networks (LNNs) Classification**
   - 作者: SeyedMuhammadHosseinMousavi
   - 链接: https://github.com/SeyedMuhammadHosseinMousavi/Liquid-Neural-Networks-LNNs-Classification
   - 分类、聚类、回归

### 教程资源
6. **Liquid Neural Networks: Simple Implementation**
   - Plain English博客
   - 从零构建LNN

7. **Build Your Own Liquid Neural Network with PyTorch**
   - AI Startup Scout
   - PyTorch实现教程

8. **Liquid Neural Networks: A Basic Implementation for Time Series**
   - GOpenAI博客
   - 时序预测基础实现

9. **Kaggle: Liquid Neural Networks**
   - 作者: newtonbaba12345
   - 链接: https://www.kaggle.com/code/newtonbaba12345/liquid-neural-networks
   - 使用ncps模块实现

---

## 🎓 教育资源

### 视频教程
1. **Liquid Neural Networks | Ramin Hasani | TEDxMIT**
   - YouTube
   - 链接: https://www.youtube.com/watch?v=RI35E5ewBuI

2. **Inventing liquid neural networks**
   - MIT CSAIL
   - 链接: https://www.youtube.com/watch?v=iRXZ5vQ6mGE

3. **Liquid Time-Constant Networks - Simons Institute**
   - 讲座
   - 链接: https://simons.berkeley.edu/talks/liquid-time-constant-networks

---

## 🔑 关键人物

| 姓名 | 机构 | 角色 | Google Scholar | 主页 |
|------|------|------|----------------|------|
| **Ramin Hasani** | MIT CSAIL / Liquid AI CEO | LTC主要提出者 | https://scholar.google.com/citations?user=YarJF3QAAAAJ | https://www.liquid.ai/team/ramin-hasani |
| **Mathias Lechner** | MIT / ISTA | LTC共同提出者 | - | - |
| **Daniela Rus** | MIT CSAIL主任 | 机器人领域权威 | - | - |
| **Alexander Amini** | MIT | LTC合作者 | - | - |

---

## 📚 推荐阅读顺序

### 入门路线
1. 观看TED演讲了解直观概念
2. 阅读Nature 2022的闭式解论文
3. 运行官方GitHub代码
4. 尝试Kaggle或教程实现

### 深入研究
1. 精读AAAI 2021的LTC奠基论文
2. 阅读对比研究论文
3. 选择一个应用领域论文精读
4. 尝试改进或应用到自己的项目

---

## 📝 文献收集日志

**2026-03-06 15:45** - 第二阶段完成
- 识别40+篇文献
- 覆盖理论、自动驾驶、机器人、时序预测
- 找到10+个开源实现
- 确定4位核心人物

**下一步**: 第三阶段 - 分类整理
