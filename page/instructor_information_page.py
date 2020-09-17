from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 讲师信息页面
class InstructorInformationPage(BaseAction):

    # 讲师与导师按钮
    lecturer_and_tutor_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[7]/span[2]"

    # 讲师信息按钮
    lecturer_info_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[8]/span[2]"
