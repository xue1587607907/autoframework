import time
import pytest
from page.training_manage.exam_manage_page import ExamManagePage
from page.training_manage.live_manage_page import LiveManagePage
from utils.driver_utils import DriverUtils


# 直播管理测试脚本
class TestLiveManageCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.exam_manage = ExamManagePage(self.driver)
        self.live_manage_page = LiveManagePage(self.driver)

    def teardown(self):
        time.sleep(1)
        DriverUtils.quit_driver()

    @pytest.mark.run(order=74)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_query(self):
        self.exam_manage.refresh_page()
        self.exam_manage.click_train_manage_btn()
        self.live_manage_page.click_live_manage_btn()
        self.live_manage_page.input_live_name_search("测试")
        self.live_manage_page.click_keys_enter(self.live_manage_page.live_name_search)
        self.live_manage_page.refresh_page()
        self.live_manage_page.click_live_type_filter()
        self.live_manage_page.click_select_course_live()
        self.live_manage_page.click_live_type_filter()
        self.live_manage_page.click_select_custom_live()
        self.live_manage_page.refresh_page()
        self.live_manage_page.click_organizational_form()
        self.live_manage_page.click_select_direct_initiation()
        self.live_manage_page.click_organizational_form()
        self.live_manage_page.click_select_indirect_initiation()
        self.live_manage_page.refresh_page()
        self.live_manage_page.click_status_filter()
        self.live_manage_page.click_select_unpublished()
        self.live_manage_page.click_status_filter()
        self.live_manage_page.click_select_end()

    @pytest.mark.run(order=75)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_add_course_live(self):
        self.live_manage_page.refresh_page()
        self.live_manage_page.click_add_live_btn()
        self.live_manage_page.click_live_name_input()
        self.live_manage_page.click_select_interaction_course()
        self.live_manage_page.click_determine_btn1()
        self.live_manage_page.click_train_sort_input()
        self.live_manage_page.click_select_train_sort()
        self.live_manage_page.click_select_blank_area()
        self.live_manage_page.click_lecturer_input()
        self.live_manage_page.click_select_lecturer()
        self.live_manage_page.click_determine_btn2()
        self.live_manage_page.input_section_name("小节1")
        self.live_manage_page.click_live_date_input()
        self.live_manage_page.click_select_date()
        self.live_manage_page.click_select_live_start_time()
        self.live_manage_page.click_select_live_end_time()
        self.live_manage_page.click_next_btn()
        self.live_manage_page.click_add_user_btn()
        self.live_manage_page.click_select_all()
        self.live_manage_page.click_determine_btn4()
        self.live_manage_page.click_publish_btn()

    @pytest.mark.run(order=76)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_add_custom_live(self):
        self.live_manage_page.refresh_page()
        self.live_manage_page.click_add_live_btn()
        self.live_manage_page.click_custom_live_btn()
        self.live_manage_page.input_live_name("自定义直播")
        self.live_manage_page.click_train_sort_input1()
        self.live_manage_page.click_select_train_sort1()
        self.live_manage_page.click_blank_area1()
        self.live_manage_page.input_credit("4")
        self.live_manage_page.input_class_hour("3")
        self.live_manage_page.click_lecturer_input1()
        self.live_manage_page.click_select_lecturer1()
        self.live_manage_page.click_determine_btn6()
        self.live_manage_page.input_section("小节1")
        self.live_manage_page.click_live_date_input1()
        self.live_manage_page.click_select_live_date()
        self.live_manage_page.click_select_live_start_time1()
        self.live_manage_page.click_select_live_end_time1()
        self.live_manage_page.click_next_btn1()
        self.live_manage_page.click_add_user_btn1()
        self.live_manage_page.click_select_all1()
        self.live_manage_page.click_determine_btn8()
        self.live_manage_page.click_publish_btn1()




