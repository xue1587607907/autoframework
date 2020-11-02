import time
import pytest
from page.training_manage.exam_manage_page import ExamManagePage
from utils.driver_utils import DriverUtils


# 考试管理测试脚本
class TestExamManageCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.exam_manage = ExamManagePage(self.driver)

    def teardown(self):
        time.sleep(1)
        DriverUtils.quit_driver()

    @pytest.mark.run(order=70)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_query(self):
        self.exam_manage.click_train_manage_btn()
        self.exam_manage.click_exam_manage_btn()
        self.exam_manage.input_keyword_search("测试")
        self.exam_manage.click_keys_enter(self.exam_manage.keyword_search)
        self.exam_manage.refresh_page()
        self.exam_manage.click_status_filter()
        self.exam_manage.click_have_in_hand_btn()
        self.exam_manage.click_status_filter()
        self.exam_manage.click_no_started_btn()
        self.exam_manage.refresh_page()
        self.exam_manage.click_exam_organ_filter()
        self.exam_manage.click_direct_initiation()
        self.exam_manage.click_exam_organ_filter()
        self.exam_manage.click_project_initiation()

    @pytest.mark.run(order=71)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_add(self):
        self.exam_manage.click_new_btn()
        self.exam_manage.click_papers_used_input()
        self.exam_manage.click_select_paper()
        self.exam_manage.click_determine_btn()
        self.exam_manage.input_exam_name("测试")
        self.exam_manage.click_start_time_input()
        self.exam_manage.click_select_exam_period()
        self.exam_manage.click_determine1_btn()
        self.exam_manage.input_exam_duration(3)
        self.exam_manage.input_pass_score(5)
        self.exam_manage.input_credit(3)
        self.exam_manage.click_next_btn()
        self.exam_manage.click_add_user_btn()
        self.exam_manage.click_select_user()
        self.exam_manage.click_determine2_btn()
        self.exam_manage.click_save_and_publish()






