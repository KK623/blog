# Liquid Neural Network 领域地图
## LNN Research Landscape

```
                    ┌─────────────────────────────────────┐
                    │     LIQUID NEURAL NETWORKS          │
                    │         液态神经网络                │
                    └──────────────┬──────────────────────┘
                                   │
          ┌────────────────────────┼────────────────────────┐
          │                        │                        │
          ▼                        ▼                        ▼
┌─────────────────┐    ┌──────────────────┐    ┌──────────────────┐
│   FOUNDATIONS   │    │   ALGORITHMS     │    │  APPLICATIONS    │
│     理论基础    │    │    算法架构      │    │    应用场景      │
└────────┬────────┘    └────────┬─────────┘    └────────┬─────────┘
         │                      │                       │
    ┌────┴────┐            ┌────┴────┐           ┌────┴────┐
    │         │            │         │           │         │
    ▼         ▼            ▼         ▼           ▼         │
┌────────┐ ┌────────┐  ┌────────┐ ┌────────┐  ┌────────┐   │
│Neural  │ │Dynamic │  │ LTC    │ │Closed  │  │Autonomous│   │
│ODE     │ │Systems │  │Networks│ │Form    │  │Driving  │   │
└────────┘ └────────┘  └────────┘ └────────┘  └────────┘   │
    │         │            │         │           │         │
┌────────┐ ┌────────┐  ┌────────┐ ┌────────┐  ┌────────┐   │
│ODE Solvers│ │Bifurcation│ │NCP    │ │Approximate│ │Drone   │   │
│        │ │Theory  │  │       │ │Solution│  │Control │   │
└────────┘ └────────┘  └────────┘ └────────┘  └────────┘   │
                                                   │         │
                                              ┌────────┐    │
                                              │Robotics│    │
                                              └────────┘    │
                                                   │        │
                                              ┌────────┐    │
                                              │Time    │    │
                                              │Series  │────┘
                                              └────────┘

═══════════════════════════════════════════════════════════════════

TIMELINE: LNN发展时间线
═══════════════════════════════════════════════════════════════════

2018 ──┬── Neural ODE论文发表 (NeurIPS)
       │   提出用ODE描述神经网络
       │
2020 ──┼── Liquid Time-Constant Networks
       │   Ramin Hasani et al. (arXiv)
       │   奠定LTC理论基础
       │
2021 ──┼── LTC正式发表 (AAAI)
       │   获得广泛关注
       │
2022 ──┼── Closed-form Solution (Nature)
       │   计算效率突破
       │   训练速度提升10-100倍
       │
2023 ──┼── Drone Navigation (Science Robotics)
       │   19个神经元控制无人机
       │   证明超强泛化能力
       │
2024 ──┼── LTC-SE for Embedded Systems
       │   扩展到资源受限设备
       │
2025 ──┴── Robotic Manipulators (Nature SR)
       └── 逆运动学应用突破

═══════════════════════════════════════════════════════════════════

KEY PLAYERS: 关键人物与机构
═══════════════════════════════════════════════════════════════════

MIT CSAIL (美国)
├── Ramin Hasani ──────── Liquid AI CEO, LTC主要提出者
├── Mathias Lechner ───── LTC共同提出者
├── Daniela Rus ───────── CSAIL主任, 机器人权威
└── Alexander Amini ───── LTC合作者

相关研究机构
├── ISTA (奥地利) ─────── Mathias Lechner
├── University of Adelaide ─ Jinho Choi
├── UNICAMP (巴西) ────── Pedro Valadares
└── Huawei ────────────── Kayol Mayer

═══════════════════════════════════════════════════════════════════

RELATED FIELDS: 相关领域
═══════════════════════════════════════════════════════════════════

Continuous-Time Learning
├── Neural ODE ─────────── 神经微分方程
├── ODE-RNN ────────────── ODE循环网络
├── Latent ODE ─────────── 隐空间ODE
└── Neural CDE ─────────── 神经控制微分方程

Sequence Models
├── RNN/LSTM/GRU ───────── 传统循环网络
├── Transformers ───────── 注意力机制
├── S4/Mamba ───────────── 状态空间模型
└── RetNet/RWKV ────────── 新架构

Dynamical Systems
├── Reservoir Computing ── 储备池计算
├── Echo State Networks ── 回声状态网络
├── Liquid State Machines ─ 液态状态机
└── Spiking Neural Networks ─ 脉冲神经网络

═══════════════════════════════════════════════════════════════════

APPLICATION MAP: 应用地图
═══════════════════════════════════════════════════════════════════

Robotics & Control
├── 🚁 Drone Navigation ── 无人机导航 (MIT)
├── 🤖 Robot Manipulation ─ 机械臂控制
├── 🚗 Autonomous Driving ─ 自动驾驶
└── 🦿 Legged Locomotion ── 足式机器人

Time Series & Prediction
├── 📈 Stock Prediction ─── 股价预测
├── ⚡ Energy Forecasting ─ 能源预测
├── 🏥 Medical Signals ─── 医疗信号
└── 🌤️ Weather Prediction ─ 天气预测

Other Domains
├── 🧠 Neuroscience ────── 神经科学建模
├── 🔒 Cybersecurity ───── 网络安全
├── 🎮 Gaming/RL ───────── 游戏/强化学习
└── 📡 Signal Processing ─ 信号处理

═══════════════════════════════════════════════════════════════════

RESOURCES: 资源汇总
═══════════════════════════════════════════════════════════════════

📄 Papers
├── arXiv:2006.04439 ──── Liquid Time-constant Networks (AAAI 2021)
├── arXiv:2106.13898 ──── Closed-form Solution (Nature 2022)
└── arXiv:2401.03965 ──── Differential Equations Survey (2024)

💻 Code
├── Official GitHub ────── raminmh/liquid_time_constant_networks
├── ncps Library ───────── Neural Continuous Processes
└── Community ──────────── 10+ PyTorch/TensorFlow implementations

🎥 Videos
├── TEDxMIT ────────────── Ramin Hasani演讲
├── MIT CSAIL ──────────── 发明LNN的故事
└── Simons Institute ───── LTC讲座

🏢 Companies
├── Liquid AI ──────────── liquid.ai (Ramin Hasani创立)
└── Research Groups ────── MIT CSAIL, ISTA, etc.

═══════════════════════════════════════════════════════════════════

METRICS: 关键指标对比
═══════════════════════════════════════════════════════════════════

                    LSTM        LTC (LNN)       提升
Parameters         100K+         1K-10K        10-100x ↓
Training Speed     1x            10-100x       10-100x ↑
OOD Robustness     Baseline      Excellent     Significant ↑
Adaptability       Low           High          Major ↑
Interpretability   Low           Medium        ↑

═══════════════════════════════════════════════════════════════════
