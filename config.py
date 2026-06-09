"""
项目配置文件
集中管理所有可配置参数，避免硬编码
"""

# 目标元素配置
TARGET_CONFIG = {
    "text": "畅游时代",
    "clickable": True,
    "timeout": 10,  # 查找超时时间（秒）
    "retry_count": 3  # 重试次数
}

# 延时配置
DELAY_CONFIG = {
    "after_click": 2,  # 点击后等待时间（秒）
    "between_actions": 1,  # 操作间隔时间（秒）
    "page_load": 3  # 页面加载等待时间（秒）
}

# 日志配置
LOG_CONFIG = {
    "level": "INFO",  # 日志级别：DEBUG, INFO, WARNING, ERROR
    "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    "file": "logs/app.log"  # 日志文件路径
}

# Toast 消息配置
MESSAGE_CONFIG = {
    "not_found": "未找到：{target}",
    "click_success": "点击：{target}",
    "error": "错误：{error}"
}
