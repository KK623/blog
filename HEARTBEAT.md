# HEARTBEAT.md - 定时任务检查清单

## Heartbeat 检测逻辑

**每次Heartbeat执行时，我会**：
1. 读取当天的memory/YYYY-MM-DD.md，查看任务记录
2. 检查GitHub上报告文件是否存在
3. 检查飞书消息是否已发送
4. **如未完成，立即补做**

---

## 每日检查任务

### 凌晨任务（Cron执行）
- **LLM Research Daily**: 每天 03:00
- **CVNN Research Daily**: 每天 04:00

**Heartbeat检测**：早上7:30-8:30检查
- 检查 /blog/posts/YYYY/MM/DD/llm-research-*.html 是否存在
- 检查 /blog/posts/YYYY/MM/DD/cvnn-research-*.html 是否存在
- **如不存在 → 立即手动补做**

### 定时任务（Cron执行）
- **Backup OpenClaw Config**: 每天 08:00, 20:00
- **Daily Report to K**: 每天 21:00

**Heartbeat检测**：
- 检查备份文件是否存在
- 检查日报是否已发送
- **如未完成 → 立即补做**

---

## 执行策略

### 早上检查 (06:00-06:30)
1. 检查LLM报告是否完成（文件存在？GitHub已推送？）
2. 检查CVNN报告是否完成（文件存在？GitHub已推送？）
3. 检查Backup是否完成
4. **发现未完成 → 立即补做 → 发送飞书通知**

### 晚上检查 (20:30)
1. 检查Backup是否完成
2. 检查Daily Report是否需要准备
3. **发现未完成 → 立即补做 → 发送飞书通知**

---

## 关键原则

**不依赖Cron的成功通知**！
- Cron可能失败且不发通知
- Heartbeat主动检查结果
- **任务完成标准：文件存在 + GitHub已推送 + 飞书已通知**

---
*更新于 2026-03-09*