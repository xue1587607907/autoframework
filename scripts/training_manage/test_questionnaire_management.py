import time
import pytest
from page.training_manage.questionnaire_management_page import QuestionnaireManagementPage
from page.training_manage.train_sort_page import TrainSortPage
from utils.driver_utils import DriverUtils


# 问卷管理测试脚本
class TestTrainSortCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.train_sort_page = TrainSortPage(self.driver)
        self.questionnaire_management_page = QuestionnaireManagementPage(self.driver)

    # def teardown(self):
    #     DriverUtils.quit_driver()

    def teardown_class(self):
        DriverUtils.set_switch(False)
        time.sleep(2)
        DriverUtils.quit_driver()

    @pytest.mark.run(order=77)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_query(self):
        self.questionnaire_management_page.refresh_page()
        self.train_sort_page.click_train_manage_btn()
        self.questionnaire_management_page.click_questionnaire_management_btn()
        self.questionnaire_management_page.input_questionnaire_name("问卷")
        self.questionnaire_management_page.click_keys_enter(self.questionnaire_management_page.keyword_search)
        self.questionnaire_management_page.refresh_page()
        self.questionnaire_management_page.click_organizational_form_filter()
        self.questionnaire_management_page.click_select_learn_project()
        self.questionnaire_management_page.click_organizational_form_filter()
        self.questionnaire_management_page.click_select_directly_by()
        self.questionnaire_management_page.refresh_page()
        self.questionnaire_management_page.click_status_filter()
        self.questionnaire_management_page.click_select_unpublished()
        self.questionnaire_management_page.click_status_filter()
        self.questionnaire_management_page.click_select_under_way()
        self.questionnaire_management_page.refresh_page()

    @pytest.mark.run(order=78)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_add_copy_template(self):
        self.questionnaire_management_page.refresh_page()
        self.questionnaire_management_page.click_add_questionnaire_btn()
        self.questionnaire_management_page.click_copy_template_btn()
        self.questionnaire_management_page.click_questionnaire_template_select()
        self.questionnaire_management_page.click_select_template()
        self.questionnaire_management_page.click_determine_btn()
        self.questionnaire_management_page.input_questionnaire_name_input("测试问卷{}".format(time.strftime("%M%S")))
        self.questionnaire_management_page.input_questionnaire_declare("问卷说明的内容")
        self.questionnaire_management_page.click_start_time_select()
        self.questionnaire_management_page.click_end_time_select()
        self.questionnaire_management_page.input_upper_bound("2")
        self.questionnaire_management_page.click_next_btn()
        self.questionnaire_management_page.click_next_btn1()
        self.questionnaire_management_page.click_checkbox()
        self.questionnaire_management_page.click_add_user_btn()
        self.questionnaire_management_page.input_name_search("xue")
        self.questionnaire_management_page.click_keys_enter(self.questionnaire_management_page.name_input)
        self.questionnaire_management_page.click_select_all()
        self.questionnaire_management_page.click_determine_btn1()
        self.questionnaire_management_page.click_publish_btn()

    @pytest.mark.run(order=79)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_add_directly_by(self):
        self.questionnaire_management_page.refresh_page()
        self.questionnaire_management_page.click_add_questionnaire_btn()
        self.questionnaire_management_page.click_new_direct()
        self.questionnaire_management_page.input_questionnaire_name1("直接发起的问卷")
        self.questionnaire_management_page.input_questionnaire_declare1("问卷说明的内容")
        self.questionnaire_management_page.click_start_time_input()
        self.questionnaire_management_page.click_end_time_input()
        self.questionnaire_management_page.input_upper(2)
        self.questionnaire_management_page.click_next_btn2()
        self.questionnaire_management_page.click_single_choice_btn()
        self.questionnaire_management_page.input_subject("单选题题目")
        self.questionnaire_management_page.input_option_input("选项答案")
        self.questionnaire_management_page.click_determine_btn2()
        self.questionnaire_management_page.click_next_btn3()
        self.questionnaire_management_page.click_publish_btn1()

    def test_a(self):
        pass
