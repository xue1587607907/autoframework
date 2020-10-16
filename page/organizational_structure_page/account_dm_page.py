from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 账号部门页面,增删改查操作
class AccountDM(BaseAction):

    # 新增按钮
    add_user = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[1]/div/button/span"

    # 用户账号
    user_account = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/form/div[1]/div/div[1]/div/input"

    # 姓名
    username = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/form/div[2]/div/div[1]/div/input"

    # 部门
    department = By.CSS_SELECTOR, ".el-cascader > div:nth-child(1) > input:nth-child(1)"
    d1 = By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/ul/li/label/span[1]/span"
    d2 = By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/ul/li[2]/label/span[1]/span"
    d3 = By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[1]/ul/li[2]/label/span[1]/span"
    d4 = By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/ul/li[1]/label/span[1]/span"
    d5 = By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[1]/ul/li[1]/label/span[1]/span"

    # 保存按钮
    preservation = By.CSS_SELECTOR, "button.el-button--primary:nth-child(1) > span:nth-child(1)"

    # 修改"账号名"按钮
    account_button = By.CSS_SELECTOR, ".el-table__fixed > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)"

    # 第一个搜索框
    first_search = By.CSS_SELECTOR, ".jw-tree-data-contain > div:nth-child(1) > input:nth-child(1)"

    # 部门放大镜
    department_mag = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div/div[1]/span/span/i"

    # 账号名放大镜
    account_mag = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[1]/main/div/div[1]/div/span/span/i"

    # 第二个搜索框
    second_search = By.CSS_SELECTOR, "div.jw-inline-block:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 状态筛选框
    status_filter = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[1]/main/div/div[2]/div/div/div"

    # 状态下的启用按钮
    enable = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 禁用
    disable = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]/span"

    # "禁用"该用户的"确定"按钮
    determine_btn = By.XPATH, "/html/body/div[3]/div/div[3]/button[2]"

    # 有效期输入框
    time_of_validity_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/form/div[13]/div/div[1]/div/input"

    # 选择日期按钮
    date_btn = By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[7]/div/span"

    # 空白区域
    blank_area = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/ul"

    # 点击新增
    def click_add_user(self):
        return self.click(self.add_user)

    # 输入用户账号
    def input_user_account(self, content):
        return self.input(self.user_account, content)

    # 输入用户名
    def input_username(self, content):
        return self.input(self.username, content)

    # 选择部门
    def select_department(self):
        self.click(self.department)
        self.click(self.d1)
        self.click(self.d2)
        return self.click(self.d3)

    # 点击保存
    def click_preservation(self):
        return self.click(self.preservation)

    # 点击用户名进入编辑
    def click_account_button(self):
        return self.click(self.account_button)

    # 清空用户账号内容
    def clear_user_account(self):
        return self.clear(self.user_account)

    # 清空姓名内容
    def clear_username(self):
        return self.clear(self.username)

    # 通过部门查询
    def input_department(self, content):
        self.input(self.first_search, content)
        self.click_enter()
        return self.clear_department()

    # 清空部门内容
    def clear_department(self):
        return self.clear(self.second_search)

    # 点击部门放大镜
    def click_department_mag(self):
        return self.click(self.department_mag)

    # 通过账号查询
    def input_account(self, content):
        self.input(self.second_search, content)
        return self.click_enter()

    # 清空账号内容
    def clear_account(self):
        return self.clear(self.second_search)

    # 点击账号放大镜
    def click_account_mag(self):
        return self.click(self.account_mag)

    # 点击状态筛选
    def click_status_filter(self):
        return self.click(self.status_filter)

    # 点击启用进行筛选
    def click_enable(self):
        return self.click(self.enable)

    # 点击禁用进行筛选
    def click_disable(self):
        return self.click(self.disable)

    # 点击回车
    def click_enter(self):
        return self.click_keys_enter(self.first_search)

    # "更多"按钮
    more_button = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[2]/div[1]/div/div/div[5]/div[2]/table/tbody/tr[1]/td[8]/div/main/main/div/button"

    # "更多"下的"禁用"按钮
    more_disable_button = By.XPATH, "/html/body/ul/li[2]"

    # 点击更多按钮
    def click_more_btn(self):
        return self.click(self.more_button)

    # 点击禁用按钮
    def click_more_disable_btn(self):
        return self.click(self.more_disable_button)

    # 点击确定按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 点击有效期输入框
    def click_time_of_validity_input(self):
        return self.click(self.time_of_validity_input)

    # 选择日期
    def select_time_of_validity(self):
        return self.click(self.date_btn)

    # 点击空白区域
    def click_blank_area(self):
        return self.click(self.blank_area)



