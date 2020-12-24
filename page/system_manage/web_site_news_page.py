from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 网站新闻公告页面
class WebSiteNewsPage(BaseAction):

    # 系统管理按钮
    system_manage_btn = By.XPATH, "/html/body/div/div/div[3]/div[2]/ul/li[6]/span"

    # 名称搜索框
    name_search = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[1]/main/div/div/div[1]/input"

    # 状态筛选框
    status_filter = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[1]/main/div/div/div[2]/div/input"

    # 已发布
    published_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 未发布
    unpublished_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]/span"

    # 创建公告按钮
    create_announcement_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/button/span"

    # 公告标题输入框
    announcement_title_input = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/form/div[1]/div/div[1]/input"

    # 公告内容输入框
    announcement_content_input = By.CLASS_NAME, "w-e-text"

    # 保存并发布按钮
    save_and_publish_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/button[2]/span"

    # 标题按钮(点击进入编辑)
    title_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/span/span"

    # 置顶按钮
    topping_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/main/main/span[1]"

    # 删除按钮
    remove_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[5]/div/main/main/span[2]"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div[2]/div/div[3]/button[2]/span"

    # 点击系统管理
    def click_system_manage_btn(self):
        return self.click(self.system_manage_btn)

    # 输入标题名称进行搜索
    def input_name_search(self, content):
        return self.input(self.name_search, content)

    # 点击状态筛选框
    def click_status_filter(self):
        return self.click(self.status_filter)

    # 点击已发布
    def click_published_btn(self):
        return self.click(self.published_btn)

    # 点击未发布
    def click_unpublished_btn(self):
        return self.click(self.unpublished_btn)

    # 点击创建公告按钮
    def click_create_announcement_btn(self):
        return self.click(self.create_announcement_btn)

    # 输入公告标题
    def input_announcement_title_input(self, content):
        return self.input(self.announcement_title_input, content)

    # 输入公告内容
    def input_announcement_content_input(self, content):
        return self.input(self.announcement_content_input, content)

    # 点击保存并发布
    def click_save_and_publish_btn(self):
        return self.click(self.save_and_publish_btn)

    # 点击标题按钮
    def click_title_btn(self):
        return self.click(self.title_btn)

    # 清空标题内容
    def clear_announcement_title_input(self):
        return self.clear(self.announcement_title_input)

    # 点击置顶按钮
    def click_topping_btn(self):
        return self.click(self.topping_btn)

    # 点击删除按钮
    def click_remove_btn(self):
        return self.click(self.remove_btn)

    # 点击确定按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)


