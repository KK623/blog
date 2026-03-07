import re

# Read the generated JS data
with open('scholars_js_data.txt', 'r', encoding='utf-8') as f:
    js_data = f.read()

# Read the HTML file
with open('blog/posts/2026/03/06/cvnn-scholars-landscape.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Extract lines up to id 50 and from id 127 onwards (stats rows)
lines = js_data.strip().split(',\n')
valid_scholars = []
for line in lines:
    # Skip lines with '总计' or '复数网络+无线通信' (stats rows)
    if '"id":' in line:
        # Extract id number
        match = re.search(r'id:\s*(\d+)', line)
        if match:
            id_num = int(match.group(1))
            if id_num <= 126:  # Only keep scholars with id 1-126
                valid_scholars.append(line)

print(f"Found {len(valid_scholars)} valid scholars")

# Create the new scholars array
new_array = '[\n' + ',\n'.join(valid_scholars) + '\n]'

# Find and replace the loadScholars function content
pattern = r"(loadScholars\(\) \{\s*// 126 scholars data\s*this\.scholars = )\[.*?\](;\s*\},\s*loadTopScholars)"
replacement = r"\1" + new_array + r"\2"

new_html = re.sub(pattern, replacement, html_content, flags=re.DOTALL)

# Check if replacement worked
if new_html == html_content:
    print("Pattern not matched, trying alternative approach...")
    # Alternative: Find the array directly
    pattern2 = r"(this\.scholars = )\[\s*\{ id: 1, name:.*?\}\s*\](;\s*// Add placeholder)"
    new_html = re.sub(pattern2, r"\1" + new_array + r"\2", html_content, flags=re.DOTALL)

# Write the updated HTML
with open('blog/posts/2026/03/06/cvnn-scholars-landscape.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("HTML file updated successfully!")
