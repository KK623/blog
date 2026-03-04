#!/usr/bin/env python3
"""
Extract all content and images from a webpage
"""

import os
import sys
import argparse
from extract import WebExtractor
from download_images import ImageDownloader

def main():
    parser = argparse.ArgumentParser(description='Extract all content and images from webpage')
    parser.add_argument('url', help='Webpage URL')
    parser.add_argument('--output-dir', '-o', default='./output', help='Output directory')
    parser.add_argument('--method', default='auto', help='Extraction method')
    parser.add_argument('--max-images', type=int, default=20, help='Maximum images to download')
    
    args = parser.parse_args()
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    print(f"🌐 Extracting from: {args.url}")
    print(f"📁 Output directory: {args.output_dir}\n")
    
    # Extract content
    print("=" * 50)
    print("📄 Extracting content...")
    print("=" * 50)
    
    extractor = WebExtractor()
    try:
        content = extractor.extract(args.url, args.method)
        
        # Save content
        content_file = os.path.join(args.output_dir, 'content.md')
        with open(content_file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"✓ Content saved to: {content_file}\n")
        
    except Exception as e:
        print(f"✗ Content extraction failed: {e}\n")
    
    # Download images
    print("=" * 50)
    print("🖼️  Downloading images...")
    print("=" * 50)
    
    images_dir = os.path.join(args.output_dir, 'images')
    downloader = ImageDownloader(min_size=5000)  # Skip small images
    
    try:
        count = downloader.download_from_url(
            args.url,
            output_dir=images_dir,
            max_images=args.max_images
        )
        print(f"✓ Downloaded {count} images to: {images_dir}\n")
        
    except Exception as e:
        print(f"✗ Image download failed: {e}\n")
    
    print("=" * 50)
    print(f"✅ Done! Check: {args.output_dir}")
    print("=" * 50)

if __name__ == '__main__':
    main()
