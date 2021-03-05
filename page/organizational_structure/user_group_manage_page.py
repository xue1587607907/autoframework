from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 用户组页面
class UserGroupManagePage(BaseAction):

    # 用户组管理按钮
    user_group_manage_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[1]/ul/li[4]"

    # 用户组搜索框
    user_group_search = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[1]/main/div/div/div/input"

    # 新增按钮
    new_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/button/span"

    # 用户组名称输入框
    user_group_name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/div/div[2]/form/div[1]/div/div[1]/input"
    # 编辑用户组,用户组名称的属性有更改
    user_group_name_input1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/div/div[2]/form/div[1]/div/div/input"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/button[1]/span"

    # 用户组名称按钮(点击进入编辑)
    user_group_name_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/span/span"

    # 管理用户按钮
    manage_user_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div/div[2]/div[2]/div/div/div[5]/div[2]/table/tbody/tr[1]/td[4]/div/main/div/span[1]"

    # "添加"用户按钮
    add_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/button[1]"

    # 全选框
    select_all = By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[3]/div[2]/div/div/div[2]/table/thead/tr/th[1]/div/label/span/span"

    # 确定按钮
    determine1_btn = By.XPATH, "/html/body/div[2]/div/div[3]/div/button[1]/span"

    # 选择所有数据(移除)
    select_the_first = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[2]/div/div/div[4]/div[1]/table/thead/tr/th[1]/div/label/span/span"

    # 移除按钮
    remove_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/button[2]/span"

    # 删除按钮
    remove1_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div/div[2]/div[2]/div/div/div[5]/div[2]/table/tbody/tr[1]/td[4]/div/main/div/span[2]"

    # 确定按钮
    determine2_btn = By.XPATH, "/html/body/div[2]/div/div[3]/button[2]/span"

    # 点击用户组管理
    def click_user_group_manage_btn(self):
        return self.click(self.user_group_manage_btn)

    # 搜索框输入内容
    def input_user_group_name(self, content):
        return self.input(self.user_group_search, content)

    # 点击新增
    def click_new_btn(self):
        return self.click(self.new_btn)

    # 输入用户组名称
    def input_user_group_name1(self, content):
        return self.input(self.user_group_name_input, content)

    # 点击确定按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 点击用户组名称进入编辑
    def click_user_group_name_btn(self):
        return self.click(self.user_group_name_btn)

    # 清空原有名称
    def clear_user_group_name(self):
        return self.clear(self.user_group_name_input1)

    # 点击管理用户按钮
    def click_manage_user_btn(self):
        return self.click(self.manage_user_btn)

    # 点击添加用户
    def click_add_btn(self):
        return self.click(self.add_btn)

    # 点击全选
    def click_select_all(self):
        return self.click(self.select_all)

    # 点击确定
    def click_determine1_btn(self):
        return self.click(self.determine1_btn)

    # 选择第一条数据
    def click_select_the_first(self):
        return self.click(self.select_the_first)

    # 点击移除
    def click_remove_btn(self):
        return self.click(self.remove_btn)

    # 点击删除按钮,删除用户组
    def click_remove1_btn(self):
        return self.click(self.remove1_btn)

    # 点击确定按钮
    def click_determine2_btn(self):
        return self.click(self.determine2_btn)



