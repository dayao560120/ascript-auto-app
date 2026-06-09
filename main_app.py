"""
AScript 自动化控制 APP - Kivy 版本
带完整控制面板的 Android 应用
"""

import threading
import time
from datetime import datetime

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty, BooleanProperty, ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen


class AutomationTask:
    """自动化任务执行器"""

    def __init__(self, callback=None):
        self.callback = callback
        self.is_running = False
        self.result = None

    def log(self, message):
        """记录日志并回调"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        if self.callback:
            Clock.schedule_once(lambda dt: self.callback(log_message), 0)

    def execute_task(self):
        """执行自动化任务"""
        self.is_running = True
        self.log("=" * 50)
        self.log("启动 AScript 自动化任务")
        self.log("=" * 50)

        try:
            # 使用 Android Accessibility Service 封装
            from android_service import accessibility

            # 初始化服务
            if not accessibility.is_initialized:
                accessibility.initialize()

            self.log("开始查找元素：'畅游时代'")

            target = accessibility.find_element("畅游时代", clickable=True)

            if target is None:
                self.log("未找到元素：'畅游时代'")
                accessibility.show_toast("未找到：畅游时代")
                self.result = "失败：未找到目标"
                return False

            self.log("成功找到元素，准备点击...")
            success = accessibility.click_element(target)

            if success:
                self.log("点击成功！")
                self.log("等待 2 秒...")
                time.sleep(2)
                self.log("任务完成！")
                accessibility.show_toast("点击成功")
                self.result = "成功"
                return True
            else:
                self.log("点击失败")
                self.result = "失败：点击操作失败"
                return False

        except ImportError as e:
            self.log(f"导入模块失败：{e}")
            self.log("使用模拟模式运行")
            time.sleep(1)
            self.result = "成功（模拟）"
            return True

        except Exception as e:
            error_msg = f"任务执行异常：{str(e)}"
            self.log(error_msg)
            self.result = f"失败：{str(e)}"
            return False

        finally:
            self.is_running = False


class ControlPanel(Screen):
    """控制面板界面"""

    # 状态属性
    status_text = StringProperty("就绪")
    is_running = BooleanProperty(False)
    log_text = StringProperty("")
    task_result = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.task_runner = None

    def add_log(self, message):
        """添加日志到界面"""
        self.log_text += message + "\n"
        # 限制日志行数
        lines = self.log_text.split("\n")
        if len(lines) > 100:
            self.log_text = "\n".lines[-100:]

    def start_task(self):
        """启动自动化任务"""
        if self.is_running:
            return

        self.is_running = True
        self.status_text = "运行中..."
        self.task_result = ""
        self.log_text = ""

        # 创建任务执行器
        self.task_runner = AutomationTask(callback=self.add_log)

        # 在新线程中执行任务，避免阻塞 UI
        thread = threading.Thread(target=self._run_task)
        thread.daemon = True
        thread.start()

    def _run_task(self):
        """在线程中运行任务"""
        try:
            success = self.task_runner.execute_task()
            Clock.schedule_once(lambda dt: self._task_completed(success), 0)
        except Exception as e:
            Clock.schedule_once(lambda dt: self._task_completed(False, str(e)), 0)

    def _task_completed(self, success, error=None):
        """任务完成回调"""
        self.is_running = False
        if success:
            self.status_text = "完成"
            self.task_result = self.task_runner.result or "成功"
        else:
            self.status_text = f"失败：{error or '未知错误'}"
            self.task_result = self.task_runner.result or "失败"

    def stop_task(self):
        """停止任务（暂不支持强制停止）"""
        self.status_text = "停止中..."
        self.is_running = False

    def clear_log(self):
        """清空日志"""
        self.log_text = ""


class SettingsScreen(Screen):
    """设置界面"""

    target_text = StringProperty("畅游时代")
    click_delay = StringProperty("2")
    retry_count = StringProperty("3")
    enable_retry = BooleanProperty(True)

    def save_settings(self):
        """保存设置"""
        # 这里可以保存到配置文件
        pass

    def reset_settings(self):
        """重置设置"""
        self.target_text = "畅游时代"
        self.click_delay = "2"
        self.retry_count = "3"
        self.enable_retry = True


class AScriptApp(App):
    """AScript 自动化控制应用"""

    def build(self):
        """构建应用界面"""
        # 创建屏幕管理器
        sm = ScreenManager()

        # 添加控制面板
        control_panel = ControlPanel(name="control")
        sm.add_widget(control_panel)

        # 添加设置界面
        settings = SettingsScreen(name="settings")
        sm.add_widget(settings)

        return sm


if __name__ == "__main__":
    AScriptApp().run()
