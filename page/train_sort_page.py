from selenium.webdriver.common.by import By

from base.base_action import BaseAction


# 培训分类页面
class TrainSortPage(BaseAction):

    # 培训规划按钮
    train_plan_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[1]/span[2]"

    # 培训分类按钮
    train_sort_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[2]"

    #