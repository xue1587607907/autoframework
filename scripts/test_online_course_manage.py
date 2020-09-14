import time
import pytest
from page.online_course_manage_page import OnlineCourseManagePage
from utils.driver_utils import DriverUtils


# 学习资源管理增删改查
class TestStudyResourcesCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.online_course = OnlineCourseManagePage(self.driver)

    # def teardown(self):
    #     time.sleep(2)
    #     DriverUtils.quit_driver()

    def teardown_class(self):
        time.sleep(2)
        DriverUtils.set_switch(False)
        DriverUtils.quit_driver()

    @pytest.mark.skipif(condition=True, reason=None)
    def test_course_query(self):
        self.online_course.click_online_course_manage_btn()
        self.online_course.click_course_name_search()


