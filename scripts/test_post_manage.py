import time
import pytest
from page.post_manage_page import PostManagePage
from utils.driver_utils import DriverUtils


# 岗位管理测试脚本
class TestPostManageCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.post_manage_page = PostManagePage(self.driver)
        # self.train_sort_page = TrainSortPage(self.driver)

    def teardown(self):
        time.sleep(2)
        DriverUtils.quit_driver()

    @pytest.mark.run(order=39)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_query(self):
        self.post_manage_page.click_post_manage_btn()
        self.post_manage_page.input_first_search("研发")
        self.post_manage_page.click_keys_enter(self.post_manage_page.first_search)
        self.post_manage_page.input_second_search("技术")
        self.post_manage_page.click_keys_enter(self.post_manage_page.second_search)

    @pytest.mark.run(order=40)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_add_post(self):
        self.post_manage_page.refresh_page()
        self.post_manage_page.click_new_btn()
        self.post_manage_page.click_classification_select()
        self.post_manage_page.select_third_sort()
        self.post_manage_page.input_post_name(123)
        self.post_manage_page.click_determine_btn()

    @pytest.mark.run(order=41)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_modify(self):
        self.post_manage_page.click_post_name1_btn()
        self.post_manage_page.clear(self.post_manage_page.post_name_input)
        self.post_manage_page.input_post_name("修改后的名称{}".format(time.strftime("%M%S")))
        self.post_manage_page.click_determine_btn()

    @pytest.mark.run(order=42)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_remove(self):
        self.post_manage_page.click_remove_btn()
        self.post_manage_page.click_determine1_btn()
