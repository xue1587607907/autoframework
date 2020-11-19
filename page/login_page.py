from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 登录页
class LoginPage(BaseAction):

    # 用户名输入框
    input_username = By.CSS_SELECTOR, "div.el-form-item:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(2)"
    # 密码输入框
    input_password = By.CSS_SELECTOR, ".el-input--suffix > input:nth-child(2)"
    # 登录按钮
    login_button = By.CSS_SELECTOR, ".login-btn"
    # 获取信息
    info = By.CSS_SELECTOR, "div.jw-top-menu-item:nth-child(3) > span:nth-child(1) "

    # 输入用户名
    def username_input(self, content):
        return self.input(self.input_username, content)

    # 输入密码
    def password_input(self, content):
        return self.input(self.input_password, content)

    # 点击登录按钮
    def click_login_button(self):
        return self.click(self.login_button)

    # 获取信息
    def get_info(self):
        return self.find_el(self.info).text





