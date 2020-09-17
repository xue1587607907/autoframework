from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 岗位管理页面
class PostManagePage(BaseAction):

    # 岗位管理按钮
    post_manage_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[2]"

    # 岗位搜索框
    post_search = By.CSS_SELECTOR, ".jw-tree-data-contain > div:nth-child(1) > input:nth-child(1)"

    # 岗位名称搜索框
    post_name_search = By.CSS_SELECTOR, "div.jw-inline-block > div:nth-child(1) > input:nth-child(1)"

