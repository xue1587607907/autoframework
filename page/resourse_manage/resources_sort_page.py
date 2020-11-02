import time
from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 资源分类页
class ResourcesSortPage(BaseAction):

    # 资源管理按钮
    resources_btn = By.XPATH, "/html/body/div/div/div[3]/div[2]/ul/li[3]/span"

    # 新增按钮
    add_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[1]/div/button/span"

    # 父级分类输入框
    parent_sort = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[1]/main/div/div[2]/div/div[2]/form/div[1]/div/div/div[1]/input"

    # 资源分类
    d1 = By.XPATH, "/html/body/div[3]/div[1]/div[1]/div[1]/ul/li/span"
    d2 = By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/ul/li/span"
    d3 = By.XPATH, "/html/body/div[3]/div[1]/div[3]/div[1]/ul/li/label/span[1]/span"

    # 分类名称
    sort_name = By.CSS_SELECTOR, "div.el-form-item:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)"

    # 点击任意空白处
    blank_space = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[1]/main/div/div[2]/div/div[1]"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[1]/main/div/div[2]/div/div[3]/div/button[1]"

    # 资源名称
    resources_name = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[3]/td[1]/div/div/span"

    # 上移按钮
    move_up_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr[3]/td[2]/div/main/main/div/span[2]"

    # 下移按钮
    move_down_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr[2]/td[2]/div/main/main/div/span[3]"

    # 删除按钮
    remove_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr[3]/td[2]/div/main/main/div/span[1]"

    # 删除弹出的"确定"按钮
    remove_determine_btn = By.CSS_SELECTOR, "button.el-button--small:nth-child(2) > span:nth-child(1)"

    # 部门搜索框
    department_search = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div/div[1]/input"

    # 资源名称搜索框
    resources_name_search = By.CSS_SELECTOR, "div.jw-inline-block > div:nth-child(1) > input:nth-child(1)"

    #  点击资源管理
    def click_resources_manage(self):
        return self.click(self.resources_btn)

    # 点击新增按钮
    def click_add_btn(self):
        return self.click(self.add_btn)

    # 选择父级分类
    def select_parent_sort(self):
        self.click(self.parent_sort)
        self.click(self.d1)
        self.click(self.d2)
        self.click(self.d3)

    # 输入分类名称
    def input_sort_name(self, content):
        return self.input(self.sort_name, content)

    # 点击空白处
    def click_blank_space(self):
        return self.click(self.blank_space)

    # 点击"确定"按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 点击资源名称
    def click_resources_name(self):
        return self.click(self.resources_name)

    # 清空资源名称输入框
    def clear_resources_name_input(self):
        return self.clear(self.sort_name)

    # 点击上移按钮
    def click_move_up_btn(self):
        return self.click(self.move_up_btn)

    # 点击下移按钮
    def click_move_down_btn(self):
        return self.click(self.move_down_btn)

    # 点击删除按钮
    def click_remove_btn(self):
        return self.click(self.remove_btn)

    # 删除的弹窗的"确定"按钮
    def click_remove_determine_btn(self):
        return self.click(self.remove_determine_btn)

    # 点击资源分类输入框
    def click_resources_sort_search(self):
        return self.click(self.resources_name_search)

    # 在资源分类输入框输入内容
    def input_resources_sort(self, feature):
        return self.input(self.resources_name_search, feature)



