from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 合作机构管理页面
class CooperativeOrganizationPage(BaseAction):

    # 讲师与导师按钮
    lecturer_and_tutor_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[7]/div/span[2]"

    # 合作机构管理按钮
    coo_organ_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[7]/li[2]/div/span[2]"

    # 关键字搜搜
    keyword_search = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[1]/main/div/div/div[1]/input"

    # 状态筛选框
    status_filter = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[1]/main/div/div/div[2]/div[1]/input"

    # 启用/禁用
    enable_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]"
    disable_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]"

    # 新增按钮
    new_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/button/span"

    # 名称输入框
    name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/div/div[2]/form/div[1]/div/div/input"

    # 联系人输入框
    contacts_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/div/div[2]/form/div[2]/div/div/input"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/button[1]/span"

    # 管理按钮
    manage_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div/div[2]/div[2]/div/div/div[5]/div[2]/table/tbody/tr[1]/td[6]/div/main/div/span"

    # 禁用
    disable1_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[2]/div/button[1]/span"

    # 确定按钮
    determine1_btn = By.XPATH, "/html/body/div[2]/div/div[3]/button[2]/span"

    # 删除按钮
    remove_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[2]/div/button[2]/span"

    # 点击讲师与导师按钮
    def click_lecturer_and_tutor_btn(self):
        return self.click(self.lecturer_and_tutor_btn)

    # 点击合作机构管理
    def click_coo_organ_btn(self):
        return self.click(self.coo_organ_btn)

    # 输入机构名称进行搜索
    def input_name_search(self, content):
        return self.input(self.keyword_search, content)

    # 点击状态筛选框
    def click_status_filter(self):
        return self.click(self.status_filter)

    # 点击启用
    def click_enable_btn(self):
        return self.click(self.enable_btn)

    # 点击禁用
    def click_disable_btn(self):
        return self.click(self.disable_btn)

    # 点击新增
    def click_new_btn(self):
        return self.click(self.new_btn)

    # 输入机构名称
    def input_mechanism_name(self, content):
        return self.input(self.name_input, content)

    # 点击确定按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 点击管理按钮
    def click_manage_btn(self):
        return self.click(self.manage_btn)

    # 点击禁用按钮
    def click_disable1_btn(self):
        return self.click(self.disable1_btn)

    # 点击确定按钮
    def click_determine1_btn(self):
        return self.click(self.determine1_btn)

    # 点击删除按钮
    def click_remove_btn(self):
        return self.click(self.remove_btn)
