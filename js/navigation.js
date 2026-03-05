/**
 * 博客导航系统 - 混合方案
 * 功能：面包屑导航 + 分类侧边栏 + 智能链接
 */

(function() {
  'use strict';

  const CONFIG = {
    baseUrl: 'https://kk623.github.io/blog',
    siteName: '孙凯 | AI 研究院',
    categories: {
      'llm': { name: 'LLM 量化/部署/蒸馏', icon: '📚' },
      'cvnn': { name: 'CVNN 复数神经网络', icon: '🔬' },
      'mwc2026': { name: 'MWC 2026 专栏', icon: '📱' },
      'chip': { name: '芯片分析', icon: '🔷' },
      'product': { name: '产品设计', icon: '📱' },
      'deep-analysis': { name: '单篇深度分析', icon: '📖' }
    }
  };

  // 面包屑导航生成
  function generateBreadcrumb() {
    const path = window.location.pathname.replace('/blog/', '').split('/').filter(Boolean);
    if (path.length === 0) return '';

    let html = '<nav class="breadcrumb" aria-label="面包屑导航">';
    html += '<a href="' + CONFIG.baseUrl + '/">首页</a>';

    let buildPath = '';
    path.forEach((segment, index) => {
      buildPath += '/' + segment;
      const isLast = index === path.length - 1;
      const displayName = getSegmentName(segment);
      
      html += ' <span class="sep">/</span> ';
      if (isLast) {
        html += '<span class="current">' + displayName + '</span>';
      } else {
        html += '<a href="' + CONFIG.baseUrl + buildPath + '">' + displayName + '</a>';
      }
    });

    html += '</nav>';
    return html;
  }

  // 获取路径段显示名称
  function getSegmentName(segment) {
    if (segment.match(/^\d{4}$/)) return segment + '年';
    if (segment.match(/^\d{2}$/)) return segment + '月';
    if (segment === 'posts') return '博客';
    if (segment === 'mwc2026') return 'MWC 2026';
    // 从文件名提取标题
    return segment.replace(/-/g, ' ').replace(/\.html$/, '').substring(0, 20) + '...';
  }

  // 主导航栏（绝对路径）
  function generateMainNav() {
    return `
      <nav class="main-nav" aria-label="主导航">
        <a href="${CONFIG.baseUrl}/">🏠 首页</a>
        <a href="${CONFIG.baseUrl}/posts/">📚 博客</a>
        <a href="${CONFIG.baseUrl}/mwc2026/">📱 MWC 2026</a>
        <a href="https://github.com/KK623" target="_blank">💻 GitHub</a>
      </nav>
    `;
  }

  // 分类侧边栏
  function generateCategorySidebar() {
    const currentPath = window.location.pathname;
    let currentCategory = null;
    
    // 自动检测当前分类
    if (currentPath.includes('llm') || currentPath.includes('quant')) currentCategory = 'llm';
    else if (currentPath.includes('cvnn') || currentPath.includes('euler') || currentPath.includes('rfm')) currentCategory = 'cvnn';
    else if (currentPath.includes('mwc')) currentCategory = 'mwc2026';
    else if (currentPath.includes('nvidia') || currentPath.includes('chip')) currentCategory = 'chip';

    let html = '<aside class="category-sidebar" aria-label="分类导航">';
    html += '<h3>📂 文章分类</h3>';
    html += '<ul>';
    
    for (const [key, info] of Object.entries(CONFIG.categories)) {
      const isActive = key === currentCategory;
      const activeClass = isActive ? ' class="active"' : '';
      html += `<li${activeClass}><a href="${CONFIG.baseUrl}/posts/#${key}">${info.icon} ${info.name}</a></li>`;
    }
    
    html += '</ul>';
    html += '</aside>';
    return html;
  }

  // 返回顶部按钮
  function generateBackToTop() {
    return '<button class="back-to-top" onclick="window.scrollTo({top:0,behavior:\'smooth\'})" aria-label="返回顶部">↑</button>';
  }

  // 初始化导航
  function init() {
    // 插入主导航
    const container = document.querySelector('.container');
    if (container) {
      const mainNav = document.createElement('div');
      mainNav.innerHTML = generateMainNav() + generateBreadcrumb();
      container.insertBefore(mainNav.firstElementChild, container.firstElementChild);
      container.insertBefore(mainNav.lastElementChild, container.children[1]);
    }

    // 插入侧边栏（如果有文章主体）
    const content = document.querySelector('article') || document.querySelector('.content');
    if (content && !document.querySelector('.category-sidebar')) {
      const sidebar = document.createElement('div');
      sidebar.innerHTML = generateCategorySidebar();
      // 插入到合适位置
    }

    // 插入返回顶部按钮
    document.body.insertAdjacentHTML('beforeend', generateBackToTop());

    // 添加样式
    addStyles();
  }

  // 添加导航样式
  function addStyles() {
    const styles = `
      /* 主导航 */
      .main-nav {
        display: flex;
        gap: 20px;
        padding: 16px 0;
        margin-bottom: 20px;
        border-bottom: 1px solid #eee;
        flex-wrap: wrap;
      }
      .main-nav a {
        color: #0066cc;
        text-decoration: none;
        font-size: 14px;
        transition: color 0.2s;
      }
      .main-nav a:hover {
        color: #0055aa;
        text-decoration: underline;
      }

      /* 面包屑 */
      .breadcrumb {
        font-size: 13px;
        color: #666;
        margin-bottom: 24px;
        padding: 8px 0;
      }
      .breadcrumb a {
        color: #0066cc;
        text-decoration: none;
      }
      .breadcrumb a:hover {
        text-decoration: underline;
      }
      .breadcrumb .sep {
        color: #999;
        margin: 0 4px;
      }
      .breadcrumb .current {
        color: #333;
        font-weight: 500;
      }

      /* 分类侧边栏 */
      .category-sidebar {
        background: #f8f9fa;
        border-radius: 8px;
        padding: 16px;
        margin: 20px 0;
      }
      .category-sidebar h3 {
        font-size: 14px;
        margin-bottom: 12px;
        color: #333;
      }
      .category-sidebar ul {
        list-style: none;
        margin: 0;
        padding: 0;
      }
      .category-sidebar li {
        margin: 8px 0;
      }
      .category-sidebar li.active a {
        color: #0066cc;
        font-weight: 500;
        background: #e3f2fd;
        padding: 4px 8px;
        border-radius: 4px;
        margin-left: -8px;
      }
      .category-sidebar a {
        color: #555;
        text-decoration: none;
        font-size: 13px;
        display: block;
        padding: 4px 0;
      }
      .category-sidebar a:hover {
        color: #0066cc;
      }

      /* 返回顶部 */
      .back-to-top {
        position: fixed;
        bottom: 30px;
        right: 30px;
        width: 40px;
        height: 40px;
        background: #0066cc;
        color: white;
        border: none;
        border-radius: 50%;
        cursor: pointer;
        font-size: 18px;
        opacity: 0;
        transition: opacity 0.3s;
        z-index: 1000;
      }
      .back-to-top.visible {
        opacity: 0.8;
      }
      .back-to-top:hover {
        opacity: 1;
      }
    `;
    
    const styleEl = document.createElement('style');
    styleEl.textContent = styles;
    document.head.appendChild(styleEl);

    // 滚动显示返回顶部按钮
    window.addEventListener('scroll', function() {
      const btn = document.querySelector('.back-to-top');
      if (btn) {
        btn.classList.toggle('visible', window.scrollY > 300);
      }
    });
  }

  // DOM加载完成后初始化
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
