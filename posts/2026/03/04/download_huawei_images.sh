#!/bin/bash
# 华为 MWC 2026 报告图片下载脚本
# 使用方法: bash download_huawei_images.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
IMAGE_DIR="${SCRIPT_DIR}/images/huawei"

echo "========================================"
echo "华为 MWC 2026 报告图片下载工具"
echo "========================================"
echo ""

# 创建图片目录
mkdir -p "${IMAGE_DIR}"
echo "✓ 图片目录: ${IMAGE_DIR}"
echo ""

# 图片列表
# 格式: 文件名|描述|建议来源
declare -a IMAGES=(
    "huawei-u6ghz-aau.jpg|Huawei U6GHz 256 TRX AAU|https://carrier.huawei.com/en/products/wireless-networks/"
    "huawei-u6ghz-smallcell.jpg|Huawei U6GHz Small Cell|https://carrier.huawei.com/en/products/wireless-networks/"
    "huawei-atlas-950.jpg|Atlas 950 SuperPoD|https://www.huawei.com/en/news/2026/3/mwc-superpod-ai"
    "huawei-taishan-950.jpg|TaiShan 950 SuperPoD|https://www.huawei.com/en/news/2026/3/mwc-superpod-ai"
    "huawei-booth-mwc26.jpg|Huawei MWC 2026 Booth Hall 1|https://www.huawei.com/en/news/2026/3/mwc-ai-centric-network"
    "huawei-li-peng-keynote.jpg|Li Peng Keynote MWC 2026|https://www.huawei.com/en/news/2026/3/mwc-ai-centric-network"
    "huawei-ai-centric-network.jpg|AI-Centric Network Architecture|https://www.huawei.com/en/news/2026/3/mwc-ai-centric-network"
    "huawei-agentic-core.jpg|Agentic Core Architecture|https://www.huawei.com/en/news/2026/3/mwc-ai-centric-network"
    "huawei-ubb-2025.jpg|UBB 2025 Release|https://carrier.huawei.com/en/products/fixed-network/"
    "huawei-ng-wan.jpg|NG WAN Architecture|https://carrier.huawei.com/en/products/fixed-network/"
)

echo "需要下载的图片列表:"
echo "========================================"
for img_info in "${IMAGES[@]}"; do
    IFS='|' read -r filename description source <<< "$img_info"
    echo "  - ${filename}"
    echo "    描述: ${description}"
    echo "    来源: ${source}"
    echo ""
done

echo "========================================"
echo "下载说明:"
echo "========================================"
echo "由于图片版权和网络限制，此脚本不直接下载图片。"
echo ""
echo "请按以下步骤操作:"
echo ""
echo "1. 访问华为官方网站获取图片:"
echo "   - MWC 2026 主页: https://carrier.huawei.com/en/minisite/events/mwc2026/"
echo "   - 产品图片: https://carrier.huawei.com/en/products/"
echo ""
echo "2. 或联系华为媒体部门获取授权图片:"
echo "   - media@huawei.com"
echo ""
echo "3. 将下载的图片保存到以下目录:"
echo "   ${IMAGE_DIR}"
echo ""
echo "4. 图片命名规范:"
echo "   - huawei-u6ghz-aau.jpg (U6GHz 宏站设备)"
echo "   - huawei-atlas-950.jpg (Atlas 950 SuperPoD)"
echo "   - huawei-booth-mwc26.jpg (展台照片)"
echo "   - 等等..."
echo ""
echo "5. 建议图片规格:"
echo "   - 格式: JPG 或 WebP"
echo "   - 宽度: 800-1200px"
echo "   - 大小: < 200KB"
echo ""
echo "========================================"
echo "当前图片目录内容:"
echo "========================================"
ls -la "${IMAGE_DIR}" 2>/dev/null || echo "(目录为空)"
echo ""
echo "完成!"
