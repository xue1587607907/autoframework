import time
import pytest
from page.resourse_manage.questionnaire_template_page import QuestionnaireTemplatePage
from page.resourse_manage.resources_sort_page import ResourcesSortPage
from utils.driver_utils import DriverUtils


# 问卷模板增删改查测试脚本
class TestResourcesSortCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.questionnaire_template_page = QuestionnaireTemplatePage(self.driver)
        self.resources_sort_page = ResourcesSortPage(self.driver)

    def teardown(self):
        DriverUtils.quit_driver()

    @pytest.mark.run(order=59.2)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_query(self):
        self.questionnaire_template_page.refresh_page()
        self.resources_sort_page.click_resources_manage()
        self.questionnaire_template_page.click_questionnaire_template_btn()
        self.questionnaire_template_page.input_keyword("测试")
        self.questionnaire_template_page.click_keys_enter(self.questionnaire_template_page.keyword_search)
        self.questionnaire_template_page.refresh_page()
        self.questionnaire_template_page.click_time_filter_box()
        self.questionnaire_template_page.click_last_week_btn()
        self.questionnaire_template_page.click_time_filter_box()
        self.questionnaire_template_page.click_last_month_btn()
        self.questionnaire_template_page.refresh_page()
        self.questionnaire_template_page.click_status_filter()
        self.questionnaire_template_page.click_enable_btn()
        self.questionnaire_template_page.click_status_filter()
        self.questionnaire_template_page.click_disable_btn()

    @pytest.mark.run(order=59.4)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_add(self):
        self.questionnaire_template_page.click_add_btn()
        self.questionnaire_template_page.input_template_name("问卷模板{}".format(time.strftime("%M%S")))
        self.questionnaire_template_page.click_determine_btn()
        self.questionnaire_template_page.click_determine_btn1()
        self.questionnaire_template_page.click_single_choice_btn()
        self.questionnaire_template_page.input_topic("单选题题目")
        self.questionnaire_template_page.input_option_input("111")
        self.questionnaire_template_page.click_add_option_btn()
        self.questionnaire_template_page.input_option_input2("222")
        self.questionnaire_template_page.click_determine_btn2()

    @pytest.mark.run(order=59.6)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_more(self):
        self.questionnaire_template_page.click_questionnaire_template_btn()
        self.questionnaire_template_page.click_disable_btn1()
        self.questionnaire_template_page.click_determine_btn3()
        self.questionnaire_template_page.click_remove_btn()
        self.questionnaire_template_page.click_determine_btn3()

