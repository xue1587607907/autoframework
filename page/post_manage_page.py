from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 岗位管理页面
class PostManagePage(BaseAction):
    # 岗位管理按钮
    post_manage_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[2]"

    # 第一个搜索框
    first_search = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div/div[1]/input"

    # 第二个搜索框
    second_search = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[1]/main/div/div/div/input"

    # 新建按钮
    new_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[1]/div/button/span"

    # 所属分类输入框
    classification_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/form/div[1]/div/div/div/input"

    # 选择分类
    d1 = By.XPATH, "/html/body/div[3]/div[1]/div[1]/div[1]/ul/li/span"
    d2 = By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[1]/span"
    d3 = By.XPATH, "/html/body/div[3]/div[1]/div[3]/div[1]/ul/li[2]/label/span[1]/span"

    # 空白区域
    blank_area = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div"

    # 岗位名称输入框
    post_name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/form/div[2]/div/div[1]/input"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[1]/div/div/div/div[3]/div/button[1]"

    # 岗位名称按钮(点击进入编辑)
    post_name1_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[3]/td[1]/div/span/span"

    # 管理用户
    manage_user_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/main/main/button[1]"

    # 删除按钮
    remove_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr[3]/td[8]/div/main/main/button[2]"

    # 弹窗的确定按钮
    determine1_btn = By.CSS_SELECTOR, "button.el-button--small:nth-child(2) > span:nth-child(1)"

    # 点击岗位管理按钮
    def click_post_manage_btn(self):
        return self.click(self.post_manage_btn)

    # 通过第一个搜索框进行搜索
    def input_first_search(self, content):
        return self.input(self.first_search, content)

    # 通过第二个搜索框进行搜索
    def input_second_search(self, content):
        return self.input(self.second_search, content)

    # 点击新建按钮
    def click_new_btn(self):
        return self.click(self.new_btn)

    # 点击所属分类
    def click_classification_select(self):
        return self.click(self.classification_input)

    # 选择三类分类
    def select_third_sort(self):
        self.click(self.d1)
        self.click(self.d2)
        self.click(self.d3)
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






