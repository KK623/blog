#!/bin/bash
# 强制验证脚本 - 任何报告发布后必须运行
# 用法: ./verify-report.sh <报告类型> <日期>
# 例如: ./verify-report.sh llm 2026-03-13

REPORT_TYPE=$1
DATE=$2
URL="https://kk623.github.io/blog/posts/${DATE//-//}/${REPORT_TYPE}-research-${DATE}.html"
LOCAL_PATH="/root/.openclaw/workspace/blog/posts/${DATE//-//}/${REPORT_TYPE}-research-${DATE}.html"

echo "=== 强制验证: ${REPORT_TYPE} ${DATE} ==="

# 1. 本地文件检查
echo "[1/3] 检查本地文件..."
if [ -f "$LOCAL_PATH" ]; then
    echo "✅ 本地文件存在: $LOCAL_PATH"
else
    echo "❌ 本地文件不存在！"
    exit 1
fi

# 2. GitHub推送检查
echo "[2/3] 检查GitHub Pages (等待30秒部署)..."
sleep 30

# 3. URL可访问检查
echo "[3/3] 验证URL可访问..."
STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
if [ "$STATUS" == "200" ]; then
    echo "✅ URL 200 OK: $URL"
    echo "✅ 验证通过，可以发送通知"
    exit 0
else
    echo "❌ URL返回 $STATUS"
    echo "❌ 验证失败！不能发送通知"
    exit 1
fi
