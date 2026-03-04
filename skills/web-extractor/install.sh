#!/bin/bash
# Install web-extractor skill dependencies

echo "Installing web-extractor dependencies..."

# Check Python version
python3 --version

# Install required packages
pip3 install requests beautifulsoup4 lxml -q

# Optional: Install Scrapling for advanced scraping
echo "Installing Scrapling (optional)..."
pip3 install scrapling -q 2>/dev/null || echo "⚠️ Scrapling installation failed (optional)"

echo "✓ Installation complete!"
echo ""
echo "Usage:"
echo "  python3 extract.py https://example.com"
echo "  python3 download_images.py https://example.com -o ./images"
echo "  python3 extract_all.py https://example.com -o ./output"
