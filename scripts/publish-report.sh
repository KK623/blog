#!/bin/bash
# 发布流程 - 强制检查，失败立即补做，通过后再继续
# 用法: ./publish-report.sh <类型> <日期> 
# 例如: ./publish-report.sh llm 2026-03-13

set -e  # 任何错误立即退出

TYPE=$1
DATE=$2
MAX_RETRY=3

if [ -z "$TYPE" ] || [ -z "$DATE" ]; then
    echo "错误: 缺少参数"
    echo "用法: ./publish-report.sh <llm|cvnn> <YYYY-MM-DD>"
    exit 1
fi

echo "========================================"
echo "发布流程: ${TYPE} ${DATE}"
echo "========================================"
echo ""

# 步骤1: 生成报告文件
retry_count=0
while [ $retry_count -lt $MAX_RETRY ]; do
    echo "[步骤1/7] 检查报告文件..."
    if [ -f "/root/.openclaw/workspace/memory/${TYPE}-research-${DATE}.md" ] && \
       [ -f "/root/.openclaw/workspace/blog/posts/${DATE//-//}/${TYPE}-research-${DATE}.html" ]; then
        echo "✅ 报告文件已生成"
        break
    else
        echo "❌ 报告文件不存在，需要补做"
        # 这里应该调用报告生成命令，或者退出让用户处理
        echo "请先生成报告文件，然后重新运行此脚本"
        exit 1
    fi
    retry_count=$((retry_count + 1))
done
echo ""

# 步骤2: 更新首页链接
retry_count=0
while [ $retry_count -lt $MAX_RETRY ]; do
    echo "[步骤2/7] 检查首页链接..."
    if grep -q "${DATE}" /root/.openclaw/workspace/blog/index.html; then
        echo "✅ 首页链接已更新"
        break
    else
        echo "❌ 首页未更新 ${DATE} 链接，正在补做..."
        # 这里应该调用更新首页的代码
        # 如果手动更新，请编辑 index.html 添加链接
        echo "请手动更新 index.html 添加 ${DATE} 链接，然后重新运行"
        exit 1
    fi
    retry_count=$((retry_count + 1))
done
echo ""

# 步骤3: 更新博客页面链接
retry_count=0
while [ $retry_count -lt $MAX_RETRY ]; do
    echo "[步骤3/7] 检查博客页面链接..."
    if grep -q "${DATE}" /root/.openclaw/workspace/blog/posts/index.html; then
        echo "✅ 博客页面链接已更新"
        break
    else
        echo "❌ 博客页面未更新 ${DATE} 链接，正在补做..."
        echo "请手动更新 posts/index.html 添加 ${DATE} 链接，然后重新运行"
        exit 1
    fi
    retry_count=$((retry_count + 1))
done
echo ""

# 步骤4: 推送GitHub
retry_count=0
while [ $retry_count -lt $MAX_RETRY ]; do
    echo "[步骤4/7] 推送GitHub..."
    cd /root/.openclaw/workspace/blog
    git add -A
    git commit -m "发布 ${TYPE} Research Daily ${DATE}" || true
    if git push origin main; then
        echo "✅ GitHub推送完成"
        break
    else
        echo "❌ GitHub推送失败，重试中..."
        sleep 5
    fi
    retry_count=$((retry_count + 1))
done

if [ $retry_count -eq $MAX_RETRY ]; then
    echo "错误: GitHub推送失败 ${MAX_RETRY} 次"
    exit 1
fi
echo ""

# 步骤5: 等待部署并验证报告可访问
retry_count=0
while [ $retry_count -lt $MAX_RETRY ]; do
    echo "[步骤5/7] 等待GitHub Pages部署(60秒)..."
    sleep 60
    
    URL="https://kk623.github.io/blog/posts/${DATE//-//}/${TYPE}-research-${DATE}.html"
    echo "验证报告URL: ${URL}"
    
    STATUS=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
    if [ "$STATUS" == "200" ]; then
        echo "✅ 报告页面 200 OK"
        break
    else
        echo "❌ 报告URL返回 ${STATUS}，等待后重试..."
    fi
    retry_count=$((retry_count + 1))
done

if [ $retry_count -eq $MAX_RETRY ]; then
    echo "错误: 报告页面无法访问 ${MAX_RETRY} 次"
    exit 1
fi
echo ""

# 步骤6: 验证首页可访问
retry_count=0
while [ $retry_count -lt $MAX_RETRY ]; do
    echo "[步骤6/7] 验证首页..."
    HOME_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "https://kk623.github.io/blog/")
    if [ "$HOME_STATUS" != "200" ]; then
        echo "❌ 首页返回 ${HOME_STATUS}，重试中..."
        retry_count=$((retry_count + 1))
        sleep 10
        continue
    fi
    
    # 验证首页包含新文章
    if curl -s "https://kk623.github.io/blog/" | grep -q "${DATE}"; then
        echo "✅ 首页已更新并显示新文章"
        break
    else
        echo "❌ 首页未显示 ${DATE} 文章，等待后重试..."
    fi
    retry_count=$((retry_count + 1))
    sleep 10
done

if [ $retry_count -eq $MAX_RETRY ]; then
    echo "错误: 首页验证失败 ${MAX_RETRY} 次"
    exit 1
fi
echo ""

# 步骤7: 验证博客页面可访问
retry_count=0
while [ $retry_count -lt $MAX_RETRY ]; do
    echo "[步骤7/7] 验证博客页面..."
    POSTS_STATUS=$(curl -s -o /dev/null -w "%{http_code}" "https://kk623.github.io/blog/posts/")
    if [ "$POSTS_STATUS" != "200" ]; then
        echo "❌ 博客页面返回 ${POSTS_STATUS}，重试中..."
        retry_count=$((retry_count + 1))
        sleep 10
        continue
    fi
    
    # 验证博客页面包含新文章
    if curl -s "https://kk623.github.io/blog/posts/" | grep -q "${DATE}"; then
        echo "✅ 博客页面已更新并显示新文章"
        break
    else
        echo "❌ 博客页面未显示 ${DATE} 文章，等待后重试..."
    fi
    retry_count=$((retry_count + 1))
    sleep 10
done

if [ $retry_count -eq $MAX_RETRY ]; then
    echo "错误: 博客页面验证失败 ${MAX_RETRY} 次"
    exit 1
fi
echo ""

echo "========================================"
echo "✅ 所有步骤完成，可以发送飞书通知"
echo "========================================"
echo ""
echo "飞书通知内容模板:"
echo "📊 ${DATE} ${TYPE^^} Research Daily 已发布"
echo ""
echo "🔗 https://kk623.github.io/blog/posts/${DATE//-//}/${TYPE}-research-${DATE}.html"
echo "✅ 已更新: 首页 + 博客页面"
echo "✅ 已验证: GitHub Pages 200 OK"

