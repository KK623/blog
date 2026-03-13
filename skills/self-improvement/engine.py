# Self-Improvement Dialogue System
# 自我提升对话系统 - 核心引擎

class SelfImprovementSystem:
    """
    用户个人专属的自我提升对话系统
    持续学习用户偏好，优化对话质量
    """
    
    def __init__(self, user_id="K"):
        self.user_id = user_id
        self.preference_profile = self._load_profile()
        self.conversation_history = []
        self.error_log = []
        
    def _load_profile(self):
        """加载用户偏好档案"""
        return {
            "communication_style": "direct_efficient",
            "priority_triggers": ["检查一下", "怎么样了", "去修复", "为什么"],
            "anger_signals": ["？？", "！！", "太垃圾", "为什么又是"],
            "trust_builders": ["立即执行", "主动汇报", "验证完成"],
            "report_format": {
                "llm": {"theme": "purple", "gradient": "#667eea → #764ba2"},
                "cvnn": {"theme": "green", "gradient": "#059669 → #10b981"}
            }
        }
    
    def analyze_input(self, user_input):
        """
        分析用户输入，识别情绪和意图
        """
        emotion_score = 0
        urgency_level = "normal"
        
        # 检测愤怒信号
        if any(signal in user_input for signal in self.preference_profile["anger_signals"]):
            emotion_score = -2
            urgency_level = "critical"
        
        # 检测高优先级触发词
        elif any(trigger in user_input for trigger in self.preference_profile["priority_triggers"]):
            urgency_level = "high"
        
        # 检测简短催促
        if len(user_input) < 10 and "？" in user_input:
            urgency_level = "high"
            
        return {
            "emotion": emotion_score,
            "urgency": urgency_level,
            "requires_immediate_action": urgency_level in ["critical", "high"]
        }
    
    def generate_response(self, user_input, context):
        """
        基于用户偏好生成响应
        """
        analysis = self.analyze_input(user_input)
        
        # 愤怒/不满时的响应策略
        if analysis["emotion"] < -1:
            return {
                "style": "action_first",
                "include_explanation": False,
                "tone": "concise_direct",
                "action_required": True
            }
        
        # 高优先级任务
        if analysis["urgency"] == "high":
            return {
                "style": "immediate_action",
                "include_status": True,
                "tone": "efficient",
                "proactive_follow_up": True
            }
        
        # 正常对话
        return {
            "style": "helpful_concise",
            "include_explanation": True,
            "tone": "natural",
            "anticipate_next_question": True
        }
    
    def learn_from_interaction(self, user_input, my_response, user_feedback):
        """
        从每次交互中学习
        """
        lesson = {
            "input_pattern": user_input,
            "response_type": my_response,
            "user_reaction": user_feedback,
            "timestamp": "auto",
            "improvement": None
        }
        
        # 如果用户再次追问同样问题，说明响应不够清晰
        if user_feedback and any(word in user_feedback for word in ["为什么", "到底", "还没"]):
            lesson["improvement"] = "需要更直接的结果展示，减少过程描述"
            self.error_log.append(lesson)
        
        # 如果用户简短回复后沉默，说明问题解决
        if user_feedback and len(user_feedback) < 5:
            lesson["improvement"] = "这种响应风格有效，继续保持"
        
        return lesson
    
    def proactive_check(self):
        """
        主动检查潜在问题
        """
        checks = []
        
        # 检查定时任务状态
        checks.append({
            "type": "cron_status",
            "action": "verify_file_exists",
            "fallback": "immediate_regenerate"
        })
        
        # 检查报告格式一致性
        checks.append({
            "type": "format_compliance",
            "action": "validate_against_template",
            "fallback": "auto_reformat"
        })
        
        # 检查链接有效性
        checks.append({
            "type": "link_validation",
            "action": "curl_check_200",
            "fallback": "report_immediately"
        })
        
        return checks
    
    def get_memory_prompt(self):
        """
        生成用于对话的内存提示
        """
        return f"""
[SYSTEM CONTEXT - Self-Improvement Dialogue System]

用户: {self.user_id}
沟通风格: 直接高效，结果导向

核心原则:
1. 用行动代替解释 - 用户愤怒时立即修复，不辩解
2. 验证后才汇报 - 任何任务完成后必须curl验证200
3. 主动发现问题 - 不等待用户询问才汇报问题
4. 格式严格一致 - 所有报告使用统一模板

情绪响应:
- 看到"？？""！！”"太垃圾" → 立即行动，不解释
- 看到"检查一下""怎么样了" → 立即执行+状态汇报
- 看到"为什么" → 快速解释+立即解决

报告标准:
- LLM Research: 紫色主题，亮色背景，返回链接
- CVNN Research: 绿色主题，亮色背景，返回链接
- 必须包含: 时间范围说明、信源验证、PDF链接

历史教训:
- 绝不信任系统报告，必须手动验证文件
- 宁可少做一篇，不做空壳内容
- 推送后必须验证用户可见，不能说"应该可以了"
- 定时任务失败必须立即补做，不等待用户提醒

[END CONTEXT]
"""

# 系统实例
sis = SelfImprovementSystem(user_id="K")
