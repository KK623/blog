#!/usr/bin/env python3
"""
arXiv Paper Image Fetcher - 优化版
自动获取 arXiv 论文的原图

Features:
1. 从 ar5iv.org 获取论文 HTML 版（图片较全）
2. 从 arxiv.org 获取 PDF 并用 pdfimages 提取
3. 自动下载并保存到指定目录
"""

import os
import sys
import requests
import re
import subprocess
import base64
from pathlib import Path
from urllib.parse import urljoin

AR5IV_BASE = "https://ar5iv.org"
ARXIV_BASE = "https://arxiv.org"

def log(msg):
    print(f"[INFO] {msg}")

def fetch_from_ar5iv(arxiv_id, output_dir):
    """从 ar5iv.org 获取图片"""
    images = []
    
    # 获取 HTML 版本
    url = f"{AR5IV_BASE}/html/{arxiv_id}"
    log(f"Fetching ar5iv: {url}")
    
    try:
        resp = requests.get(url, timeout=30)
        if resp.status_code != 200:
            log(f"ar5iv failed: {resp.status_code}")
            return images
        
        html = resp.text
        
        # 提取所有图片 URL
        # 1. 相对路径图片
        img_patterns = [
            r'src="(/' + arxiv_id + r'/[^"]+\.(png|jpg|jpeg|svg))"',
            r'src="(figures/[^"]+\.(png|jpg|jpeg|svg))"',
        ]
        
        # 2. 绝对路径
        abs_patterns = [
            r'src="(https?://[^"]+\.(?:png|jpg|jpeg|svg|webp))"',
        ]
        
        img_urls = set()
        
        for pattern in img_patterns:
            for match in re.findall(pattern, html):
                if isinstance(match, tuple):
                    path = match[0]
                else:
                    path = match
                full_url = f"{AR5IV_BASE}{path}"
                img_urls.add(full_url)
        
        # 下载图片
        for i, img_url in enumerate(img_urls):
            try:
                resp = requests.get(img_url, timeout=20)
                if resp.status_code == 200:
                    # 猜扩展名
                    ext = img_url.split('.')[-1].split('?')[0][:4]
                    if ext not in ['png', 'jpg', 'jpeg', 'svg']:
                        ext = 'png'
                    
                    filename = Path(output_dir) / f"{arxiv_id}_ar5iv_{i}.{ext}"
                    with open(filename, 'wb') as f:
                        f.write(resp.content)
                    
                    size = len(resp.content)
                    if size > 500:  # 忽略太小的
                        log(f"✓ Downloaded: {filename.name} ({size} bytes)")
                        images.append(filename)
            except Exception as e:
                log(f"✗ Failed: {img_url[:50]}...")
        
        # 提取 base64 图片
        base64_pattern = r'data:image/([^;]+);base64,([A-Za-z0-9+/=]+)'
        for match in re.findall(base64_pattern, html):
            fmt, data = match
            try:
                filename = Path(output_dir) / f"{arxiv_id}_base64.{fmt}"
                with open(filename, 'wb') as f:
                    f.write(base64.b64decode(data))
                log(f"✓ Saved base64: {filename.name}")
                images.append(filename)
            except:
                pass
                
    except Exception as e:
        log(f"Error fetching ar5iv: {e}")
    
    return images

def fetch_from_pdf(arxiv_id, output_dir):
    """从 PDF 提取图片"""
    images = []
    
    # 下载 PDF
    pdf_url = f"{ARXIV_BASE}/pdf/{arxiv_id}.pdf"
    pdf_path = Path(output_dir) / f"{arxiv_id}.pdf"
    
    log(f"Downloading PDF: {pdf_url}")
    
    try:
        resp = requests.get(pdf_url, timeout=60)
        if resp.status_code == 200:
            with open(pdf_path, 'wb') as f:
                f.write(resp.content)
            log(f"Saved PDF: {pdf_path}")
            
            # 尝试用 pdfimages 提取
            try:
                result = subprocess.run(
                    ["pdfimages", "-list", str(pdf_path)],
                    stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30
                )
                result.stdout = result.stdout.decode('utf-8', errors='ignore')
                
                # 检查输出
                lines = result.stdout.strip().split('\n')
                image_count = 0
                for line in lines:
                    if 'jpeg' in line or 'png' in line:
                        image_count += 1
                
                if image_count > 0:
                    # 提取图片
                    subprocess.run(
                        ["pdfimages", "-png", "-nodir", str(pdf_path), 
                         str(Path(output_dir) / arxiv_id)],
                        stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120
                    )
                    
                    # 重命名文件
                    for f in Path(output_dir).glob(f"{arxiv_id}*"):
                        if f.suffix in ['.png', '.jpg']:
                            # 移动到输出目录
                            new_name = f"{arxiv_id}_pdf_{f.stem}{f.suffix}"
                            f.rename(Path(output_dir) / new_name)
                            log(f"✓ Extracted: {new_name}")
                            images.append(Path(output_dir) / new_name)
                            
            except FileNotFoundError:
                log("pdfimages not installed, skipping PDF extraction")
            except Exception as e:
                log(f"PDF extraction error: {e}")
                
    except Exception as e:
        log(f"PDF download failed: {e}")
    
    return images

def get_paper_title(arxiv_id):
    """获取论文标题"""
    try:
        url = f"{AR5IV_BASE}/html/{arxiv_id}"
        resp = requests.get(url, timeout=15)
        if resp.status_code == 200:
            match = re.search(r'<title>\s*\[?([^\]]+)\]?\s*([^<]+)</title>', resp.text)
            if match:
                return match.group(2).strip()
    except:
        pass
    return arxiv_id

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 fetch_arxiv_img.py <arxiv_id> [output_dir]")
        print("Example: python3 fetch_arxiv_img.py 2602.22592 ./images")
        sys.exit(1)
    
    arxiv_id = sys.argv[1].strip()
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./arxiv_images"
    
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    print("=" * 50)
    log(f"Paper: {arxiv_id}")
    log(f"Title: {get_paper_title(arxiv_id)}")
    log(f"Output: {output_dir}")
    print("=" * 50)
    
    all_images = []
    
    # 方法1: ar5iv.org
    log("\n[Method 1] Fetching from ar5iv.org...")
    images1 = fetch_from_ar5iv(arxiv_id, output_dir)
    all_images.extend(images1)
    log(f"Got {len(images1)} images from ar5iv")
    
    # 方法2: PDF extraction
    log("\n[Method 2] Extracting from PDF...")
    images2 = fetch_from_pdf(arxiv_id, output_dir)
    all_images.extend(images2)
    log(f"Got {len(images2)} images from PDF")
    
    # 统计
    print("\n" + "=" * 50)
    log(f"Total images: {len(all_images)}")
    
    # 列出所有图片
    for f in sorted(Path(output_dir).glob(f"{arxiv_id}*")):
        if f.is_file() and f.suffix in ['.png', '.jpg', '.jpeg', '.svg', '.pdf']:
            size = f.stat().st_size
            log(f"  {f.name} ({size} bytes)")
    
    print("=" * 50)
    
    return 0 if all_images else 1

if __name__ == "__main__":
    sys.exit(main())
