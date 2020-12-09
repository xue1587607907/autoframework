import time
import pytest
from page.organizational_structure.post_manage_page import PostManagePage
from utils.driver_utils import DriverUtils


# 岗位管理测试脚本
class TestPostManageCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.post_manage_page = PostManagePage(self.driver)

    def teardown(self):
        # time.sleep(1)
        DriverUtils.quit_driver()

    @pytest.mark.run(order=6)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_query(self):
        self.post_manage_page.refresh_page()
        self.post_manage_page.click_post_manage_btn()
        self.post_manage_page.input_first_search("研发")
        self.post_manage_page.click_keys_enter(self.post_manage_page.first_search)
        self.post_manage_page.input_second_search("技术")
        self.post_manage_page.click_keys_enter(self.post_manage_page.second_search)

    @pytest.mark.run(order=7)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_add_post(self):
        self.post_manage_page.refresh_page()
        self.post_manage_page.click_new_btn()
        self.post_manage_page.click_classification_select()
        self.post_manage_page.select_third_sort()
        self.post_manage_page.input_post_name("测试{}".format(time.strftime("%M%S")))
        self.post_manage_page.click_determine_btn()

    @pytest.mark.run(order=8)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_modify(self):
        self.post_manage_page.click_post_name1_btn()
        self.post_manage_page.clear(self.post_manage_page.post_name_input)
        self.post_manage_page.input_post_name("修改后的名称{}".format(time.strftime("%M%S")))
        self.post_manage_page.click_determine_btn()
        # 打开新窗口,切换句柄
        self.post_manage_page.click_manage_user_btn1()
        self.post_manage_page.switch_window()
        self.post_manage_page.click_select_user_radio()
        self.post_manage_page.click_adjust_post_btn()
        self.post_manage_page.click_new_post_select()
        self.post_manage_page.click_select_post()
        self.post_manage_page.click_blank_area1()
        self.post_manage_page.click_select_post_input()
        self.post_manage_page.click_select_specific_post()
        self.post_manage_page.click_determine2_btn()

    @pytest.mark.run(order=9)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_remove(self):
        self.post_manage_page.click_post_manage_btn()
        self.post_manage_page.click_remove_btn()
        self.post_manage_page.click_determine1_btn()
