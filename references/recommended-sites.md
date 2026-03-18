# 推荐搜索源网站

## 营销/广告/创意类

| 网站 | URL | 说明 | 搜索建议 |
|------|-----|------|---------|
| **数英网** | https://www.digitaling.com | 数字营销案例库，广告创意作品 | 品牌营销案例首选 |
| **SocialBeta** | https://socialbeta.com | 社交媒体营销案例、品牌动态 | 最新营销资讯 |
| **站酷** | https://www.zcool.com.cn | 设计师社区，创意作品展示 | 视觉设计、创意广告 |
| **人人都是产品经理** | https://www.woshipm.com | 产品运营、营销方法论 | 产品营销、运营案例 |

## 视频/影像类

| 网站 | URL | 说明 | 搜索建议 |
|------|-----|------|---------|
| **新片场素材** | https://stock.xinpianchang.com | 视频素材、广告片参考 | 视频广告、TVC 参考 |

## 科技/商业资讯类

| 网站 | URL | 说明 | 搜索建议 |
|------|-----|------|---------|
| **第一财经** | https://www.cbndata.com | 商业数据新闻、品牌报道 | 品牌商业分析 |
| **TechCrunch** | https://techcrunch.com | 全球科技新闻、创业公司 | 国际科技动态（英文） |
| **巴士的报** | https://www.bastillepost.com/hongkong | 香港新闻、科技版块 | 港澳地区资讯 |
| **unwire.hk** | https://unwire.hk/category/fun-tech/ | 香港科技资讯、趣味科技 | 科技产品评测 |

## 使用方式

### 站内搜索命令

```bash
# 数英网搜索杜蕾斯营销案例
web_fetch(url="https://www.digitaling.com/search?keyword=杜蕾斯", extractMode="markdown")

# SocialBeta 搜索
web_fetch(url="https://socialbeta.com/search?keyword=营销案例", extractMode="markdown")

# 站酷搜索
web_fetch(url="https://www.zcool.com.cn/search?word=广告设计", extractMode="markdown")

# 人人都是产品经理
web_fetch(url="https://www.woshipm.com/search?word=营销策略", extractMode="markdown")

# 新片场
web_fetch(url="https://stock.xinpianchang.com/search?keyword=广告", extractMode="markdown")

# 第一财经
web_fetch(url="https://www.cbndata.com/search?keyword=品牌营销", extractMode="markdown")

# TechCrunch 搜索
web_fetch(url="https://techcrunch.com/?s=marketing", extractMode="markdown")

# 巴士的报
web_fetch(url="https://www.bastillepost.com/hongkong/search?keyword=营销", extractMode="markdown")

# unwire.hk
web_fetch(url="https://unwire.hk/category/fun-tech/", extractMode="markdown")
```

### Google 站内搜索

```bash
# 数英网
web_fetch(url="https://www.google.com.hk/search?q=site:digitaling.com+杜蕾斯&hl=zh-CN", extractMode="markdown")

# SocialBeta
web_fetch(url="https://www.google.com.hk/search?q=site:socialbeta.com+营销案例&hl=zh-CN", extractMode="markdown")

# 站酷
web_fetch(url="https://www.google.com.hk/search?q=site:zcool.com.cn+广告设计&hl=zh-CN", extractMode="markdown")

# 人人都是产品经理
web_fetch(url="https://www.google.com.hk/search?q=site:woshipm.com+营销策略&hl=zh-CN", extractMode="markdown")

# 第一财经
web_fetch(url="https://www.google.com.hk/search?q=site:cbndata.com+品牌&hl=zh-CN", extractMode="markdown")

# TechCrunch
web_fetch(url="https://www.google.com/search?q=site:techcrunch.com+marketing", extractMode="markdown")
```

## 推荐搜索流程

1. **先搜综合引擎**（必应/Google）找相关结果
2. **发现专业网站**后，用站内搜索深入查找
3. **对重要页面**用 `web_fetch` 抓取详细内容

## 网站特点总结

| 需求 | 推荐网站 |
|------|---------|
| 广告创意案例 | 数英网、站酷 |
| 社交媒体营销 | SocialBeta |
| 产品运营方法 | 人人都是产品经理 |
| 视频广告参考 | 新片场 |
| 商业品牌分析 | 第一财经 |
| 国际科技动态 | TechCrunch |
| 港澳地区资讯 | 巴士的报、unwire.hk |

---

**最后更新：** 2026-03-18  
**版本：** 1.0
