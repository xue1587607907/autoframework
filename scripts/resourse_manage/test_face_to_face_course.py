import time
import pytest
from page.resourse_manage.face_to_face_course_page import FaceToFaceCoursePage
from page.resourse_manage.resources_sort_page import ResourcesSortPage
from utils.driver_utils import DriverUtils


# 面授课程管理测试脚本
class TestFaceToFaceCourseCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.face_page = FaceToFaceCoursePage(self.driver)
        self.resources_sort_page = ResourcesSortPage(self.driver)

    def teardown(self):
        time.sleep(1)
        DriverUtils.quit_driver()

    @pytest.mark.run(order=37)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_course_query(self):
        self.face_page.refresh_page()
        self.resources_sort_page.click_resources_manage()
        self.face_page.click_face_to_face_course_btn()
        self.face_page.click_course_name_search()
        self.face_page.input_courses_name("测试")
        self.face_page.click_keys_enter(self.face_page.course_name_search)
        self.face_page.refresh_page()
        self.face_page.click_time_filter()
        self.face_page.click_last_week_btn()
        self.face_page.click_time_filter()
        self.face_page.click_last_month_btn()
        self.face_page.refresh_page()
        self.face_page.click_status_filter()
        self.face_page.click_enable_btn()
        self.face_page.click_status_filter()
        self.face_page.click_disable_btn()

    @pytest.mark.run(order=38)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_add_course(self):
        self.face_page.click_new_courses()
        self.face_page.input_courses_name1("测试{}".format(time.strftime("%H%M%S")))
        self.face_page.click_resources_sort_input()
        self.face_page.select_courses_sort()
        self.face_page.input_credit(3)
        self.face_page.input_class_hours(2)
        self.face_page.click_save_and_publish()

    @pytest.mark.run(order=39)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_modify_course_content(self):
        self.face_page.click_course_name_btn()
        self.face_page.clear_courses_name_input()
        self.face_page.input_courses_name1("修改后{}".format(time.strftime("%H%M%S")))
        self.face_page.clear(self.face_page.credit_input)
        self.face_page.input_credit(4)
        self.face_page.clear(self.face_page.class_hours)
        self.face_page.input_class_hours(3)
        self.face_page.click_save_and_publish()

    @pytest.mark.run(order=40)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_more(self):
        self.face_page.refresh_page()
        self.face_page.click_disable1_btn()
        self.face_page.click_determine_btn()
        self.face_page.click_remove_btn()
        self.face_page.click_determine_btn()
        self.face_page.refresh_page()
        # self.face_page.click_page_right()
        # self.face_page.click_page_left()
        # self.face_page.click_page_num_filter()
        # self.face_page.click_first_btn()
