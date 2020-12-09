import time
import pytest
from page.resourse_manage.study_resources_manage_page import StudyResourcesManagePage
from utils.driver_utils import DriverUtils


# 学习资源管理增删改查
class TestStudyResourcesCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.study = StudyResourcesManagePage(self.driver)

    def teardown(self):
        DriverUtils.quit_driver()

    @pytest.mark.run(order=27)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_video_library_query(self):
        self.study.refresh_page()
        self.study.click_resources_manage()
        self.study.click_study_resources_manage()
        self.study.click_search()
        self.study.input_search_content("测试")
        self.study.click_keys_enter(self.study.resources_name_search)
        self.study.refresh_page()
        self.study.click_status_filter1()
        self.study.click_transcoding_successful()
        self.study.click_status_filter1()
        self.study.click_transcoding_fail()

    @pytest.mark.run(order=28)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_modify_resources_info(self):
        self.study.refresh_page()
        self.study.click_edit_btn()
        self.study.click_resources_sort_btn()
        self.study.select_all(self.study.edit_resources_name_input)
        self.study.click_key_backspace(self.study.edit_resources_name_input)
        self.study.input(self.study.edit_resources_name_input, "测试{}".format(time.strftime("%H%M%S")))
        self.study.click_determine_btn()

    @pytest.mark.run(order=29)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_remove_resources(self):
        self.study.click_remove_btn()
        self.study.click_determine1_btn()

    @pytest.mark.run(order=30)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_database_query(self):
        self.study.refresh_page()
        self.study.click_database_btn()
        self.study.click_type_filter()
        self.study.click_first_type_btn()
        self.study.refresh_page()
        self.study.click_database_btn()
        self.study.click_time_filter()
        self.study.click_first_time_filter()
        self.study.click_time_filter()
        self.study.click_second_time_filter()
        self.study.refresh_page()
        self.study.click_database_btn()
        self.study.click_status_filter2()
        self.study.click_enable_btn()
        self.study.click_status_filter2()
        self.study.click_disable_btn()

    @pytest.mark.run(order=31)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_more_operation(self):
        self.study.refresh_page()
        self.study.click_database_btn()
        self.study.click_related_courses()
        self.study.select_related_courses()
        self.study.click_related_courses_determine()
        self.study.move_mouse(self.study.more_btn)
        self.study.click_more_enable()
        self.study.refresh_page()
        self.study.click_database_btn()
        self.study.click_download_btn()
        self.study.click_more_btn()
        self.study.click_more_remove_btn()
        self.study.click_determine2_btn()




