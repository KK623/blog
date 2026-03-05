=== 博客链接检查报告 ===
检查时间: Thu Mar  5 2026

========================================
📊 总体统计
========================================
检查文件数: 22
总链接数: 约150+
失效链接数: 13
正常链接: 约137+

========================================
📄 各文件链接统计
========================================

| 文件 | 链接总数 | 失效链接 |
|------|----------|----------|
| 02/llm-research.html | 0 | 0 |
| 03/cvnn-research-2026-03-03.html | 5 | 0 |
| 03/llm-quantization-techniques.html | 9 | 0 |
| 03/llm-research-2026-03-03.html | 6 | 0 |
| 03/llm-research-classic-before-2026-02.html | 5 | 0 |
| 03/pquant-analysis.html | 5 | 0 |
| 04/china-mobile-mwc-2026-report.html | 7 | 1 |
| 04/cvnn-research-2026-03-04.html | 8 | 0 |
| 04/huawei-mwc-2026-report.html | 13 | 1 |
| 04/ibm-mwc-2026-report.html | 8 | 0 |
| 04/kt-mwc-2026-report.html | 7 | 0 |
| 04/llm-research-2026-03-04.html | 6 | 0 |
| 04/microsoft-mwc-2026-report.html | 16 | 3 |
| 04/nvidia-blackwell-vs-rubin.html | 2 | 0 |
| 04/zte-mwc-2026-report.html | 11 | 1 |
| 05/cvnn-research-2026-03-05.html | 7 | 0 |
| 05/eulerformer-deep-analysis.html | 7 | 1 |
| 05/eulernet-deep-analysis.html | 6 | 1 |
| 05/llm-research-2026-03-05.html | 7 | 0 |
| 05/pi-quant-deep-analysis.html | 6 | 1 |
| 05/rfm-deep-analysis.html | 8 | 2 |
| 05/rucaibox-complex-networks-comparison.html | 6 | 0 |
| 05/shanghai-travel-miniprogram-design.html | 6 | 1 |

========================================
❌ 失效链接详情
========================================

**04/china-mobile-mwc-2026-report.html (1个失效)**
- https://www.telecoms.com/partner-content/mwc-2026-china-mobile-evp-li-huidi-an-l4-powering-the-iq-era
  状态: 403 (禁止访问)

**04/huawei-mwc-2026-report.html (1个失效)**
- https://www.telecoms.com/5g-6g/huawei-launches-u6ghz-kit-to-prepare-telcos-for-ai-and-6g
  状态: 403 (禁止访问)

**04/microsoft-mwc-2026-report.html (3个失效)**
- https://finance.yahoo.com/news/mwc-2026-amdocs-collaborates-microsoft-210500371.html
  状态: 429 (请求过多)
- https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/foundry-iq-unlocking-ubiquitous-knowledge-for-agents/4470812
  状态: 403 (禁止访问)
- https://techcommunity.microsoft.com/blog/windows-itpro-blog/microsoft-and-ericsson-advance-enterprise-mobility-with-windows-11-and-surface-5/4494680
  状态: 403 (禁止访问)

**04/zte-mwc-2026-report.html (1个失效)**
- https://www.lightreading.com/digital-transformation/zte-showcases-full-stack-ai-innovations-at-mwc-barcelona-2026-creating-an-intelligent-future
  状态: 403 (禁止访问)

**05/eulerformer-deep-analysis.html (1个失效)**
- https://doi.org/10.1145/3626772.3657805
  状态: 403 (禁止访问)

**05/eulernet-deep-analysis.html (1个失效)**
- https://doi.org/10.1145/3539618.3591681
  状态: 403 (禁止访问)

**05/pi-quant-deep-analysis.html (1个失效)**
- https://dl.acm.org/doi/10.1145/3637528.3671740
  状态: 403 (禁止访问)

**05/rfm-deep-analysis.html (2个失效)**
- https://dl.acm.org/doi/10.1145/3637528.3671740
  状态: 403 (禁止访问)
- https://doi.org/10.1145/3637528.3671740
  状态: 403 (禁止访问)

**05/shanghai-travel-miniprogram-design.html (1个失效)**
- https://developers.weixin.qq.com/wxcloud/basis/getting-started.html
  状态: 404 (页面不存在)

========================================
🔧 失效原因分析及修复建议
========================================

**类型1: 403 禁止访问 (11个链接)**
影响文件:
- 04/china-mobile-mwc-2026-report.html
- 04/huawei-mwc-2026-report.html
- 04/microsoft-mwc-2026-report.html
- 04/zte-mwc-2026-report.html
- 05/eulerformer-deep-analysis.html
- 05/eulernet-deep-analysis.html
- 05/pi-quant-deep-analysis.html
- 05/rfm-deep-analysis.html

原因:
- 网站有反爬虫机制，阻止了自动化访问
- 部分网站(如telecoms.com、lightreading.com、techcommunity.microsoft.com)需要特定请求头或Cookie
- 学术链接(doi.org、dl.acm.org)可能有访问限制

建议修复方案:
1. **手动验证**: 在浏览器中手动打开这些链接确认是否可访问
2. **添加备用链接**: 为学术文章寻找arXiv预印本或其他开放获取版本
3. **更新链接**: 查找文章是否有新的URL或替代来源
4. **添加说明**: 对于403的链接，在页面上添加说明"可能需要登录访问"

**类型2: 404 页面不存在 (1个链接)**
影响文件:
- 05/shanghai-travel-miniprogram-design.html

失效链接:
- https://developers.weixin.qq.com/wxcloud/basis/getting-started.html

原因:
- 微信云开发文档页面已被移除或URL已变更

建议修复方案:
1. 查找微信云开发文档的新地址
2. 可能的替代URL: https://developers.weixin.qq.com/miniprogram/dev/wxcloud/basis/getting-started.html
3. 或更新为微信官方文档主页: https://developers.weixin.qq.com/miniprogram/dev/framework/

**类型3: 429 请求过多 (1个链接)**
影响文件:
- 04/microsoft-mwc-2026-report.html

失效链接:
- https://finance.yahoo.com/news/mwc-2026-amdocs-collaborates-microsoft-210500371.html

原因:
- Yahoo Finance有严格的速率限制

建议修复方案:
1. 手动验证链接是否有效
2. 寻找新闻的替代来源或存档版本
3. 考虑使用archive.org的存档链接

========================================
✅ 内部链接检查结果
========================================
所有内部链接(/blog/开头)检查完毕:
- 未发现失效的内部链接
- 所有引用的本地文件均存在

========================================
📋 修复优先级建议
========================================

**高优先级 (立即修复):**
1. 05/shanghai-travel-miniprogram-design.html - 微信文档404错误

**中优先级 (建议修复):**
1. 04/microsoft-mwc-2026-report.html - 3个失效链接
2. 05/rfm-deep-analysis.html - 2个失效链接

**低优先级 (手动验证后决定):**
1. 其他403错误的学术链接 - 可能是访问限制而非真正失效

========================================
📝 备注
========================================
- 大部分失效链接返回403状态码，这可能是网站的反爬虫机制导致的误判
- 建议在浏览器中手动验证这些链接的实际可访问性
- 学术文章链接(doi.org、dl.acm.org)通常需要订阅才能访问全文，但链接本身是正确的
