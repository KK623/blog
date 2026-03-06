# CVNN学者全景图谱（交互版）设计文档

**日期**: 2026-03-06  
**版本**: 方案三 - 折中优化版  
**状态**: 已批准，待实施

---

## 1. 项目概述

### 1.1 目标
创建一个可交互的CVNN（复数神经网络）领域学者全景图谱，展示30-50位核心研究者的深度档案、合作关系和领域分布。

### 1.2 核心功能
- 30-50位学者的深度档案卡片（可折叠展开）
- 实时搜索和领域筛选
- 可视化图表（领域分布、机构排名）
- 学者合作关系网络（简化版）
- 数据导出功能（JSON/CSV）

### 1.3 技术要求
- **前端框架**: Alpine.js（轻量，2.8KB）
- **样式**: Tailwind CSS
- **图表**: Chart.js
- **数据**: 本地JSON（从505篇论文提取）
- **交付**: 单个HTML文件（可离线使用）

---

## 2. 页面结构

### 2.1 Hero区域
- 标题: "CVNN领域学者全景图谱"
- 副标题: "30位核心研究者 · 深度档案 · 合作网络"
- 实时统计: 学者数、机构数、领域数、论文总数

### 2.2 控制面板
- 搜索框（实时过滤姓名/机构）
- 领域标签按钮（可点击筛选）
- 排序选项（按引用数/h-index/活跃年份）

### 2.3 学者网格
- 响应式布局: 手机1列 / 平板2列 / 桌面3列
- 每张卡片包含:
  - 头像、姓名、机构
  - h-index、引用数
  - 领域标签
  - [点击展开] 按钮

### 2.4 展开详情
展开后显示:
- 核心贡献（200字描述）
- 代表作10篇（标题、会议、引用数）
- 主要合作者（可点击跳转）

### 2.5 可视化区
- **领域分布饼图**: 点击饼块筛选对应学者
- **机构排名柱状图**: Top 10机构学者数量
- **时间轴**: 学者活跃时间段分布

### 2.6 合作网络（简化版）
- 力导向图简化实现
- 鼠标悬停高亮合作关系
- 节点大小=影响力，连线粗细=合作强度

### 2.7 导出工具
- [导出JSON] 按钮
- [导出CSV] 按钮
- [打印视图] 按钮

### 2.8 页脚
- 数据来源说明
- 生成时间
- 方法论简述

---

## 3. 数据结构

### 3.1 学者档案 Schema
```json
{
  "scholars": [
    {
      "id": "chiheb-trabelsi",
      "name": "Chiheb Trabelsi",
      "name_zh": "基赫布·特拉贝尔西",
      "institution": "Université de Montréal",
      "institution_zh": "蒙特利尔大学",
      "country": "加拿大",
      "country_flag": "🇨🇦",
      "photo": "https://scholar.googleusercontent.com/...",
      "photo_fallback": "https://ui-avatars.com/api/?name=Chiheb+Trabelsi",
      "h_index": 25,
      "h_index_5y": 20,
      "citations": 3200,
      "citations_5y": 2100,
      "fields": ["理论奠基", "架构设计"],
      "fields_en": ["Theory", "Architecture"],
      "contributions": "Deep Complex Networks奠基工作，提出复数批归一化、复数权重初始化等关键技术...",
      "contributions_en": "Pioneer of Deep Complex Networks, proposed complex batch normalization...",
      "bio": "博士后研究员，专注于复数神经网络的深度学习理论研究...",
      "top_papers": [
        {
          "title": "Deep Complex Networks",
          "title_zh": "深度复数网络",
          "venue": "ICLR",
          "year": 2018,
          "citations": 800,
          "arxiv": "https://arxiv.org/abs/1705.09792"
        }
      ],
      "collaborators": ["yoshua-bengio", "li-jing", "..."],
      "active_years": "2016-2025",
      "homepage": "https://...",
      "scholar_url": "https://scholar.google.com/citations?user=..."
    }
  ]
}
```

### 3.2 合作关系 Schema
```json
{
  "collaborations": [
    {
      "source": "chiheb-trabelsi",
      "target": "yoshua-bengio",
      "strength": 5,
      "papers": ["paper1", "paper2", "..."]
    }
  ]
}
```

### 3.3 机构数据 Schema
```json
{
  "institutions": [
    {
      "id": "universite-de-montreal",
      "name": "Université de Montréal",
      "name_zh": "蒙特利尔大学",
      "country": "加拿大",
      "scholar_count": 3,
      "total_citations": 5000
    }
  ]
}
```

---

## 4. 交互功能详细设计

### 4.1 搜索功能
- 实时响应（debounce 200ms）
- 搜索范围: 姓名、机构、领域
- 高亮匹配文本
- 空状态提示

### 4.2 筛选功能
- 单选/多选领域标签
- 筛选结果计数显示
- URL参数同步（可分享筛选状态）
- 一键清除筛选

### 4.3 卡片展开/收起
- 点击卡片任意位置展开
- 展开时其他卡片自动收起（手风琴效果）
- 平滑动画过渡（300ms）
- 展开后滚动到视图中央

### 4.4 图表交互
- 点击饼图扇区 → 筛选对应领域学者
- 点击柱状图 → 筛选对应机构学者
- 悬停显示详细数据tooltip

### 4.5 合作网络
- 鼠标悬停学者节点 → 高亮相关合作者
- 点击节点 → 展开该学者详情卡片
- 拖拽调整布局（可选）

### 4.6 导出功能
- **JSON导出**: 完整学者数据，便于二次开发
- **CSV导出**: 表格形式，便于Excel分析
- **打印视图**: 优化打印样式，生成PDF友好

---

## 5. 视觉设计

### 5.1 配色方案
- **主色**: #0066cc (蓝色)
- **辅色**: #28a745 (绿色，成功状态)
- **强调色**: #ffc107 (黄色，高亮)
- **背景**: 渐变浅灰 (#f8fafc → #e2e8f0)
- **卡片**: 纯白 + 阴影

### 5.2 字体
- **英文**: Inter
- **中文**: Noto Sans SC
- **代码**: JetBrains Mono (可选)

### 5.3 响应式断点
- **手机**: < 640px (1列)
- **平板**: 640px - 1024px (2列)
- **桌面**: > 1024px (3列)

### 5.4 动画效果
- 卡片hover: translateY(-4px) + shadow增强
- 展开/收起: height过渡 + opacity淡入
- 筛选切换: fade过渡

---

## 6. 数据来源与处理

### 6.1 原始数据
- CVNN_Research_Report.md (34篇论文)
- CVNN_Theory_Supplement_16papers.md
- CVNN_OFDM_PHY_78篇.md
- CVNN_6G_Supplement_30papers.md
- CVNN_Radar_Supplement_35papers.md
- CVNN_MRI_Supplement_Papers.md
- 其他报告文件

### 6.2 数据处理流程
1. **提取作者信息**: 从所有论文中提取作者、机构、年份
2. **统计频次**: 计算每位作者的论文数、被引用情况（从已有数据推断）
3. **识别核心学者**: 按论文数和影响力排序，取Top 30-50
4. **分类领域**: 根据论文所属领域标记学者研究方向
5. **构建合作网络**: 从共同作者关系构建合作图谱
6. **补充元数据**: 查询Google Scholar获取h-index（可选，时间允许时）

### 6.3 质量检查
- 去重：同名作者合并
- 校验：机构名称标准化
- 补全：缺失字段标记为"待补充"

---

## 7. 技术实现细节

### 7.1 Alpine.js 状态管理
```javascript
data() {
  return {
    scholars: [],           // 全部学者数据
    filteredScholars: [],   // 筛选后的学者
    selectedFields: [],     // 选中的领域
    searchQuery: '',        // 搜索关键词
    expandedCard: null,     // 当前展开的卡片ID
    sortBy: 'citations',    // 排序方式
    viewMode: 'grid'        // 视图模式: grid/list
  }
}
```

### 7.2 关键计算属性
- `filteredScholars`: 根据搜索+筛选+排序返回结果
- `fieldStats`: 领域分布统计
- `institutionStats`: 机构统计
- `collaborationGraph`: 合作网络图数据

### 7.3 性能优化
- 虚拟滚动（如果学者数>50）
- 图片懒加载
- JSON数据内联（避免额外请求）
- Debounce搜索输入

---

## 8. 交付标准

### 8.1 功能完成标准
- [ ] 30-50位学者数据完整
- [ ] 搜索功能正常工作
- [ ] 筛选功能正常工作
- [ ] 卡片展开/收起正常
- [ ] 图表交互正常
- [ ] 导出功能正常
- [ ] 响应式布局正常

### 8.2 质量检查清单
- [ ] 手机端可用
- [ ] 无控制台错误
- [ ] 加载时间 < 3秒
- [ ] 所有链接可点击
- [ ] 打印样式正确

### 8.3 文件输出
- 单个HTML文件 (~300-400KB)
- 可选：单独的JSON数据文件（便于更新）

---

## 9. 风险与应对

| 风险 | 概率 | 影响 | 应对措施 |
|------|------|------|----------|
| 学者照片获取困难 | 中 | 低 | 使用ui-avatars生成头像 |
| h-index数据缺失 | 高 | 中 | 从已有论文数推断影响力 |
| 同名作者区分 | 中 | 中 | 结合机构+研究领域人工校验 |
| 合作关系数据不完整 | 高 | 低 | 基于共同作者计算，标注"不完整" |
| 页面体积过大 | 低 | 中 | 压缩JSON，延迟加载图片 |

---

## 10. 后续扩展（可选）

### 10.1 短期扩展
- 添加学者主页链接
- 添加论文PDF链接
- 添加机构Logo

### 10.2 长期扩展
- 接入Google Scholar API实时更新
- 添加学者活跃度趋势图
- 添加研究领域热度趋势
- 多语言支持（中英文切换）

---

## 11. 批准记录

**设计者**: Jarvis  
**批准者**: K  
**批准时间**: 2026-03-06  
**状态**: ✅ 已批准，进入实施阶段

---

## 12. 附录

### 12.1 参考资源
- Alpine.js文档: https://alpinejs.dev/
- Chart.js文档: https://www.chartjs.org/
- Tailwind CSS文档: https://tailwindcss.com/

### 12.2 类似项目参考
- CSRankings: https://csrankings.org/
- Semantic Scholar: https://www.semanticscholar.org/
- Connected Papers: https://www.connectedpapers.com/

### 12.3 数据文件清单
```
workspace/
├── CVNN_Research_Report.md
├── CVNN_Theory_Supplement_16papers.md
├── CVNN_OFDM_PHY_78篇.md
├── CVNN_6G_Supplement_30papers.md
├── CVNN_Radar_Supplement_35papers.md
├── CVNN_MRI_Supplement_Papers.md
└── blog/posts/2026/03/05/cvnn-*.html (已生成的报告)
```

---

**文档版本**: v1.0  
**最后更新**: 2026-03-06 12:05 CST
