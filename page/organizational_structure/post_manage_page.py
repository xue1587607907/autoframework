from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 岗位管理页面
class PostManagePage(BaseAction):

    # 岗位管理按钮
    post_manage_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[2]"

    # 第一个搜索框
    first_search = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[1]/div[1]/div[1]/input"

    # 状态筛选框
    second_search = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[1]/div[1]/div[2]/div/input"

    # 待发布
    no_publish_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 已发布
    publish_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]/span"

    # 新建岗位按钮
    new_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/button/span"

    # 所属分类输入框
    classification_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/div/div/div[2]/form/div[1]/div/div/div[1]/input"

    # 选择分类
    d1 = By.XPATH, "/html/body/div[3]/div[1]/div[1]/div[1]/ul/li[1]/label/span[1]/span"

    # 空白区域
    blank_area = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/div/div/div[1]"

    # 岗位名称输入框
    post_name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/div/div/div[2]/form/div[2]/div/div/input"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/div/div/div[3]/div/button[1]/span"

    # 岗位名称按钮(点击进入编辑)
    post_name1_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[2]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/span/span"

    # 删除按钮
    remove_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[2]/div/div/div[5]/div[2]/table/tbody/tr[1]/td[6]/div/main/div/span[3]"

    # 弹窗的确定按钮
    determine1_btn = By.XPATH, "/html/body/div[3]/div/div[3]/button[2]/span"

    # # 管理用户按钮
    # manage_user_btn1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[2]/div/div/div[5]/div[2]/table/tbody/tr[3]/td[5]/div/main/main/span[1]"
    #
    # # 用户单选框
    # user_radio = By.CSS_SELECTOR, ".el-table__fixed-body-wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(1) > span:nth-child(1)"
    #
    # # 调整岗位按钮
    # adjust_post_btn = By.CSS_SELECTOR, ".btn-box > button:nth-child(1) > span:nth-child(1)"
    #
    # # 新岗位选择框
    # new_post_select = By.CSS_SELECTOR, "div.el-cascader:nth-child(1) > div:nth-child(1) > input:nth-child(1)"
    #
    # # 选择岗位分类
    # select_post = By.XPATH, "/html/body/div[3]/div[1]/div[1]/div[1]/ul/li/label/span[1]/span"
    #
    # # 点击空白区域
    # blank_area1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/div/div/div[1]"
    #
    # # 选择岗位输入框
    # select_post_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/div/div/div[2]/form/div[2]/div/div/div[2]/div/div/div/input"
    #
    # # 选择具体岗位
    # select_specific_post = By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li[1]/span"
    #
    # # 点击确定按钮
    # determine2_btn = By.CSS_SELECTOR, ".dialog-footer > button:nth-child(1) > span:nth-child(1)"

    # 点击岗位管理按钮
    def click_post_manage_btn(self):
        return self.click(self.post_manage_btn)

    # 通过第一个搜索框进行搜索
    def input_first_search(self, content):
        return self.input(self.first_search, content)

    # 点击状态筛选框
    def click_second_search(self):
        return self.click(self.second_search)

    # 点击待发布
    def click_no_publish_btn(self):
        return self.click(self.no_publish_btn)

    # 点击已发布
    def click_publish_btn(self):
        return self.click(self.publish_btn)

    # 点击新建按钮
    def click_new_btn(self):
        return self.click(self.new_btn)

    # 点击所属分类
    def click_classification_select(self):
        return self.click(self.classification_input)

    # 选择岗位分类
    def select_third_sort(self):
        self.click(self.d1)
        self.click(self.blank_area)

    # 输入岗位名称
    def input_post_name(self, content):
        return self.input(self.post_name_input, content)

    # 点击确定按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 岗位名称按钮(点击进入编辑)
    def click_post_name1_btn(self):
        return self.click(self.post_name1_btn)

    # 点击删除按钮
    def click_remove_btn(self):
        return self.click(self.remove_btn)

    # 点击确定按钮
    def click_determine1_btn(self):
        return self.click(self.determine1_btn)

    # # 点击管理用户按钮
    # def click_manage_user_btn1(self):
    #     return self.click(self.manage_user_btn1)
    #
    # # 选择用户单选框(进行调整岗位)
    # def click_select_user_radio(self):
    #     return self.click(self.user_radio)
    #
    # # 点击调整岗位按钮
    # def click_adjust_post_btn(self):
    #     return self.click(self.adjust_post_btn)
    #
    # # 点击新岗位输入框
    # def click_new_post_select(self):
    #     return self.click(self.new_post_select)
    #
    # # 选择岗位分类
    # def click_select_post(self):
    #     return self.click(self.select_post)
    #
    # # 点击空白区域
    # def click_blank_area1(self):
    #     return self.click(self.blank_area1)
    #
    # # 选择岗位输入框
    # def click_select_post_input(self):
    #     return self.click(self.select_post_input)
    #
    # # 选择具体岗位
    # def click_select_specific_post(self):
    #     return self.click(self.select_specific_post)
    #
    # # 点击确定按钮
    # def click_determine2_btn(self):
    #     return self.click(self.determine2_btn)






