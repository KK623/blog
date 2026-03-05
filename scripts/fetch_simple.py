#!/usr/bin/env python3
"""
Simple arXiv Image Fetcher - 简单版
直接从 ar5iv.org HTML 提取图片

Usage: python3 fetch_simple.py <arxiv_id>
Example: python3 fetch_simple.py 2602.22592
"""

import sys
import requests
import re
from pathlib import Path

def fetch_images(arxiv_id, output_dir="."):
    """从 ar5iv.org 获取论文图片"""
    
    # 获取 HTML
    url = f"https://ar5iv.org/html/{arxiv_id}"
    print(f"Fetching {url}...")
    
    response = requests.get(url, timeout=30)
    if response.status_code != 200:
        print(f"Failed: {response.status_code}")
        return []
    
    html = response.text
    
    # 提取标题
    title_match = re.search(r'<title>([^<]+)</title>', html)
    title = title_match.group(1) if title_match else arxiv_id
    print(f"Title: {title}")
    
    # 提取图片 (arxiv.org 的 PDF/图片链接)
    img_patterns = [
        r'src="(https?://arxiv\.org/[^"]+\.(?:png|jpg|jpeg|svg))"',
        r'src="(https?://[^"]+/(?:figure[0-9]+|fig[0-9]+)[^"]*\.(?:png|jpg|jpeg|svg))"',
    ]
    
    img_urls = set()
    for pattern in img_patterns:
        img_urls.update(re.findall(pattern, html))
    
    # 也提取 base64 图片
    base64_imgs = re.findall(r'data:image/([^;]+);base64,([A-Za-z0-9+/=]+)', html)
    
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    downloaded = []
    
    # 下载 URL 图片
    for i, img_url in enumerate(list(img_urls)[:5]):  # 最多5张
        try:
            resp = requests.get(img_url, timeout=20)
            if resp.status_code == 200:
                # 猜扩展名
                ext = 'png'
                if 'jpeg' in img_url or 'jpg' in img_url:
                    ext = 'jpg'
                elif 'svg' in img_url:
                    ext = 'svg'
                
                filename = Path(output_dir) / f"{arxiv_id}_fig{i}.{ext}"
                with open(filename, 'wb') as f:
                    f.write(resp.content)
                print(f"✓ Saved: {filename.name}")
                downloaded.append(filename)
        except Exception as e:
            print(f"✗ Failed: {img_url[:50]}...")
    
    # 处理 base64 图片
    for i, (fmt, data) in enumerate(base64_imgs[:3]):
        import base64
        try:
            filename = Path(output_dir) / f"{arxiv_id}_base64_{i}.{fmt}"
            with open(filename, 'wb') as f:
                f.write(base64.b64decode(data))
            print(f"✓ Saved base64: {filename.name}")
            downloaded.append(filename)
        except:
            pass
    
    return downloaded

if __name__ == "__main__":
    arxiv_id = sys.argv[1] if len(sys.argv) > 1 else "2602.22592"
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "."
    
    fetch_images(arxiv_id, output_dir)
