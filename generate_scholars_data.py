import re
import json

# Read the markdown file
with open('CVNN_100_Scholars_List.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract scholar data from tables
def parse_table(table_text, category, category_short):
    scholars = []
    lines = table_text.strip().split('\n')
    
    for line in lines:
        if line.startswith('| **') and '---' not in line and '姓名' not in line:
            parts = line.split('|')
            if len(parts) >= 4:
                name = parts[1].strip().replace('**', '')
                institution = parts[2].strip()
                contribution = parts[3].strip()
                
                if name and name != '姓名':
                    scholars.append({
                        'name': name,
                        'institution': institution,
                        'contribution': contribution,
                        'category': category,
                        'categoryShort': category_short
                    })
    return scholars

# Define categories with their mapping
categories = [
    ('复数Transformer', 'CT', '复数Transformer / 复数Attention'),
    ('Deep Complex', 'DC', 'Deep Complex Networks核心团队'),
    ('Unitary RNN', 'UR', 'Unitary RNN / 正交RNN'),
    ('CVNN理论', 'TH', 'CVNN综述/理论奠基'),
    ('复数CNN', 'CC', '复数CNN / 复数卷积'),
    ('复数激活', 'AF', '复数激活函数'),
    ('四元数', 'QN', '四元数神经网络'),
    ('语音处理', 'SP', '复数信号/语音处理'),
    ('架构组件', 'AC', '复数网络架构/组件'),
    ('新兴方向', 'EX', '新兴/扩展方向'),
    ('无线通信', 'WC', '复数网络+无线通信'),
]

all_scholars = []
scholar_id = 1

for cat_short, cat_code, cat_full in categories:
    # Find the section
    pattern = rf'## [^\n]*{re.escape(cat_full)}[^\n]*\n\n[^\n]*\|[^\n]*\|[^\n]*\|[^\n]*\|\n[^\n]*\|[^-]*-\|[^\n]*\|\n((?:\|[^\n]*\n)+)'
    match = re.search(pattern, content)
    
    if match:
        table_content = match.group(1)
        scholars = parse_table(table_content, cat_short, cat_code)
        for s in scholars:
            s['id'] = scholar_id
            s['fields'] = [cat_short]  # Default field
            all_scholars.append(s)
            scholar_id += 1

# Generate JavaScript array
js_data = []
for s in all_scholars:
    js_obj = f"""{{ id: {s['id']}, name: "{s['name']}", institution: "{s['institution']}", contribution: "{s['contribution']}", fields: {json.dumps(s['fields'], ensure_ascii=False)}, category: "{s['category']}", categoryShort: "{s['categoryShort']}", papers: [] }}"""
    js_data.append(js_obj)

# Write output
with open('scholars_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_scholars, f, ensure_ascii=False, indent=2)

print(f"Generated {len(all_scholars)} scholars")
print(f"First 5: {[s['name'] for s in all_scholars[:5]]}")
print(f"Last 5: {[s['name'] for s in all_scholars[-5:]]}")
