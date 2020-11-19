from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 学习中心页面
class LearningCenterPage(BaseAction):

    # 头像按钮
    head_portrait = By.CSS_SELECTOR, "#app > div > div.jw-bottom-flow-auto > div.jw-main-content-contain.jw-position-relative > div.jw-header-top > div > div.jw-header-top-right > div > div.jw-user-face"

    # 切换管理端按钮
    switch_manage_btn = By.CSS_SELECTOR, "#app > div > div.jw-bottom-flow-auto > div.jw-main-content-contain.jw-position-relative > div.jw-header-top > div > div.jw-header-top-right > div > div.jw-user-content > div.jw-user-main > div.jw-user-bottom > span:nth-child(1)"

    # 点击客户端头像
    def click_head_portrait(self):
        return self.click(self.head_portrait)

    # 点击切换管理端
    def click_switch_manage_btn(self):
        return self.click(self.switch_manage_btn)
