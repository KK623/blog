#!/usr/bin/env python3
"""
arXiv Paper Image Fetcher - 最终版
多源获取论文图片

Sources:
1. ar5iv.org HTML
2. paperswithcode.com
3. 从 PDF 提取（需要外部工具）
"""

import os
import sys
import requests
import re
import base64
from pathlib import Path
import json

def log(msg):
    print(f"[INFO] {msg}")

def fetch_from_ar5iv(arxiv_id, output_dir):
    """从 ar5iv.org 获取图片"""
    images = []
    url = f"https://ar5iv.org/html/{arxiv_id}"
    
    log(f"Fetching ar5iv: {url}")
    try:
        resp = requests.get(url, timeout=30)
        if resp.status_code != 200:
            return images
        
        html = resp.text
        
        # 找图片 (相对路径)
        patterns = [
            rf'src="(/{arxiv_id}/[^"]+\.(png|jpg|jpeg|svg))"',
            r'src="(figures/[^"]+\.(png|jpg|jpeg|svg))"',
        ]
        
        for pattern in patterns:
            for match in re.findall(pattern, html):
                path = match[0] if isinstance(match, tuple) else match
                img_url = f"https://ar5iv.org{path}"
                
                try:
                    r = requests.get(img_url, timeout=15)
                    if r.status_code == 200 and len(r.content) > 500:
                        ext = path.split('.')[-1][:4]
                        if ext not in ['png','jpg','jpeg']: ext = 'png'
                        f = Path(output_dir) / f"{arxiv_id}_ar5iv_{len(images)}.{ext}"
                        f.write_bytes(r.content)
                        log(f"✓ {f.name} ({len(r.content)}b)")
                        images.append(f)
                except: pass
        
        # base64
        for fmt,data in re.findall(r'data:image/([^;]+);base64,([A-Za-z0-9+/=]+)', html):
            try:
                f = Path(output_dir) / f"{arxiv_id}_b64.{fmt}"
                f.write_bytes(base64.b64decode(data))
                log(f"✓ base64: {f.name}")
                images.append(f)
            except: pass
                
    except Exception as e:
        log(f"ar5iv error: {e}")
    
    return images

def fetch_from_paperswithcode(arxiv_id, output_dir):
    """从 paperswithcode 获取论文图片"""
    images = []
    
    # 搜索论文
    url = f"https://www.paperswithcode.com/api/v1/papers/?arxiv_id={arxiv_id}"
    log(f"Fetching paperswithcode: {url}")
    
    try:
        resp = requests.get(url, timeout=20)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('results'):
                paper = data['results'][0]
                title = paper.get('title', '')
                
                # 获取论文页面获取图表
                page_url = f"https://www.paperswithcode.com/paper/{arxiv_id}"
                try:
                    page = requests.get(page_url, timeout=15).text
                    
                    # 找方法图、结果图等
                    img_patterns = [
                        r'src="(https://production-media.paperswithcode.com/[^"]+\.(?:png|jpg))"',
                    ]
                    
                    for pattern in img_patterns:
                        for match in re.findall(pattern, page):
                            try:
                                r = requests.get(match, timeout=15)
                                if r.status_code == 200 and len(r.content) > 1000:
                                    ext = match.split('.')[-1].split('?')[0][:3]
                                    if ext not in ['png','jpg']: ext = 'png'
                                    f = Path(output_dir) / f"{arxiv_id}_pwc_{len(images)}.{ext}"
                                    f.write_bytes(r.content)
                                    log(f"✓ {f.name} ({len(r.content)}b)")
                                    images.append(f)
                            except: pass
                except: pass
                    
    except Exception as e:
        log(f"paperswithcode error: {e}")
    
    return images

def fetch_from_github_readme(arxiv_id, output_dir):
    """从 GitHub README 获取图表"""
    images = []
    
    # 尝试常见模式
    gh_urls = [
        f"https://raw.githubusercontent.com/{arxiv_id.replace('.','')}/main/README.png",
    ]
    
    for url in gh_urls:
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200 and len(r.content) > 500:
                f = Path(output_dir) / f"{arxiv_id}_github.png"
                f.write_bytes(r.content)
                log(f"✓ GitHub: {f.name}")
                images.append(f)
        except: pass
    
    return images

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fetch_img.py <arxiv_id> [output_dir]")
        sys.exit(1)
    
    arxiv_id = sys.argv[1].strip()
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./images"
    
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    print("=" * 50)
    log(f"Paper: {arxiv_id}")
    print("=" * 50)
    
    all_images = []
    
    # 多源尝试
    all_images.extend(fetch_from_ar5iv(arxiv_id, output_dir))
    all_images.extend(fetch_from_paperswithcode(arxiv_id, output_dir))
    all_images.extend(fetch_from_github_readme(arxiv_id, output_dir))
    
    print("\n" + "=" * 50)
    log(f"Total: {len(all_images)} images")
    
    for f in sorted(Path(output_dir).glob(f"{arxiv_id}*")):
        if f.is_file() and f.stat().st_size > 500:
            log(f"  {f.name} ({f.stat().st_size}b)")
    
    print("=" * 50)
    
    return 0 if all_images else 1

if __name__ == "__main__":
    sys.exit(main())
