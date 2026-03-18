# 免 API Key 搜索方案（推荐！）

## 为什么需要免 API 方案？

Brave Search API 需要注册和配置，有时搜索结果还不够中文。本方案通过直接抓取搜索引擎结果页，实现**无需 API Key**的中文搜索。

## 方案原理

使用 `web_fetch` 直接抓取搜索引擎的结果页面，解析出搜索结果。

**支持的搜索引擎：**
- 必应中国 (cn.bing.com) ✅ 推荐
- Google (www.google.com) ✅ 新增
- Google 香港 (www.google.com.hk) ✅ 新增
- 百度 (www.baidu.com)
- 搜狗 (www.sogou.com)

## 🚀 快速使用（复制粘贴）

### 必应中国搜索（推荐）

```bash
# 微信公众号搜索
web_fetch(url="https://cn.bing.com/search?q=多莉斯+公众号", extractMode="markdown")

# 通用搜索
web_fetch(url="https://cn.bing.com/search?q=你的关键词", extractMode="markdown")
```

### Google 搜索（结果更全面）

```bash
# Google 主站
web_fetch(url="https://www.google.com/search?q=多莉斯+营销&hl=zh-CN", extractMode="markdown")

# Google 香港（中文结果好）
web_fetch(url="https://www.google.com.hk/search?q=多莉斯+营销&hl=zh-CN", extractMode="markdown")

# 精确搜索
web_fetch(url="https://www.google.com/search?q=%22多莉斯%22+公众号&hl=zh-CN", extractMode="markdown")
```

### 百度搜索

```bash
web_fetch(url="https://www.baidu.com/s?wd=多莉斯+公众号", extractMode="markdown")
```

### 搜索知乎内容

```bash
# 必应
web_fetch(url="https://cn.bing.com/search?q=AI+讨论+site:zhihu.com", extractMode="markdown")

# Google
web_fetch(url="https://www.google.com/search?q=site:zhihu.com+AI+讨论&hl=zh-CN", extractMode="markdown")
```

### 搜索最新新闻（一周内）

```bash
# 必应
web_fetch(url="https://cn.bing.com/search?q=科技新闻&freshness=week", extractMode="markdown")

# Google
web_fetch(url="https://www.google.com/search?q=科技新闻&hl=zh-CN&tbs=qdr:w", extractMode="markdown")
```

## 常用搜索 URL 模板

| 场景 | 必应中国 | Google |
|------|---------|--------|
| 通用搜索 | `https://cn.bing.com/search?q=关键词` | `https://www.google.com/search?q=关键词&hl=zh-CN` |
| 微信公众号 | `https://cn.bing.com/search?q=名称+公众号` | `https://www.google.com/search?q=名称+公众号&hl=zh-CN` |
| 知乎内容 | `https://cn.bing.com/search?q=关键词+site:zhihu.com` | `https://www.google.com/search?q=site:zhihu.com+关键词&hl=zh-CN` |
| GitHub 项目 | `https://cn.bing.com/search?q=关键词+site:github.com` | `https://www.google.com/search?q=site:github.com+关键词&hl=zh-CN` |
| 最新内容（周） | `https://cn.bing.com/search?q=关键词&freshness=week` | `https://www.google.com/search?q=关键词&hl=zh-CN&tbs=qdr:w` |
| PDF 文档 | `https://cn.bing.com/search?q=关键词+filetype:pdf` | `https://www.google.com/search?q=关键词+filetype:pdf&hl=zh-CN` |

## 优缺点对比

| 方案 | 优点 | 缺点 |
|------|------|------|
| **免 API 方案** | 无需配置、纯中文结果、支持微信/知乎 | 需要手动构造 URL、可能反爬 |
| **API 方案** | 结构化结果、稳定、快速 | 需要 API Key、英文结果多 |

## 注意事项

1. **URL 编码**：中文关键词的空格用 `+` 或 `%20` 替换
2. **反爬虫**：频繁请求可能被限流，建议间隔 5-10 秒
3. **结果解析**：抓取的是 HTML 转换的 Markdown，需要手动提取有用信息

---

**最后更新：** 2026-03-17
