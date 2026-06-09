[app]

# APP 基本信息
title = AScript自动化控制
package.name = ascript_auto
package.domain = org.example

# 主脚本文件
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
source.exclude_exts = spec,md,txt
source.exclude_dirs = tests,doc,__pycache__,.vscode,.git

# 版本信息
version = 1.0.0
version.regex = __version__
version.filename = %(source.dir)s/main_app.py

# 依赖包
requirements = python3,kivy==2.2.1,android,plyer

# Android 配置
orientation = portrait
fullscreen = 0
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 30
android.archs = arm64-v8a,armeabi-v7a

# Android 权限
android.permissions = ACCESSIBILITY_SERVICE,BIND_ACCESSIBILITY_SERVICE,SYSTEM_ALERT_WINDOW,FOREGROUND_SERVICE

# 图标和启动画面
icon.filename = %(source.dir)s/res/img/logo.png
splash.background_color = #FFFFFF
splash.useSplashScreen = true

# 日志
log_level = 2

# 调试模式
debug = 0

[buildozer]

# 构建目录
build_dir = ./.buildozer

# 输出目录
bin_dir = ./dist

# 忽略警告
ignore_warnings = 1
