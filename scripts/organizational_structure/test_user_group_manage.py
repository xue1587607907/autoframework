import time
import pytest
from page.organizational_structure.user_group_manage_page import UserGroupManagePage
from utils.driver_utils import DriverUtils


# 用户组管理
class TestUserGroupManageCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.user_group_manage_page = UserGroupManagePage(self.driver)

    def teardown(self):
        time.sleep(1)
        DriverUtils.quit_driver()

    @pytest.mark.run(order=12)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_query_and_add(self):
        self.user_group_manage_page.refresh_page()
        self.user_group_manage_page.click_user_group_manage_btn()
        self.user_group_manage_page.input_user_group_name("教育")
        self.user_group_manage_page.click_keys_enter(self.user_group_manage_page.user_group_search)
        self.user_group_manage_page.refresh_page()
        self.user_group_manage_page.click_new_btn()
        self.user_group_manage_page.input_user_group_name1("测试用户组")
        self.user_group_manage_page.click_determine_btn()

    @pytest.mark.run(order=13)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_modify(self):
        self.user_group_manage_page.click_user_group_name_btn()
        self.user_group_manage_page.clear_user_group_name()
        self.user_group_manage_page.input(self.user_group_manage_page.user_group_name_input1, "修改后{}".format(time.strftime("%M%S")))
        self.user_group_manage_page.click(self.user_group_manage_page.determine_btn)

    @pytest.mark.run(order=14)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_more(self):
        self.user_group_manage_page.click_manage_user_btn()
        self.user_group_manage_page.switch_window()
        self.user_group_manage_page.click_add_btn()
        self.user_group_manage_page.click_select_all()
        self.user_group_manage_page.click_determine1_btn()
        self.user_group_manage_page.click_select_the_first()
        self.user_group_manage_page.click_remove_btn()
        self.user_group_manage_page.click_user_group_manage_btn()
        self.user_group_manage_page.click_remove1_btn()
        self.user_group_manage_page.click_determine2_btn()
