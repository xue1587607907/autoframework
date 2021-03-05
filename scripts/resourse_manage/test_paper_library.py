import time
import pytest
from page.resourse_manage.paper_library_page import PaperLibraryPage
from page.resourse_manage.question_bank_page import QuestionBankPage
from page.resourse_manage.resources_sort_page import ResourcesSortPage
from utils.driver_utils import DriverUtils


# 试卷库测试脚本
class TestPaperLibraryCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.resources_sort_page = ResourcesSortPage(self.driver)
        self.question_bank_page = QuestionBankPage(self.driver)
        self.paper_page = PaperLibraryPage(self.driver)

    def teardown(self):
        DriverUtils.quit_driver()

    @pytest.mark.run(order=46)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_question_bank_query(self):
        self.question_bank_page.refresh_page()
        self.resources_sort_page.click_resources_manage()
        self.question_bank_page.click_papers_and_questions_btn()
        self.paper_page.click_paper_btn()
        self.question_bank_page.click_course_name_search()
        self.question_bank_page.input_courses_name("测试")
        self.question_bank_page.click_keys_enter(self.question_bank_page.course_name_search)
        self.question_bank_page.refresh_page()
        self.question_bank_page.click_time_filter()
        self.question_bank_page.click_last_week_btn()
        self.question_bank_page.click_time_filter()
        self.question_bank_page.click_last_month_btn()
        self.question_bank_page.refresh_page()
        self.paper_page.click_status_filter()
        self.question_bank_page.click_enable_btn()
        self.paper_page.click_status_filter()
        self.question_bank_page.click_disable_btn()

    @pytest.mark.run(order=48)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_add_random_paper(self):
        self.paper_page.refresh_page()
        self.paper_page.click_paper_btn()
        self.paper_page.click_new_btn()
        self.paper_page.click_random_papers_btn()
        self.paper_page.click_question_bank_select_btn1()
        self.paper_page.click_select_all1()
        self.paper_page.click_determine2_btn()
        self.paper_page.input_select_question(3)
        self.paper_page.input_score1(4)
        self.paper_page.input_random_paper("随机试卷{}".format(time.strftime("%H%M%S")))
        self.paper_page.click_determine3_btn()

    @pytest.mark.run(order=50)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_remove_paper(self):
        self.paper_page.refresh_page()
        self.paper_page.click_disable1_btn()
        self.paper_page.click_determine4_btn()
        self.paper_page.click_remove1_btn()
        self.paper_page.click_determine5_btn()








