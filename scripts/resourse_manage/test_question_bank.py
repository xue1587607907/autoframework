import time
import pytest
from page.resourse_manage.question_bank_page import QuestionBankPage
from page.resourse_manage.resources_sort_page import ResourcesSortPage
from utils.driver_utils import DriverUtils


# 试题库测试脚本
class TestQuestionBankCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.resources_sort_page = ResourcesSortPage(self.driver)
        self.question_bank_page = QuestionBankPage(self.driver)

    def teardown(self):
        DriverUtils.quit_driver()

    @pytest.mark.run(order=41)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_question_bank_query(self):
        self.question_bank_page.refresh_page()
        self.resources_sort_page.click_resources_manage()
        self.question_bank_page.click_papers_and_questions_btn()
        self.question_bank_page.click_question_bank_btn()
        self.question_bank_page.click_course_name_search()
        self.question_bank_page.input_courses_name("测试")
        self.question_bank_page.click_keys_enter(self.question_bank_page.course_name_search)
        self.question_bank_page.refresh_page()
        self.question_bank_page.click_time_filter()
        self.question_bank_page.click_last_week_btn()
        self.question_bank_page.click_time_filter()
        self.question_bank_page.click_last_month_btn()
        self.question_bank_page.refresh_page()
        self.question_bank_page.click_status_filter()
        self.question_bank_page.click_enable_btn()
        self.question_bank_page.click_status_filter()
        self.question_bank_page.click_disable_btn()

    @pytest.mark.run(order=42)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_add_question_bank(self):
        self.question_bank_page.refresh_page()
        self.question_bank_page.click_new_btn()
        self.question_bank_page.input_question_bank_name("测试题库")
        self.question_bank_page.click_sort_input()
        self.question_bank_page.select_third_sort()
        self.question_bank_page.click_determine_btn()
        self.question_bank_page.click_determine5_btn()
        self.question_bank_page.switch_window()
        self.question_bank_page.click_single_choice_questions_btn()
        self.question_bank_page.input_subject(123)
        self.question_bank_page.input_option_a(123)
        self.question_bank_page.input_option_b(321)
        self.question_bank_page.select_answer()
        self.question_bank_page.click_determine1_btn()
        self.question_bank_page.click_determine2_btn()

    @pytest.mark.run(order=44)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_disable_and_remove(self):
        self.question_bank_page.refresh_page()
        self.question_bank_page.click_disable1_btn()
        self.question_bank_page.click_determine3_btn()
        self.question_bank_page.click_remove_btn()
        self.question_bank_page.click_determine3_btn()




