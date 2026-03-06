#!/usr/bin/env python3
"""批量更新博客文章导航系统 - 修正版"""

import os
import re
import glob

def get_category_from_filename(filepath):
    """根据文件路径和名称判断分类"""
    filename = os.path.basename(filepath).lower()
    parent_dir = os.path.dirname(filepath).lower()
    
    # CVNN 相关
    if 'cvnn' in filename or 'cvnn' in parent_dir:
        return 'cvnn'
    
    # MWC 相关（包括各厂商MWC报告）
    if 'mwc' in filename or 'mwc' in parent_dir:
        return 'mwc'
    
    # LLM 相关
    if 'llm' in filename or 'quantization' in filename:
        return 'llm'
    
    # Chip/硬件相关
    if any(x in filename for x in ['nvidia', 'blackwell', 'rubin', 'quant', 'rfm', 'pi-quant', 'chip']):
        return 'chip'
    
    # 默认分类
    return 'product'

def get_date_from_path(filepath):
    """从路径中提取日期 2026-03-XX"""
    match = re.search(r'/2026/03/(\d{2})/', filepath)
    if match:
        day = match.group(1)
        return f"2026-03-{day}"
    return "2026-03-01"

def remove_old_navigation(content):
    """移除旧的硬编码导航代码"""
    # 匹配 <div class="back">...</div> 及其内容
    content = re.sub(r'\s*<div class="back">.*?\u003c/div>', '', content, flags=re.DOTALL)
    # 匹配单独的返回链接
    content = re.sub(r'\s*<p class="back">.*?\u003c/p>', '', content, flags=re.DOTALL)
    return content

def add_navigation_to_head(content, category, date):
    """在<head>中添加meta标签和脚本"""
    has_category = f'name="category"' in content
    has_date = f'name="date"' in content
    has_nav = 'navigation.js' in content
    
    # 如果都已存在，直接返回
    if has_category and has_date and has_nav:
        return content, False
    
    # 构建插入内容
    insert_lines = []
    if not has_category:
        insert_lines.append(f'  <meta name="category" content="{category}">')
    if not has_date:
        insert_lines.append(f'  <meta name="date" content="{date}">')
    if not has_nav:
        insert_lines.append('  <script src="https://kk623.github.io/blog/js/navigation.js" defer></script>')
    
    insert_text = '\n' + '\n'.join(insert_lines)
    
    # 在</head>前插入
    head_end_match = re.search(r'(\s*)</head>', content)
    if head_end_match:
        insert_pos = head_end_match.start()
        content = content[:insert_pos] + insert_text + content[insert_pos:]
        return content, True
    
    return content, False

def process_file(filepath):
    """处理单个文件"""
    print(f"处理: {os.path.basename(filepath)}")
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    category = get_category_from_filename(filepath)
    date = get_date_from_path(filepath)
    
    original_content = content
    
    # 移除旧导航
    content = remove_old_navigation(content)
    nav_removed = content != original_content
    
    # 添加新导航
    content, nav_added = add_navigation_to_head(content, category, date)
    
    # 保存修改
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✓ 分类:{category} 日期:{date} {'(移除旧导航)' if nav_removed else ''} {'(添加meta)' if nav_added else ''}")
        return True
    else:
        print(f"  - 无需更改")
        return False

def main():
    base_dir = '/root/.openclaw/workspace/blog/posts/2026/03'
    
    # 获取所有HTML文件
    html_files = []
    for day in ['02', '03', '04', '05']:
        pattern = os.path.join(base_dir, day, '*.html')
        html_files.extend(glob.glob(pattern))
    
    html_files.sort()
    
    print(f"找到 {len(html_files)} 个HTML文件\n")
    
    updated_count = 0
    for filepath in html_files:
        if process_file(filepath):
            updated_count += 1
    
    print(f"\n========================================")
    print(f"总计: {len(html_files)} 个文件")
    print(f"已更新: {updated_count} 个文件")
    print(f"未变动: {len(html_files) - updated_count} 个文件")

if __name__ == '__main__':
    main()
