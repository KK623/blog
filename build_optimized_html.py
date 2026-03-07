import re

# Read scholars data
with open('scholars_js_data.txt', 'r', encoding='utf-8') as f:
    raw_data = f.read()

# Filter valid scholars (id 1-126)
lines = raw_data.strip().split(',\n')
valid_scholars = []
for line in lines:
    match = re.search(r'id:\s*(\d+)', line)
    if match:
        id_num = int(match.group(1))
        if id_num <= 126 and '**' not in line:
            valid_scholars.append(line.strip())

scholars_js = '[\n    ' + ',\n    '.join(valid_scholars) + '\n]'

# Build optimized HTML
html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CVNN学者全景图谱 | 126位复数神经网络研究者</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600,700&family=Noto+Sans+SC:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        * {{ font-family: 'Inter', 'Noto Sans SC', sans-serif; }}
        .gradient-bg {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }}
        .card-hover {{ transition: transform 0.2s ease; }}
        .card-hover:hover {{ transform: translateY(-2px); box-shadow: 0 10px 25px rgba(0,0,0,0.1); }}
        [x-cloak] {{ display: none !important; }}
        .lazy-image {{ opacity: 0; transition: opacity 0.3s; }}
        .lazy-image.loaded {{ opacity: 1; }}
        .pagination-btn {{ transition: all 0.2s; }}
        .pagination-btn:hover:not(:disabled) {{ background-color: #4f46e5; color: white; }}
        .pagination-btn:disabled {{ opacity: 0.5; cursor: not-allowed; }}
    </style>
</head>
<body class="bg-slate-50 text-slate-800" x-data="scholarApp()" x-init="init()">
    <header class="gradient-bg text-white py-10 px-4">
        <div class="max-w-7xl mx-auto">
            <div class="flex flex-col md:flex-row md:items-center md:justify-between">
                <div>
                    <h1 class="text-3xl md:text-4xl font-bold mb-2">CVNN学者全景图谱</h1>
                    <p class="text-lg opacity-90">126位复数神经网络核心研究者</p>
                </div>
                <div class="mt-4 md:mt-0 grid grid-cols-4 gap-3 text-center">
                    <div class="bg-white/10 backdrop-blur rounded-lg p-3">
                        <div class="text-2xl font-bold" x-text="totalCount">126</div>
                        <div class="text-xs opacity-80">总学者</div>
                    </div>
                    <div class="bg-white/10 backdrop-blur rounded-lg p-3">
                        <div class="text-2xl font-bold">45+</div>
                        <div class="text-xs opacity-80">机构</div>
                    </div>
                    <div class="bg-white/10 backdrop-blur rounded-lg p-3">
                        <div class="text-2xl font-bold">11</div>
                        <div class="text-xs opacity-80">领域</div>
                    </div>
                    <div class="bg-white/10 backdrop-blur rounded-lg p-3">
                        <div class="text-2xl font-bold">2025</div>
                        <div class="text-xs opacity-80">更新</div>
                    </div>
                </div>
            </div>
        </div>
    </header>

    <section class="sticky top-0 z-40 bg-white shadow-md border-b border-slate-200 py-3 px-4">
        <div class="max-w-7xl mx-auto">
            <div class="flex flex-col lg:flex-row gap-3 items-start lg:items-center">
                <div class="relative flex-1 w-full lg:max-w-sm">
                    <input type="text" x-model="searchQuery" @input="handleSearch()" placeholder="搜索学者姓名、机构..." 
                        class="w-full pl-9 pr-3 py-2 border border-slate-300 rounded-lg text-sm focus:ring-2 focus:ring-indigo-500">
                    <svg class="absolute left-2.5 top-2 w-4 h-4 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                    </svg>
                </div>
                <div class="flex flex-wrap gap-1.5 max-w-2xl">
                    <button @click="selectedField = ''" :class="selectedField === '' ? 'bg-indigo-600 text-white' : 'bg-slate-100 text-slate-700'"
                        class="px-2.5 py-1 rounded-full text-xs font-medium transition">全部</button>
                    <template x-for="field in fieldCategories" :key="field">
                        <button @click="selectedField = field" 
                            :class="selectedField === field ? 'bg-indigo-600 text-white' : 'bg-slate-100 text-slate-700'"
                            class="px-2.5 py-1 rounded-full text-xs font-medium transition whitespace-nowrap" x-text="field"></button>
                    </template>
                </div>
                <select x-model="sortBy" @change="handleSort()" class="px-2 py-1.5 border border-slate-300 rounded text-xs">
                    <option value="name">按姓名</option>
                    <option value="institution">按机构</option>
                    <option value="category">按领域</option>
                </select>
            </div>
            <div class="mt-2 flex items-center justify-between text-xs text-slate-600">
                <span>显示 <span class="font-semibold text-indigo-600" x-text="displayedScholars.length"></span> / <span x-text="totalCount"></span> 位学者</span>
                <button x-show="selectedField || searchQuery" @click="resetFilters()" class="text-indigo-600 hover:underline">清除筛选</button>
            </div>
        </div>
    </section>

    <main class="max-w-7xl mx-auto py-6 px-4">
        <section class="mb-6">
            <h2 class="text-lg font-bold mb-3 text-slate-800">领域分布可视化</h2>
            <div class="grid md:grid-cols-2 gap-4">
                <div class="bg-white p-3 rounded-lg shadow-sm border border-slate-200">
                    <canvas id="categoryChart" height="180"></canvas>
                </div>
                <div class="bg-white p-3 rounded-lg shadow-sm border border-slate-200">
                    <canvas id="institutionChart" height="180"></canvas>
                </div>
            </div>
        </section>

        <section>
            <div class="flex items-center justify-between mb-3">
                <h2 class="text-lg font-bold text-slate-800">学者列表</h2>
                <div class="flex items-center gap-2 text-sm">
                    <button @click="prevPage()" :disabled="currentPage === 1" class="pagination-btn px-3 py-1 border border-slate-300 rounded bg-white text-xs">上一页</button>
                    <span class="text-slate-600 text-xs">第 <span x-text="currentPage"></span> / <span x-text="totalPages"></span> 页</span>
                    <button @click="nextPage()" :disabled="currentPage === totalPages" class="pagination-btn px-3 py-1 border border-slate-300 rounded bg-white text-xs">下一页</button>
                </div>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                <template x-for="scholar in paginatedScholars" :key="scholar.id">
                    <div class="bg-white rounded-lg shadow-sm border border-slate-200 overflow-hidden card-hover">
                        <div class="p-4">
                            <div class="flex items-start gap-3 mb-2">
                                <img :src="getAvatar(scholar)" :alt="scholar.name" loading="lazy" 
                                    class="w-10 h-10 rounded-full object-cover bg-slate-200 lazy-image" 
                                    @load="$event.target.classList.add('loaded')">
                                <div class="flex-1 min-w-0">
                                    <h3 class="font-bold text-base text-slate-800 truncate" x-text="scholar.name"></h3>
                                    <p class="text-xs text-slate-500 truncate" x-text="scholar.institution"></p>
                                </div>
                                <span class="text-xs px-2 py-0.5 rounded-full font-medium shrink-0" 
                                    :class="getCategoryColor(scholar.category)" x-text="scholar.categoryShort"></span>
                            </div>
                            <p class="text-sm text-slate-600 mb-2 line-clamp-2" x-text="scholar.contribution"></p>
                            <div class="flex flex-wrap gap-1">
                                <template x-for="f in scholar.fields.slice(0, 2)" :key="f">
                                    <span class="text-xs px-1.5 py-0.5 bg-slate-100 text-slate-600 rounded" x-text="f"></span>
                                </template>
                            </div>
                        </div>
                    </div>
                </template>
            </div>

            <div class="mt-4 flex items-center justify-center gap-2">
                <button @click="goToPage(1)" :disabled="currentPage === 1" class="pagination-btn px-2 py-1 border border-slate-300 rounded bg-white text-xs">首页</button>
                <button @click="prevPage()" :disabled="currentPage === 1" class="pagination-btn px-2 py-1 border border-slate-300 rounded bg-white text-xs">上一页</button>
                <div class="flex gap-1">
                    <template x-for="page in visiblePages" :key="page">
                        <button @click="goToPage(page)" 
                            :class="page === currentPage ? 'bg-indigo-600 text-white' : 'bg-white text-slate-700 hover:bg-slate-100'"
                            class="w-7 h-7 rounded text-xs font-medium transition" x-text="page"></button>
                    </template>
                </div>
                <button @click="nextPage()" :disabled="currentPage === totalPages" class="pagination-btn px-2 py-1 border border-slate-300 rounded bg-white text-xs">下一页</button>
                <button @click="goToPage(totalPages)" :disabled="currentPage === totalPages" class="pagination-btn px-2 py-1 border border-slate-300 rounded bg-white text-xs">末页</button>
            </div>
        </section>

        <div x-show="displayedScholars.length === 0" class="text-center py-12" x-cloak>
            <p class="text-slate-500">未找到匹配的学者</p>
        </div>
    </main>

    <footer class="bg-slate-800 text-slate-400 py-6 px-4 mt-12 text-center text-sm">
        <p>CVNN学者全景图谱 | 数据来源：arXiv、Google Scholar、IEEE Xplore</p>
        <p class="mt-1">最后更新：2026-03-06</p>
    </footer>

    <script>
        const SCHOLARS_DATA = {scholars_js};

        function scholarApp() {{
            return {{
                scholars: [],
                searchQuery: '',
                selectedField: '',
                sortBy: 'name',
                currentPage: 1,
                pageSize: 12,
                totalCount: 126,
                fieldCategories: ['复数Transformer', 'Deep Complex', 'Unitary RNN', 'CVNN理论', '复数CNN', '复数激活', '四元数', '语音处理', '架构组件', '新兴方向', '无线通信'],
                
                get displayedScholars() {{
                    let result = this.scholars;
                    if (this.searchQuery) {{
                        const q = this.searchQuery.toLowerCase();
                        result = result.filter(s => s.name.toLowerCase().includes(q) || s.institution.toLowerCase().includes(q));
                    }}
                    if (this.selectedField) {{
                        result = result.filter(s => s.category === this.selectedField);
                    }}
                    return result;
                }},
                
                get paginatedScholars() {{
                    const start = (this.currentPage - 1) * this.pageSize;
                    return this.displayedScholars.slice(start, start + this.pageSize);
                }},
                
                get totalPages() {{
                    return Math.ceil(this.displayedScholars.length / this.pageSize) || 1;
                }},
                
                get visiblePages() {{
                    const pages = [];
                    const maxVisible = 5;
                    let start = Math.max(1, this.currentPage - Math.floor(maxVisible / 2));
                    let end = Math.min(this.totalPages, start + maxVisible - 1);
                    if (end - start + 1 < maxVisible) start = Math.max(1, end - maxVisible + 1);
                    for (let i = start; i <= end; i++) pages.push(i);
                    return pages;
                }},
                
                init() {{
                    this.scholars = SCHOLARS_DATA;
                    this.$nextTick(() => this.initCharts());
                }},
                
                handleSearch() {{
                    this.currentPage = 1;
                }},
                
                handleSort() {{
                    const sortFn = {{
                        'name': (a, b) => a.name.localeCompare(b.name),
                        'institution': (a, b) => a.institution.localeCompare(b.institution),
                        'category': (a, b) => a.category.localeCompare(b.category)
                    }};
                    this.scholars.sort(sortFn[this.sortBy]);
                    this.currentPage = 1;
                }},
                
                resetFilters() {{
                    this.searchQuery = '';
                    this.selectedField = '';
                    this.currentPage = 1;
                }},
                
                prevPage() {{ if (this.currentPage > 1) this.currentPage--; }},
                nextPage() {{ if (this.currentPage < this.totalPages) this.currentPage++; }},
                goToPage(p) {{ this.currentPage = p; }},
                
                getAvatar(scholar) {{
                    return `https://ui-avatars.com/api/?name=${{encodeURIComponent(scholar.name)}}&background=${{this.getColor(scholar.category)}}&color=fff&size=64`;
                }},
                
                getColor(category) {{
                    const colors = {{'复数Transformer': '667eea', 'Deep Complex': 'f093fb', 'Unitary RNN': '4facfe', 'CVNN理论': '43e97b', '复数CNN': 'fa709a', '复数激活': 'feca57', '四元数': '5f27cd', '语音处理': '00d2d3', '架构组件': 'ff9ff3', '新兴方向': '54a0ff', '无线通信': 'ee5a24'}};
                    return colors[category] || '6c757d';
                }},
                
                getCategoryColor(category) {{
                    const colors = {{'复数Transformer': 'bg-indigo-100 text-indigo-700', 'Deep Complex': 'bg-purple-100 text-purple-700', 'Unitary RNN': 'bg-blue-100 text-blue-700', 'CVNN理论': 'bg-green-100 text-green-700', '复数CNN': 'bg-pink-100 text-pink-700', '复数激活': 'bg-yellow-100 text-yellow-700', '四元数': 'bg-violet-100 text-violet-700', '语音处理': 'bg-cyan-100 text-cyan-700', '架构组件': 'bg-fuchsia-100 text-fuchsia-700', '新兴方向': 'bg-sky-100 text-sky-700', '无线通信': 'bg-orange-100 text-orange-700'}};
                    return colors[category] || 'bg-gray-100 text-gray-700';
                }},
                
                initCharts() {{
                    const catCtx = document.getElementById('categoryChart');
                    if (catCtx) {{
                        new Chart(catCtx, {{
                            type: 'doughnut',
                            data: {{
                                labels: this.fieldCategories,
                                datasets: [{{ data: [12, 10, 11, 10, 15, 10, 12, 10, 8, 8, 20], backgroundColor: ['#667eea', '#f093fb', '#4facfe', '#43e97b', '#fa709a', '#feca57', '#5f27cd', '#00d2d3', '#ff9ff3', '#54a0ff', '#ee5a24'] }}]
                            }},
                            options: {{ responsive: true, maintainAspectRatio: false, plugins: {{ legend: {{ position: 'right', labels: {{ font: {{ size: 10 }} }} }} }} }}
                        }});
                    }}
                    const instCtx = document.getElementById('institutionChart');
                    if (instCtx) {{
                        new Chart(instCtx, {{
                            type: 'bar',
                            data: {{ labels: ['Mila', 'MIT', 'Southeast', 'Stevens', 'Münster', 'Avignon', 'Tampere', 'Texas A&M', 'Imperial', 'Cornell'], datasets: [{{ label: '学者数', data: [12, 8, 6, 5, 4, 4, 3, 3, 2, 2], backgroundColor: '#667eea' }}] }},
                            options: {{ responsive: true, maintainAspectRatio: false, plugins: {{ legend: {{ display: false }} }}, scales: {{ y: {{ beginAtZero: true, ticks: {{ stepSize: 2, font: {{ size: 10 }} }} }}, x: {{ ticks: {{ font: {{ size: 9 }} }} }} }} }}
                        }});
                    }}
                }}
            }};
        }}
    </script>
</body>
</html>'''

with open('blog/posts/2026/03/06/cvnn-scholars-landscape.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"Generated optimized HTML with {len(valid_scholars)} scholars")
