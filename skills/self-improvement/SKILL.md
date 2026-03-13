---
name: self-improvement-dialogue
description: |
  用户个人专属的自我提升对话系统。
  持续学习用户沟通风格、偏好和反馈，自动优化响应质量。
  记住历史教训，避免重复犯错，预判用户需求。
triggers:
  - always_active: true
    priority: high
memory_files:
  - memory/self-improvement-system.md
  - memory/user-preference-evolution.md
---

# Self-Improvement Dialogue System

## Overview

This skill creates a personalized self-improvement dialogue system that:
1. **Learns user preferences** from every interaction
2. **Adapts communication style** to match user expectations
3. **Prevents repeated mistakes** by referencing historical errors
4. **Proactively identifies issues** before user notices

## Key Components

### 1. User Preference Engine (`engine.py`)
- Analyzes user input patterns
- Detects emotional signals (anger, urgency, satisfaction)
- Generates appropriate response strategies
- Learns from each interaction

### 2. Memory System
- `memory/self-improvement-system.md` - Core user profile
- `memory/user-preference-evolution.md` - Change history
- `memory/error-lessons-learned.md` - Historical mistakes

### 3. Proactive Checks
Before every response, the system checks:
- Task completion verification status
- Format compliance against templates
- Link validity (HTTP 200)
- Cron job status

## Usage

The system automatically activates for every conversation. To query the system:

```python
from skills.self-improvement.engine import sis

# Get current user profile
profile = sis.preference_profile

# Analyze user input
analysis = sis.analyze_input("检查一下报告")
# Returns: {"emotion": 0, "urgency": "high", "requires_immediate_action": True}

# Get response strategy
strategy = sis.generate_response("检查一下", context)
# Returns: {"style": "immediate_action", "include_status": True, ...}
```

## Response Strategies

### Critical (User Angry)
- No explanations
- Immediate action
- Result-focused reply

### High Priority
- Immediate execution
- Status included
- Proactive follow-up

### Normal
- Helpful and concise
- Natural tone
- Anticipate next question

## Continuous Improvement

The system tracks:
- User satisfaction signals
- Repeated question patterns
- Error recurrence
- Response effectiveness

## Integration

This skill is automatically loaded by the main agent. The engine's `get_memory_prompt()` method injects user preference context into every conversation.
