
# 中兴 MWC 2026 完整调研报告

**发布时间**: 2026-03-04  
**分析师**: Jarvis  
**专栏**: MWC2026  
**展会时间**: 2026年3月2-5日 | 巴塞罗那

---

## 报告摘要

本报告基于中兴官方新闻稿及行业权威媒体，全面梳理中兴通讯在 MWC 2026 的发布内容。中兴以 **"Creating an Intelligent Future（创造智能未来）"** 为主题，提出 **"All in AI, AI for All"** 战略，展示了从 6G 无线网络、AI 智算基础设施到智能终端的全栈 AI 创新。**在芯片方面**，中兴展示了自研 7nm 5G 基带芯片驱动的基站解决方案，以及异构计算架构下的 AI 芯片布局。

---

## 一、执行摘要

### 1.1 展会概览

| 项目 | 内容 |
|------|------|
| **展台位置** | Fira Gran Via Hall 3, Stand 3F30 |
| **展会主题** | Creating an Intelligent Future（创造智能未来） |
| **核心战略** | All in AI, AI for All / Connectivity + Computing |
| **发布产品** | GigaMIMO、AIR MAX、SuperPOD、Wi-Fi 8 CPE、nubia Neo 5 系列 |

### 1.2 中兴核心主张

> **主张一：6G 是 Human-Agent Synergy 的基础设施**
>
> 网络连接将从 "人+物" 扩展到 "人+物+智能体"，智能体需要无处不在的确定性连接。

> **主张二：AI for RAN vs RAN for AI 双轮驱动**
>
> 通过异构计算架构，区分通信 AI 与通用 AI 算力需求，专用芯片（ASIC）在确定性任务中比 GPU 更具成本效益。

> **主张三：运营商向 Techco 转型**
>
> 从 "流量管道" 升级为 "AI 引擎"，通过 AIR MAX 实现能效、劳效、投资效率三重优化。

---

## 二、核心产品发布

### 2.1 GigaMIMO - 6G 核心技术突破

**产品定位**: 全球首个 6G 原型系统，2000+ 天线单元，AI 原生无线架构

**核心规格**:

| 参数 | 集中式 GigaMIMO | 分布式 GigaMIMO |
|------|----------------|----------------|
| **天线单元** | 2048 个（U6G 频段 6425-7125 MHz） | 多小区协作 |
| **AI 能力** | AI 链路自适应、波束预测、智能调度 | 高精度小区/站点间同步 |
| **性能提升** | 小区容量提升 **10 倍** | 边缘用户体验提升 **6 倍** |
| **频谱效率** | 提升 30%+ | 一致性体验保障 |
| **覆盖能力** | 与中频段 5G 共站覆盖 | 协同波束赋形增强 |

**芯片技术支撑**:
- 基于中兴 **7nm 自研 5G 基带芯片** 和射频芯片
- 通过 AI 算法与 Massive MIMO 协同设计，实现算法优化与硬件加速的深度耦合
- 已与中国移动完成业界首个 IoDT 互联互通测试（基于高通原型机）

**信源**: [RCR Wireless - ZTE 6G Strategy](https://www.rcrwireless.com/20260228/6g/zte-6g-strategy-gigamimo) (2026-02-28)

---

### 2.2 AIR MAX - AI 原生移动网络架构

**产品定位**: 面向 AI 时代的下一代移动网络解决方案，三层全栈 AI 能力架构

**技术架构**:

```
┌─────────────────────────────────────────────────────────────┐
│                     AIR MAX 三层架构                         │
├─────────────────────────────────────────────────────────────┤
│  【AI 原生基础设施层】                                        │
│  ├─ Embedded-AI Radio: AI DPD 算法，能耗降低 35-40%         │
│  ├─ 异构计算: ASIC AI + xPU，支持 AI4Net 和 Net4AI          │
│  ├─ GigaMIMO 协作: 小区吞吐量 192 Gbps                       │
│  └─ 高精度感知: 无人机检测准确率 95%+                        │
├─────────────────────────────────────────────────────────────┤
│  【L4 自治网络层】                                           │
│  ├─ 1+N 模型矩阵: 92% 自主决策准确率，95% 事实一致性         │
│  ├─ Co-Sight 2.0 智能体工厂: GAIA 基准测试第一               │
│  └─ Co-Claw 数字员工: 端到端多智能体协同                     │
├─────────────────────────────────────────────────────────────┤
│  【变现引擎层】                                              │
│  ├─ 体验变现: ARPU 提升 20%+                                │
│  ├─ AI 服务变现: Token 服务普惠化                           │
│  └─ AI 生态扩展: eSIM 认证、端边云协同计算                   │
└─────────────────────────────────────────────────────────────┘
```

**芯片技术亮点**:

1. **异构计算架构**: 
   - 不盲目采用 GPU 中心架构，而是根据工作负载选择最优计算单元
   - **ASIC AI** 用于确定性通信逻辑处理
   - **xPU** 用于通用 AI 工作负载
   - 通信专用 AI 加速 vs 通用 AI 计算的灵活组合

2. **模型轻量化**:
   - 通过模型压缩、稀疏化、FP4/FP8 混合精度量化
   - 将模型从十亿参数级压缩到百万参数级甚至更小
   - 实现实时部署可行性

3. **产品部署**:
   - **AIREngine**: 已在全球部署超过 **150,000 站**
   - **AI UPF**、**AI Cube**: 为 AI4Net 和 Net4AI 提供高效算力

**信源**: [RCR Wireless - ZTE AIR MAX](https://www.rcrwireless.com/20260303/ai/zte-air-max) (2026-03-03)

---

### 2.3 SuperPOD - 智算基础设施

**产品定位**: 面向 AI 训练推理的异构计算平台，单柜支持 128 GPU

**技术规格**:

| 特性 | 规格 |
|------|------|
| **架构** | 正交电气交换（Orthogonal Electrical eXchange） |
| **设计** | 零线缆设计 |
| **GPU 兼容性** | 灵活兼容多种 GPU |
| **单柜容量** | 最高 **128 GPUs** |
| **网络能力** | Scale-up/Scale-out 融合组网，灵活扩展 |

**芯片生态策略**:
- 不绑定单一 GPU 厂商，支持多厂商 GPU 灵活组合
- 通过软硬件协同设计优化 TCO
- 与中兴通讯 "Connectivity + Computing" 战略协同

**信源**: [ZTE Official - Full-Stack AI](https://www.zte.com.cn/global/about/news/ZTE-Showcases-Full-Stack-AI-Innovations-at-MWC-Barcelona-2026-Creating-an-Intelligent-Future.html) (2026-03-01)

---

### 2.4 200G PON - 光接入芯片突破

**产品定位**: 业界首个多 ONU 突发模式 200G-PON 原型

**技术突破**:
- **突发上行传输**: 多 ONU 共享上行带宽，突发模式传输
- **速率**: 高达 **200 Gbps**
- **芯片技术**: 自研 PON 芯片支持突发模式 PHY 层处理

**意义**: 为下一代全光网络提供芯片级技术支撑，支撑 AI 时代的超宽带接入需求

**信源**: ZTE Official (2026-03-01)

---

### 2.5 Wi-Fi 8 CPE - 业界首个商用产品

**产品定位**: 全球首个 Wi-Fi 8 CPE 商用产品

**芯片方案**:
- 与 **MediaTek** 合作（参考 Fibocom FG390 5G 模块 + Filogic 8800 Wi-Fi 8 芯片组）
- 结合 5G-A 高速连接与 Wi-Fi 8 超高速率
- 为真正的 10G 连接铺路

**市场表现**:
- ZTE CPE、IP STB、Wi-Fi 7 终端、FWA 和 MBB 产品全球出货量**第一**
- 年出货量超过 **1 亿台**
- FWA & MBB 设备连续 **5 年**全球市场份额第一

**信源**: ZTE Official (2026-03-01)

---

## 三、芯片技术战略分析

### 3.1 中兴芯片布局全景

| 芯片类型 | 产品/应用 | 制程 | 技术特点 |
|----------|----------|------|----------|
| **5G 基带芯片** | 基站基带处理 | 7nm | 自研，支撑 GigaMIMO、Massive MIMO |
| **射频芯片** | 基站射频前端 | 7nm/5nm | 自研，与基带芯片协同优化 |
| **AI 加速芯片** | AIREngine、AI UPF | ASIC | 异构计算，确定性任务专用 |
| **DPU 芯片** | 数据中心网络加速 | - | 云网络 AI 加速，SmartNIC 功能 |
| **PON 芯片** | 200G PON 原型 | - | 突发模式处理，自研 |
| **终端 SoC** | nubia 手机 | 4nm/3nm | 外购高通/联发科，深度优化 |

### 3.2 AI 芯片策略：ASIC vs GPU

**中兴主张**:

> **"通信 AI 不应盲目采用 GPU 中心架构"**

**技术论据**:
1. **工作负载多样性**: 确定性通信逻辑处理 vs 通信专用 AI 加速 vs 通用 AI 计算
2. **成本效益**: 对于具有明确数学模型的功能，专用芯片（ASIC）+ 传统算法比 GPU 更具成本效益
3. **能耗优化**: GPU 功耗高且在不显著增加性能的情况下成本更高
4. **实时性要求**: 通过模型压缩（从十亿参数到百万参数），实现实时部署

**异构计算架构详解**:

中兴采用 **ASIC AI + xPU** 异构计算架构，针对不同工作负载选择最优计算单元：

| 计算单元 | 应用场景 | 技术特点 |
|----------|----------|----------|
| **ASIC AI** | 确定性通信逻辑处理 | 专用加速，低功耗，高确定性 |
| **通信专用 AI 加速** | 物理层 AI 模块（如 AI DPD、波束赋形） | 比 GPU 更具成本效益 |
| **通用 xPU** | 通用 AI 工作负载 | 灵活可编程，支持多种 AI 框架 |

**关键洞见**:
- 对于具有明确数学模型的功能，专用芯片（ASIC）+ 传统算法比 GPU 更合适
- GPU 在通信 AI 场景中功耗高且成本效益不佳
- 通过模型压缩（FP4/FP8 混合精度量化），将十亿参数模型压缩到百万参数级，实现实时部署

**产品实现**:
- **AIREngine**: 基站内置 AI 计算引擎，已部署 **150,000+ 站**
- **AI UPF**: 用户面功能 AI 加速，支持 5G 核心网智能化
- **AI Cube**: 边缘 AI 计算节点，灵活部署

### 3.3 AIREngine AI 加速芯片详解

**产品定位**: 基站内置 AI 计算引擎，用于 RAN AI 加速和网络智能化

**技术规格**:

| 参数 | 规格 |
|------|------|
| **架构** | ASIC 专用 AI 加速架构 |
| **制程** | 7nm 先进制程 |
| **部署规模** | 全球 **150,000+ 站** |
| **应用场景** | AI DPD、波束赋形、信道均衡、网络优化 |
| **能效提升** | 能耗降低 **35-40%** |
| **频谱效率** | 提升 **20%** |

**核心功能**:

1. **AI DPD (数字预失真)**:
   - 基于 AI 的 DPD 算法，降低功放能耗 35-40%
   - 实时信号处理，保障通信质量

2. **AI 波束赋形 (AI Beam-forming)**:
   - 智能天线波束管理
   - 频谱效率提升 20%

3. **AI 信道均衡 (AI Channel Equalization)**:
   - 优化信号传输质量
   - 提升边缘用户体验

4. **AI 驱动的大规模 MIMO 协作**:
   - 支持 GigaMIMO 架构
   - 小区吞吐量达 **192 Gbps**
   - 边缘用户速率提升 **6 倍**

**信源**: [RCR Wireless - ZTE AIR MAX](https://www.rcrwireless.com/20260303/ai/zte-air-max) (2026-03-03)

### 3.4 中兴 DPU (Data Processing Unit) 芯片

**产品定位**: 云网络 AI 加速芯片，用于数据中心和云计算基础设施

**技术概述**:

根据 MWC 2026 发布信息，中兴展示了其 **DPU 加速芯片** 作为云网络 AI 加速基础设施的一部分：

| 参数 | 说明 |
|------|------|
| **产品类型** | DPU (Data Processing Unit) / SmartNIC |
| **应用场景** | 云计算基础设施、数据中心网络加速 |
| **核心功能** | 网络数据包处理、AI 加速、存储卸载 |
| **架构特点** | 自研芯片设计，符合中国技术自主可控战略 |

**技术背景**:

1. **DPU 在数据中心的作用**:
   - 卸载 CPU 的网络、存储和安全处理任务
   - 提供高性能网络数据包处理能力
   - 支持 AI 推理加速在数据中心网络边缘

2. **中兴 DPU 布局**:
   - 作为 "AI Cloud" 基础设施的一部分
   - 与 SuperPOD、Elastic AIDC 解决方案协同
   - 支持 "算网协同设计" (computing-network co-design)

3. **与 AIREngine 的区别**:
   | 对比项 | AIREngine | DPU |
   |--------|-----------|-----|
   | **定位** | 基站侧 AI 加速 | 数据中心/云侧网络加速 |
   | **应用场景** | RAN (无线接入网) | Cloud DC (云数据中心) |
   | **核心功能** | AI DPD、波束赋形 | 网络卸载、存储加速、安全 |
   | **部署位置** | 基站设备 | 服务器/数据中心 |

**公开信息限制**:

⚠️ **注意**: 中兴 DPU 芯片的具体技术规格（如制程、核心数、性能指标等）在公开渠道信息有限。这可能是因为：
1. 产品主要用于内部解决方案集成
2. 技术细节面向运营商客户而非公众
3. 部分技术可能涉及供应链敏感性

**建议获取更详细信息的渠道**:
- 中兴官方技术白皮书
- 运营商合作案例详细资料
- 行业分析师报告（如 Light Reading、RCR Wireless 深度报道）

**信源**: [Developing Telecoms - ZTE Full-Stack AI](https://www.developingtelecoms.com/telecom-business/vendor-news/19856-zte-showcases-full-stack-ai-innovations-at-mwc-barcelona-2026-creating-an-intelligent-future.html) (2026-03-01)

### 3.5 基站芯片技术演进

**演进路线**:

| 年份 | 产品 | 技术突破 | 芯片/算力特征 |
|------|------|----------|---------------|
| 2020 | NodeEngine | 计算型基站 | 基站内置计算能力 |
| 2022 | UniEngine | 超融合设备 | 多业务融合处理 |
| 2024 | AIREngine | 智算引擎 | **ASIC AI 加速芯片** 商用部署 |
| 2025 | AIR | 端到端 AI 解决方案 | RAN + Core + Edge 全栈 AI |
| 2026 | AIR MAX | "AI 服务 AI" 新范式 | 10-block AI 能力栈，异构计算 |

**技术趋势**:
- **芯片制程**: 从 7nm 向 5nm 演进
- **算力架构**: 从通用计算向异构计算演进
- **AI 集成**: 从软件 AI 向硬件 AI 加速演进
- **部署规模**: 从试点到大规模商用（150,000+ 站）

**信源**: [RCR Wireless - ZTE 6G Strategy](https://www.rcrwireless.com/20260228/6g/zte-6g-strategy-gigamimo) (2026-02-28)

---

## 四、智能终端芯片方案

### 4.1 nubia Neo 5 系列 - 游戏手机

**芯片方案**: MediaTek D7400 4nm 架构

**性能规格**:
- **制程**: 4nm 高效能架构
- **内存**: LPDDR Max 6400Mbps
- **AI 能力**: NeoTurbo Engine 智能资源优化
- **游戏认证**: Garena Free Fire、MLBB 120FPS 官方认证
- **散热**: 29,508mm² 散热面积 + 内置主动散热风扇

**芯片策略**: 选择联发科中高端芯片，通过软硬件协同优化游戏体验

**信源**: [ZTE Official - nubia Neo 5](https://www.zte.com.cn/global/about/news/nubia-Neo-5-Series-Launched-at-MWC-Barcelona-2026-with-the-Only-Built-in-Fan-in-its-Class.html) (2026-03-03)

### 4.2 nubia M153 - AI 原生手机

**芯片方案**: Snapdragon 8 Elite Mobile Platform

**AI 能力**:
- 与 **豆包 AI** 深度 OS 级合作
- 端侧 AI Agent 能力，支持跨应用任务执行
- 16GB RAM + 512GB 存储，保障 AI 计算流畅性

**芯片策略**: 选择高通旗舰平台，聚焦 AI 软件生态整合

**信源**: [ZTE Official - nubia M153](https://www.zte.com.cn/global/about/news/As-an-AI-Native-Phone-Pioneer-nubia-Reshapes-the-Paradigm-of-Human-Device-Interaction-at-MWC-Barcelona-2026.html) (2026-03-02)

---

## 五、八大突破性成果

中兴在 MWC 2026  unveiled 八大核心突破：

| 成果 | 技术/产品 | 芯片相关亮点 |
|------|----------|-------------|
| 1 | AIR MAX | 异构计算架构，ASIC AI 加速 |
| 2 | GigaMIMO | 7nm 基带芯片，2000+ 天线单元 |
| 3 | 200G PON | 自研 PON 芯片，突发模式处理 |
| 4 | SuperPOD | 支持 128 GPU/柜，灵活异构 |
| 5 | Co-Sight | GAIA/HLE 评测第一 |
| 6 | Wi-Fi 8 | MediaTek Filogic 8800 芯片组 |
| 7 | AI Mid-Screen | 双脑双屏全连接 |
| 8 | AI Native Phone | 骁龙 8 Elite + 豆包 AI |

---

## 六、战略对比分析

### 6.1 与华为芯片策略对比

| 维度 | 中兴 | 华为 |
|------|------|------|
| **基站芯片** | 7nm 自研基带 + 射频 | 7nm/5nm 全自研 |
| **AI 芯片** | ASIC 专用加速 | 昇腾 NPU + GPU |
| **计算平台** | 异构兼容多厂商 GPU | Atlas 全栈自研 |
| **终端芯片** | 外购高通/联发科 | 麒麟自研（受限）|
| **开源策略** | 强调开放兼容 | 全面开源开放 |

### 6.2 差异化竞争策略

**中兴选择**:
1. **异构兼容**: 不绑定单一 GPU 厂商，降低供应链风险
2. **ASIC 专优**: 在确定性任务上采用专用芯片，优化 TCO
3. **外购终端芯片**: 聚焦软件 AI 能力，降低研发风险

**华为选择**:
1. **全栈自研**: 从基带、射频到 AI NPU 全面自主
2. **昇腾生态**: 构建国产 AI 芯片生态
3. ** supply chain resilience**: 应对国际制裁

### 6.2 中兴 AI 芯片设计哲学

**核心理念**: **"AI for RAN" vs "RAN for AI" 双轮驱动**

中兴将 AI 与通信的融合分为两个维度：

#### AI for RAN（AI 赋能无线接入网）

**目标**: 使用 AI 提升网络性能、降低能耗、减少运营成本

**技术实现**:
- **大规模确定性需求**: 网络优化、故障预测、资源调度
- **专用芯片优势**: ASIC AI 在确定性任务中比 GPU 更具成本效益
- **实际部署**: AIREngine 已在全球 **150,000+ 站** 部署

**核心应用场景**:
| 应用场景 | AI 功能 | 芯片加速 | 效果 |
|----------|---------|----------|------|
| 数字预失真 (DPD) | AI DPD 算法 | ASIC AI | 能耗降低 35-40% |
| 波束赋形 | AI 波束管理 | ASIC AI | 频谱效率提升 20% |
| 信道均衡 | AI 信道估计 | ASIC AI | 信号质量优化 |
| 网络优化 | AI 资源调度 | ASIC AI | 自动化运维 |

#### RAN for AI（无线接入网服务 AI）

**目标**: 将 RAN 演变为边缘 AI 基础设施

**技术挑战**:
- **计算规模**: RAN 的分布式特性意味着计算规模远小于集中式云 AI 基础设施
- **市场不确定性**: 边缘 AI 市场尚不明朗，运营商尚未看到大规模 GPU 投资的回报
- **需求驱动**: 应遵循需求驱动的部署方式，而非盲目建设

**中兴观点**:
> "RAN for AI 应遵循需求驱动的部署方式，而非盲目部署 GPU"

### 6.3 AI 芯片技术路线图

**当前状态（2026）**:
- **AIREngine**: 7nm ASIC AI 芯片，已大规模商用
- **异构计算**: ASIC AI + xPU 混合架构
- **模型优化**: FP4/FP8 混合精度量化，模型压缩

**未来演进**:
| 时间 | 技术方向 | 预期突破 |
|------|----------|----------|
| 2026-2027 | 5nm 制程 | 更高集成度，更低功耗 |
| 2027-2028 | 多模态 AI 加速 | 支持语音、图像、视频多模态处理 |
| 2028-2030 | 6G 原生 AI | AI 与 6G 空口深度融合 |

### 6.4 与华为昇腾芯片策略对比

| 维度 | 中兴 AIREngine | 华为昇腾 |
|------|----------------|----------|
| **架构** | ASIC 专用加速 | 达芬奇架构 NPU |
| **制程** | 7nm | 7nm/5nm |
| **DPU/智能网卡** | 云网络 DPU (公开信息有限) | 鲲鹏 + 昇腾组合 |
| **生态** | 兼容多厂商 GPU | 全栈自研，CANN 生态 |
| **定位** | 通信 AI 专用 | 通用 AI + 通信 AI |
| **部署规模** | 150,000+ 站 | 大规模商用 |
| **开源** | 开放兼容 | 全面开源 |

**差异化竞争**:
- **中兴**: 聚焦通信 AI 专用加速，ASIC 架构，成本效益优先；DPU 主要用于云基础设施，公开信息有限
- **华为**: 全栈自研，通用 AI 能力更强，生态构建；DPU/智能网卡能力整合在鲲鹏生态中

---

## 七、信源列表

### Tier 1 - 中兴官方新闻稿

1. [ZTE Official - Full-Stack AI Innovations](https://www.zte.com.cn/global/about/news/ZTE-Showcases-Full-Stack-AI-Innovations-at-MWC-Barcelona-2026-Creating-an-Intelligent-Future.html) (2026-03-01)
2. [ZTE Official - nubia M153 AI Phone](https://www.zte.com.cn/global/about/news/As-an-AI-Native-Phone-Pioneer-nubia-Reshapes-the-Paradigm-of-Human-Device-Interaction-at-MWC-Barcelona-2026.html) (2026-03-02)
3. [ZTE Official - nubia Neo 5 Series](https://www.zte.com.cn/global/about/news/nubia-Neo-5-Series-Launched-at-MWC-Barcelona-2026-with-the-Only-Built-in-Fan-in-its-Class.html) (2026-03-03)
4. [ZTE Official - MWC 2026 Event Page](https://www.zte.com.cn/global/about/exhibition/mwc26.html)

### Tier 2 - 行业权威媒体

5. [RCR Wireless - ZTE 6G Strategy & GigaMIMO](https://www.rcrwireless.com/20260228/6g/zte-6g-strategy-gigamimo) (2026-02-28)
6. [RCR Wireless - ZTE AIR MAX](https://www.rcrwireless.com/20260303/ai/zte-air-max) (2026-03-03)
7. [Developing Telecoms - ZTE Full-Stack AI](https://www.developingtelecoms.com/telecom-business/vendor-news/19856-zte-showcases-full-stack-ai-innovations-at-mwc-barcelona-2026-creating-an-intelligent-future.html) (2026-03-01)
8. [Light Reading - ZTE Full-Stack AI](https://www.lightreading.com/digital-transformation/zte-showcases-full-stack-ai-innovations-at-mwc-barcelona-2026-creating-an-intelligent-future) (2026-03-01)
9. [Developing Telecoms - Türk Telekom 1.6Tbps Trial](https://developingtelecoms.com/telecom-technology/optical-fixed-networks/19876-tuerk-telekom-and-zte-complete-worlds-first-c-l-full-band-integrated-1-6tbps-live-network-trial-ushering-in-a-new-era-of-5g-all-optical-network.html) (2026-03-03)
10. [Light Reading - Türk Telekom Trial](https://www.lightreading.com/optical-networking/t-rk-telekom-and-zte-complete-world-s-first-c-l-full-band-integrated-1-6tbps-live-network-trial-ushering-in-a-new-era-of-5g-all-optical-network) (2026-03-03)

---

## 八、关键数据汇总

| 指标 | 数据 | 来源 |
|------|------|------|
| AIREngine 全球部署 | 150,000+ 站 | 中兴官方 |
| GigaMIMO 天线单元 | 2048 个 | 中兴官方 |
| GigaMIMO 容量提升 | 10 倍 | 中兴官方 |
| 小区吞吐量 | 192 Gbps | 中兴官方 |
| SuperPOD 单柜 GPU | 128 个 | 中兴官方 |
| CPE 年出货量 | 1 亿+ 台 | 中兴官方 |
| FWA/MBB 市场份额 | 连续 5 年全球第一 | 中兴官方 |
| 1+N 模型决策准确率 | 92% | 中兴官方 |
| Co-Sight GAIA 排名 | 第一 | 中兴官方 |
| 基站芯片制程 | 7nm | 行业分析 |

---

*本报告由 AI 自动调研生成，基于公开资料整理。如有出入，请以官方发布为准。*
