# 快速参考卡片

## 一键搜索命令

```bash
# 通用中文搜索
web_search(query="关键词", country="CN", language="zh", search_lang="zh-hans")

# 微信公众号
web_search(query="公众号名称 公众号", country="CN", language="zh", search_lang="zh-hans")

# 最新新闻（24 小时内）
web_search(query="关键词", freshness="day", country="CN", language="zh")

# 一周内内容
web_search(query="关键词", freshness="week", country="CN", language="zh")

# 搜索特定网站
web_search(query="关键词 site:zhihu.com", country="CN", language="zh")

# 搜索 PDF 文档
web_search(query="关键词 filetype:pdf", country="CN", language="zh")
```

## 内容抓取命令

```bash
# 抓取网页为 Markdown
web_fetch(url="https://example.com", extractMode="markdown")

# 抓取网页为文本（限制长度）
web_fetch(url="https://example.com", extractMode="text", maxChars=3000)
```

## 常用搜索场景

| 场景 | 搜索词示例 | 参数 |
|------|-----------|------|
| 微信公众号 | "多莉斯 公众号" | country=CN |
| 知乎内容 | "AI 讨论 site:zhihu.com" | - |
| 最新新闻 | "AI 突破" | freshness=day |
| 教程资料 | "Python 教程 入门" | - |
| 产品价格 | "iPhone 16 价格" | freshness=week |
| 学术论文 | "机器学习 论文 filetype:pdf" | - |
|  GitHub 项目 | "openclaw site:github.com" | - |

## 故障排查

### 问题 1：提示 `missing_brave_api_key`

**原因：** 未配置 API key

**解决：**
```bash
openclaw configure --section web
```

### 问题 2：搜索结果都是英文

**原因：** 未指定中文参数

**解决：** 添加以下参数：
```bash
country="CN", language="zh", search_lang="zh-hans"
```

### 问题 3：web_fetch 抓取失败

**原因：** 网页可能反爬虫或需要登录

**解决：**
- 尝试其他来源
- 使用 `extractMode="text"` 而非 `"markdown"`
- 减少 `maxChars` 值

### 问题 4：搜索结果不相关

**原因：** 搜索词太宽泛

**解决：**
- 添加更多关键词
- 使用引号精确匹配 `"精确词组"`
- 使用 `-` 排除不需要的词 `苹果 -手机`

## 性能优化

| 优化项 | 建议值 | 说明 |
|--------|--------|------|
| count | 5-10 | 结果数量，越多越慢 |
| maxChars | 3000-5000 | 抓取内容长度限制 |
| 同时抓取 | 2-3 个 | 避免一次性抓取太多页面 |
| freshness | 按需使用 | 时间过滤会增加搜索时间 |

## 安全提醒

⚠️ **外部内容风险：**

从互联网抓取的内容可能包含：
- 恶意指令（prompt injection）
- 虚假信息
- 过期内容

**最佳实践：**
1. 交叉验证多个来源
2. 注意内容发布时间
3. 不要盲目信任单一来源
4. 重要信息核实后再使用

---

**最后更新：** 2026-03-17
**版本：** 1.0.0
