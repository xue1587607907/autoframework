import time
import pytest
from page.organizational_structure.role_permission_manage_page import RolePermissionManagePage
from utils.driver_utils import DriverUtils


# 角色权限管理
class TestRolePermissionManageCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.role_permission_manage_page = RolePermissionManagePage(self.driver)

    def teardown(self):
        time.sleep(1)
        DriverUtils.quit_driver()

    @pytest.mark.run(order=14.2)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_add(self):
        self.role_permission_manage_page.refresh_page()
        self.role_permission_manage_page.click_role_permission_manage_btn()
        self.role_permission_manage_page.input_keyword_search("讲师")
        self.role_permission_manage_page.click_keys_enter(self.role_permission_manage_page.keyword_search)
        self.role_permission_manage_page.refresh_page()
        self.role_permission_manage_page.click_add_btn()
        self.role_permission_manage_page.input_role_name("管理员{}".format(time.strftime("%M%S")))
        self.role_permission_manage_page.input_role_explain("角色说明内容")
        self.role_permission_manage_page.click_function_check_box()
        self.role_permission_manage_page.click_determine_btn()

    @pytest.mark.run(order=14.4)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_remove_and_manage(self):
        self.role_permission_manage_page.refresh_page()
        self.role_permission_manage_page.click_manage_user()
        self.role_permission_manage_page.switch_window()
        self.role_permission_manage_page.click_add_user_btn()
        self.role_permission_manage_page.click_select_all()
        self.role_permission_manage_page.click_determine_btn1()
        self.role_permission_manage_page.click_role_permission_manage_btn()
        self.role_permission_manage_page.click_copy_role()
        self.role_permission_manage_page.clear_role_name_input()
        self.role_permission_manage_page.input_role_name("复制后{}".format(time.strftime("%M%S")))
        self.role_permission_manage_page.click_determine_btn()
        # self.role_permission_manage_page.click_remove_role()
        # self.role_permission_manage_page.click_determine_btn2()




