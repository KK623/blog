#!/usr/bin/env python3
"""
Web Content Extractor
Supports: markdown.new, defuddle.md, r.jina.ai, Scrapling fallback
"""

import requests
import sys
import argparse
from typing import Optional

class WebExtractor:
    """Extract web content using multiple fallback methods"""
    
    METHODS = [
        ("markdown.new", "https://markdown.new/{url}"),
        ("defuddle.md", "https://defuddle.md/{url}"),
        ("r.jina.ai", "https://r.jina.ai/http://{url}"),
    ]
    
    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
    
    def extract(self, url: str, method: str = "auto") -> str:
        """
        Extract content from URL
        
        Args:
            url: Target URL
            method: 'auto', 'markdown.new', 'defuddle.md', 'r.jina.ai', or 'scrapling'
        
        Returns:
            Extracted content as string
        """
        if method == "auto":
            return self._try_all_methods(url)
        elif method == "scrapling":
            return self._scrapling_extract(url)
        else:
            return self._extract_with_method(url, method)
    
    def _try_all_methods(self, url: str) -> str:
        """Try all methods in order until one succeeds"""
        # Ensure URL has protocol
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        for method_name, template in self.METHODS:
            try:
                print(f"Trying {method_name}...", file=sys.stderr)
                
                # Format URL for the service
                if method_name == "r.jina.ai":
                    # r.jina.ai needs URL without protocol
                    url_clean = url.replace('https://', '').replace('http://', '')
                    extract_url = template.format(url=url_clean)
                else:
                    extract_url = template.format(url=url)
                
                response = requests.get(
                    extract_url, 
                    headers=self.headers, 
                    timeout=self.timeout
                )
                
                if response.status_code == 200 and len(response.text) > 100:
                    print(f"✓ Success with {method_name}", file=sys.stderr)
                    return response.text
                    
            except Exception as e:
                print(f"✗ {method_name} failed: {e}", file=sys.stderr)
                continue
        
        # Fallback to Scrapling
        print("Trying Scrapling fallback...", file=sys.stderr)
        return self._scrapling_extract(url)
    
    def _extract_with_method(self, url: str, method: str) -> str:
        """Extract using specific method"""
        for method_name, template in self.METHODS:
            if method_name == method:
                if method_name == "r.jina.ai":
                    url_clean = url.replace('https://', '').replace('http://', '')
                    extract_url = template.format(url=url_clean)
                else:
                    extract_url = template.format(url=url)
                
                response = requests.get(
                    extract_url, 
                    headers=self.headers, 
                    timeout=self.timeout
                )
                response.raise_for_status()
                return response.text
        
        raise ValueError(f"Unknown method: {method}")
    
    def _scrapling_extract(self, url: str) -> str:
        """Fallback using Scrapling"""
        try:
            from scrapling import Fetcher
            
            fetcher = Fetcher()
            page = fetcher.get(url)
            
            # Try to get main content
            content = page.markdown
            if content:
                return content
            
            # Fallback to text
            return page.text
            
        except ImportError:
            # If Scrapling not installed, use basic requests + BS4
            return self._basic_extract(url)
    
    def _basic_extract(self, url: str) -> str:
        """Basic extraction with requests + BeautifulSoup"""
        from bs4 import BeautifulSoup
        
        response = requests.get(url, headers=self.headers, timeout=self.timeout)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()
        
        # Get text
        text = soup.get_text(separator='\n', strip=True)
        
        # Clean up
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Extract web content')
    parser.add_argument('url', help='URL to extract')
    parser.add_argument('--method', default='auto', 
                       choices=['auto', 'markdown.new', 'defuddle.md', 'r.jina.ai', 'scrapling'],
                       help='Extraction method')
    parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    parser.add_argument('--timeout', type=int, default=30, help='Request timeout')
    
    args = parser.parse_args()
    
    extractor = WebExtractor(timeout=args.timeout)
    
    try:
        content = extractor.extract(args.url, args.method)
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Content saved to {args.output}", file=sys.stderr)
        else:
            print(content)
            
    except Exception as e:
        print(f"✗ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
