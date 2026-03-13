# 小红书自动化环境变量
export XHS_TOOLKIT_DIR=/root/.openclaw/workspace/skills/openclaw-xhs/xhs-toolkit
export XHS_DATA_DIR=/root/.openclaw/credentials

# Chromium 路径 (Playwright安装)
export CHROME_BIN=/root/.cache/ms-playwright/chromium-1208/chrome-linux64/chrome
export CHROMIUM_PATH=/root/.cache/ms-playwright/chromium-1208/chrome-linux64/chrome

# 图片生成API配置
export IMAGE_API_KEY=${OPENROUTER_API_KEY:-}
export IMAGE_BASE_URL=https://openrouter.ai/api/v1
export IMAGE_MODEL=google/gemini-2.0-flash-exp:free

# 添加到PATH
export PATH="/root/.local/bin:$PATH"

echo "✅ xhs-toolkit 环境变量已配置"
echo "Chromium路径: $CHROME_BIN"
