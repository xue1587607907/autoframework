import pytest
from page.system_manage.operation_log_page import OperationLogPage
from page.system_manage.web_site_news_page import WebSiteNewsPage
from utils.driver_utils import DriverUtils


# 操作日志测试脚本
class TestOperationLogCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.web_site_news_page = WebSiteNewsPage(self.driver)
        self.operation_log_page = OperationLogPage(self.driver)

    def teardown(self):
        DriverUtils.quit_driver()

    @pytest.mark.run(order=18.5)
    # @pytest.mark.skipif(condition=True, reason=None)
    def test_query(self):
        self.web_site_news_page.click_system_manage_btn()
        self.operation_log_page.click_operation_log_btn()
        self.operation_log_page.input_account_search("xue")
        self.operation_log_page.click_keys_enter(self.operation_log_page.account_search)
        self.operation_log_page.refresh_page()
        self.operation_log_page.click_operation_type_filter()
        self.operation_log_page.click_add_btn()
        self.operation_log_page.click_operation_type_filter()
        self.operation_log_page.click_edit_btn()
        self.operation_log_page.refresh_page()
        self.operation_log_page.click_module_filter()
        self.operation_log_page.click_system_manage_btn()
        self.operation_log_page.click_module_filter()
        self.operation_log_page.click_train_manage_btn()
        self.operation_log_page.click_function_filter()
        self.operation_log_page.click_train_sort_btn()
        self.operation_log_page.click_function_filter()
        self.operation_log_page.click_post_learn()
        self.operation_log_page.refresh_page()
        self.operation_log_page.click_time_filter()
        self.operation_log_page.click_last_week_btn()
        self.operation_log_page.click_time_filter()
        self.operation_log_page.click_last_month_btn()
