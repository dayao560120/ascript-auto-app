# 🚀 GitHub 部署指南

## ✅ 已完成的步骤

- ✅ 初始化 Git 仓库
- ✅ 创建 .gitignore 文件
- ✅ 添加所有项目文件
- ✅ 创建初始提交（包含完整的项目代码和文档）

---

## 📋 推送到 GitHub 的步骤

### 步骤 1：在 GitHub 上创建新仓库

1. **访问 GitHub**
   - 打开 https://github.com/new
   - 或点击 GitHub 右上角 "+" → "New repository"

2. **填写仓库信息**
   ```
   Repository name: ascript-auto-app  （或您喜欢的名称）
   Description: AScript 自动化控制 APP - Kivy Android 应用
   Visibility: Public（公开，免费使用 Actions）或 Private
   ⚠️ 不要勾选 "Initialize this repository with a README"
   ```

3. **点击 "Create repository"**

---

### 步骤 2：关联本地仓库并推送

复制以下命令并在项目根目录执行：

```bash
# 添加远程仓库（替换为您的仓库地址）
git remote add origin https://github.com/你的用户名/ascript-auto-app.git

# 验证远程仓库
git remote -v

# 推送到 GitHub
git push -u origin master
```

**示例**（假设您的用户名是 `zhangsan`）：
```bash
git remote add origin https://github.com/zhangsan/ascript-auto-app.git
git push -u origin master
```

---

### 步骤 3：触发自动构建 APK

推送成功后，GitHub Actions 会自动开始构建：

1. **查看构建进度**
   - 进入仓库页面
   - 点击 "Actions" 标签
   - 查看正在运行的工作流

2. **等待构建完成**
   - 首次构建：约 30-40 分钟
   - 后续构建：约 5-10 分钟（有缓存）

3. **下载 APK**
   - 点击完成的运行记录
   - 在页面底部找到 "Artifacts"
   - 点击 "ascript-auto-apk" 下载

---

## 🔧 常见问题

### Q1: 提示 "remote origin already exists"？

**解决方案**：
```bash
# 删除现有远程仓库
git remote remove origin

# 重新添加
git remote add origin https://github.com/你的用户名/仓库名.git
```

### Q2: 推送时要求输入用户名和密码？

**原因**：GitHub 已停用密码认证

**解决方案 A：使用 Personal Access Token**
1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 勾选权限：`repo`, `workflow`
4. 生成后复制 token
5. 推送时使用：
   ```
   Username: 你的GitHub用户名
   Password: 粘贴token（不会显示）
   ```

**解决方案 B：使用 SSH（推荐）**
```bash
# 生成 SSH 密钥（如果没有）
ssh-keygen -t ed25519 -C "your_email@example.com"

# 查看公钥
cat ~/.ssh/id_ed25519.pub

# 添加到 GitHub
# 访问 https://github.com/settings/ssh/new
# 粘贴公钥内容

# 修改远程仓库为 SSH 方式
git remote set-url origin git@github.com:你的用户名/仓库名.git

# 推送
git push -u origin master
```

### Q3: 推送失败，提示需要权限？

**检查清单**：
- [ ] 确认 GitHub 账号已登录
- [ ] 确认 Token 或 SSH 密钥配置正确
- [ ] 确认仓库存在且您有写入权限
- [ ] 确认网络连接正常

### Q4: 如何修改最后一次提交的作者信息？

```bash
# 修改配置
git config user.name "Your Name"
git config user.email "your_email@example.com"

# 修改最后一次提交的作者
git commit --amend --reset-author --no-edit

# 强制推送（如果已经推送过）
git push --force
```

---

## 📊 推送后的验证

### 检查文件是否上传成功

访问您的 GitHub 仓库页面，应该看到：

```
📁 ascript-auto-app/
├── 📁 .github/workflows/
│   └── build-apk.yml
├── 📁 utils/
│   ├── __init__.py
│   ├── logger.py
│   └── retry.py
├── main_app.py
├── ascript.kv
├── android_service.py
├── config.py
├── buildozer.spec
├── QUICK_START.md
├── BUILD_README.md
├── GITHUB_ACTIONS_GUIDE.md
└── ...
```

### 检查 Actions 是否触发

1. 点击仓库顶部的 **"Actions"** 标签
2. 应该看到一个正在运行或已完成的工作流
3. 点击可查看详细的构建日志

---

## 🎯 快速命令汇总

```bash
# 1. 查看当前状态
git status

# 2. 查看远程仓库
git remote -v

# 3. 查看提交历史
git log --oneline

# 4. 添加远程仓库
git remote add origin https://github.com/用户名/仓库名.git

# 5. 推送到 GitHub
git push -u origin master

# 6. 后续推送（简化命令）
git push

# 7. 拉取最新代码
git pull
```

---

## 📝 后续操作建议

### 每次修改后推送

```bash
# 修改代码后...
git add .
git commit -m "描述你的修改"
git push
```

### 创建版本标签

```bash
# 打标签
git tag v1.0.0

# 推送标签
git push origin v1.0.0

# 会自动触发 GitHub Release 创建（见 build-apk.yml）
```

### 分支管理

```bash
# 创建开发分支
git checkout -b develop

# 推送分支
git push -u origin develop

# 合并到主分支
git checkout master
git merge develop
git push
```

---

## 🔗 相关资源

- [GitHub 官方文档](https://docs.github.com/)
- [GitHub Actions 文档](https://docs.github.com/en/actions)
- [Git 学习教程](https://learngitbranching.js.org/)

---

## ✨ 总结

✅ **本地 Git 仓库已就绪**
✅ **初始提交已完成**
✅ **GitHub Actions 已配置**

**下一步**：
1. 在 GitHub 创建仓库
2. 执行推送命令
3. 等待自动构建 APK

祝您部署顺利！🚀
