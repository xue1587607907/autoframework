import pytest
from page.system_manage.web_site_news_page import WebSiteNewsPage
from utils.driver_utils import DriverUtils


# 网站新闻管理测试脚本
class TestWebSiteNewsCRUD:

    def setup(self):
        self.driver = DriverUtils.get_driver()
        DriverUtils.set_switch(True)
        self.web_site_news_page = WebSiteNewsPage(self.driver)

    def teardown(self):
        DriverUtils.quit_driver()

    @pytest.mark.run(order=15)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_query(self):
        self.web_site_news_page.click_system_manage_btn()
        self.web_site_news_page.input_name_search("上海")
        self.web_site_news_page.click_keys_enter(self.web_site_news_page.name_search)
        self.web_site_news_page.refresh_page()
        self.web_site_news_page.click_status_filter()
        self.web_site_news_page.click_published_btn()
        self.web_site_news_page.click_status_filter()
        self.web_site_news_page.click_unpublished_btn()

    @pytest.mark.run(order=16)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_add(self):
        self.web_site_news_page.click_create_announcement_btn()
        self.web_site_news_page.input_announcement_title_input("测试公告")
        self.web_site_news_page.click(self.web_site_news_page.announcement_content_input)
        self.web_site_news_page.input_announcement_content_input("测试公告内容")
        self.web_site_news_page.click_save_and_publish_btn()

    @pytest.mark.run(order=17)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_modify(self):
        self.web_site_news_page.click_title_btn()
        self.web_site_news_page.clear_announcement_title_input()
        self.web_site_news_page.input_announcement_title_input("修改标题")
        self.web_site_news_page.click_save_and_publish_btn()

    @pytest.mark.run(order=18)
    @pytest.mark.skipif(condition=True, reason=None)
    def test_remove(self):
        self.web_site_news_page.click_topping_btn()
        self.web_site_news_page.click_remove_btn()
        self.web_site_news_page.click_determine_btn()



