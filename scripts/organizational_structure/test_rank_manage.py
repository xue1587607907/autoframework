import random
import pytest
from page.organizational_structure.rank_manage import RankManagePage
from utils.driver_utils import DriverUtils


# 职级管理测试脚本
class TestRankManageCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.rank_manage_page = RankManagePage(self.driver)

    def teardown(self):
        DriverUtils.quit_driver()

    # @pytest.mark.run(order=9.2)
    # # @pytest.mark.skipif(condition=True, reason=None)
    # def test_add_rank(self):
    #     self.rank_manage_page.refresh_page()
    #     self.rank_manage_page.click_rank_manage_btn()
    #     self.rank_manage_page.click_new_btn()
    #     self.rank_manage_page.input_rank_name("P{}".format(random.randint(11, 20)))
    #     self.rank_manage_page.click_determine_btn()

    @pytest.mark.run(order=11)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_move_and_remove(self):
        self.rank_manage_page.refresh_page()
        self.rank_manage_page.click_rank_manage_btn()
        self.rank_manage_page.click_move_up_btn()
        self.rank_manage_page.click_move_down_btn()
