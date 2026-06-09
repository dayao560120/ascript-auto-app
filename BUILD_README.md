# AScript 自动化 APP 打包指南

## 📱 项目说明

这是一个基于 **Kivy** 框架开发的 Android 自动化控制应用，可以将您的 AScript 脚本打包成独立的 APK 文件，方便在手机上安装和运行。

### 主要功能
- ✅ 图形化控制面板
- ✅ 实时执行日志显示
- ✅ 任务状态监控
- ✅ 参数配置界面
- ✅ 自动重试机制
- ✅ Toast 提示反馈

---

## 🛠️ 环境准备

### 方式一：Linux/macOS（推荐）

Buildozer 官方支持 Linux 和 macOS，推荐使用 Ubuntu 20.04+。

#### 1. 安装系统依赖

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y \
    python3-pip \
    openjdk-17-jdk \
    unzip \
    autoconf \
    automake \
    libtool \
    pkg-config \
    libncurses5-dev \
    libncursesw5-dev \
    build-essential \
    libssl-dev \
    libffi-dev \
    wget \
    curl

# 安装 Python3（如果还没有）
sudo apt-get install python3 python3-venv python3-dev
```

#### 2. 安装 Buildozer

```bash
pip3 install --user buildozer
# 或者
pip3 install buildozer
```

验证安装：
```bash
buildozer --version
```

#### 3. 初始化构建环境

在项目根目录执行：
```bash
cd d:/ascode/001  # 或在 Linux 中进入项目目录
buildozer init
```

这会生成 `buildozer.spec` 配置文件（已为您创建好）。

---

### 方式二：Windows（使用 WSL2）

Windows 原生不支持 Buildozer，需要使用 WSL2（Windows Subsystem for Linux）。

#### 1. 启用 WSL2

```powershell
# 以管理员身份运行 PowerShell
wsl --install
wsl --set-default-version 2
```

#### 2. 安装 Ubuntu

从 Microsoft Store 安装 Ubuntu 22.04 LTS。

#### 3. 在 WSL2 中安装依赖

打开 Ubuntu 终端，执行"方式一"中的步骤 1-2。

#### 4. 访问 Windows 文件

WSL2 可以访问 Windows 文件系统：
```bash
cd /mnt/d/ascode/001
```

---

## 📦 打包 APK

### 步骤 1：检查配置文件

确保 `buildozer.spec` 配置正确（已为您配置好）：

```ini
[app]
title = AScript自动化控制
package.name = ascript_auto
package.domain = org.example
requirements = python3,kivy==2.2.1,android,plyer
android.api = 33
android.permissions = ACCESSIBILITY_SERVICE,...
```

### 步骤 2：首次构建（下载依赖）

```bash
buildozer android debug
```

首次构建会下载 Android SDK、NDK 等，可能需要 30-60 分钟。

### 步骤 3：后续构建

```bash
# 清理后重新构建
buildozer android clean
buildozer android debug

# 仅重新编译（更快）
buildozer android debug deploy run
```

### 步骤 4：查找生成的 APK

构建成功后，APK 文件位于：
```
dist/ascript_auto-1.0.0-arm64-v8a-debug.apk
```

---

## 🔧 高级配置

### 自定义应用图标

将图标保存为 PNG 格式，替换 `res/img/logo.png`：
- 尺寸：512x512 或 1024x1024
- 格式：PNG（支持透明背景）

### 修改应用名称

编辑 `buildozer.spec`：
```ini
title = 你的应用名称
package.name = your_app_name
```

### 调整权限

根据需求修改 `buildozer.spec` 中的权限：
```ini
android.permissions = INTERNET,ACCESS_NETWORK_STATE,VIBRATE
```

常用权限：
- `INTERNET` - 网络访问
- `VIBRATE` - 震动
- `CAMERA` - 相机
- `READ_EXTERNAL_STORAGE` - 读取存储
- `WRITE_EXTERNAL_STORAGE` - 写入存储

---

## 🚀 安装到手机

### 方法一：USB 传输

```bash
# 通过 ADB 安装
adb install dist/ascript_auto-1.0.0-arm64-v8a-debug.apk

# 或直接复制 APK 到手机，手动点击安装
```

### 方法二：二维码分享

使用 Python 快速启动 HTTP 服务器：
```bash
cd dist
python3 -m http.server 8080
```

在手机浏览器访问电脑 IP 地址下载。

### 方法三：发送到聊天软件

将 APK 文件发送到微信、QQ 等，在手机上下载安装。

---

## ⚙️ 使用说明

### 首次运行

1. **开启辅助功能权限**
   - 设置 > 辅助功能 > AScript自动化控制 > 启用

2. **授予悬浮窗权限**（如果需要）
   - 设置 > 应用管理 > AScript自动化控制 > 允许悬浮窗

3. **启动应用**
   - 点击"开始执行"按钮
   - 查看实时日志
   - 在"设置"页面调整参数

### 功能说明

- **控制面板**：启动/停止自动化任务
- **执行日志**：实时显示任务执行过程
- **设置页面**：配置目标文本、延时、重试次数等

---

## 🐛 故障排除

### 问题 1：构建失败 - 缺少依赖

**错误信息**：
```
ModuleNotFoundError: No module named 'xxx'
```

**解决方案**：
在 `buildozer.spec` 中添加缺失的模块：
```ini
requirements = python3,kivy,xxx
```

### 问题 2：APK 安装失败

**原因**：未允许安装未知来源应用

**解决方案**：
设置 > 安全 > 允许安装未知来源应用

### 问题 3：应用闪退

**查看日志**：
```bash
adb logcat | grep python
```

或在手机上查看：
```
/storage/emulated/0/org.example.ascript_auto/app.log
```

### 问题 4：无法找到 ascript 模块

**说明**：AScript 是特定框架，标准 Android 环境中不存在

**解决方案**：
- 应用会自动切换到模拟模式
- 如需真实功能，需要在支持 AScript 的环境中运行

---

## 📝 项目结构

```
d:/ascode/001/
├── main_app.py              # Kivy 主应用
├── ascript.kv               # Kivy 界面描述
├── android_service.py       # Android 服务封装
├── config.py                # 配置文件
├── utils/                   # 工具模块
│   ├── logger.py
│   └── retry.py
├── buildozer.spec           # Buildozer 配置
├── res/img/logo.png         # 应用图标
└── BUILD_README.md          # 本文档
```

---

## 🔗 相关资源

- [Kivy 官方文档](https://kivy.org/doc/stable/)
- [Buildozer GitHub](https://github.com/kivy/buildozer)
- [Kivy 中文教程](https://www.kivy.cn/)

---

## 💡 开发建议

### 调试技巧

```bash
# 查看详细构建日志
buildozer -v android debug

# 仅编译不安装
buildozer android debug

# 构建 Release 版本（需要签名）
buildozer android release
```

### 性能优化

1. **减少 APK 体积**
   ```ini
   # buildozer.spec
   source.exclude_dirs = tests,doc,__pycache__
   ```

2. **优化启动速度**
   - 延迟加载非必要模块
   - 使用线程执行耗时操作

3. **内存管理**
   - 及时释放无用对象
   - 避免内存泄漏

---

## 📄 许可证

本项目仅供学习和个人使用。如需商业分发，请确保遵守相关法律法规和平台政策。

---

**最后更新**：2026-06-09
**作者**：Qoder AI Assistant
