import time
import pytest
from page.instructor_information_page import InstructorInformationPage
from page.resources_sort_page import ResourcesSortPage
from utils.driver_utils import DriverUtils


# 讲师信息测试脚本
class TestInstructorInformationCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.resources_sort_page = ResourcesSortPage(self.driver)
        self.ins_info_page = InstructorInformationPage(self.driver)

    def teardown(self):
        time.sleep(2)
        DriverUtils.quit_driver()

    @pytest.mark.run(order=35.1)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_query(self):
        self.resources_sort_page.refresh_page()
        self.resources_sort_page.click_resources_manage()
        self.ins_info_page.click_lecturer_and_tutor_btn()
        self.ins_info_page.click_lecturer_info_btn()
        # self.ins_info_page.input_keyword_search("张三")
        # self.ins_info_page.click_keys_enter(self.ins_info_page.keyword_search)
        # self.ins_info_page.refresh_page()
        # self.ins_info_page.click_lecturer_type_filter()
        # self.ins_info_page.click_inside_lecturer()
        # self.ins_info_page.click_lecturer_type_filter()
        # self.ins_info_page.click_outside_lecturer()
        # self.ins_info_page.refresh_page()
        # self.ins_info_page.click_teach_type_filter()
        # self.ins_info_page.click_first_btn()
        # self.ins_info_page.refresh_page()
        # self.ins_info_page.click_lecturer_level_filter()
        # self.ins_info_page.click_primary_lecturer()
        # self.ins_info_page.click_lecturer_level_filter()
        # self.ins_info_page.click_intermediate_lecturer()
        # self.ins_info_page.refresh_page()
        # self.ins_info_page.click_status_filter()
        # self.ins_info_page.click_enable_btn()
        # self.ins_info_page.click_status_filter()
        # self.ins_info_page.click_disable_btn()

    @pytest.mark.run(order=35.2)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_add_outside_lecturer(self):
        self.ins_info_page.click_add_lecturer_btn()
        self.ins_info_page.click_add_outside_lecturer()
        self.ins_info_page.input_lecturer_name("张三{}".format(time.strftime("%M%S")))
        self.ins_info_page.input_account("{}".format(time.strftime("%H%M%S")))
        self.ins_info_page.select_sex_radio()
        self.ins_info_page.click_determine_btn()

    @pytest.mark.run(order=35.3)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_modify_lecturer_info(self):
        self.ins_info_page.click_name_btn()
        self.ins_info_page.clear_lecturer_name_input()
        self.ins_info_page.input_lecturer_name("修改后{}".format(time.strftime("%M%S")))
        self.ins_info_page.clear(self.ins_info_page.account_input)
        self.ins_info_page.input_account("{}".format(time.strftime("%H%M%S")))
        self.ins_info_page.click_determine_btn()

    @pytest.mark.run(order=35.4)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_remove_and_disable(self):
        self.ins_info_page.click_disable1_btn()
        self.ins_info_page.click_determine1_btn()
        self.ins_info_page.click_remove_btn()
        self.ins_info_page.click_determine1_btn()

    @pytest.mark.run(order=35.5)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_add_inside_lecturer(self):
        self.ins_info_page.click_add_lecturer_btn()
        self.ins_info_page.click_add_inside_lecturer()
        self.ins_info_page.click_lecturer_name_input1()
        self.ins_info_page.click_select_inside_lecturer()
        self.ins_info_page.click_determine2_btn()
        self.ins_info_page.click_determine3_btn()

