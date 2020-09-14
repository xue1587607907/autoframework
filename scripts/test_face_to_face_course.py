import time
import pytest
from page.face_to_face_course_page import FaceToFaceCoursePage
from page.resources_sort_page import ResourcesSortPage
from utils.driver_utils import DriverUtils


# 面授课程管理测试脚本
class TestFaceToFaceCourseCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.face_page = FaceToFaceCoursePage(self.driver)
        self.resources_sort_page = ResourcesSortPage(self.driver)

    # def teardown(self):
    #     time.sleep(2)
    #     DriverUtils.quit_driver()

    def teardown_class(self):
        time.sleep(2)
        DriverUtils.set_switch(False)
        DriverUtils.quit_driver()

    @pytest.mark.run(order=21)
    @pytest.mark.skipif(condition=True, reason=None)
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
