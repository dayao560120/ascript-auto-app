"""
日志工具模块
提供统一的日志记录功能
"""

import logging
import os
from config import LOG_CONFIG


def setup_logger(name: str = "AScript") -> logging.Logger:
    """
    配置并返回日志记录器

    Args:
        name: 日志记录器名称

    Returns:
        配置好的 Logger 实例
    """
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, LOG_CONFIG["level"]))

    # 创建日志目录
    log_dir = os.path.dirname(LOG_CONFIG["file"])
    os.makedirs(log_dir, exist_ok=True)

    # 文件处理器
    file_handler = logging.FileHandler(LOG_CONFIG["file"], encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)

    # 控制台处理器
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # 设置格式
    formatter = logging.Formatter(LOG_CONFIG["format"])
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# 创建全局 logger 实例
logger = setup_logger()
