import time
import pytest
from page.resourse_manage.resources_sort_page import ResourcesSortPage
from utils.driver_utils import DriverUtils


# 资源分类增删改查测试脚本
class TestResourcesSortCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.resources_sort_page = ResourcesSortPage(self.driver)

    def teardown(self):
        DriverUtils.quit_driver()

    @pytest.mark.run(order=19)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_add_resources_sort(self):
        self.resources_sort_page.refresh_page()
        self.resources_sort_page.click_resources_manage()
        self.resources_sort_page.click_add_btn()
        self.resources_sort_page.select_parent_sort()
        self.resources_sort_page.click_blank_space()
        self.resources_sort_page.input_sort_name("三级分类{}".format(time.strftime("%M%S")))
        self.resources_sort_page.click_determine_btn()

    @pytest.mark.run(order=21)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_move_up_and_down(self):
        self.resources_sort_page.click_move_up_btn()
        self.resources_sort_page.click_move_down_btn()

    @pytest.mark.run(order=22)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_remove_resources_sort(self):
        self.resources_sort_page.input_sort_name_search("三级分类")
        self.resources_sort_page.click_keys_enter(self.resources_sort_page.sort_name_search)
        self.resources_sort_page.click_remove_btn()
        self.resources_sort_page.click_remove_determine_btn()







