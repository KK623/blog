import re
import json

with open('CVNN_100_Scholars_List.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

scholars = []
current_category = None
category_map = {
    '复数Transformer / 复数Attention': ('复数Transformer', 'CT'),
    'Deep Complex Networks核心团队': ('Deep Complex', 'DC'),
    'Unitary RNN / 正交RNN': ('Unitary RNN', 'UR'),
    'CVNN综述/理论奠基': ('CVNN理论', 'TH'),
    '复数CNN / 复数卷积': ('复数CNN', 'CC'),
    '复数激活函数': ('复数激活', 'AF'),
    '四元数神经网络': ('四元数', 'QN'),
    '复数信号/语音处理': ('语音处理', 'SP'),
    '复数网络架构/组件': ('架构组件', 'AC'),
    '新兴/扩展方向': ('新兴方向', 'EX'),
    '复数网络+无线通信': ('无线通信', 'WC'),
}

# Find category headers and extract data
for line in lines:
    line = line.strip()
    
    # Check for category header
    if line.startswith('## '):
        for cat_name, (cat_short, cat_code) in category_map.items():
            if cat_name in line:
                current_category = (cat_short, cat_code)
                break
    
    # Parse scholar row
    if current_category and line.startswith('| **'):
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 5 and parts[1] and parts[1] != '姓名':
            name = parts[1].replace('**', '').strip()
            institution = parts[2].strip()
            contribution = parts[3].strip()
            
            if name and name != '姓名' and '---' not in name:
                scholars.append({
                    'name': name,
                    'institution': institution,
                    'contribution': contribution,
                    'category': current_category[0],
                    'categoryShort': current_category[1]
                })

# Add IDs and fields
for i, s in enumerate(scholars, 1):
    s['id'] = i
    s['fields'] = [s['category']]
    s['papers'] = []

print(f"Total scholars: {len(scholars)}")

# Generate JavaScript
js_lines = []
for s in scholars:
    name = s['name'].replace('"', '\\"')
    inst = s['institution'].replace('"', '\\"')
    contrib = s['contribution'].replace('"', '\\"').replace('\n', ' ')
    fields_json = json.dumps(s['fields'], ensure_ascii=False)
    
    js_lines.append(f'{{ id: {s["id"]}, name: "{name}", institution: "{inst}", contribution: "{contrib}", fields: {fields_json}, category: "{s["category"]}", categoryShort: "{s["categoryShort"]}", papers: [] }}')

# Write to file
with open('scholars_js_data.txt', 'w', encoding='utf-8') as f:
    f.write(',\n'.join(js_lines))

print(f"Generated JS data for {len(scholars)} scholars")
print(f"First 3: {scholars[:3]}")
