from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 学习中心页面
class LearningCenterPage(BaseAction):

    # 头像按钮
    # head_portrait = By.CLASS_NAME, "jw-user-face"
    head_portrait = By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/div/div[2]/div"

    # 点击头像进入后台
    def click_head_portrait(self):
        return self.click(self.head_portrait)
