---
name: web-extractor
description: Extract web content using markdown.new, defuddle.md, r.jina.ai, or Scrapling as fallback. Supports image extraction and download.
metadata:
  openclaw:
    emoji: 🌐
    requires:
      bins: [python3, pip3]
---

# Web Extractor Skill

Extract web content and images using multiple fallback methods.

## Methods (in order)

1. **markdown.new/** - For Cloudflare-protected sites
2. **defuddle.md/** - Alternative markdown extractor
3. **r.jina.ai/** - Jina AI summarizer/extractor
4. **Scrapling** - Advanced web scraper (fallback)

## Usage

### Extract webpage content

```bash
# Using the skill
python3 {baseDir}/extract.py https://example.com

# Or with options
python3 {baseDir}/extract.py https://example.com --method auto --output content.md
```

### Download images from webpage

```bash
python3 {baseDir}/download_images.py https://example.com --output ./images
```

### Extract and download all

```bash
python3 {baseDir}/extract_all.py https://example.com --output-dir ./output
```

## Methods Detail

| Method | Prefix | Best For | Speed |
|--------|--------|----------|-------|
| markdown.new | `https://markdown.new/https://example.com` | Cloudflare sites | Fast |
| defuddle.md | `https://defuddle.md/https://example.com` | General sites | Fast |
| r.jina.ai | `https://r.jina.ai/http://example.com` | Article extraction | Fast |
| Scrapling | Direct request | Complex/JS sites | Slow |

## Python API

```python
from extract import WebExtractor

extractor = WebExtractor()
content = extractor.extract("https://example.com")
print(content)
```

## Image Download

```python
from download_images import ImageDownloader

downloader = ImageDownloader()
downloader.download_from_url("https://example.com", output_dir="./images")
```

## Installation

```bash
pip3 install requests beautifulsoup4 lxml
# Optional: Install Scrapling for advanced scraping
pip3 install scrapling
```

## Examples

### Extract Huawei MWC page
```bash
python3 {baseDir}/extract.py https://carrier.huawei.com/en/minisite/events/mwc2026/
```

### Download all images from page
```bash
python3 {baseDir}/download_images.py https://example.com --min-size 10000
```
