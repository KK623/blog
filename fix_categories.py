#!/usr/bin/env python3
"""修正分类错误的脚本"""

import os
import re

def fix_category_in_file(filepath, correct_category):
    """修正文件中的分类"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 替换错误的分类
    pattern = r'<meta name="category" content="[^"]*">'
    replacement = f'<meta name="category" content="{correct_category}">'
    
    # 检查是否有多个category meta
    matches = re.findall(pattern, content)
    if len(matches) > 1:
        print(f"发现多个category meta: {filepath}")
        # 移除所有然后添加一个
        content = re.sub(r'\s*<meta name="category" content="[^"]*">', '', content)
        # 在第一个meta charset后插入
        content = re.sub(
            r'(<meta charset="UTF-8">)',
            f'\\1\n  <meta name="category" content="{correct_category}">',
            content
        )
        changed = True
    elif len(matches) == 1:
        old_category = re.search(r'<meta name="category" content="([^"]*)">', content).group(1)
        if old_category != correct_category:
            content = re.sub(pattern, replacement, content)
            print(f"修正 {os.path.basename(filepath)}: {old_category} -> {correct_category}")
            changed = True
        else:
            changed = False
    else:
        # 没有category meta，添加
        content = re.sub(
            r'(<meta charset="UTF-8">)',
            f'\\1\n  <meta name="category" content="{correct_category}">',
            content
        )
        print(f"添加分类到 {os.path.basename(filepath)}: {correct_category}")
        changed = True
    
    if changed:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    return changed

def main():
    # 定义正确的分类
    corrections = {
        '/root/.openclaw/workspace/blog/posts/2026/03/05/pi-quant-deep-analysis.html': 'chip',
        '/root/.openclaw/workspace/blog/posts/2026/03/05/rfm-deep-analysis.html': 'chip',
    }
    
    updated = 0
    for filepath, category in corrections.items():
        if os.path.exists(filepath):
            if fix_category_in_file(filepath, category):
                updated += 1
        else:
            print(f"文件不存在: {filepath}")
    
    print(f"\n已修正 {updated} 个文件")

if __name__ == '__main__':
    main()
