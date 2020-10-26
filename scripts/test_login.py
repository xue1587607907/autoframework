import time
import pytest
from page.learning_center.learning_center_page import LearningCenterPage
from page.login_page import LoginPage
from utils.driver_utils import DriverUtils


# 登录测试脚本
class TestLogin:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.login_page = LoginPage(self.driver)
        self.learning_center_page = LearningCenterPage(self.driver)
        self.driver.get("http://test.elearning.learnfuture.com")

    def teardown(self):
        time.sleep(1)
        # DriverUtils.set_switch(False)
        DriverUtils.quit_driver()

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("params", [{"username": "cw01", "password": "cw01", "info": "学习中心"}])
    def test_login(self, params):
        self.login_page.username_input(params["username"])
        self.login_page.password_input(params["password"])
        self.login_page.click_login_button()
        # print(self.login_page.get_info())
        # assert self.login_page.get_info() == params["info"]
        self.learning_center_page.click_head_portrait()
        self.learning_center_page.click_switch_manage_btn()
        time.sleep(1)













