import time
import pytest
from page.paper_library_page import PaperLibraryPage
from page.question_bank_page import QuestionBankPage
from page.resources_sort_page import ResourcesSortPage
from utils.driver_utils import DriverUtils


# 试题库测试脚本
class TestQuestionBankCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.resources_sort_page = ResourcesSortPage(self.driver)
        self.question_bank_page = QuestionBankPage(self.driver)
        self.paper_page = PaperLibraryPage(self.driver)

    def teardown(self):
        time.sleep(2)
        DriverUtils.quit_driver()

    @pytest.mark.run(order=30)
    @pytest.mark.skipif(condition=True, reason=None)
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

    @pytest.mark.run(order=32)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_add_fixed_paper(self):
        self.paper_page.click_new_btn()
        self.paper_page.click_fixed_papers_btn()
        self.paper_page.input_paper_name("测试{}".format(time.strftime("%H%M%S")))
        self.paper_page.click_question_bank_select_btn()
        self.paper_page.input_question_bank("测试新建完题库后，立马改题库")
        self.paper_page.click_search_btn()
        # self.paper_page.click_keys_enter(self.paper_page.search_question_bank_input)
        self.paper_page.select_question_bank1_btn()
        self.paper_page.click_select_all()
        self.paper_page.click_determine_btn()
        self.paper_page.click_remove_btn()
        self.paper_page.click_determine1_btn()
        self.paper_page.input_score(5)
        self.paper_page.click_save_btn()

    @pytest.mark.run(order=31)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_add_random_paper(self):
        self.paper_page.click_new_btn()
        self.paper_page.click_random_papers_btn()
        self.paper_page.click_question_bank_select_btn()
        self.paper_page.click_select_all1()
        self.paper_page.click_determine2_btn()
        self.paper_page.input_select_question(3)
        self.paper_page.input_score1(4)
        self.paper_page.input_random_paper("测试{}".format(time.strftime("%H%M%S")))
        self.paper_page.click_determine3_btn()

    @pytest.mark.run(order=32)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_modify_paper_content(self):
        self.paper_page.click_more_btn()
        self.paper_page.move_mouse(self.paper_page.more_btn)
        self.paper_page.click_edit_btn()
        self.paper_page.clear(self.paper_page.random_paper_input)
        self.paper_page.input_random_paper("修改后{}".format(time.strftime("%H%M%S")))
        self.paper_page.click_determine3_btn()
        self.paper_page.refresh_page()
        self.paper_page.click_more_btn()
        self.paper_page.click_disable1_btn()
        self.paper_page.click_determine4_btn()

    @pytest.mark.run(order=33)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_remove_paper(self):
        self.paper_page.click_radio()
        self.paper_page.click_remove1_btn()
        self.paper_page.click_determine5_btn()

    @pytest.mark.run(order=34)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_turn_the_page(self):
        self.question_bank_page.refresh_page()
        self.question_bank_page.click_page_right()
        self.question_bank_page.click_page_left()
        self.question_bank_page.click_page_num_filter()
        self.question_bank_page.click_first_btn()






