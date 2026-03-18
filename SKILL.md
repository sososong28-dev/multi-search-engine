---
name: multi-search-engine
description: 多引擎联网搜索技能，支持免 API 和 API 两种模式。支持必应中国、Google、百度等搜索引擎，以及数英网、SocialBeta 等专业网站。当用户需要搜索营销案例、广告创意、产品设计、科技资讯或中文互联网信息时使用此技能。
---

# Multi-Search-Engine 技能

## 快速开始

### 免 API 模式（推荐）

```bash
# 必应中国
web_fetch(url="https://cn.bing.com/search?q=关键词", extractMode="markdown")

# Google
web_fetch(url="https://www.google.com/search?q=关键词&hl=zh-CN", extractMode="markdown")

# Google 香港
web_fetch(url="https://www.google.com.hk/search?q=关键词&hl=zh-CN", extractMode="markdown")
```

### API 模式

需要 Brave API Key：`openclaw configure --section web`

```bash
web_search(query="关键词", country="CN", language="zh", search_lang="zh-hans")
```

## 核心功能

- **多引擎搜索**：必应中国、Google、Google 香港、百度、搜狗
- **专业网站**：数英网、SocialBeta、站酷、第一财经等（见 `references/recommended-sites.md`）
- **时间过滤**：`freshness=week`（必应）或 `tbs=qdr:w`（Google）
- **站内搜索**：`site:zhihu.com` 或 Google 站内搜索

## 常用场景

| 场景 | 命令 |
|------|------|
| 微信公众号 | `cn.bing.com/search?q=名称 + 公众号` |
| 知乎内容 | `cn.bing.com/search?q=关键词+site:zhihu.com` |
| 最新新闻 | `cn.bing.com/search?q=关键词&freshness=week` |
| 营销案例 | `site:digitaling.com` 或 `site:socialbeta.com` |
| 设计创意 | `site:zcool.com.cn` |

## 详细文档

- **搜索引擎配置**：`references/search-config.json`
- **免 API 搜索指南**：`references/no-api-search.md`
- **推荐网站列表**：`references/recommended-sites.md`
- **快速参考**：`references/quick-reference.md`
- **部署指南**：`references/deployment.md`

## 脚本工具

```bash
# 测试配置
python scripts/test_search.py

# 免 API 搜索
python scripts/search_no_api.py "关键词" [引擎]
```

---

**触发条件**：搜索、查一下、找找、google、百度、联网搜索、营销案例、广告创意、设计等关键词。
