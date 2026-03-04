#!/usr/bin/env python3
"""
Image Downloader from Webpage
Supports multiple extraction methods and concurrent downloads
"""

import os
import sys
import requests
import argparse
from urllib.parse import urljoin, urlparse
from typing import List, Set
import re

class ImageDownloader:
    """Download images from webpages"""
    
    def __init__(self, timeout: int = 30, min_size: int = 0):
        self.timeout = timeout
        self.min_size = min_size  # Minimum file size in bytes
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "image/webp,image/apng,image/*,*/*;q=0.8"
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def extract_image_urls(self, page_url: str, use_js: bool = False) -> Set[str]:
        """
        Extract image URLs from webpage
        
        Args:
            page_url: URL of the webpage
            use_js: Use Scrapling for JavaScript-rendered content
        
        Returns:
            Set of image URLs
        """
        if use_js:
            return self._extract_with_scrapling(page_url)
        else:
            return self._extract_with_bs4(page_url)
    
    def _extract_with_bs4(self, page_url: str) -> Set[str]:
        """Extract using BeautifulSoup"""
        from bs4 import BeautifulSoup
        
        response = self.session.get(page_url, timeout=self.timeout)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'lxml')
        images = set()
        
        # Find all img tags
        for img in soup.find_all('img'):
            src = img.get('src') or img.get('data-src') or img.get('data-original')
            if src:
                full_url = urljoin(page_url, src)
                images.add(full_url)
        
        # Find background images in style attributes
        style_pattern = re.compile(r'background-image:\s*url\([\'"]?([^\'")]+)[\'"]?\)')
        for tag in soup.find_all(style=True):
            match = style_pattern.search(tag['style'])
            if match:
                full_url = urljoin(page_url, match.group(1))
                images.add(full_url)
        
        return images
    
    def _extract_with_scrapling(self, page_url: str) -> Set[str]:
        """Extract using Scrapling (for JS-rendered content)"""
        try:
            from scrapling import Fetcher
            
            fetcher = Fetcher()
            page = fetcher.get(page_url)
            
            images = set()
            for img in page.find_all('img'):
                src = img.get('src') or img.get('data-src')
                if src:
                    full_url = urljoin(page_url, src)
                    images.add(full_url)
            
            return images
            
        except ImportError:
            print("Scrapling not installed, falling back to BeautifulSoup", file=sys.stderr)
            return self._extract_with_bs4(page_url)
    
    def download_image(self, url: str, output_dir: str, filename: Optional[str] = None) -> bool:
        """
        Download single image
        
        Args:
            url: Image URL
            output_dir: Directory to save image
            filename: Optional custom filename
        
        Returns:
            True if successful
        """
        try:
            # Get referer from URL
            parsed = urlparse(url)
            referer = f"{parsed.scheme}://{parsed.netloc}/"
            
            headers = {
                **self.headers,
                "Referer": referer
            }
            
            response = self.session.get(url, headers=headers, timeout=self.timeout, stream=True)
            response.raise_for_status()
            
            # Check content type
            content_type = response.headers.get('content-type', '')
            if not content_type.startswith('image/'):
                return False
            
            # Check content length
            content_length = int(response.headers.get('content-length', 0))
            if self.min_size > 0 and content_length < self.min_size:
                return False
            
            # Determine filename
            if not filename:
                # Extract from URL
                path = urlparse(url).path
                filename = os.path.basename(path) or 'image.jpg'
                
                # Add extension if missing
                if not os.path.splitext(filename)[1]:
                    ext = self._get_extension_from_content_type(content_type)
                    filename += ext
            
            # Save file
            output_path = os.path.join(output_dir, filename)
            
            # Handle duplicates
            counter = 1
            base, ext = os.path.splitext(output_path)
            while os.path.exists(output_path):
                output_path = f"{base}_{counter}{ext}"
                counter += 1
            
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            
            print(f"✓ Downloaded: {filename} ({content_length} bytes)", file=sys.stderr)
            return True
            
        except Exception as e:
            print(f"✗ Failed: {url} - {e}", file=sys.stderr)
            return False
    
    def _get_extension_from_content_type(self, content_type: str) -> str:
        """Get file extension from content type"""
        mapping = {
            'image/jpeg': '.jpg',
            'image/jpg': '.jpg',
            'image/png': '.png',
            'image/gif': '.gif',
            'image/webp': '.webp',
            'image/svg+xml': '.svg',
            'image/bmp': '.bmp',
        }
        return mapping.get(content_type, '.jpg')
    
    def download_from_url(self, page_url: str, output_dir: str = "./images", 
                         use_js: bool = False, max_images: int = 0) -> int:
        """
        Download all images from webpage
        
        Args:
            page_url: URL of the webpage
            output_dir: Directory to save images
            use_js: Use Scrapling for JS-rendered content
            max_images: Maximum images to download (0 = unlimited)
        
        Returns:
            Number of successfully downloaded images
        """
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        
        print(f"Extracting images from {page_url}...", file=sys.stderr)
        image_urls = self.extract_image_urls(page_url, use_js)
        
        print(f"Found {len(image_urls)} images", file=sys.stderr)
        
        if max_images > 0:
            image_urls = list(image_urls)[:max_images]
            print(f"Limited to {max_images} images", file=sys.stderr)
        
        # Download images
        success_count = 0
        for i, url in enumerate(image_urls, 1):
            print(f"[{i}/{len(image_urls)}] Downloading...", file=sys.stderr)
            if self.download_image(url, output_dir):
                success_count += 1
        
        print(f"\n✓ Downloaded {success_count}/{len(image_urls)} images to {output_dir}", file=sys.stderr)
        return success_count


def main():
    parser = argparse.ArgumentParser(description='Download images from webpage')
    parser.add_argument('url', help='Webpage URL')
    parser.add_argument('--output', '-o', default='./images', help='Output directory')
    parser.add_argument('--min-size', type=int, default=0, help='Minimum file size in bytes')
    parser.add_argument('--max-images', type=int, default=0, help='Maximum images to download')
    parser.add_argument('--use-js', action='store_true', help='Use Scrapling for JS-rendered content')
    parser.add_argument('--timeout', type=int, default=30, help='Request timeout')
    
    args = parser.parse_args()
    
    downloader = ImageDownloader(timeout=args.timeout, min_size=args.min_size)
    
    try:
        downloader.download_from_url(
            args.url, 
            output_dir=args.output,
            use_js=args.use_js,
            max_images=args.max_images
        )
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
