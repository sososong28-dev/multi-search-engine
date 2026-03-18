# 发布指南

## 发布到 ClawHub

### 1. 登录

```bash
npx clawhub@latest login
```

这会打开浏览器让你登录 GitHub 账号并授权。

### 2. 发布

```bash
npx clawhub@latest publish "C:\Users\User\.openclaw\workspace\skills\multi-search-engine"
```

或从 skill 目录：
```bash
cd C:\Users\User\.openclaw\workspace\skills\multi-search-engine
npx clawhub@latest publish .
```

### 3. 验证发布

访问 https://clawhub.ai/skills/multi-search-engine 查看已发布的技能。

## 发布到 GitHub（可选）

### 1. 初始化 Git 仓库

```bash
cd C:\Users\User\.openclaw\workspace\skills\multi-search-engine
git init
git add .
git commit -m "Initial release v1.4.0"
```

### 2. 创建 GitHub 仓库

访问 https://github.com/new 创建新仓库，例如：
- 仓库名：`multi-search-engine`
- 描述：`多引擎联网搜索技能 for OpenClaw`

### 3. 推送代码

```bash
git remote add origin https://github.com/YOUR_USERNAME/multi-search-engine.git
git branch -M main
git push -u origin main
```

## 发布前检查清单

- [x] SKILL.md 已精简（<500 行）
- [x] package.json 包含必要字段（name, version, description, keywords）
- [x] README.md 包含使用说明
- [x] references/ 包含详细文档
- [x] scripts/ 包含测试和工具脚本
- [x] 无冗余文件（如 .gitignore, .env 等）
- [ ] 已在 ClawHub 发布
- [ ] 已在 GitHub 发布（可选）

## 版本更新

修改 `package.json` 中的 version 字段，然后重新发布：

```bash
# 修改 version，例如 1.4.0 → 1.4.1
# 然后重新发布
npx clawhub@latest publish .
```

## 技能信息

- **名称**: multi-search-engine
- **当前版本**: 1.4.0
- **作者**: Nelson
- **License**: MIT
- **关键词**: search, web, chinese, marketing, design, no-api

## 相关链接

- [ClawHub](https://clawhub.ai)
- [OpenClaw 文档](https://docs.openclaw.ai)
- [技能创建指南](https://docs.openclaw.ai/skills/creating)
