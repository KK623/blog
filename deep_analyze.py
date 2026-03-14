#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A股标的深度分析
对筛选出的股票进行多维度详细分析
"""

import requests
import json
import pandas as pd
from datetime import datetime, timedelta
import time

class DeepAnalyzer:
    """深度分析器"""
    
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def log(self, msg):
        print(msg, flush=True)
    
    def get_stock_detail(self, code: str) -> dict:
        """获取股票详细信息"""
        try:
            # 判断市场
            if code.startswith('6'):
                secid = f"1.{code}"
            else:
                secid = f"0.{code}"
            
            url = "http://push2.eastmoney.com/api/qt/stock/get"
            params = {
                'secid': secid,
                'ut': 'fa5fd1943c7b386f172d6893dbfba10b',
                'fields': 'f43,f44,f45,f46,f47,f48,f49,f50,f51,f52,f57,f58,f60,f107,f111,f112,f113,f114,f115,f116,f117,f118,f119,f120,f121,f122,f123,f124,f125,f126,f127,f128,f129,f130,f131,f132,f133,f134,f135,f136,f137,f138,f139,f140,f141,f142,f143,f144,f145,f146,f147,f148,f149,f150,f151,f152,f153,f154,f155,f156,f157,f158,f159,f160,f161,f162,f163,f164,f165,f166,f167,f168,f169,f170,f171,f172,f173,f174,f175,f176,f177,f178,f179,f180,f181,f182,f183,f184,f185,f186,f187',
                '_': int(time.time() * 1000)
            }
            
            resp = self.session.get(url, params=params, timeout=10)
            data = resp.json()
            
            if data.get('data'):
                d = data['data']
                return {
                    'name': d.get('f58', ''),
                    'industry': d.get('f20', ''),  # 所属行业
                    'concept': d.get('f128', ''),   # 所属概念
                    'total_cap': d.get('f116', 0),  # 总市值
                    'float_cap': d.get('f117', 0),  # 流通市值
                    'pe': d.get('f162', 0),         # 市盈率
                    'pb': d.get('f167', 0),         # 市净率
                    'roe': d.get('f173', 0),        # ROE
                    'revenue_growth': d.get('f174', 0),  # 营收增长率
                    'profit_growth': d.get('f175', 0),   # 净利润增长率
                }
            return {}
        except Exception as e:
            return {}
    
    def get_stock_history(self, code: str, days: int = 30) -> pd.DataFrame:
        """获取历史K线数据"""
        try:
            if code.startswith('6'):
                secid = f"1.{code}"
            else:
                secid = f"0.{code}"
            
            end_date = datetime.now().strftime('%Y%m%d')
            start_date = (datetime.now() - timedelta(days=days*2)).strftime('%Y%m%d')
            
            url = "http://push2his.eastmoney.com/api/qt/stock/kline/get"
            params = {
                'secid': secid,
                'ut': 'fa5fd1943c7b386f172d6893dbfba10b',
                'fields1': 'f1,f2,f3,f4,f5,f6',
                'fields2': 'f51,f52,f53,f54,f55,f56,f57,f58,f59,f60,f61',
                'klt': '101',
                'fqt': '0',
                'beg': start_date,
                'end': end_date,
                '_': int(time.time() * 1000)
            }
            
            resp = self.session.get(url, params=params, timeout=10)
            data = resp.json()
            
            if data.get('data') and data['data'].get('klines'):
                klines = data['data']['klines']
                rows = []
                for line in klines:
                    parts = line.split(',')
                    rows.append({
                        'date': parts[0],
                        'open': float(parts[1]),
                        'close': float(parts[2]),
                        'high': float(parts[3]),
                        'low': float(parts[4]),
                        'volume': float(parts[5]),
                        'amount': float(parts[6]),
                        'amplitude': float(parts[7]),
                        'change_pct': float(parts[8]),
                        'change': float(parts[9]),
                        'turnover': float(parts[10]) if len(parts) > 10 else 0,
                    })
                return pd.DataFrame(rows)
            return None
        except:
            return None
    
    def get_hot_sectors(self) -> list:
        """获取热门板块"""
        try:
            url = "http://push2.eastmoney.com/api/qt/clist/get"
            params = {
                'pn': 1, 'pz': 50, 'po': 1, 'np': 1,
                'ut': 'bd1d9ddb04089700cf9c27f6f7426281',
                'fltt': 2, 'invt': 2, 'fid': 'f3',
                'fs': 'm:90+t:2',
                'fields': 'f12,f14,f3,f5,f6,f8,f104,f105',
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
                            'volume': item.get('f5', 0),
                            'amount': item.get('f6', 0),
                            'turnover': item.get('f8', 0),
                            'up_count': item.get('f104', 0),  # 上涨家数
                            'down_count': item.get('f105', 0), # 下跌家数
                        })
            return sectors[:20]
        except:
            return []
    
    def get_stock_sectors(self, code: str) -> list:
        """获取股票所属板块"""
        try:
            url = "http://push2.eastmoney.com/api/qt/stock/get"
            if code.startswith('6'):
                secid = f"1.{code}"
            else:
                secid = f"0.{code}"
            
            params = {
                'secid': secid,
                'ut': 'fa5fd1943c7b386f172d6893dbfba10b',
                'fields': 'f20,f128',
                '_': int(time.time() * 1000)
            }
            
            resp = self.session.get(url, params=params, timeout=10)
            data = resp.json()
            
            sectors = []
            if data.get('data'):
                industry = data['data'].get('f20', '')
                concept = data['data'].get('f128', '')
                if industry:
                    sectors.extend([s.strip() for s in str(industry).split(',') if s.strip()])
                if concept:
                    sectors.extend([s.strip() for s in str(concept).split(',') if s.strip()])
            return sectors
        except:
            return []
    
    def analyze_limit_up_history(self, code: str, df: pd.DataFrame) -> dict:
        """分析涨停历史"""
        if df is None or df.empty:
            return {}
        
        # 判断涨停标准
        limit_pct = 19.9 if code.startswith('3') or code.startswith('68') else 9.9
        
        # 近30天涨停次数
        recent = df.tail(30)
        limit_ups = recent[recent['change_pct'] >= limit_pct]
        limit_up_count = len(limit_ups)
        
        # 最近一次涨停日期
        last_limit_up = limit_ups.iloc[-1]['date'] if len(limit_ups) > 0 else None
        
        # 近5日最大涨幅
        recent_5d = recent.tail(5)
        max_gain_5d = recent_5d['change_pct'].max()
        
        # 近10日最大涨幅
        recent_10d = recent.tail(10)
        max_gain_10d = recent_10d['change_pct'].max()
        
        # 连板潜力分析
        consecutive_days = 0
        for i in range(len(recent)-1, -1, -1):
            if recent.iloc[i]['change_pct'] > 0:
                consecutive_days += 1
            else:
                break
        
        return {
            'limit_up_30d': limit_up_count,
            'last_limit_up': last_limit_up,
            'max_gain_5d': max_gain_5d,
            'max_gain_10d': max_gain_10d,
            'consecutive_up_days': consecutive_days,
        }
    
    def analyze_trend(self, df: pd.DataFrame) -> dict:
        """分析趋势"""
        if df is None or len(df) < 20:
            return {}
        
        # 计算均线
        df['ma5'] = df['close'].rolling(5).mean()
        df['ma10'] = df['close'].rolling(10).mean()
        df['ma20'] = df['close'].rolling(20).mean()
        df['ma30'] = df['close'].rolling(30).mean()
        
        latest = df.iloc[-1]
        
        # 趋势判断
        short_trend = latest['ma5'] > latest['ma10']
        mid_trend = latest['ma10'] > latest['ma20']
        long_trend = latest['ma20'] > latest['ma30'] if not pd.isna(latest['ma30']) else True
        
        # 均线多头排列
        ma_bullish = latest['ma5'] > latest['ma10'] > latest['ma20']
        
        # 价格位置（相对于均线）
        above_ma5 = latest['close'] > latest['ma5']
        above_ma10 = latest['close'] > latest['ma10']
        above_ma20 = latest['close'] > latest['ma20']
        
        # 成交量分析
        recent_vol = df['volume'].tail(5).mean()
        prev_vol = df['volume'].tail(10).head(5).mean()
        volume_expansion = recent_vol > prev_vol * 1.5 if prev_vol > 0 else False
        vol_ratio = recent_vol / prev_vol if prev_vol > 0 else 1
        
        # 波动率
        volatility = df['change_pct'].tail(20).std()
        
        return {
            'short_trend': short_trend,
            'mid_trend': mid_trend,
            'long_trend': long_trend,
            'ma_bullish': ma_bullish,
            'above_ma5': above_ma5,
            'above_ma10': above_ma10,
            'above_ma20': above_ma20,
            'volume_expansion': volume_expansion,
            'volume_ratio': vol_ratio,
            'volatility': volatility,
            'current_price': latest['close'],
            'ma5': latest['ma5'],
            'ma10': latest['ma10'],
            'ma20': latest['ma20'],
        }
    
    def analyze_support_resistance(self, df: pd.DataFrame) -> dict:
        """分析支撑阻力位"""
        if df is None or len(df) < 20:
            return {}
        
        recent = df.tail(20)
        
        # 近期高点/低点
        recent_high = recent['high'].max()
        recent_low = recent['low'].min()
        
        # 当前价格位置
        current = df.iloc[-1]['close']
        position = (current - recent_low) / (recent_high - recent_low) * 100 if recent_high > recent_low else 50
        
        # 突破判断
        near_high = current > recent_high * 0.97  # 接近近期高点3%以内
        
        return {
            'recent_high': recent_high,
            'recent_low': recent_low,
            'position_pct': position,
            'near_high': near_high,
        }
    
    def analyze_deep(self, code: str, name: str, board_type: str) -> dict:
        """深度分析单只股票"""
        self.log(f"\n📊 深度分析: {name} ({code})")
        
        # 获取历史数据
        df = self.get_stock_history(code, 60)
        if df is None or df.empty:
            return None
        
        # 基本信息
        detail = self.get_stock_detail(code)
        
        # 所属板块
        sectors = self.get_stock_sectors(code)
        
        # 涨停历史
        limit_history = self.analyze_limit_up_history(code, df)
        
        # 趋势分析
        trend = self.analyze_trend(df)
        
        # 支撑阻力
        sr = self.analyze_support_resistance(df)
        
        # 涨停目标价
        current_price = trend.get('current_price', 0)
        limit_up_price = current_price * (1.2 if board_type == '创业板' else 1.1)
        
        return {
            'code': code,
            'name': name,
            'board_type': board_type,
            'current_price': current_price,
            'limit_up_price': limit_up_price,
            'up_room_pct': ((limit_up_price / current_price) - 1) * 100 if current_price > 0 else 0,
            'detail': detail,
            'sectors': sectors,
            'limit_history': limit_history,
            'trend': trend,
            'support_resistance': sr,
        }
    
    def print_analysis(self, result: dict):
        """打印分析结果"""
        if not result:
            return
        
        r = result
        self.log("=" * 70)
        self.log(f"📈 {r['name']} ({r['code']}) - {r['board_type']}")
        self.log("=" * 70)
        
        # 价格信息
        self.log(f"\n💰 价格信息:")
        self.log(f"   当前价: ¥{r['current_price']:.2f}")
        self.log(f"   涨停价: ¥{r['limit_up_price']:.2f} (+{r['up_room_pct']:.0f}%)")
        
        # 所属板块
        if r['sectors']:
            self.log(f"\n🏷️ 所属板块/概念:")
            self.log(f"   {', '.join(r['sectors'][:8])}")
        
        # 涨停基因
        lh = r['limit_history']
        if lh:
            self.log(f"\n🔥 涨停基因:")
            self.log(f"   近30天涨停次数: {lh.get('limit_up_30d', 0)} 次")
            if lh.get('last_limit_up'):
                self.log(f"   最近一次涨停: {lh['last_limit_up']}")
            self.log(f"   近5日最大涨幅: {lh.get('max_gain_5d', 0):+.2f}%")
            self.log(f"   近10日最大涨幅: {lh.get('max_gain_10d', 0):+.2f}%")
            self.log(f"   连续上涨天数: {lh.get('consecutive_up_days', 0)} 天")
        
        # 趋势分析
        t = r['trend']
        if t:
            self.log(f"\n📊 趋势分析:")
            self.log(f"   短期趋势: {'↗️ 向上' if t.get('short_trend') else '↘️ 向下'}")
            self.log(f"   中期趋势: {'↗️ 向上' if t.get('mid_trend') else '↘️ 向下'}")
            self.log(f"   均线多头排列: {'✅ 是' if t.get('ma_bullish') else '❌ 否'}")
            self.log(f"   位于MA5之上: {'✅ 是' if t.get('above_ma5') else '❌ 否'}")
            self.log(f"   成交量放大: {'✅ 是' if t.get('volume_expansion') else '❌ 否'} (比值: {t.get('volume_ratio', 1):.2f}x)")
            self.log(f"   20日波动率: {t.get('volatility', 0):.2f}%")
            self.log(f"   MA5: ¥{t.get('ma5', 0):.2f} | MA10: ¥{t.get('ma10', 0):.2f} | MA20: ¥{t.get('ma20', 0):.2f}")
        
        # 支撑阻力
        sr = r['support_resistance']
        if sr:
            self.log(f"\n🎯 支撑阻力:")
            self.log(f"   近20日高点: ¥{sr.get('recent_high', 0):.2f}")
            self.log(f"   近20日低点: ¥{sr.get('recent_low', 0):.2f}")
            self.log(f"   当前位置: {sr.get('position_pct', 50):.1f}% (0%=低点, 100%=高点)")
            self.log(f"   接近突破: {'✅ 是' if sr.get('near_high') else '❌ 否'}")
        
        # 基本面
        d = r.get('detail', {})
        if d:
            self.log(f"\n📋 基本面:")
            self.log(f"   总市值: {d.get('total_cap', 0)/100000000:.2f} 亿")
            self.log(f"   流通市值: {d.get('float_cap', 0)/100000000:.2f} 亿")
            self.log(f"   市盈率(PE): {d.get('pe', 0):.2f}")
            self.log(f"   市净率(PB): {d.get('pb', 0):.2f}")
            if d.get('roe'):
                self.log(f"   ROE: {d.get('roe', 0):.2f}%")
        
        self.log("")
    
    def run(self):
        """运行深度分析"""
        # 待分析的股票
        stocks_to_analyze = [
            ('301389', '隆扬电子', '创业板'),
            ('301307', '美利信', '创业板'),
            ('605305', '中际联合', '主板'),
            ('603716', '塞力医疗', '主板'),
        ]
        
        self.log("=" * 70)
        self.log("A股标的深度分析报告")
        self.log(f"分析时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.log("=" * 70)
        
        # 获取热门板块
        self.log("\n📊 当前热门板块 (Top 15):")
        hot_sectors = self.get_hot_sectors()
        for i, s in enumerate(hot_sectors[:15], 1):
            up_ratio = s['up_count'] / (s['up_count'] + s['down_count']) * 100 if (s['up_count'] + s['down_count']) > 0 else 0
            self.log(f"   {i}. {s['name']}: {s['change_pct']:+.2f}% (涨{s['up_count']}家/跌{s['down_count']}家)")
        
        # 深度分析每只股票
        results = []
        for code, name, board_type in stocks_to_analyze:
            result = self.analyze_deep(code, name, board_type)
            if result:
                self.print_analysis(result)
                results.append(result)
            time.sleep(0.3)
        
        # 汇总对比
        self.log("\n" + "=" * 70)
        self.log("📊 四只标的横向对比")
        self.log("=" * 70)
        
        self.log(f"\n{'名称':<12} {'涨停次数':<10} {'连涨天数':<10} {'均线多头':<10} {'成交量':<10} {'突破前高':<10}")
        self.log("-" * 70)
        
        for r in results:
            name = r['name'][:10]
            limit_ups = r['limit_history'].get('limit_up_30d', 0)
            consec = r['limit_history'].get('consecutive_up_days', 0)
            bullish = '✅' if r['trend'].get('ma_bullish') else '❌'
            vol = f"{r['trend'].get('volume_ratio', 1):.1f}x"
            near_high = '✅' if r['support_resistance'].get('near_high') else '❌'
            self.log(f"{name:<12} {limit_ups:<10} {consec:<10} {bullish:<10} {vol:<10} {near_high:<10}")
        
        # 综合评级
        self.log("\n" + "=" * 70)
        self.log("⭐ 综合评级与建议")
        self.log("=" * 70)
        
        for r in results:
            score = 0
            reasons = []
            
            # 涨停基因
            if r['limit_history'].get('limit_up_30d', 0) >= 2:
                score += 25
                reasons.append("涨停基因强")
            elif r['limit_history'].get('limit_up_30d', 0) >= 1:
                score += 15
                reasons.append("有涨停记录")
            
            # 趋势
            if r['trend'].get('ma_bullish'):
                score += 25
                reasons.append("均线多头排列")
            elif r['trend'].get('short_trend'):
                score += 15
                reasons.append("短期趋势向上")
            
            # 成交量
            if r['trend'].get('volume_expansion'):
                score += 20
                reasons.append("成交量放大")
            
            # 突破
            if r['support_resistance'].get('near_high'):
                score += 20
                reasons.append("接近前高/突破在即")
            elif r['support_resistance'].get('position_pct', 50) > 60:
                score += 10
                reasons.append("处于高位")
            
            # 连涨
            if r['limit_history'].get('consecutive_up_days', 0) >= 2:
                score += 10
                reasons.append("连续上涨")
            
            rating = "🔥强烈推荐" if score >= 80 else "⭐推荐" if score >= 60 else "⭕观望"
            
            self.log(f"\n{r['name']} ({r['code']})")
            self.log(f"   综合评分: {score}/100")
            self.log(f"   评级: {rating}")
            self.log(f"   核心亮点: {' | '.join(reasons[:4])}")
            self.log(f"   操作建议: {'适合激进操作' if score >= 80 else '可轻仓参与' if score >= 60 else '建议观望'}")
        
        self.log("\n" + "=" * 70)
        self.log("⚠️ 风险提示")
        self.log("=" * 70)
        self.log("1. 以上分析基于技术面和资金面，不构成投资建议")
        self.log("2. 涨停预测存在不确定性，需结合当日市场情绪")
        self.log("3. 建议设置止损位（如跌破MA5或亏损5%）")
        self.log("4. 控制仓位，分散风险")
        self.log("=" * 70)

if __name__ == '__main__':
    analyzer = DeepAnalyzer()
    analyzer.run()
