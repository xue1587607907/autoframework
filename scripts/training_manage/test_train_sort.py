import pytest
import time
from page.training_manage.train_sort_page import TrainSortPage
from utils.driver_utils import DriverUtils


# 培训分类测试脚本
class TestTrainSortCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.train_sort_page = TrainSortPage(self.driver)

    def teardown(self):
        DriverUtils.quit_driver()

    @pytest.mark.run(order=60)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_sort_query(self):
        self.train_sort_page.click_train_manage_btn()
        self.train_sort_page.input_content_first_search("普通员工")
        self.train_sort_page.click_keys_enter(self.train_sort_page.first_search)
        self.train_sort_page.input_content_second_search("公司会议")
        self.train_sort_page.click_keys_enter(self.train_sort_page.first_search)
        self.train_sort_page.refresh_page()
        self.train_sort_page.click_new_btn()
        self.train_sort_page.click_parent_sort()
        self.train_sort_page.select_sort()
        self.train_sort_page.click_blank_area()
        self.train_sort_page.input_sort_name("二级分类{}".format(time.strftime("%M%S")))
        self.train_sort_page.click_determine_btn()

    @pytest.mark.run(order=61)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_modify_sort_content(self):
        self.train_sort_page.refresh_page()
        self.train_sort_page.input_sort_name1("二级分类")
        self.train_sort_page.click_keys_enter(self.train_sort_page.sort_name_search)
        self.train_sort_page.click_sort_name_btn()
        self.train_sort_page.clear(self.train_sort_page.sort_name_input)
        self.train_sort_page.input_sort_name("修改后{}".format(time.strftime("%M%S")))
        self.train_sort_page.click_determine_btn()

    @pytest.mark.run(order=62)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_more_operation(self):
        self.train_sort_page.refresh_page()
        self.train_sort_page.click_move_up_btn()
        self.train_sort_page.click_move_down_btn()
        # self.train_sort_page.click_remove_btn()
        # self.train_sort_page.click_determine1_btn()

