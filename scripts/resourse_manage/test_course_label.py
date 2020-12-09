import time
import pytest
from page.resourse_manage.course_label_page import CourseLabelPage
from page.resourse_manage.resources_sort_page import ResourcesSortPage
from utils.driver_utils import DriverUtils


# 试题库测试脚本
class TestQuestionBankCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.resources_sort_page = ResourcesSortPage(self.driver)
        self.course_label_page = CourseLabelPage(self.driver)

    def teardown(self):
        DriverUtils.quit_driver()

    @pytest.mark.run(order=24)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_add_course_label(self):
        self.resources_sort_page.refresh_page()
        self.resources_sort_page.click_resources_manage()
        self.course_label_page.click_course_label_btn()
        self.course_label_page.click_resources_sort_input()
        self.course_label_page.select_third_sort()
        self.course_label_page.click_new_btn()
        self.course_label_page.input_label_sort(123)
        self.course_label_page.input_label_name1(123)
        self.course_label_page.click_add_label_btn()
        self.course_label_page.input_label_name2("测试")
        self.course_label_page.click_move_up_btn()
        self.course_label_page.click_move_down_btn()
        self.course_label_page.click_remove_label_btn()
        self.course_label_page.click_determine_btn()

    @pytest.mark.run(order=25)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_modify_label_sort(self):
        self.course_label_page.click_edit_label_btn()
        self.course_label_page.clear(self.course_label_page.label_sort_input)
        self.course_label_page.input_label_sort("修改后{}".format(time.strftime("%H%M%S")))
        self.course_label_page.clear(self.course_label_page.label_name_input1)
        self.course_label_page.input_label_name1("修改后{}".format(time.strftime("%H%M%S")))
        self.course_label_page.click_determine_btn()

    @pytest.mark.run(order=26)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_remove_label_sort(self):
        self.course_label_page.click_remove1_label_btn()
        self.course_label_page.click_determine1_btn()



