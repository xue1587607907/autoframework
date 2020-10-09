import time
import pytest
from page.cooperative_organization_page import CooperativeOrganizationPage
from page.resources_sort_page import ResourcesSortPage
from utils.driver_utils import DriverUtils


# 合作机构管理测试脚本
class TestCooperativeOrganizationCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.resources_sort_page = ResourcesSortPage(self.driver)
        self.coo_organ_page = CooperativeOrganizationPage(self.driver)

    def teardown(self):
        time.sleep(2)
        DriverUtils.quit_driver()

    @pytest.mark.run(order=35.6)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_query(self):
        self.resources_sort_page.refresh_page()
        self.resources_sort_page.click_resources_manage()
        self.coo_organ_page.click_lecturer_and_tutor_btn()
        self.coo_organ_page.click_coo_organ_btn()
        self.coo_organ_page.input_name_search("嘉为")
        self.coo_organ_page.click_keys_enter(self.coo_organ_page.keyword_search)
        self.coo_organ_page.refresh_page()
        self.coo_organ_page.click_status_filter()
        self.coo_organ_page.click_enable_btn()
        self.coo_organ_page.click_status_filter()
        self.coo_organ_page.click_disable_btn()
        self.coo_organ_page.refresh_page()

    @pytest.mark.run(order=35.7)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_add(self):
        self.coo_organ_page.click_new_btn()
        self.coo_organ_page.input_mechanism_name("{}".format(time.strftime("%M%S")))
        self.coo_organ_page.click_determine_btn()

    @pytest.mark.run(order=35.8)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_remove_and_disable(self):
        self.coo_organ_page.click_disable1_btn()
        self.coo_organ_page.click_determine1_btn()
        self.coo_organ_page.click_remove_btn()
        self.coo_organ_page.click_determine1_btn()
