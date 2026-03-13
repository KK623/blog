# TOOLS.md - 本地笔记

## 任务完成标准（强制执行）

### 通用原则
**任务完成 = 用户可验证的结果**

每次完成任务前必须执行验证步骤，不能直接说"做好了"。

---

### 网页/博客文章
- [ ] 文件写入磁盘（write/edit完成）
- [ ] 文件存在验证（ls -la 确认）
- [ ] 推送到GitHub（git add/commit/push）
- [ ] 网页可访问验证（web_fetch 返回200）
- [ ] 提供完整URL给用户
- [ ] 说明可能的缓存问题

### 配置文件
- [ ] 文件写入/修改完成
- [ ] 语法检查（如JSON/YAML有效）
- [ ] 服务重启/加载验证
- [ ] 提供验证命令给用户

### 代码分析
- [ ] 读取目标文件
- [ ] 分析完成
- [ ] 输出文件创建（如有）
- [ ] 提供文件路径或展示关键内容

---

## 常用验证命令

```bash
# 文件存在
ls -la /path/to/file

# 网页可访问
curl -s -o /dev/null -w "%{http_code}" https://example.com

# JSON有效
python3 -m json.tool < config.json

# 服务运行
ps aux | grep service_name
```

---

## 历史教训

### 2026-03-10 EulerFormer文章
- 错误：推送GitHub后就说"做好了"，没考虑Pages部署延迟
- 改进：web_fetch验证返回200后再告知

### 2026-03-10 A股监控
- 错误：服务启动就说"成功"，没验证公网访问
- 改进：curl验证外网可访问后再告知
