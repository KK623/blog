#!/usr/bin/env python3
"""
实时学习模块 - 从每次对话中学习并更新用户偏好
"""

import json
import re
from datetime import datetime
from pathlib import Path

class RealTimeLearner:
    """实时分析对话，提取用户偏好变化"""
    
    def __init__(self, memory_dir="/root/.openclaw/workspace/memory"):
        self.memory_dir = Path(memory_dir)
        self.system_file = self.memory_dir / "self-improvement-system.md"
        self.evolution_file = self.memory_dir / "user-preference-evolution.md"
        
    def analyze_conversation(self, user_messages, assistant_responses):
        """
        分析对话模式，提取学习点
        """
        insights = {
            "timestamp": datetime.now().isoformat(),
            "patterns_detected": [],
            "effectiveness_score": 0,
            "improvement_suggestions": []
        }
        
        # 分析用户追问模式
        for i, user_msg in enumerate(user_messages):
            if i > 0 and self._is_follow_up_question(user_msg, user_messages[i-1]):
                insights["patterns_detected"].append({
                    "type": "repeated_question",
                    "issue": "Previous response didn't fully address user need",
                    "user_msg": user_msg,
                    "suggestion": "Provide more direct result, less process explanation"
                })
        
        # 分析用户满意度信号
        last_user_msg = user_messages[-1] if user_messages else ""
        if self._is_satisfaction_signal(last_user_msg):
            insights["effectiveness_score"] = 1.0
        elif self._is_frustration_signal(last_user_msg):
            insights["effectiveness_score"] = -1.0
            insights["improvement_suggestions"].append("Reduce response length, increase action")
        
        # 分析响应延迟影响
        if len(user_messages) > 2:
            insights["patterns_detected"].append({
                "type": "conversation_flow",
                "observation": "User sends multiple messages when waiting",
                "suggestion": "Provide progress updates during long tasks"
            })
        
        return insights
    
    def _is_follow_up_question(self, current, previous):
        """检测是否是追问"""
        follow_up_patterns = [
            r"为什么.*",
            r"到底.*",
            r"还没.*",
            r".*呢\？",
            r"怎么样了"
        ]
        return any(re.match(pattern, current) for pattern in follow_up_patterns)
    
    def _is_satisfaction_signal(self, message):
        """检测满意信号"""
        satisfaction_signals = ["哦哦", "好", "OK", "可以", "行"]
        return any(sig in message for sig in satisfaction_signals) and len(message) < 10
    
    def _is_frustration_signal(self, message):
        """检测沮丧信号"""
        frustration_signals = ["？？", "！！", "太垃圾", "不行", "又错了", "怎么还没"]
        return any(sig in message for sig in frustration_signals)
    
    def update_user_profile(self, insights):
        """
        根据洞察更新用户档案
        """
        # 读取当前档案
        current_profile = self._read_system_file()
        
        # 如果有重复问题模式，更新响应策略
        for pattern in insights.get("patterns_detected", []):
            if pattern["type"] == "repeated_question":
                self._add_lesson_learned(pattern)
        
        # 更新效果评分历史
        if insights["effectiveness_score"] != 0:
            self._record_effectiveness(insights)
        
        return True
    
    def _read_system_file(self):
        """读取系统档案"""
        if self.system_file.exists():
            return self.system_file.read_text()
        return ""
    
    def _add_lesson_learned(self, pattern):
        """添加新学到的教训"""
        lesson_entry = f"""
### {datetime.now().strftime('%Y-%m-%d %H:%M')}
- **触发模式:** {pattern['user_msg']}
- **问题:** {pattern['issue']}
- **改进:** {pattern['suggestion']}
- **状态:** 🔄 持续观察
"""
        # 追加到历史教训部分
        content = self._read_system_file()
        if "## 历史教训" in content:
            # 在表格后添加
            content = content.replace(
                "---\n\n*此档案随每次对话自动更新",
                f"{lesson_entry}\n---\n\n*此档案随每次对话自动更新"
            )
            self.system_file.write_text(content)
    
    def _record_effectiveness(self, insights):
        """记录效果评分"""
        entry = f"""
| {datetime.now().strftime('%Y-%m-%d %H:%M')} | {insights['effectiveness_score']:.1f} | {len(insights['patterns_detected'])} | {insights['improvement_suggestions'][:1] or '无'} |
"""
        if self.evolution_file.exists():
            content = self.evolution_file.read_text()
        else:
            content = """# 用户偏好演进记录

| 时间 | 效果评分 | 检测模式数 | 主要改进点 |
|------|----------|------------|------------|
"""
        content += entry
        self.evolution_file.write_text(content)
    
    def get_contextual_memory(self):
        """
        获取当前对话的上下文记忆
        """
        profile = self._read_system_file()
        
        # 提取关键偏好
        key_preferences = {
            "communication_style": "直接高效，结果导向",
            "anger_triggers": ["？？", "！！”", "太垃圾"],
            "high_priority_words": ["检查一下", "怎么样了", "去修复"],
            "trust_signals": ["立即执行", "主动汇报", "验证完成"],
            "report_requirements": [
                "格式必须一致",
                "必须验证链接200",
                "必须说明时间范围"
            ]
        }
        
        return key_preferences

# 全局学习器实例
learner = RealTimeLearner()

if __name__ == "__main__":
    # 测试
    test_messages = ["怎么样了？", "为什么还没好？", "检查一下"]
    test_responses = ["正在处理", "马上好", "已修复"]
    
    insights = learner.analyze_conversation(test_messages, test_responses)
    print(json.dumps(insights, indent=2, ensure_ascii=False))
