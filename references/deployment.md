# 部署指南

## 快速开始（5 分钟）

### 步骤 1：确认技能已安装

```bash
openclaw skills list
```

应该看到：
```
✓ ready | 📦 multi-search-engine
```

### 步骤 2：获取 Brave API Key

1. 访问 https://brave.com/search/api/
2. 注册/登录账号
3. 点击 "Get Started" 或 "Create API Key"
4. 填写基本信息（免费套餐：每月 2000 次搜索）
5. 复制生成的 API key（格式类似：`BSAxxxxxxxxxxxxxxxx`）

### 步骤 3：配置 API Key

**方法 A：使用 OpenClaw 命令（推荐）**

```bash
openclaw configure --section web
```

按提示粘贴 API key。

**方法 B：手动设置环境变量**

Windows PowerShell:
```powershell
$env:BRAVE_API_KEY="你的_API_Key"
```

Windows 永久设置:
1. 右键"此电脑" → 属性
2. 高级系统设置 → 环境变量
3. 新建系统变量：
   - 变量名：`BRAVE_API_KEY`
   - 变量值：`你的_API_Key`
4. 重启 OpenClaw 网关

### 步骤 4：验证配置

运行测试脚本：
```bash
cd skills/multi-search-engine
python scripts/test_search.py
```

或在 OpenClaw 中直接测试：
```
帮我搜索一下"AI 新闻"
```

### 步骤 5：开始使用

现在可以正常使用搜索功能了！

**示例命令：**
- "搜索最新的科技新闻"
- "帮我找一下多莉斯公众号"
- "查一下 Python 3.13 的新特性"
- "搜索知乎上关于 AI 的讨论"

---

## 高级配置

### 自定义默认搜索引擎

编辑 `references/search-config.json`：

```json
{
  "defaultEngine": "baidu",  // 改为百度
  "forceChinese": true
}
```

### 添加自定义搜索源

在 `search-config.json` 中添加：

```json
{
  "engines": {
    "custom-engine": {
      "name": "自定义引擎",
      "country": "CN",
      "language": "zh",
      "search_lang": "zh-hans",
      "priority": 5
    }
  }
}
```

### 配置搜索参数默认值

修改 `references/search-config.json` 中的 `defaultParams`：

```json
{
  "defaultParams": {
    "count": 10,
    "freshness": "week",
    "country": "CN",
    "language": "zh"
  }
}
```

---

## 故障排查

### 问题：提示 `missing_brave_api_key`

**原因：** API key 未配置或未生效

**解决：**
1. 确认已运行 `openclaw configure --section web`
2. 重启 OpenClaw 网关
3. 检查环境变量：`echo $env:BRAVE_API_KEY`

### 问题：搜索结果都是英文

**原因：** 未使用中文搜索参数

**解决：** 确保搜索时包含：
```bash
country="CN", language="zh", search_lang="zh-hans"
```

本技能已默认配置这些参数。

### 问题：搜索失败或超时

**原因：** 网络问题或 API 限流

**解决：**
1. 检查网络连接
2. 等待几分钟后重试
3. 检查 API quota：https://brave.com/search/api/dashboard

### 问题：技能未加载

**原因：** 技能未正确安装

**解决：**
```bash
# 重新加载技能
openclaw skills sync

# 检查技能状态
openclaw skills list
```

---

## 性能优化建议

### 减少 Token 消耗

1. **限制搜索结果数量**
   ```bash
   web_search(query="...", count=5)  # 默认 10
   ```

2. **限制抓取内容长度**
   ```bash
   web_fetch(url="...", maxChars=3000)  # 默认 5000
   ```

3. **使用时间过滤**
   ```bash
   web_search(query="...", freshness="week")  # 只搜索一周内
   ```

### 提高搜索质量

1. **使用精确关键词**
   - 加引号：`"精确匹配"`
   - 排除词：`苹果 -手机`
   - 站内搜索：`site:zhihu.com`

2. **交叉验证**
   - 对重要信息搜索多个关键词
   - 使用 `web_fetch` 抓取原文核实

---

## 更新技能

```bash
# 从 ClawHub 更新
npx clawhub@latest sync multi-search-engine

# 或手动更新
# 1. 备份自定义配置
# 2. 重新下载技能文件
# 3. 恢复自定义配置
```

---

## 相关资源

- [Brave Search API 文档](https://brave.com/search/api/docs/)
- [OpenClaw web 工具文档](https://docs.openclaw.ai/tools/web)
- [ClawHub 技能市场](https://clawhub.ai/skills/multi-search-engine)

---

**最后更新：** 2026-03-17  
**版本：** 1.1.0  
**作者：** Nelson
