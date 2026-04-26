#!/bin/bash
DIR=/root/.openclaw/workspace/blog/posts/2026/04/27/images

# Compress images to <100KB
# 2604.21057 TRACES - pick img-031.png (154KB, needs compression)
convert "$DIR/2604.21057/img-031.png" -resize 800x600 -quality 85 "$DIR/traces-early-stopping.png" 2>/dev/null || cp "$DIR/2604.21057/img-031.png" "$DIR/traces-early-stopping.png"

# 2604.21335 Sub-Token Routing - pick img-004.png (122KB)
convert "$DIR/2604.21335/img-004.png" -resize 800x600 -quality 85 "$DIR/subtoken-routing.png" 2>/dev/null || cp "$DIR/2604.21335/img-004.png" "$DIR/subtoken-routing.png"

# 2604.21255 AgentEcho - pick img-014.jpg (157KB)
convert "$DIR/2604.21255/img-014.jpg" -resize 800x600 -quality 85 "$DIR/agentecho-distillation.jpg" 2>/dev/null || cp "$DIR/2604.21255/img-014.jpg" "$DIR/agentecho-distillation.jpg"

# 2601.20706 NPU dLLM - pick img-000.png (515KB, needs heavy compression)
convert "$DIR/2601.20706/img-000.png" -resize 800x600 -quality 75 "$DIR/npu-dllm.png" 2>/dev/null || cp "$DIR/2601.20706/img-000.png" "$DIR/npu-dllm.png"

# 2604.21816 has no images - we'll skip

ls -la $DIR/*.png $DIR/*.jpg 2>/dev/null
