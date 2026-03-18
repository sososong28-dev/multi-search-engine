# 手动发布到 GitHub - 快速指南

由于 GitHub CLI 未安装成功，请使用以下方法手动发布：

## 方法 1：使用 GitHub 网页（最简单，无需安装任何工具）

### 步骤 1：压缩文件

1. 打开文件夹：`C:\Users\User\.openclaw\workspace\skills\multi-search-engine`
2. 选中所有文件和文件夹（Ctrl+A）
3. 右键 → 发送到 → 压缩 (zipped) 文件夹
4. 命名为：`multi-search-engine.zip`

### 步骤 2：创建 GitHub 仓库

1. 访问 https://github.com/new
2. 填写信息：
   - **Repository name**: `multi-search-engine`
   - **Description**: `多引擎联网搜索技能 for OpenClaw - 支持免 API 模式，专注中文搜索和营销案例查找`
   - **Visibility**: ✅ Public（公开）
   - ❌ 不要勾选 "Add a README file"
   - ❌ 不要添加 .gitignore
   - ❌ 不要选择 license
3. 点击 **Create repository**

### 步骤 3：上传文件

1. 在仓库页面，点击 **uploading an existing file** 链接
2. 拖拽 `multi-search-engine.zip` 到上传区域
3. 或者点击 **choose your files** 选择所有文件
4. 在 "Commit changes" 输入框填写：`Initial release v1.4.0`
5. 点击 **Commit changes**

### 步骤 4：验证

访问你的仓库：
```
https://github.com/national_geographii/multi-search-engine
```

检查 README.md 是否正确显示。

完成！✅

---

## 方法 2：使用 Git 命令行（需要安装 Git）

### 安装 Git

1. 下载：https://git-scm.com/download/win
2. 安装时保持默认选项
3. 安装完成后重启终端

### 配置 Git

```bash
git config --global user.name "Nelson"
git config --global user.email "your-email@example.com"
```

### 发布步骤

```bash
# 1. 进入项目目录
cd "C:\Users\User\.openclaw\workspace\skills\multi-search-engine"

# 2. 初始化 Git 仓库
git init

# 3. 添加所有文件
git add .

# 4. 提交
git commit -m "Initial release v1.4.0"

# 5. 创建 GitHub 仓库（访问网页）
# https://github.com/new
# 仓库名：multi-search-engine

# 6. 添加远程仓库
git remote add origin https://github.com/national_geographii/multi-search-engine.git

# 7. 推送
git branch -M main
git push -u origin main
```

完成！✅

---

## 方法 3：使用 GitHub Desktop（图形界面）

### 下载安装

1. 访问：https://desktop.github.com
2. 下载并安装 GitHub Desktop
3. 登录你的 GitHub 账号

### 发布步骤

1. **添加本地仓库**
   - File → Add Local Repository
   - 选择：`C:\Users\User\.openclaw\workspace\skills\multi-search-engine`
   - 点击 Add

2. **发布到 GitHub**
   - 点击 "Publish repository"
   - 填写：
     - Name: `multi-search-engine`
     - Description: `多引擎联网搜索技能 for OpenClaw`
     - ✅ Public
   - 点击 Publish

完成！✅

---

## 推荐

**使用方法 1（GitHub 网页）** 最简单，无需安装任何工具！

---

## 发布后

发布成功后：

1. 访问仓库页面：https://github.com/national_geographii/multi-search-engine
2. 检查文件是否完整
3. 查看 README 是否正确显示
4. 分享仓库链接给需要的人

---

## 仓库信息

- **仓库名**: multi-search-engine
- **版本**: 1.4.0
- **License**: MIT
- **作者**: Nelson (@national_geographii)

---

**最后更新**: 2026-03-18
