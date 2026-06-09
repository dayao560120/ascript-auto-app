# 🚀 AScript APP 打包快速指南

## ✅ 已完成的工作

您的项目现在已经完全准备好打包成 Android APK！以下是所有新增的文件：

### 新增文件清单

| 文件名 | 说明 | 大小 |
|--------|------|------|
| `main_app.py` | Kivy 主应用（控制面板） | 5.9 KB |
| `ascript.kv` | Kivy 界面描述文件 | 7.2 KB |
| `android_service.py` | Android 服务封装模块 | 3.0 KB |
| `buildozer.spec` | Buildozer 打包配置 | 1.1 KB |
| `BUILD_README.md` | 详细打包文档 | 6.8 KB |
| `run_app.bat` | Windows 本地测试脚本 | - |

---

## 📋 快速开始（三种方式）

### 方式 1️⃣：Windows 本地测试（推荐先测试）

```bash
# 1. 安装 Kivy
pip install kivy

# 2. 运行测试
双击 run_app.bat
或
python main_app.py
```

这会在电脑上运行应用，您可以：
- 查看界面效果
- 测试按钮功能
- 模拟执行流程

---

### 方式 2️⃣：Linux/macOS 直接打包 APK

```bash
# 1. 安装 Buildozer
pip3 install buildozer

# 2. 首次构建（会自动下载依赖，需要 30-60 分钟）
buildozer android debug

# 3. 后续构建（更快）
buildozer android clean && buildozer android debug

# 4. 生成的 APK 位置
ls dist/*.apk
```

---

### 方式 3️⃣：Windows + WSL2 打包

```powershell
# 1. 启用 WSL2（管理员权限）
wsl --install
wsl --set-default-version 2

# 2. 重启后打开 Ubuntu 终端
# 3. 进入项目目录
cd /mnt/d/ascode/001

# 4. 安装 Buildozer
pip3 install buildozer

# 5. 打包 APK
buildozer android debug
```

---

## 🎯 核心功能展示

### 控制面板界面

```
┌─────────────────────────────┐
│   AScript 自动化控制    [设置] │
├─────────────────────────────┤
│                             │
│  当前状态                    │
│  ✓ 就绪                     │
│                             │
├─────────────────────────────┤
│  [开始执行]  [停止]          │
├─────────────────────────────┤
│  执行结果: 等待执行...       │
├─────────────────────────────┤
│  执行日志:                   │
│  [12:00:00] 启动任务        │
│  [12:00:01] 查找元素...     │
│  [12:00:02] 点击成功!       │
│                             │
└─────────────────────────────┘
```

### 设置界面

```
┌─────────────────────────────┐
│ [< 返回]      设置           │
├─────────────────────────────┤
│  目标元素文本                │
│  [畅游时代____________]      │
├─────────────────────────────┤
│  点击后延时（秒）            │
│  [2___________________]      │
├─────────────────────────────┤
│  最大重试次数                │
│  [3___________________]      │
├─────────────────────────────┤
│  启用自动重试    [ON/OFF]    │
├─────────────────────────────┤
│  [重置]  [保存设置]          │
└─────────────────────────────┘
```

---

## 🔧 配置说明

### buildozer.spec 关键配置

```ini
[app]
title = AScript自动化控制         # 应用名称
package.name = ascript_auto      # 包名
package.domain = org.example     # 域名
version = 1.0.0                  # 版本号

requirements = python3,kivy==2.2.1,android,plyer

android.api = 33                 # Android API 级别
android.archs = arm64-v8a,armeabi-v7a  # CPU 架构

android.permissions =            # 权限
    ACCESSIBILITY_SERVICE,
    BIND_ACCESSIBILITY_SERVICE,
    SYSTEM_ALERT_WINDOW,
    FOREGROUND_SERVICE
```

---

## 📱 安装到手机

### 方法 A：USB 安装

```bash
# 连接手机后执行
adb install dist/ascript_auto-1.0.0-arm64-v8a-debug.apk
```

### 方法 B：扫码安装

```bash
# 在 dist 目录启动 HTTP 服务器
cd dist
python -m http.server 8080

# 手机浏览器访问电脑 IP:8080 下载
```

### 方法 C：聊天软件发送

将 APK 发送到微信/QQ，在手机上下载安装。

---

## ⚙️ 首次运行设置

1. **开启辅助功能**
   ```
   设置 > 辅助功能 > AScript自动化控制 > 启用
   ```

2. **授予悬浮窗权限**（如需要）
   ```
   设置 > 应用管理 > AScript自动化控制 > 允许悬浮窗
   ```

3. **启动应用**
   - 点击"开始执行"按钮
   - 查看实时日志
   - 调整参数设置

---

## 🐛 常见问题

### Q1: 构建时下载依赖很慢？

**A:** 使用国内镜像源：
```bash
export PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple
buildozer android debug
```

### Q2: APK 体积太大？

**A:** 正常现象，Kivy 应用通常 30-50MB。优化方法：
```ini
# buildozer.spec
source.exclude_exts = spec,md,txt
source.exclude_dirs = tests,__pycache__
```

### Q3: 应用闪退？

**A:** 查看日志：
```bash
adb logcat | grep python
```

### Q4: 找不到 ascript 模块？

**A:** 这是正常的！应用会自动切换到模拟模式。如需真实功能，需要在支持 AScript 的环境中运行。

---

## 📊 项目结构总览

```
d:/ascode/001/
│
├── 📱 APP 相关文件
│   ├── main_app.py              # Kivy 主应用
│   ├── ascript.kv               # 界面描述
│   ├── android_service.py       # Android 服务
│   └── buildozer.spec           # 打包配置
│
├── 🔧 原有项目文件
│   ├── __init__.py              # 原入口（已优化）
│   ├── config.py                # 配置文件
│   ├── utils/                   # 工具模块
│   └── build.as                 # AScript 构建配置
│
└── 📖 文档
    ├── BUILD_README.md          # 详细打包文档
    └── QUICK_START.md           # 快速指南（本文件）
```

---

## 🎓 下一步建议

### 立即行动

1. **本地测试**（5 分钟）
   ```bash
   pip install kivy
   python main_app.py
   ```

2. **准备打包环境**（10-30 分钟）
   - Linux/macOS: 直接安装 Buildozer
   - Windows: 启用 WSL2

3. **构建 APK**（30-60 分钟，仅首次）
   ```bash
   buildozer android debug
   ```

4. **安装测试**（5 分钟）
   ```bash
   adb install dist/*.apk
   ```

### 长期优化

- [ ] 添加更多自动化任务
- [ ] 实现任务调度功能
- [ ] 添加数据统计图表
- [ ] 支持云端同步配置
- [ ] 创建用户教程视频

---

## 💬 技术支持

- 📖 详细文档：查看 `BUILD_README.md`
- 🔍 问题排查：查看 `BUILD_README.md` 的"故障排除"章节
- 🌐 Kivy 官方文档：https://kivy.org/doc/stable/

---

**准备好了吗？** 从"方式 1：本地测试"开始吧！🚀
