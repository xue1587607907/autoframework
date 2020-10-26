import time
import pytest
from page.training_manage.learning_project_page import LearningProjectPage
from page.training_manage.train_needs_page import TrainNeedsPage
from utils.driver_utils import DriverUtils


# 培训需求测试脚本
class TestTrainNeedsCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.learn_pro_page = LearningProjectPage(self.driver)
        self.train_needs_page = TrainNeedsPage(self.driver)

    # def teardown(self):
    #     time.sleep(2)
    #     DriverUtils.quit_driver()

    def teardown_class(self):
        time.sleep(2)
        DriverUtils.set_switch(False)
        DriverUtils.quit_driver()

    @pytest.mark.run(order=63)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_query(self):
        self.learn_pro_page.click_train_manage_btn()
        self.train_needs_page.click_train_needs_btn()
        self.train_needs_page.input_needs_name_search("123")
        self.train_needs_page.click_keys_enter(self.train_needs_page.needs_name_search)
        self.train_needs_page.refresh_page()
        self.train_needs_page.click_status_filter()
        self.train_needs_page.click_no_finished()
        self.train_needs_page.click_status_filter()
        self.train_needs_page.click_finished()
        self.train_needs_page.refresh_page()
        self.train_needs_page.click_update_time_filter()
        self.train_needs_page.click_last_week()
        self.train_needs_page.click_update_time_filter()
        self.train_needs_page.click_last_month()

    @pytest.mark.run(order=64)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_add(self):
        self.train_needs_page.click_new_needs_btn()
        self.train_needs_page.input_needs_name("企业文化培训")
        self.train_needs_page.click_determine_btn()
        self.train_needs_page.click_need_name_btn()
        self.train_needs_page.clear_needs_name_input()
        self.train_needs_page.input_needs_name("修改后的培训需求")
        self.train_needs_page.click_determine_btn()
        self.train_needs_page.click_set_to_completed()
        self.train_needs_page.click_remove_btn()
        self.train_needs_page.click_determine1_btn()

    def test_a(self):
        pass
