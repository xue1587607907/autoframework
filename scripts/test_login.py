import time
import pytest
from page.learning_center_page import LearningCenterPage
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
    @pytest.mark.parametrize("params", [{"username": "aaa111", "password": "aaa111", "info": "学习中心"}])
    def test_login(self, params):
        self.login_page.username_input(params["username"])
        self.login_page.password_input(params["password"])
        self.login_page.click_login_button()
        # print(self.login_page.get_info())
        # assert self.login_page.get_info() == params["info"]
        self.learning_center_page.click_head_portrait()
        time.sleep(1)


    # i = 0
    # str = ""
    # while i < 3:
    #     num = random.randrange(48, 57)
    #     if num < 57:
    #         str += chr(num)
    #         i += 1
    #
    # @pytest.mark.parametrize("params", [{"useraccount": "xue"+str, "name": "xue"+str}])
    # def test_add_user(self, params):
    #     self.account_dm_page.click_add_user()
    #     self.account_dm_page.input_user_account(params["useraccount"])
    #     self.account_dm_page.input_username(params["name"])
    #     self.account_dm_page.select_department()
    #     time.sleep(2)
    #     self.account_dm_page.click_preservation()
    #
    # @pytest.mark.parametrize("params", [{"useraccount": "aaa"+str, "name": "aaa"+str}])
    # def test_modify_personal_data(self, params):
    #     self.account_dm_page.click_account_button()
    #     self.account_dm_page.clear_user_account()
    #     self.account_dm_page.input_user_account(params["useraccount"])
    #     self.account_dm_page.clear_username()
    #     self.account_dm_page.input_username(params["name"])
    #     self.account_dm_page.click_preservation()
    #     time.sleep(2)
    #
    # def test_query(self):
    #     self.account_dm_page.input_department("技术部")
    #     self.account_dm_page.input_account("aaa")
    #     self.account_dm_page.clear_account()
    #     self.account_dm_page.click_enter()
    #     self.account_dm_page.click_status_filter()
    #     self.account_dm_page.click_disable()
    #     self.account_dm_page.click_status_filter()
    #     self.account_dm_page.click_enable()
    #     time.sleep(2)
    #
    # def test_click_disable(self):
    #     self.account_dm_page.click_more_btn()
    #     self.account_dm_page.click_more_disable_btn()
    #     self.driver.implicitly_wait(10)
    #     self.account_dm_page.click_determine_btn()
    #     time.sleep(3)
    #












