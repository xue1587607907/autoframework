import random
import time
import pytest
from page.account_dm_page import AccountDM
from utils.driver_utils import DriverUtils
from page.learning_center_page import LearningCenterPage


# 组织架构增删改查
class TestAccountCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.learning_center_page = LearningCenterPage(self.driver)
        self.account_dm_page = AccountDM(self.driver)

    def teardown(self):
        time.sleep(2)
        # DriverUtils.set_switch(False)
        DriverUtils.quit_driver()

    i = 0
    str = ""
    while i < 3:
        num = random.randrange(48, 57)
        if num < 57:
            str += chr(num)
            i += 1

    @pytest.mark.run(order=2)
    @pytest.mark.skipif(condition=True, reason=None)
    @pytest.mark.parametrize("params", [{"useraccount": "xue"+str, "name": "xue"+str}])
    def test_add_user(self, params):
        self.account_dm_page.click_add_user()
        self.account_dm_page.input_user_account(params["useraccount"])
        self.account_dm_page.input_username(params["name"])
        self.account_dm_page.select_department()
        self.account_dm_page.click_preservation()

    @pytest.mark.run(order=3)
    @pytest.mark.skipif(condition=True, reason=None)
    @pytest.mark.parametrize("params", [{"useraccount": "abc{}".format(time.strftime("%H%M%S")), "name": "abc{}".format(time.strftime("%H%M%S"))}])
    def test_modify_personal_data(self, params):
        self.account_dm_page.click_account_button()
        self.account_dm_page.clear_user_account()
        self.account_dm_page.input_user_account(params["useraccount"])
        self.account_dm_page.clear_username()
        self.account_dm_page.input_username(params["name"])
        self.account_dm_page.click_preservation()

    @pytest.mark.run(order=4)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_query(self):
        self.account_dm_page.input_department("技术部")
        self.account_dm_page.input_account("jack")
        self.account_dm_page.refresh_page()
        self.account_dm_page.click_status_filter()
        self.account_dm_page.click_disable()
        self.account_dm_page.click_status_filter()
        self.account_dm_page.click_enable()

    @pytest.mark.run(order=5)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_click_disable(self):
        self.account_dm_page.click_more_btn()
        self.account_dm_page.click_more_disable_btn()
        self.driver.implicitly_wait(10)
        self.account_dm_page.click_determine_btn()

