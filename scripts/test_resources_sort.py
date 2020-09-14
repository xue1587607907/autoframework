import random
import time
import pytest
from page.resources_sort_page import ResourcesSortPage
from utils.driver_utils import DriverUtils


# 资源分类增删改查测试脚本
class TestResourcesSortCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.resources_sort_page = ResourcesSortPage(self.driver)

    def teardown(self):
        time.sleep(1)
        DriverUtils.quit_driver()

    # def teardown_class(self):
    #     time.sleep(2)
    #     DriverUtils.set_switch(False)
    #     DriverUtils.quit_driver()

    i = 0
    str = ""
    while i < 4:
        num = random.randrange(48, 57)
        if num < 57:
            str += chr(num)
            i += 1

    @pytest.mark.run(order=6)
    @pytest.mark.skipif(condition=True, reason=None)
    @pytest.mark.parametrize("params", [{"name": "三级分类"+str}])
    def test_add_resources_sort(self, params):
        self.resources_sort_page.refresh_page()
        self.resources_sort_page.click_resources_manage()
        self.resources_sort_page.click_add_btn()
        self.resources_sort_page.select_parent_sort()
        self.resources_sort_page.click_blank_space()
        self.resources_sort_page.input_sort_name(params["name"])
        self.resources_sort_page.click_determine_btn()

    @pytest.mark.run(order=7)
    @pytest.mark.skipif(condition=True, reason=None)
    @pytest.mark.parametrize("params", [{"name": "修改后的分类{}".format(time.strftime("%Y%m%d%H%M%S"))}])
    def test_modify_resources_name(self, params):
        self.resources_sort_page.refresh_page()
        self.resources_sort_page.click_resources_name()
        self.resources_sort_page.clear_resources_name_input()
        self.resources_sort_page.input_sort_name(params["name"])
        self.resources_sort_page.click_determine_btn()
        time.sleep(3)

    @pytest.mark.run(order=8)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_move_up_and_down(self):
        self.resources_sort_page.refresh_page()
        self.resources_sort_page.click_move_up_btn()
        # self.resources_sort_page.move_mouse_resources_sort()
        # js = "window.scrollTo(0,1000)"
        # self.driver.execute_script(js)
        # self.resources_sort_page.click_wps()
        self.resources_sort_page.click_move_down_btn()
        time.sleep(3)

    @pytest.mark.run(order=9)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_remove_resources_sort(self):
        self.resources_sort_page.click_remove_btn()
        self.resources_sort_page.click_remove_determine_btn()
        self.resources_sort_page.refresh_page()
        # self.resources_sort_page.click_wps()
        time.sleep(1)

    @pytest.mark.run(order=10)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_query_resources_sort(self):
        self.resources_sort_page.click_resources_sort_search()
        self.resources_sort_page.input_resources_sort("三级分类")
        self.resources_sort_page.click_keys_enter(self.resources_sort_page.resources_name_search)
        self.resources_sort_page.refresh_page()





