/**
 * 博客导航系统 - 混合方案
 * 功能：面包屑导航 + 主导航 + 返回顶部
 */

(function() {
  'use strict';

  const CONFIG = {
    baseUrl: 'https://kk623.github.io/blog',
    siteName: '孙凯 | AI 研究院'
  };

  // 面包屑导航生成
  function generateBreadcrumb() {
    const path = window.location.pathname.replace('/blog/', '').split('/').filter(Boolean);
    if (path.length === 0) return '';

    let html = '<nav class="breadcrumb-nav">';
    html += '<a href="' + CONFIG.baseUrl + '/">首页</a>';

    let buildPath = '';
    path.forEach((segment, index) => {
      buildPath += '/' + segment;
      const isLast = index === path.length - 1;
      
      html += ' <span class="sep">/</span> ';
      if (isLast) {
        html += '<span class="current">' + getSegmentName(segment) + '</span>';
      } else {
        html += '<a href="' + CONFIG.baseUrl + buildPath + '">' + getSegmentName(segment) + '</a>';
      }
    });

    html += '</nav>';
    return html;
  }

  function getSegmentName(segment) {
    if (/^\d{4}$/.test(segment)) return segment;
    if (/^\d{2}$/.test(segment)) return segment;
    if (segment === 'posts') return '博客';
    if (segment === 'mwc2026') return 'MWC 2026';
    return segment.substring(0, 15);
  }

  // 主导航
  function generateMainNav() {
    return '<nav class="main-nav">' +
      '<a href="' + CONFIG.baseUrl + '/">🏠 首页</a>' +
      '<a href="' + CONFIG.baseUrl + '/posts/">📚 博客</a>' +
      '<a href="' + CONFIG.baseUrl + '/mwc2026/">📱 MWC 2026</a>' +
      '<a href="https://github.com/KK623" target="_blank">💻 GitHub</a>' +
      '</nav>';
  }

  // 返回顶部
  function generateBackToTop() {
    return '<button class="back-to-top" onclick="window.scrollTo({top:0,behavior:\'smooth\'})" title="返回顶部">↑</button>';
  }

  // 样式
  function addStyles() {
    const styles = document.createElement('style');
    styles.textContent = `
      .main-nav { display: flex; gap: 20px; padding: 16px 0; margin-bottom: 20px; border-bottom: 1px solid #eee; flex-wrap: wrap; }
      .main-nav a { color: #0066cc; text-decoration: none; font-size: 14px; }
      .main-nav a:hover { text-decoration: underline; }
      .breadcrumb-nav { font-size: 13px; color: #666; margin-bottom: 24px; }
      .breadcrumb-nav a { color: #0066cc; text-decoration: none; }
      .breadcrumb-nav .sep { color: #999; margin: 0 4px; }
      .breadcrumb-nav .current { color: #333; font-weight: 500; }
      .back-to-top { position: fixed; bottom: 30px; right: 30px; width: 40px; height: 40px; background: #0066cc; color: white; border: none; border-radius: 50%; cursor: pointer; font-size: 18px; opacity: 0; transition: opacity 0.3s; z-index: 1000; }
      .back-to-top.visible { opacity: 0.8; }
      .back-to-top:hover { opacity: 1; }
    `;
    document.head.appendChild(styles);
  }

  // 初始化
  function init() {
    const container = document.querySelector('.container');
    if (!container) return;

    addStyles();

    // 插入主导航和面包屑
    const navWrapper = document.createElement('div');
    navWrapper.innerHTML = generateMainNav() + generateBreadcrumb();
    container.insertBefore(navWrapper, container.firstChild);

    // 插入返回顶部
    document.body.insertAdjacentHTML('beforeend', generateBackToTop());

    // 滚动监听
    window.addEventListener('scroll', function() {
      const btn = document.querySelector('.back-to-top');
      if (btn) btn.classList.toggle('visible', window.scrollY > 300);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
