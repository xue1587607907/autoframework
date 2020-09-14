import time
import pytest
from page.study_resources_manage_page import StudyResourcesManagePage
from utils.driver_utils import DriverUtils


# 学习资源管理增删改查
class TestStudyResourcesCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.study = StudyResourcesManagePage(self.driver)
        # self.learning_center_page = LearningCenterPage(self.driver)
        # self.account_dm_page = AccountDM(self.driver)

    def teardown(self):
        time.sleep(2)
        DriverUtils.quit_driver()

    # def teardown_class(self):
    #     time.sleep(2)
    #     DriverUtils.set_switch(False)
    #     DriverUtils.quit_driver()

    @pytest.mark.run(order=11)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_video_library_query(self):
        self.study.refresh_page()
        # self.study.click_resources_manage()
        self.study.click_study_resources_manage()
        self.study.click_search()
        self.study.input_search_content("测试")
        self.study.click_keys_enter(self.study.resources_name_search)
        self.study.refresh_page()
        self.study.click_status_filter1()
        self.study.click_transcoding_successful()
        self.study.click_status_filter1()
        self.study.click_transcoding_fail()
        # self.study.refresh_page()

    @pytest.mark.run(order=12)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_modify_resources_info(self):
        self.study.refresh_page()
        self.study.click_edit_btn()
        # self.study.click_resources_sort_select()
        # self.study.select_third_sort()
        self.study.click_resources_sort_btn()
        self.study.select_all(self.study.edit_resources_name_input)
        self.study.click_key_backspace(self.study.edit_resources_name_input)
        self.study.input(self.study.edit_resources_name_input, "测试{}".format(time.strftime("%H%M%S")))
        self.study.click_determine_btn()

    @pytest.mark.run(order=13)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_remove_resources(self):
        self.study.click_remove_btn()
        self.study.click_determine1_btn()

    @pytest.mark.run(order=14)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_turn_the_page(self):
        self.study.refresh_page()
        self.study.click_page_right()
        self.study.click_page_left()
        self.study.click_num_btn_page()
        self.study.click_page_size()
        self.study.move_mouse(self.study.turn_the_page_area)
        self.study.click_third_btn()

    @pytest.mark.run(order=15)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_database_query(self):
        self.study.refresh_page()
        self.study.click_database_btn()
        self.study.click_type_filter()
        self.study.click_first_type_btn()
        self.study.click_type_filter()
        self.study.click_second_type_btn()
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

    @pytest.mark.run(order=16)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_more_operation(self):
        self.study.refresh_page()
        self.study.click_database_btn()
        self.study.move_mouse(self.study.more_btn)
        self.study.click_more_enable()
        self.study.refresh_page()
        self.study.click_database_btn()
        self.study.click_more_btn()
        self.study.click_download_btn()
        # time.sleep(1)
        self.study.click_more_btn()
        self.study.click_related_courses()
        self.study.select_related_courses()
        self.study.click_related_courses_determine()
        self.study.click_more_btn()
        self.study.click_more_remove_btn()
        self.study.click_determine2_btn()








