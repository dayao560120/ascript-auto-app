# 🚀 使用 GitHub Actions 自动打包 APK

## ✅ 已完成配置

我已经为您创建了自动化构建工作流文件：`.github/workflows/build-apk.yml`

---

## 📋 打包步骤（超简单）

### 步骤 1：上传到 GitHub

```bash
# 在项目根目录执行
git init
git add .
git commit -m "Initial commit: AScript APP with auto-build"

# 创建 GitHub 仓库（在 github.com 上）
# 然后关联远程仓库
git remote add origin https://github.com/你的用户名/仓库名.git
git push -u origin main
```

### 步骤 2：触发构建

**方法 A：推送代码自动构建**
- 每次 push 代码都会自动触发 APK 构建

**方法 B：手动触发**
1. 进入 GitHub 仓库页面
2. 点击 "Actions" 标签
3. 选择 "Build Android APK"
4. 点击 "Run workflow" → "Run workflow"

### 步骤 3：下载 APK

构建完成后（约 20-40 分钟）：

1. 进入 **Actions** 页面
2. 点击最近的一次运行记录
3. 在页面底部找到 **"Artifacts"**
4. 点击 **"ascript-auto-apk"** 下载
5. 解压后得到 `.apk` 文件

---

## ⚙️ 自定义配置

### 修改应用名称

编辑 `buildozer.spec`：
```ini
[app]
title = 你的应用名称
package.name = your_app_name
```

### 调整版本号

编辑 `main_app.py`，在开头添加：
```python
__version__ = "1.0.0"
```

### 添加更多依赖

编辑 `buildozer.spec`：
```ini
requirements = python3,kivy==2.2.1,android,plyer,requests,numpy
```

---

## 💡 优势

✅ **无需本地环境** - 不需要安装 Android SDK/NDK
✅ **完全免费** - GitHub Actions 每月赠送 2000 分钟
✅ **自动缓存** - 第二次构建只需 5-10 分钟
✅ **版本管理** - 每次构建都有记录可追溯
✅ **团队协作** - 团队成员都可以触发构建

---

## 🐛 常见问题

### Q1: 构建失败怎么办？

查看 Actions 日志：
1. 进入 Actions 页面
2. 点击失败的运行记录
3. 展开错误步骤查看详细日志

### Q2: 构建太慢？

首次构建需要下载依赖（30-40 分钟），后续会使用缓存（5-10 分钟）。

### Q3: 如何发布正式版本？

```bash
# 打标签
git tag v1.0.0
git push origin v1.0.0

# 会自动创建 GitHub Release 并附加 APK
```

---

## 📊 构建时间参考

| 构建类型 | 预计时间 | 说明 |
|---------|---------|------|
| 首次构建 | 30-40 分钟 | 需下载所有依赖 |
| 后续构建 | 5-10 分钟 | 使用缓存加速 |
| 清理后构建 | 30-40 分钟 | 缓存失效 |

---

## 🔗 相关资源

- [GitHub Actions 文档](https://docs.github.com/en/actions)
- [Buildozer 官方文档](https://buildozer.readthedocs.io/)
- [Kivy 中文教程](https://www.kivy.cn/)

---

**准备好了吗？** 现在就 push 代码到 GitHub，让云端帮您打包！🚀
