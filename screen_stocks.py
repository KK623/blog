#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A股涨停潜力股快速筛选器
基于实时数据快速筛选
"""

import requests
import json
import pandas as pd
from datetime import datetime
import time

class QuickScreener:
    """快速筛选器"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def log(self, msg):
        print(msg, flush=True)
    
    def get_all_stocks(self) -> pd.DataFrame:
        """获取全市场A股列表"""
        all_stocks = []
        
        for page in range(1, 60):
            url = "http://push2.eastmoney.com/api/qt/clist/get"
            params = {
                'pn': page, 'pz': 100, 'po': 1, 'np': 1,
                'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
                'fltt': 2, 'invt': 2, 'fid': 'f12',
                'fs': 'm:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23',
                'fields': 'f12,f14,f2,f3,f5,f6,f8,f20,f9,f23,f11,f15,f16,f17,f18,f34,f35',
                '_': int(time.time() * 1000)
            }
            
            try:
                resp = self.session.get(url, params=params, timeout=10)
                data = resp.json()
                
                if data.get('data') and data['data'].get('diff'):
                    for item in data['data']['diff']:
                        stock = {
                            'code': item.get('f12', ''),
                            'name': item.get('f14', ''),
                            'price': float(item.get('f2', 0)) if item.get('f2') not in ['-', None] else 0,
                            'change_pct': float(item.get('f3', 0)) if item.get('f3') not in ['-', None] else 0,
                            'volume': float(item.get('f5', 0)) if item.get('f5') not in ['-', None] else 0,
                            'amount': float(item.get('f6', 0)) if item.get('f6') not in ['-', None] else 0,
                            'turnover': float(item.get('f8', 0)) if item.get('f8') not in ['-', None] else 0,
                            'market_cap': float(item.get('f20', 0)) if item.get('f20') not in ['-', None] else 0,
                            'pe': float(item.get('f9', 0)) if item.get('f9') not in ['-', None] else 0,
                            'amplitude': float(item.get('f34', 0)) if item.get('f34') not in ['-', None] else 0,
                            'high': float(item.get('f15', 0)) if item.get('f15') not in ['-', None] else 0,
                            'low': float(item.get('f16', 0)) if item.get('f16') not in ['-', None] else 0,
                            'open': float(item.get('f17', 0)) if item.get('f17') not in ['-', None] else 0,
                            'pre_close': float(item.get('f18', 0)) if item.get('f18') not in ['-', None] else 0,
                        }
                        if stock['code']:
                            all_stocks.append(stock)
                    
                    if len(data['data']['diff']) < 100:
                        break
            except Exception as e:
                self.log(f"  获取第{page}页出错: {e}")
                break
            
            if page % 10 == 0:
                self.log(f"  已获取 {len(all_stocks)} 只股票...")
            time.sleep(0.02)
        
        df = pd.DataFrame(all_stocks)
        df['board'] = df['code'].apply(self._classify_board)
        return df
    
    def _classify_board(self, code: str) -> str:
        if code.startswith('3'):
            return '创业板'
        elif code.startswith('688'):
            return '科创板'
        elif code.startswith('6'):
            return '沪市主板'
        elif code.startswith('0') or code.startswith('00'):
            return '深市主板'
        return '其他'
    
    def get_hot_sectors(self) -> list:
        """获取热门板块"""
        try:
            url = "http://push2.eastmoney.com/api/qt/clist/get"
            params = {
                'pn': 1, 'pz': 30, 'po': 1, 'np': 1,
                'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
                'fltt': 2, 'invt': 2, 'fid': 'f3',
                'fs': 'm:90+t:2',
                'fields': 'f12,f14,f3',
                '_': int(time.time() * 1000)
            }
            
            resp = self.session.get(url, params=params, timeout=10)
            data = resp.json()
            
            sectors = []
            excluded = ['石油', '石化', '油气', '煤炭']
            
            if data.get('data') and data['data'].get('diff'):
                for item in data['data']['diff']:
                    name = item.get('f14', '')
                    if not any(k in name for k in excluded):
                        sectors.append({
                            'code': item.get('f12', ''),
                            'name': name,
                            'change_pct': item.get('f3', 0),
                        })
            return sectors[:15]
        except Exception as e:
            return []
    
    def get_sector_top_stocks(self, sector_code: str) -> list:
        """获取板块领涨股"""
        try:
            url = "http://push2.eastmoney.com/api/qt/clist/get"
            params = {
                'pn': 1, 'pz': 50, 'po': 1, 'np': 1,
                'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
                'fltt': 2, 'invt': 2, 'fid': 'f3',
                'fs': f'b:{sector_code}',
                'fields': 'f12,f14,f3,f8,f6,f20',
                '_': int(time.time() * 1000)
            }
            
            resp = self.session.get(url, params=params, timeout=10)
            data = resp.json()
            
            stocks = []
            if data.get('data') and data['data'].get('diff'):
                for item in data['data']['diff'][:10]:  # 取前10
                    stocks.append({
                        'code': item.get('f12', ''),
                        'name': item.get('f14', ''),
                        'change_pct': item.get('f3', 0),
                        'turnover': item.get('f8', 0),
                        'amount': item.get('f6', 0),
                    })
            return stocks
        except:
            return []
    
    def screen_by_conditions(self, df: pd.DataFrame, board_type: str) -> list:
        """基于条件筛选"""
        candidates = []
        
        # 基础过滤
        df = df[(df['price'] > 5) & (df['price'] < 60)].copy()
        df = df[df['amount'] > 100000000].copy()  # 成交额1亿以上
        df = df[(df['turnover'] >= 3) & (df['turnover'] <= 25)].copy()  # 换手率3-25%
        df = df[df['amplitude'] >= 3].copy()  # 振幅3%以上（活跃）
        df = df[df['market_cap'] > 0].copy()
        
        # 今日表现（有上涨动能但未涨停）
        df = df[(df['change_pct'] > 0) & (df['change_pct'] < 18)].copy()
        
        # 计算涨停潜力分
        for _, row in df.iterrows():
            score = 0
            
            # 涨幅适中（有动能但未过热）
            if 2 <= row['change_pct'] <= 8:
                score += 25
            elif 1 <= row['change_pct'] < 2:
                score += 15
            
            # 换手率适中（活跃但不过度）
            if 5 <= row['turnover'] <= 15:
                score += 25
            elif 3 <= row['turnover'] < 5:
                score += 15
            
            # 成交额大（资金关注）
            if row['amount'] > 500000000:  # 5亿以上
                score += 20
            elif row['amount'] > 200000000:  # 2亿以上
                score += 10
            
            # 振幅大（活跃）
            if row['amplitude'] >= 5:
                score += 15
            
            # 市值适中（容易拉升）
            market_cap_yi = row['market_cap'] / 100000000
            if 50 <= market_cap_yi <= 300:
                score += 15
            elif 20 <= market_cap_yi < 50:
                score += 10
            
            candidate = {
                'code': row['code'],
                'name': row['name'],
                'board': row['board'],
                'price': row['price'],
                'change_pct': row['change_pct'],
                'turnover': row['turnover'],
                'amount': row['amount'] / 100000000,
                'market_cap': row['market_cap'] / 100000000,
                'amplitude': row['amplitude'],
                'limit_up_target': row['price'] * (1.2 if board_type == '创业板' else 1.1),
                'total_score': score,
            }
            candidates.append(candidate)
        
        # 按评分排序
        candidates.sort(key=lambda x: x['total_score'], reverse=True)
        return candidates[:10]
    
    def run(self):
        """运行筛选"""
        self.log("=" * 60)
        self.log("A股涨停潜力股快速筛选")
        self.log(f"时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.log("=" * 60)
        
        # 获取数据
        self.log("\n📊 获取全市场数据...")
        all_stocks = self.get_all_stocks()
        self.log(f"获取到 {len(all_stocks)} 只股票")
        
        if len(all_stocks) == 0:
            return {'创业板': [], '主板': []}
        
        # 分离板块
        cyb = all_stocks[all_stocks['board'] == '创业板'].copy()
        zb = all_stocks[all_stocks['board'].isin(['沪市主板', '深市主板'])].copy()
        
        self.log(f"创业板: {len(cyb)} 只 | 主板: {len(zb)} 只")
        
        # 筛选
        self.log("\n🔍 筛选创业板标的...")
        cyb_results = self.screen_by_conditions(cyb, '创业板')
        self.log(f"找到 {len(cyb_results)} 只候选")
        
        self.log("\n🔍 筛选主板标的...")
        zb_results = self.screen_by_conditions(zb, '主板')
        self.log(f"找到 {len(zb_results)} 只候选")
        
        # 输出结果
        self.log("\n" + "=" * 60)
        self.log("📋 最终推荐结果")
        self.log("=" * 60)
        
        results = {
            '创业板': cyb_results,
            '主板': zb_results
        }
        
        for board_type, stocks in results.items():
            limit_pct = '20%' if board_type == '创业板' else '10%'
            self.log(f"\n【{board_type}】今日{limit_pct}涨停潜力标的:")
            self.log("-" * 60)
            
            if not stocks:
                self.log("  暂无符合条件的标的")
                continue
            
            for i, s in enumerate(stocks[:2], 1):
                up_room = ((s['limit_up_target'] / s['price']) - 1) * 100
                self.log(f"\n  {i}. {s['name']} ({s['code']})")
                self.log(f"     💰 当前价: ¥{s['price']:.2f} → 涨停价: ¥{s['limit_up_target']:.2f} (+{up_room:.0f}%)")
                self.log(f"     📈 今日涨幅: {s['change_pct']:+.2f}%")
                self.log(f"     🔄 换手率: {s['turnover']:.2f}%")
                self.log(f"     💵 成交额: {s['amount']:.2f}亿")
                self.log(f"     📊 市值: {s['market_cap']:.2f}亿")
                self.log(f"     ⚡ 振幅: {s['amplitude']:.2f}%")
                self.log(f"     ⭐ 综合评分: {s['total_score']:.0f}/100")
        
        # 保存结果
        with open('/root/.openclaw/workspace/screening_result.json', 'w', encoding='utf-8') as f:
            json.dump({
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'results': results
            }, f, ensure_ascii=False, indent=2)
        
        self.log("\n✅ 详细结果已保存")
        return results

if __name__ == '__main__':
    screener = QuickScreener()
    screener.run()
