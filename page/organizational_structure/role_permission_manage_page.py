from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 角色权限管理页面
class RolePermissionManagePage(BaseAction):

    # 角色权限管理按钮
    role_permission_manage_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[5]/div/span[2]"

    # 关键字搜索框
    keyword_search = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[1]/main/div/div[1]/div/input"

    # 新增按钮
    add_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/button/span"

    # 角色名称输入框
    role_name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/div/div[2]/form/div[1]/div/div/input"

    # 角色说明输入框
    role_explain = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/div/div[2]/form/div[2]/div/div/textarea"

    # 功能复选框
    function_check_box = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/div/div[2]/form/div[3]/div/div[1]/div[1]/div[1]/label/span/span"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/button[1]"

    # 管理用户
    manage_user_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[2]/div/div/div[5]/div[2]/table/tbody/tr[2]/td[4]/div/main/main/main/span[1]"

    # 添加用户按钮
    add_user_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/button[1]/span"

    # 全选框
    select_all = By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[3]/div[2]/div/div/div[2]/table/thead/tr/th[1]/div/label/span/span"

    # 确定按钮
    determine_btn1 = By.XPATH, "/html/body/div[2]/div/div[3]/div/button[1]"

    # 复制角色
    copy_role = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[2]/div/div/div[5]/div[2]/table/tbody/tr[1]/td[4]/div/main/main/main/span[2]"

    # 删除角色
    remove_role = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[2]/div/div/div[5]/div[2]/table/tbody/tr[2]/td[4]/div/main/main/main/span[3]"

    # 确定按钮
    determine_btn2 = By.XPATH, "/html/body/div[2]/div/div[3]/button[2]/span"

    # 点击角色权限管理按钮
    def click_role_permission_manage_btn(self):
        return self.click(self.role_permission_manage_btn)

    # 输入关键字进行搜索
    def input_keyword_search(self, context):
        return self.input(self.keyword_search, context)

    # 点击新增按钮
    def click_add_btn(self):
        return self.click(self.add_btn)

    # 输入角色名称
    def input_role_name(self, context):
        return self.input(self.role_name_input, context)

    # 输入角色说明
    def input_role_explain(self, context):
        return self.input(self.role_explain, context)

    # 点击功能复选框
    def click_function_check_box(self):
        return self.click(self.function_check_box)

    # 点击确定按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 点击管理用户
    def click_manage_user(self):
        return self.click(self.manage_user_btn)

    # 点击添加用户
    def click_add_user_btn(self):
        return self.click(self.add_user_btn)

    # 点击全选
    def click_select_all(self):
        return self.click(self.select_all)

    # 点击确定按钮
    def click_determine_btn1(self):
        return self.click(self.determine_btn1)

    # 点击复制角色
    def click_copy_role(self):
        return self.click(self.copy_role)

    # 清空角色名称
    def clear_role_name_input(self):
        return self.clear(self.role_name_input)

    # 点击删除按钮
    def click_remove_role(self):
        return self.click(self.remove_role)

    # 点击确定按钮
    def click_determine_btn2(self):
        return self.click(self.determine_btn2)




