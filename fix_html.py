# Read the JS data file
with open('scholars_js_data.txt', 'r', encoding='utf-8') as f:
    all_data = f.read()

# Read the HTML file
with open('blog/posts/2026/03/06/cvnn-scholars-landscape.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract only valid scholars (id 1-126)
import re
lines = all_data.strip().split(',\n')
valid_lines = []
for line in lines:
    match = re.search(r'id:\s*(\d+)', line)
    if match:
        id_num = int(match.group(1))
        if id_num <= 126 and '**' not in line:  # Exclude stats rows
            valid_lines.append(line)

print(f"Valid scholars: {len(valid_lines)}")

# Build new loadScholars function
new_data = '[\n                        ' + ',\n                        '.join(valid_lines) + '\n                    ]'

# Replace the empty array and placeholder loop
old_pattern = r"(loadScholars\(\) \{\s*// 126 scholars data\s*this\.scholars = )\[\s*\](.*?// Add placeholder entries.*?\{[^}]+\}\s*\}\s*\})"
new_replacement = r"\1" + new_data + r"\2"

new_html = re.sub(old_pattern, new_replacement, html, flags=re.DOTALL)

if new_html == html:
    print("Pattern not matched, trying simpler approach")
    # Find and replace the scholars array more directly
    start_marker = "loadScholars() {"
    end_marker = "loadTopScholars()"
    
    start_idx = html.find(start_marker)
    end_idx = html.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        # Extract the function content
        before = html[:start_idx + len(start_marker)]
        after = html[end_idx:]
        
        new_func = '''
                    // 126 scholars data
                    this.scholars = ''' + new_data + ''';
                },
                
                '''
        new_html = before + new_func + after
        print("Replaced using index method")
    else:
        print("Could not find markers")
else:
    print("Pattern matched and replaced")

# Write the updated HTML
with open('blog/posts/2026/03/06/cvnn-scholars-landscape.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Done!")
