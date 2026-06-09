@echo off
chcp 65001 >nul
echo ========================================
echo   AScript 自动化 APP - 本地测试
echo ========================================
echo.
echo 正在启动 Kivy 应用...
echo 按 Ctrl+C 可以退出
echo.

python main_app.py

pause
