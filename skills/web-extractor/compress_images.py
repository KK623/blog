#!/usr/bin/env python3
"""
Compress images to target size (<100KB default)
Usage: python3 compress_images.py <input_dir> [output_dir] [target_kb]
"""

import os
import sys
from PIL import Image
import glob

def compress_image(input_path, output_path, target_kb=100):
    """压缩单张图片到目标大小以下"""
    target_bytes = target_kb * 1024
    
    # 打开图片
    img = Image.open(input_path)
    
    # 转换为RGB（处理PNG透明通道）
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')
    
    # 初始质量
    quality = 95
    
    # 逐步降低质量直到满足大小要求
    while quality > 30:
        img.save(output_path, 'JPEG', quality=quality, optimize=True)
        
        file_size = os.path.getsize(output_path)
        if file_size <= target_bytes:
            print(f"✓ {os.path.basename(input_path)}: {file_size/1024:.1f}KB (quality={quality})")
            return True
        
        quality -= 5
    
    # 如果质量降低还不够，缩小尺寸
    width, height = img.size
    while quality > 20:
        # 缩小尺寸
        new_width = int(width * 0.9)
        new_height = int(height * 0.9)
        resized = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        resized.save(output_path, 'JPEG', quality=quality, optimize=True)
        
        file_size = os.path.getsize(output_path)
        if file_size <= target_bytes:
            print(f"✓ {os.path.basename(input_path)}: {file_size/1024:.1f}KB (resized {new_width}x{new_height}, quality={quality})")
            return True
        
        width, height = new_width, new_height
        quality -= 5
    
    print(f"⚠ {os.path.basename(input_path)}: 无法压缩到 {target_kb}KB 以下")
    return False

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 compress_images.py <input_dir> [output_dir] [target_kb]")
        print("Example: python3 compress_images.py ./images ./compressed 100")
        sys.exit(1)
    
    input_dir = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else input_dir + "_compressed"
    target_kb = int(sys.argv[3]) if len(sys.argv) > 3 else 100
    
    # 创建输出目录
    os.makedirs(output_dir, exist_ok=True)
    
    # 支持的图片格式
    extensions = ['*.jpg', '*.jpeg', '*.png', '*.webp', '*.gif', '*.bmp']
    
    total = 0
    success = 0
    
    for ext in extensions:
        for img_path in glob.glob(os.path.join(input_dir, ext)):
            total += 1
            filename = os.path.basename(img_path)
            name_without_ext = os.path.splitext(filename)[0]
            output_path = os.path.join(output_dir, name_without_ext + '.jpg')
            
            try:
                if compress_image(img_path, output_path, target_kb):
                    success += 1
            except Exception as e:
                print(f"✗ {filename}: 错误 - {e}")
    
    print(f"\n{'='*50}")
    print(f"总计: {total} 张图片")
    print(f"成功: {success} 张")
    print(f"输出目录: {output_dir}")
    print(f"{'='*50}")

if __name__ == "__main__":
    main()
