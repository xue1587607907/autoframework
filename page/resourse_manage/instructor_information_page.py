from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 讲师信息页面
class InstructorInformationPage(BaseAction):

    # 讲师与导师按钮
    lecturer_and_tutor_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[7]/div/span[2]"

    # 讲师信息按钮
    lecturer_info_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[7]/li[1]/div/span[2]"

    # 关键字搜索框
    keyword_search = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/main/div[1]/div[1]/div[1]/div/input"

    # 讲师类别筛选
    lecturer_type_filter = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/main/div[1]/div[1]/div[2]/div/div/input"

    # 内部讲师按钮
    inside_lecturer = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 外部讲师
    outside_lecturer = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]/span"

    # 授课类别筛选
    teach_type_filter = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/main/div[1]/div[1]/div[3]/div/div[1]/input"

    # 选择第一个
    first_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 讲师级别筛选框
    lecturer_level_filter = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/main/div[1]/div[1]/div[4]/div/div[1]/input"

    # 初级讲师按钮
    primary_lecturer = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 中级讲师
    intermediate_lecturer = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]/span"

    # 状态筛选框
    status_filter = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/main/div[1]/div[1]/div[5]/div/div/input"

    # 启用/禁用
    enable_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"
    disable_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]/span"

    # 新建讲师按钮
    add_lecturer_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/main/div[1]/div[2]/div/button/span"

    # 外部讲师按钮
    add_outside_lecturer = By.XPATH, "/html/body/ul/li[1]/p"

    # 讲师姓名输入框
    lecturer_name_input = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[1]/form/div[1]/div/div/input"

    # 账号输入框
    account_input = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[1]/form/div[2]/div/div/input"

    # 性别单选框
    sex_radio = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[1]/form/div[4]/div/div/label[1]/span[1]/span"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[3]/div/button[1]/span"

    # 姓名按钮(点击进入编辑)
    name_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/main/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div/span"

    # 禁用按钮
    disable1_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/main/div[2]/div/div[3]/table/tbody/tr[1]/td[8]/div/main/span"

    # 禁用的确定按钮
    determine1_btn = By.XPATH, "/html/body/div[2]/div/div[3]/button[2]/span"

    # 删除按钮
    remove_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div/div[5]/div[2]/table/tbody/tr[1]/td[9]/div/button/span"

    # 内部讲师按钮-------------------------------------------------------------------------------------
    add_inside_lecturer = By.XPATH, "/html/body/ul/li[2]/p"

    # 讲师姓名输入框
    lecturer_name_input1 = By.XPATH, "//*[@id='app']/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[1]/form/div[1]/div/div/input"

    # 选择内部讲师
    select_inside_lecturer = By.CSS_SELECTOR, "tr.el-table__row:nth-child(1) > td:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(1) > span:nth-child(1)"

    # 弹窗的确定按钮
    determine2_btn = By.XPATH, "/html/body/div[2]/div/div[3]/div/button[2]"

    # 外面的确定按钮
    determine3_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[3]/div/button[1]/span"

    # 点击讲师与导师按钮
    def click_lecturer_and_tutor_btn(self):
        return self.click(self.lecturer_and_tutor_btn)

    # 点击讲师信息按钮
    def click_lecturer_info_btn(self):
        return self.click(self.lecturer_info_btn)

    # 输入关键字搜索
    def input_keyword_search(self, content):
        return self.input(self.keyword_search, content)

    # 通过类别进行筛选
    def click_lecturer_type_filter(self):
        return self.click(self.lecturer_type_filter)

    # 选择内部讲师
    def click_inside_lecturer(self):
        return self.click(self.inside_lecturer)

    # 选择外部讲师
    def click_outside_lecturer(self):
        return self.click(self.outside_lecturer)

    # 通过授课类别筛选
    def click_teach_type_filter(self):
        return self.click(self.teach_type_filter)

    # 点击第一个授课类别
    def click_first_btn(self):
        return self.click(self.first_btn)

    # 通过讲师级别筛选
    def click_lecturer_level_filter(self):
        return self.click(self.lecturer_level_filter)

    # 点击初级讲师
    def click_primary_lecturer(self):
        return self.click(self.primary_lecturer)

    # 点击中级讲师
    def click_intermediate_lecturer(self):
        return self.click(self.intermediate_lecturer)

    # 点击状态筛选
    def click_status_filter(self):
        return self.click(self.status_filter)

    # 点击启用
    def click_enable_btn(self):
        return self.click(self.enable_btn)

    # 点击禁用
    def click_disable_btn(self):
        return self.click(self.disable_btn)

    # 点击新建讲师按钮
    def click_add_lecturer_btn(self):
        return self.click(self.add_lecturer_btn)

    # 点击外部讲师
    def click_add_outside_lecturer(self):
        return self.click(self.add_outside_lecturer)

    # 输入讲师姓名
    def input_lecturer_name(self, content):
        return self.input(self.lecturer_name_input, content)

    # 输入讲师账号
    def input_account(self, content):
        return self.input(self.account_input, content)

    # 选择性别
    def select_sex_radio(self):
        return self.click(self.sex_radio)

    # 点击确定
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 点击讲师姓名(进入编辑)
    def click_name_btn(self):
        return self.click(self.name_btn)

    # 清空讲师姓名
    def clear_lecturer_name_input(self):
        return self.clear(self.lecturer_name_input)

    # 点击禁用
    def click_disable1_btn(self):
        return self.click(self.disable1_btn)

    # 点击确定按钮
    def click_determine1_btn(self):
        return self.click(self.determine1_btn)

    # 点击删除
    def click_remove_btn(self):
        return self.click(self.remove_btn)

    # 点击新建内部讲师
    def click_add_inside_lecturer(self):
        return self.click(self.add_inside_lecturer)

    # 点击讲师输入框
    def click_lecturer_name_input1(self):
        return self.click(self.lecturer_name_input1)

    # 选择内部讲师
    def click_select_inside_lecturer(self):
        return self.click(self.select_inside_lecturer)

    # 点击弹窗的确定按钮
    def click_determine2_btn(self):
        return self.click(self.determine2_btn)

    # 点击外面的确定按钮
    def click_determine3_btn(self):
        return self.click(self.determine3_btn)
