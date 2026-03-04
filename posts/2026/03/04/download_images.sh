#!/bin/bash
# MWC 2026 图片下载脚本
# 用法: chmod +x download_images.sh && ./download_images.sh

echo "=== MWC 2026 图片下载助手 ==="
echo ""

# 创建目录
mkdir -p images/huawei images/zte

echo "请手动下载以下图片并保存到对应目录:"
echo ""

# 华为图片
echo "【华为图片】保存到 images/huawei/"
echo "1. U6GHz AAU 设备图"
echo "   来源: https://carrier.huawei.com/en/minisite/events/mwc2026/"
echo "   保存为: images/huawei/u6ghz-aau.jpg"
echo ""
echo "2. Atlas 950 SuperPoD"
echo "   来源: https://www.huawei.com/en/news/2026/3/mwc-superpod-ai"
echo "   保存为: images/huawei/atlas-950.jpg"
echo ""
echo "3. 华为展台照片"
echo "   来源: Google 搜索 'Huawei MWC 2026 Barcelona'"
echo "   保存为: images/huawei/booth.jpg"
echo ""

# 中兴图片
echo "【中兴图片】保存到 images/zte/"
echo "4. GigaMIMO 天线阵列"
echo "   来源: https://www.rcrwireless.com/20260228/6g/zte-6g-strategy-gigamimo"
echo "   保存为: images/zte/gigamimo.jpg"
echo ""
echo "5. SuperPOD 设备"
echo "   来源: https://www.zte.com.cn/global/about/news/"
echo "   保存为: images/zte/superpod.jpg"
echo ""
echo "6. nubia Neo 5 GT"
echo "   来源: https://www.zte.com.cn/global/about/news/nubia-Neo-5-Series..."
echo "   保存为: images/zte/nubia-neo5.jpg"
echo ""

echo "=== 下载完成后 ==="
echo "1. 把图片放到对应目录"
echo "2. 运行: git add images/ && git commit -m '添加 MWC 图片' && git push"
echo "3. 告诉我，我帮您更新 HTML 引用"
