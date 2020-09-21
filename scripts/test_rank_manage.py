import time
import pytest
from page.rank_manage import RankManagePage
from utils.driver_utils import DriverUtils


# 岗位管理测试脚本
class TestPostManageCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.rank_manage_page = RankManagePage(self.driver)
        # self.train_sort_page = TrainSortPage(self.driver)

    # def teardown(self):
    #     time.sleep(2)
    #     DriverUtils.quit_driver()

    def teardown_class(self):
        time.sleep(2)
        DriverUtils.set_switch(False)
        DriverUtils.quit_driver()

    @pytest.mark.run(order=43)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_add_rank(self):
        self.rank_manage_page.click_rank_manage_btn()
        self.rank_manage_page.click_new_btn()
        self.rank_manage_page.input_rank_name("P{}".format(time.strftime("%M%S")))
        self.rank_manage_page.click_determine_btn()

    @pytest.mark.run(order=44)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_modify(self):
        self.rank_manage_page.click_rank_name_btn()
        self.rank_manage_page.clear_rank_name_input()
        self.rank_manage_page.input_rank_name("修改后{}".format(time.strftime("%M%S")))
        self.rank_manage_page.click_determine_btn()
        self.rank_manage_page.click_edit_btn()
        self.rank_manage_page.click_user_radio()
        self.rank_manage_page.click_adjust_rank_btn()
        self.rank_manage_page.click_new_rank()
        self.rank_manage_page.click_select_rank()
        self.rank_manage_page.click_determine1_btn()

    @pytest.mark.run(order=45)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_move_and_remove(self):
        self.rank_manage_page.click_rank_manage_btn()
        # self.rank_manage_page.refresh_page()
        self.rank_manage_page.click_move_up_btn()
        self.rank_manage_page.click_move_down_btn()
        # self.rank_manage_page.back_off()
        self.rank_manage_page.click_remove_btn()
        self.rank_manage_page.click_determine2_btn()
