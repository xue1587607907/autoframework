import pytest
from page.training_manage.exam_manage_page import ExamManagePage
from page.training_manage.post_learning_page import PostLearningPage
from utils.driver_utils import DriverUtils


# 岗位学习测试脚本
class TestPostLearningCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.exam_manage = ExamManagePage(self.driver)
        self.post_learn_page = PostLearningPage(self.driver)

    def teardown(self):
        DriverUtils.quit_driver()

    @pytest.mark.run(order=72)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_query(self):
        self.post_learn_page.refresh_page()
        self.exam_manage.click_train_manage_btn()
        self.post_learn_page.click_post_learning_btn()
        self.post_learn_page.input_post_name("java")
        self.post_learn_page.click_keys_enter(self.post_learn_page.post_name_search_input)
        self.post_learn_page.refresh_page()
        self.post_learn_page.click_status_filter()
        self.post_learn_page.select_published()
        self.post_learn_page.click_status_filter()
        self.post_learn_page.select_unpublished()

    @pytest.mark.run(order=73)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_add(self):
        self.post_learn_page.refresh_page()
        self.post_learn_page.click_new_post_learning_btn()
        self.post_learn_page.click_post_sort_input()
        self.post_learn_page.click_select_post_sort()
        self.post_learn_page.click_blank_area()
        self.post_learn_page.click_post_name_select()
        self.post_learn_page.click_select_post()
        self.post_learn_page.click_determine_btn()
        self.post_learn_page.click_add_phase_btn()
        self.post_learn_page.input_phase_name_input("基础")
        self.post_learn_page.click_determine1_btn()
        self.post_learn_page.click_video_course()
        self.post_learn_page.click_select_video()
        self.post_learn_page.click_determine2_btn()
        self.post_learn_page.click_interaction_course_btn()
        self.post_learn_page.click_select_interaction_course()
        self.post_learn_page.click_determine3_btn()
        self.post_learn_page.click_exam_btn()
        self.post_learn_page.click_user_paper_input()
        self.post_learn_page.click_select_paper()
        self.post_learn_page.click_determine4_btn()
        self.post_learn_page.input_exam_name("java入门考试")
        self.post_learn_page.input_exam_duration(60)
        self.post_learn_page.input_pass_score(4)
        self.post_learn_page.click_determine5_btn()
        self.post_learn_page.click_move_up_btn()
        self.post_learn_page.click_move_down_btn()
        self.post_learn_page.click_delete_btn()
        self.post_learn_page.click_determine6_btn()
        self.post_learn_page.click_train_set()
        self.post_learn_page.click_elective()
        self.post_learn_page.input_customs_clearance_task(1)
        self.post_learn_page.click_save_and_publish()



