from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 学习中心页面
class LearningCenterPage(BaseAction):

    # 头像按钮
    # head_portrait = By.CLASS_NAME, "jw-user-face"
    head_portrait = By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/div[2]/div"

    # 切换管理端按钮
    switch_manage_btn = By.XPATH, "/html/body/div/div/div[2]/div[1]/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/span[1]"

    # 点击客户端头像
    def click_head_portrait(self):
        return self.click(self.head_portrait)

    # 点击切换管理端
    def click_switch_manage_btn(self):
        return self.click(self.switch_manage_btn)
