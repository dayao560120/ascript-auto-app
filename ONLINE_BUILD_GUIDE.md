# 🌐 使用在线 Linux 环境打包

## 方案对比

| 服务 | 免费额度 | 配置难度 | 推荐指数 |
|------|---------|---------|---------|
| GitHub Actions | 2000分钟/月 | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| GitLab CI | 400分钟/月 | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Replit | 无限（有限制） | ⭐ | ⭐⭐⭐ |
| 本地 WSL2 | 无限制 | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

---

## 方案 1：Replit（最简单，无需安装）

### 步骤：

1. **访问 Replit**
   - 打开 https://replit.com
   - 用 GitHub 账号登录

2. **创建新项目**
   - 点击 "Create Repl"
   - 选择模板："Python (with Kivy)"
   - 或搜索 "Buildozer"

3. **上传代码**
   - 拖拽项目文件到左侧文件区
   - 或从 GitHub 导入

4. **执行打包命令**
   ```bash
   # 在 Shell 中执行
   pip install buildozer
   buildozer android debug
   ```

5. **下载 APK**
   - 构建完成后在 `dist/` 目录
   - 右键文件 → Download

**优点**：
- ✅ 无需安装任何软件
- ✅ 浏览器即可操作
- ✅ 完全免费

**缺点**：
- ⚠️ 需要网络连接
- ⚠️ 构建时间较长（可能 1 小时+）
- ⚠️ 资源受限

---

## 方案 2：GitPod（云端开发环境）

### 步骤：

1. **访问 GitPod**
   - 打开 https://gitpod.io
   - 用 GitHub 登录

2. **创建工作空间**
   ```
   https://gitpod.io/#https://github.com/你的用户名/仓库名
   ```

3. **安装依赖并打包**
   ```bash
   sudo apt-get update
   sudo apt-get install -y openjdk-17-jdk python3-pip
   pip3 install buildozer
   buildozer android debug
   ```

4. **下载 APK**
   - 在文件浏览器中找到 `dist/*.apk`
   - 右键下载

**优点**：
- ✅ 完整的 Linux 环境
- ✅ 每月 50 小时免费
- ✅ 性能较好

**缺点**：
- ⚠️ 需要 GitHub 账号
- ⚠️ 超时会自动关闭

---

## 方案 3：本地 WSL2（推荐长期使用）

### 一键安装脚本

创建 `install_wsl2.bat`：

```batch
@echo off
echo 正在启用 WSL2...
wsl --install -d Ubuntu-22.04
wsl --set-default-version 2

echo.
echo 请重启电脑后，打开 Ubuntu 终端执行以下命令：
echo.
echo cd /mnt/d/ascode/001
echo sudo apt-get update
echo sudo apt-get install -y python3-pip openjdk-17-jdk
echo pip3 install buildozer
echo buildozer android debug
echo.
pause
```

### 详细步骤：

1. **启用 WSL2**
   ```powershell
   # 管理员权限运行
   wsl --install
   wsl --set-default-version 2
   ```

2. **重启电脑**

3. **打开 Ubuntu 终端**
   ```bash
   # 进入项目目录（D盘）
   cd /mnt/d/ascode/001

   # 安装依赖
   sudo apt-get update
   sudo apt-get install -y \
       python3-pip \
       openjdk-17-jdk \
       autoconf automake libtool \
       pkg-config libncurses5-dev libncursesw5-dev \
       build-essential libssl-dev libffi-dev

   # 安装 Buildozer
   pip3 install buildozer

   # 打包 APK
   buildozer android debug
   ```

4. **等待构建完成**
   - 首次：30-40 分钟
   - 后续：5-10 分钟

5. **APK 位置**
   ```
   dist/ascript_auto-1.0.0-arm64-v8a-debug.apk
   ```

**优点**：
- ✅ 完全免费，无限制
- ✅ 性能最佳
- ✅ 可反复使用

**缺点**：
- ⚠️ 需要 Windows 10/11
- ⚠️ 首次配置较复杂
- ⚠️ 占用磁盘空间（约 15GB）

---

## 方案 4：虚拟机（备选）

### 使用 VirtualBox + Ubuntu

1. **下载 Ubuntu ISO**
   - https://ubuntu.com/download/desktop

2. **安装 VirtualBox**
   - https://www.virtualbox.org/

3. **创建虚拟机**
   - 分配 4GB+ RAM
   - 分配 30GB+ 磁盘

4. **在虚拟机中打包**
   ```bash
   sudo apt-get update
   sudo apt-get install -y python3-pip openjdk-17-jdk
   pip3 install buildozer
   buildozer android debug
   ```

---

## 🎯 推荐方案总结

### 如果您想要...

**🚀 最快上手** → Replit（方案 1）
- 浏览器打开即用
- 无需安装任何东西

**💼 团队协作** → GitHub Actions（已配置）
- 自动化构建
- 版本管理完善

**🔧 长期开发** → WSL2（方案 3）
- 本地环境最灵活
- 无网络依赖

**📱 偶尔打包** → GitPod（方案 2）
- 每月 50 小时够用
- 性能优秀

---

## ❓ 常见问题

### Q: 哪个方案成功率最高？

**A:** WSL2 > GitHub Actions > GitPod > Replit

### Q: 哪个方案最快？

**A:**
- 首次：WSL2（30-40 分钟）
- 后续：GitHub Actions（有缓存，5-10 分钟）

### Q: 我不想学习新技术，怎么办？

**A:** 使用 Replit，复制粘贴命令即可。

---

## 📞 需要帮助？

如果遇到问题：
1. 查看 `BUILD_README.md` 的故障排除章节
2. 查看各方案的官方文档
3. 提供错误日志截图

---

**选择最适合您的方案，开始打包吧！** 🚀
