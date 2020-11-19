import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


# 页面基础操作
class BaseAction:

    # 初始化驱动
    def __init__(self, driver):
        self.driver = driver

    # 定位单个元素
    def find_el(self, feature):
        return self.driver.find_element(*feature)

    # 定位一组元素
    def find_els(self, feature):
        return self.driver.find_elment(*feature)

    # 点击操作
    def click(self, feature):
        time.sleep(1)
        return self.find_el(feature).click()

    # 输入操作
    def input(self, feature, content):
        time.sleep(1)
        return self.find_el(feature).send_keys(content)

    # 清空操作
    def clear(self, feature):
        time.sleep(1)
        return self.find_el(feature).clear()

    # 切换frame
    def switch_to(self, feature_frame):
        return self.driver.switch_to.frame(self.find_el(feature_frame))

    # 切换为默认
    def switch_to_default(self):
        return self.driver.switch_to.deafault.content()

    # 切换到新窗口
    def switch_window(self):
        handles = self.driver.window_handles
        return self.driver.switch_to.window(handles[-1])

    # 回车键处理
    def click_keys_enter(self, feature):
        return self.find_el(feature).send_keys(Keys.ENTER)

    # 回退键处理
    def click_key_backspace(self, feature):
        return self.find_el(feature).send_keys(Keys.BACK_SPACE)

    # 全选
    def select_all(self, feature):
        return self.find_el(feature).send_keys(Keys.CONTROL, "a")

    # 页面刷新
    def refresh_page(self):
        time.sleep(1)
        return self.driver.refresh()

    # 后退
    def back_off(self):
        time.sleep(2)
        return self.driver.back()

    # 鼠标悬停操作
    def move_mouse(self, feature):
        action = ActionChains(self.driver)
        return action.move_to_element(self.find_el(feature)).perform()

