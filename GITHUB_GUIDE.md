# GitHub 发布指南

## 前提条件

- 已安装 Git
- 已注册 GitHub 账号
- 已配置 Git 用户名和邮箱

## 步骤 1：配置 Git（首次使用）

```bash
# 设置用户名
git config --global user.name "Nelson"

# 设置邮箱
git config --global user.email "your-email@example.com"
```

## 步骤 2：初始化仓库

```bash
cd C:\Users\User\.openclaw\workspace\skills\multi-search-engine
git init
```

## 步骤 3：添加文件

```bash
# 添加所有文件
git add .

# 或者选择性添加
git add SKILL.md package.json README.md scripts/ references/
```

## 步骤 4：提交更改

```bash
git commit -m "Initial release v1.4.0

Features:
- Multi-engine search support (Bing, Google, Baidu, Sogou)
- No-API mode for instant use
- Professional marketing/design websites integration
- Chinese search optimization
- Complete documentation and test tools"
```

## 步骤 5：创建 GitHub 仓库

### 方法 A：使用 GitHub CLI（推荐）

```bash
# 安装 gh CLI（如果未安装）
# Windows: winget install GitHub.cli

# 登录 GitHub
gh auth login

# 创建仓库
gh repo create multi-search-engine --public --source=. --push
```

### 方法 B：使用网页创建

1. 访问 https://github.com/new
2. 填写仓库信息：
   - **Repository name**: `multi-search-engine`
   - **Description**: `多引擎联网搜索技能 for OpenClaw - 支持免 API 模式，专注中文搜索和营销案例查找`
   - **Visibility**: Public ✅
   - **Initialize**: ❌ 不要勾选（我们已有本地代码）
3. 点击 "Create repository"

## 步骤 6：推送代码

### 如果是用网页创建的仓库：

```bash
# 添加远程仓库（替换 YOUR_USERNAME 为你的 GitHub 用户名）
git remote add origin https://github.com/YOUR_USERNAME/multi-search-engine.git

# 重命名分支为 main
git branch -M main

# 推送代码
git push -u origin main
```

### 如果是用 gh CLI 创建的：

代码应该已经自动推送了。

## 步骤 7：验证发布

访问你的仓库页面：
```
https://github.com/YOUR_USERNAME/multi-search-engine
```

检查：
- ✅ 所有文件已上传
- ✅ README.md 正确显示
- ✅ 文件结构完整

## 步骤 8（可选）：发布到 ClawHub

```bash
# 登录 ClawHub
npx clawhub@latest login

# 发布技能
npx clawhub@latest publish .
```

## 常见问题

### Q: 提示 "fatal: remote origin already exists"

**解决：**
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/multi-search-engine.git
```

### Q: 推送时提示认证失败

**解决：**
1. 使用 Personal Access Token 代替密码
2. 访问 https://github.com/settings/tokens
3. 创建新 token（勾选 repo 权限）
4. 使用 token 作为密码

### Q: 如何更新代码？

```bash
# 修改文件后
git add .
git commit -m "Update: 描述你的更改"
git push
```

### Q: 如何打版本标签？

```bash
# 创建标签
git tag -a v1.4.0 -m "Release version 1.4.0"

# 推送标签
git push origin v1.4.0
```

## 快速命令参考

```bash
# 初始化
git init

# 添加所有文件
git add .

# 提交
git commit -m "消息"

# 添加远程仓库
git remote add origin https://github.com/用户名/multi-search-engine.git

# 推送
git push -u origin main

# 查看状态
git status

# 查看日志
git log --oneline
```

## 仓库信息

- **仓库名**: multi-search-engine
- **版本**: 1.4.0
- **License**: MIT
- **作者**: Nelson (@national_geographii)

## 下一步

1. ✅ 推送到 GitHub
2. ✅ 验证仓库页面
3. 📝 更新 ClawHub 上的技能链接
4. 📢 分享给需要的人

---

**最后更新**: 2026-03-18
