import re

# Read current scholars data
with open('scholars_js_data.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Google Scholar URLs for top scholars
scholar_links = {
    1: "https://scholar.google.com/citations?user=M0bhIh4AAAAJ",  # Chiheb Trabelsi - actually need to check each
}

# Update the data to add scholar_url field
lines = content.strip().split(',\n')
updated_lines = []

for line in lines:
    # Extract id
    match = re.search(r'id:\s*(\d+)', line)
    if match:
        id_num = int(match.group(1))
        # Add scholar_url field (empty for now, will be populated manually)
        if 'scholar_url:' not in line:
            line = line.rstrip('}') + ', scholar_url: ""}'
    updated_lines.append(line)

with open('scholars_js_data_v2.txt', 'w', encoding='utf-8') as f:
    f.write(',\n'.join(updated_lines))

print("Added scholar_url field to all scholars")
