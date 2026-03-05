#!/usr/bin/env python3
"""
arXiv Paper Image Extractor
自动从 arXiv 论文提取图片

Usage:
    python3 fetch_arxiv_images.py <arxiv_id> [output_dir]
    Example: python3 fetch_arxiv_images.py 2602.22592 ./images
"""

import os
import sys
import requests
import subprocess
from pathlib import Path

def download_pdf(arxiv_id, output_dir):
    """下载 arXiv PDF"""
    url = f"https://arxiv.org/pdf/{arxiv_id}.pdf"
    pdf_path = Path(output_dir) / f"{arxiv_id}.pdf"
    
    print(f"Downloading PDF from {url}...")
    response = requests.get(url, timeout=60)
    
    if response.status_code == 200:
        with open(pdf_path, 'wb') as f:
            f.write(response.content)
        print(f"Saved to {pdf_path}")
        return pdf_path
    else:
        print(f"Failed to download: {response.status_code}")
        return None

def extract_images_latex(pdf_path, output_dir):
    """使用 pdfimages 提取图片 (需要 ImageMagick)"""
    arxiv_id = Path(pdf_path).stem
    cmd = [
        "pdfimages", "-list", str(pdf_path)
    ]
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        lines = result.stdout.strip().split('\n')
        
        images = []
        for line in lines[2:]:  # Skip header
            if line.strip():
                parts = line.split()
                if len(parts) >= 2:
                    img_type = parts[1]
                    if img_type in ['jpeg', 'png']:
                        images.append(parts[0])
        
        if images:
            # Extract images
            cmd = [
                "pdfimages", "-png", "-nodir", str(pdf_path), 
                str(Path(output_dir) / arxiv_id)
            ]
            subprocess.run(cmd, capture_output=True, timeout=60)
            print(f"Extracted {len(images)} images")
            
        return images
    except Exception as e:
        print(f"Error extracting images: {e}")
        return []

def get_paper_info(arxiv_id):
    """获取论文基本信息"""
    # Try ar5iv.org for HTML
    url = f"https://ar5iv.org/html/{arxiv_id}"
    response = requests.get(url, timeout=30)
    
    if response.status_code == 200:
        # Extract title
        import re
        title_match = re.search(r'<title>([^<]+)</title>', response.text)
        title = title_match.group(1) if title_match else "Unknown"
        
        # Extract image URLs
        img_urls = re.findall(r'src="(https?://[^"]+\.(?:png|jpg|jpeg))"', response.text)
        
        return {
            'title': title,
            'image_urls': img_urls[:5]  # Limit to 5 images
        }
    
    return None

def download_images_from_urls(urls, output_dir):
    """从 URLs 下载图片"""
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    for i, url in enumerate(urls):
        try:
            response = requests.get(url, timeout=30)
            if response.status_code == 200:
                ext = url.split('.')[-1].split('?')[0]
                ext = ext if ext in ['png', 'jpg', 'jpeg'] else 'png'
                filename = Path(output_dir) / f"image_{i}.{ext}"
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"Downloaded: {filename}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    arxiv_id = sys.argv[1].strip()
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "./arxiv_images"
    
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Method 1: Try ar5iv.org HTML (for extracting image URLs)
    print(f"\n=== Fetching paper: {arxiv_id} ===")
    info = get_paper_info(arxiv_id)
    
    if info and info['image_urls']:
        print(f"Title: {info['title']}")
        print(f"Found {len(info['image_urls'])} images from HTML")
        download_images_from_urls(info['image_urls'], output_dir)
    else:
        print("No images from HTML, trying PDF...")
    
    # Method 2: Download PDF and try to extract
    pdf_path = download_pdf(arxiv_id, output_dir)
    if pdf_path:
        images = extract_images_latex(pdf_path, output_dir)
        if images:
            print(f"Extracted {len(images)} images from PDF")
    
    print(f"\nDone! Images saved to: {output_dir}")
    print(os.listdir(output_dir))

if __name__ == "__main__":
    main()
