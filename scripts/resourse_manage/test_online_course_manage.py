import time
import pytest
from page.resourse_manage.online_course_manage_page import OnlineCourseManagePage
from page.resourse_manage.resources_sort_page import ResourcesSortPage
from utils.driver_utils import DriverUtils


# 在线课程管理测试脚本
class TestOnlineCourseManageCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.online_course = OnlineCourseManagePage(self.driver)
        self.resources_sort_page = ResourcesSortPage(self.driver)

    def teardown(self):
        DriverUtils.quit_driver()

    @pytest.mark.run(order=33)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_course_query(self):
        self.online_course.refresh_page()
        self.resources_sort_page.click_resources_manage()
        self.online_course.click_online_course_manage_btn()
        self.online_course.click_course_name_search()
        self.online_course.input_courses_name("测试")
        self.online_course.click_keys_enter(self.online_course.course_name_search)
        self.online_course.refresh_page()
        self.online_course.click_status_filter()
        self.online_course.click_enable_btn()
        self.online_course.click_status_filter()
        self.online_course.click_disable_btn()

    @pytest.mark.run(order=34)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_add_course(self):
        self.online_course.refresh_page()
        self.online_course.click_new_courses()
        self.online_course.click_courses_name_input()
        self.online_course.input_courses_name1("测试{}".format(time.strftime("%H%M%S")))
        self.online_course.click_resources_sort_input()
        self.online_course.select_courses_sort()
        self.online_course.click_next_btn()
        self.online_course.click_add_section()
        self.online_course.click_section_name_input()
        self.online_course.input_section_name("小节{}".format(time.strftime("%H%M%S")))
        self.online_course.click_determine1_btn()
        self.online_course.click_add_learn_content_btn()
        self.online_course.click_content_type()
        self.online_course.click_video_btn()
        self.online_course.click_select_video_btn()
        self.online_course.click_check_video_btn()
        time.sleep(2)
        js = "window.scrollTo(0, 10000)"
        self.driver.execute_script(js)
        self.online_course.click_determine2_btn()
        self.online_course.click_determine3_btn()
        self.online_course.click_add_learn_content_btn()
        self.online_course.click_content_type()
        self.online_course.click_learn_data_btn()
        self.online_course.click_select_data_btn()
        self.online_course.click_check_data_btn()
        self.online_course.click_determine2_btn()
        self.online_course.click_determine3_btn()
        self.online_course.click_release_btn()

    @pytest.mark.run(order=35)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_modify_course_content(self):
        self.online_course.click_courses_name_btn()
        self.online_course.click_courses_content_btn()
        self.online_course.click_remove1_btn()
        self.online_course.click_determine4_btn()
        self.online_course.click_go_back_btn()

    @pytest.mark.run(order=36)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_more(self):
        self.online_course.refresh_page()
        self.online_course.click_disable1_btn()
        self.online_course.click_determine5_btn()
        self.online_course.click_remove2_btn()
        self.online_course.click_determine5_btn()




