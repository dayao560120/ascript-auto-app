"""
AScript 自动化项目主入口
功能：查找并点击指定的 UI 元素
"""

# 标准库导入
import time
from typing import Optional

# 第三方库导入
from ascript.android.node import Selector, Node
from ascript.android.ui import Dialog

# 本地模块导入
from config import TARGET_CONFIG, DELAY_CONFIG, MESSAGE_CONFIG
from utils.logger import logger
from utils.retry import retry_on_failure


@retry_on_failure(max_retries=TARGET_CONFIG["retry_count"], delay=1)
def find_target_element(text: str, clickable: bool = True) -> Optional[Node]:
    """
    查找目标 UI 元素

    Args:
        text: 元素文本内容
        clickable: 是否要求元素可点击

    Returns:
        找到的节点对象，未找到返回 None
    """
    logger.info(f"开始查找元素：'{text}'")

    target = (
        Selector()
        .text(text)
        .clickable(clickable)
        .find()
    )

    if target:
        logger.info(f"成功找到元素：'{text}'")
    else:
        logger.warning(f"未找到元素：'{text}'")

    return target


def click_element(element: Node) -> bool:
    """
    点击 UI 元素

    Args:
        element: 要点击的节点对象

    Returns:
        点击是否成功
    """
    try:
        logger.info(f"点击元素：{element}")
        element.click()
        logger.info("点击成功")
        return True
    except Exception as e:
        logger.error(f"点击失败：{str(e)}")
        return False


def main():
    """
    主函数：执行自动化流程

    流程：
    1. 查找目标元素
    2. 显示提示信息
    3. 点击元素
    4. 等待界面响应
    """
    logger.info("=" * 50)
    logger.info("启动 AScript 自动化任务")
    logger.info("=" * 50)

    try:
        # 查找目标元素
        target = find_target_element(
            text=TARGET_CONFIG["text"],
            clickable=TARGET_CONFIG["clickable"]
        )

        if target is None:
            message = MESSAGE_CONFIG["not_found"].format(
                target=TARGET_CONFIG["text"]
            )
            Dialog.toast(message)
            logger.warning(message)
            return

        # 显示成功提示
        message = MESSAGE_CONFIG["click_success"].format(
            target=TARGET_CONFIG["text"]
        )
        Dialog.toast(message)

        # 点击元素
        if click_element(target):
            # 等待界面响应
            logger.info(f"等待 {DELAY_CONFIG['after_click']} 秒...")
            time.sleep(DELAY_CONFIG["after_click"])
            logger.info("任务完成")
        else:
            logger.error("点击操作失败")

    except Exception as e:
        error_message = MESSAGE_CONFIG["error"].format(error=str(e))
        Dialog.toast(error_message)
        logger.error(f"任务执行异常：{error_message}", exc_info=True)


# 程序入口
if __name__ == "__main__":
    main()