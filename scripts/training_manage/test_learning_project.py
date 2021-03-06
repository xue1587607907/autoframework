import time
import pytest
from page.training_manage.learning_project_page import LearningProjectPage
from utils.driver_utils import DriverUtils


# 学习项目测试脚本
class TestLearningProjectCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.learn_pro_page = LearningProjectPage(self.driver)

    def teardown(self):
        DriverUtils.quit_driver()

    @pytest.mark.run(order=67)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_query(self):
        self.learn_pro_page.refresh_page()
        self.learn_pro_page.click_train_manage_btn()
        self.learn_pro_page.click_train_organization_btn()
        self.learn_pro_page.click_learn_project_btn()
        self.learn_pro_page.input_keyword_search("培训")
        self.learn_pro_page.click_keys_enter(self.learn_pro_page.keyword_search)
        self.learn_pro_page.refresh_page()
        self.learn_pro_page.click_time_filter()
        self.learn_pro_page.click_last_week_btn()
        self.learn_pro_page.click_time_filter()
        self.learn_pro_page.click_last_month_btn()
        self.learn_pro_page.refresh_page()
        self.learn_pro_page.click_status_filter()
        self.learn_pro_page.click_have_in_hand_btn()
        self.learn_pro_page.click_status_filter()
        self.learn_pro_page.click_finished_btn()

    @pytest.mark.run(order=68)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_add_project(self):
        self.learn_pro_page.click_new_btn()
        self.learn_pro_page.input_project_name("测试项目{}".format(time.strftime("%M%S")))
        self.learn_pro_page.click_project_sort_input()
        self.learn_pro_page.select_third_sort()
        self.learn_pro_page.click_start_time_input()
        self.learn_pro_page.click_select_start_time()
        self.learn_pro_page.click_end_time_input()
        self.learn_pro_page.click_select_end_time()
        self.learn_pro_page.click_next_btn()
        self.learn_pro_page.click_new_stage_btn()
        self.learn_pro_page.input_stage_name("阶段一")
        self.learn_pro_page.click_determine_btn()
        self.learn_pro_page.click_face_to_face_btn()
        self.learn_pro_page.click_course_name()
        self.learn_pro_page.click_select_course()
        self.learn_pro_page.click_determine1_btn()
        self.learn_pro_page.input_content_name_input("小节1")
        self.learn_pro_page.click_start_time_input1()
        self.learn_pro_page.click_select_start_time1()
        self.learn_pro_page.click_determine11_btn()
        self.learn_pro_page.click_end_time_input1()
        self.learn_pro_page.click_select_end_time1()
        self.learn_pro_page.click_determine11_btn()
        self.learn_pro_page.click_determine2_btn()
        # 添加直播任务
        self.learn_pro_page.click_live_course_btn()
        self.learn_pro_page.click_live_name_input()
        self.learn_pro_page.click_select_interaction_course()
        self.learn_pro_page.click_determine_btn15()
        self.learn_pro_page.click_train_sort_input()
        self.learn_pro_page.click_select_train_sort()
        self.learn_pro_page.click_blank_area1()
        self.learn_pro_page.click_lecturer_input()
        self.learn_pro_page.click_select_lecturer()
        self.learn_pro_page.click_determine_btn12()
        self.learn_pro_page.input_section_name("小节1")
        self.learn_pro_page.click_live_date_input()
        self.learn_pro_page.click_select_date()
        self.learn_pro_page.click_live_time_input()
        self.learn_pro_page.click_select_live_time()
        self.learn_pro_page.click_determine_btn13()
        self.learn_pro_page.click_determine_btn14()
        # 添加视频课程任务
        self.learn_pro_page.click_video_btn()
        self.learn_pro_page.click_course_name1()
        self.learn_pro_page.click_select_course1()
        self.learn_pro_page.click_determine3_btn()
        self.learn_pro_page.click_determine4_btn()
        # 添加考试任务
        self.learn_pro_page.click_add_test_btn()
        self.learn_pro_page.click_papers_used_input()
        self.learn_pro_page.click_select_paper()
        self.learn_pro_page.click_determine5_btn()
        self.learn_pro_page.input_exam_name("考试1")
        self.learn_pro_page.click_radio_btn()
        self.learn_pro_page.click_start_time_input2()
        self.learn_pro_page.select_start_and_end_time()
        self.learn_pro_page.click_determine6_btn()
        self.learn_pro_page.input_exam_duration("4")
        self.learn_pro_page.input_pass_score_input(5)
        self.learn_pro_page.input_credit_input(4)
        self.learn_pro_page.click_determine7_btn()
        self.learn_pro_page.click_move_up_down()
        self.learn_pro_page.click_remove_btn()
        self.learn_pro_page.click_determine8_btn()
        self.learn_pro_page.click_research_settings()
        self.learn_pro_page.click_select_elective()
        self.learn_pro_page.click_next1_btn()
        self.learn_pro_page.click_add_user_btn()
        self.learn_pro_page.click_select_user()
        self.learn_pro_page.click_determine9_btn()
        self.learn_pro_page.click_next2_btn()
        self.learn_pro_page.input_elective(0)
        self.learn_pro_page.click_save_and_publish()

    @pytest.mark.run(order=69)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_modify(self):
        self.learn_pro_page.refresh_page()
        self.learn_pro_page.click_project_name_btn()
        self.learn_pro_page.clear_project_name_input()
        self.learn_pro_page.input_project_name("修改后{}".format(time.strftime("%M%S")))
        self.learn_pro_page.click_determine()




