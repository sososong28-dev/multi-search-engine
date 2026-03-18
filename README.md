# multi-search-engine

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-blue)](https://openclaw.ai)
[![Version](https://img.shields.io/badge/version-1.4.0-green.svg)](https://github.com/national_geographii/multi-search-engine)

> 多引擎联网搜索技能 for OpenClaw - 支持免 API 模式，专注中文搜索和营销案例查找

## ✨ 特性

- 🔓 **免 API 模式** - 无需配置，直接使用 `web_fetch` 抓取搜索结果
- 🔑 **API 模式** - 支持 Brave Search API（可选）
- 🌏 **多引擎支持** - 必应中国、Google、Google 香港、百度、搜狗
- 🎯 **专业网站** - 数英网、SocialBeta、站酷、第一财经等营销/设计网站
- 🇨🇳 **中文优化** - 解决搜索结果返回英文的问题
- 📚 **完整文档** - 包含部署指南、快速参考、测试工具

## 📦 安装

### 方法 1：从 ClawHub 安装（推荐）

```bash
npx clawhub@latest install multi-search-engine
```

### 方法 2：手动安装

```bash
# 克隆此仓库
git clone https://github.com/national_geographii/multi-search-engine.git

# 复制到 OpenClaw 技能目录
cp -r multi-search-engine ~/.openclaw/workspace/skills/
```

### 方法 3：直接下载

1. 下载此仓库的 ZIP 文件
2. 解压到 `~/.openclaw/workspace/skills/multi-search-engine`

## 🚀 快速使用

### 免 API 模式（推荐）

```bash
# 必应中国搜索
web_fetch(url="https://cn.bing.com/search?q=关键词", extractMode="markdown")

# Google 搜索
web_fetch(url="https://www.google.com/search?q=关键词&hl=zh-CN", extractMode="markdown")

# Google 香港（敏感内容推荐）
web_fetch(url="https://www.google.com.hk/search?q=关键词&hl=zh-CN", extractMode="markdown")
```

### API 模式

配置 Brave API Key：
```bash
openclaw configure --section web
```

使用：
```bash
web_search(query="关键词", country="CN", language="zh", search_lang="zh-hans")
```

## 📖 使用场景

| 场景 | 示例命令 |
|------|---------|
| 🔍 微信公众号 | `cn.bing.com/search?q=名称 + 公众号` |
| 💬 知乎内容 | `cn.bing.com/search?q=关键词+site:zhihu.com` |
| 📰 最新新闻 | `cn.bing.com/search?q=关键词&freshness=week` |
| 📊 营销案例 | `site:digitaling.com` 或 `site:socialbeta.com` |
| 🎨 设计创意 | `site:zcool.com.cn` |
| 📈 商业资讯 | `site:cbndata.com` |

## 🌐 支持的搜索引擎

| 引擎 | URL | 推荐场景 |
|------|-----|---------|
| 必应中国 | cn.bing.com | ✅ 日常中文搜索 |
| Google | google.com | ✅ 国际内容、技术搜索 |
| Google 香港 | google.com.hk | ✅ 敏感内容、营销案例 |
| 百度 | baidu.com | 国内内容 |
| 搜狗 | sogou.com | 微信相关内容 |

## 🎯 专业网站支持

- **数英网** (digitaling.com) - 数字营销案例
- **SocialBeta** (socialbeta.com) - 社交媒体营销
- **站酷** (zcool.com.cn) - 设计创意作品
- **人人都是产品经理** (woshipm.com) - 产品运营
- **新片场** (stock.xinpianchang.com) - 视频广告
- **第一财经** (cbndata.com) - 商业资讯
- **TechCrunch** (techcrunch.com) - 科技新闻
- **巴士的报** (bastillepost.com) - 港澳资讯
- **unwire.hk** - 香港科技资讯

## 📁 文件结构

```
multi-search-engine/
├── SKILL.md                      # 技能说明
├── README.md                     # 本文档
├── package.json                  # 配置信息
├── .gitignore                    # Git 忽略文件
├── PUBLISHING.md                 # 发布指南
├── RELEASE_NOTES.md              # 发布说明
│
├── scripts/
│   ├── search_example.py         # 搜索示例脚本
│   ├── search_no_api.py          # 免 API 搜索工具
│   └── test_search.py            # 配置测试工具
│
└── references/
    ├── search-config.json        # 搜索引擎配置
    ├── no-api-search.md          # 免 API 搜索指南
    ├── recommended-sites.md      # 推荐网站列表
    ├── quick-reference.md        # 快速参考
    └── deployment.md             # 部署指南
```

## 🧪 测试

```bash
# 测试配置
python scripts/test_search.py

# 免 API 搜索示例
python scripts/search_no_api.py "多莉斯 公众号"

# 测试 Google 搜索
python scripts/search_no_api.py "营销案例" google-hk
```

## 📝 版本历史

### v1.4.0 (2026-03-18)
- ✨ 添加 9 个专业网站支持（营销/设计/科技类）
- 📝 精简 SKILL.md 至 1.5KB
- 📚 添加完整的 README 和发布文档

### v1.3.0 (2026-03-17)
- ✨ 添加 Google 和 Google 香港支持
- 🔧 更新 search_no_api.py 脚本

### v1.2.0 (2026-03-17)
- ✨ 添加免 API 搜索模式
- 🛠️ 添加 search_no_api.py 工具

### v1.1.0 (2026-03-17)
- 🧪 添加 test_search.py 测试工具
- 📖 添加快速参考和部署指南

### v1.0.0 (2026-03-17)
- 🎉 初始版本

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

1. Fork 此仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📄 License

MIT License - 详见 [LICENSE](LICENSE) 文件

## 👨‍💻 作者

**Nelson** ([@national_geographii](https://github.com/national_geographii))

## 🔗 相关链接

- [OpenClaw 官方文档](https://docs.openclaw.ai)
- [ClawHub 技能市场](https://clawhub.ai/skills)
- [web_search 工具文档](https://docs.openclaw.ai/tools/web)
- [技能创建指南](https://docs.openclaw.ai/skills/creating)

## 📮 联系方式

- Telegram: [@national_geographii](https://t.me/national_geographii)
- GitHub: [@national_geographii](https://github.com/national_geographii)

---

<div align="center">

**如果这个技能对你有帮助，请给个 ⭐ Star 支持一下！**

Made with ❤️ by Nelson

</div>
