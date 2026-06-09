"""
重试机制模块
提供自动重试功能，增强稳定性
"""

import time
from functools import wraps
from utils.logger import logger
from config import TARGET_CONFIG


def retry_on_failure(max_retries=None, delay=1):
    """
    重试装饰器：当函数执行失败时自动重试

    Args:
        max_retries: 最大重试次数，默认使用配置文件
        delay: 每次重试之间的延迟（秒）

    Returns:
        装饰器函数
    """
    if max_retries is None:
        max_retries = TARGET_CONFIG["retry_count"]

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None

            for attempt in range(1, max_retries + 1):
                try:
                    logger.debug(f"执行 {func.__name__} (尝试 {attempt}/{max_retries})")
                    result = func(*args, **kwargs)

                    if result is not None:
                        logger.info(f"{func.__name__} 执行成功")
                        return result

                    logger.warning(f"{func.__name__} 返回 None，准备重试...")

                except Exception as e:
                    last_error = e
                    logger.error(f"{func.__name__} 执行失败：{str(e)}")

                if attempt < max_retries:
                    logger.info(f"等待 {delay} 秒后重试...")
                    time.sleep(delay)

            logger.error(f"{func.__name__} 达到最大重试次数")
            raise last_error or Exception("达到最大重试次数")

        return wrapper
    return decorator
