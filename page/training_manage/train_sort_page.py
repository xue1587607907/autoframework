from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 培训分类页面
class TrainSortPage(BaseAction):

    # 培训管理按钮
    train_manage_btn = By.XPATH, "/html/body/div/div/div[3]/div[2]/ul/li[3]/span"

    # 培训规划按钮
    train_plan_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[1]/span[2]"

    # 培训分类按钮
    train_sort_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[2]"

    # 第一个搜索框
    first_search = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div/div[1]/input"

    # 第二个搜索框
    second_search = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[1]/main/div/div[1]/div/input"

    # 新建按钮
    new_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[1]/div/button"

    # 父级分类
    parent_sort = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[1]/main/div/div[2]/div/div[2]/form/div[1]/div/div/div[1]/input"

    # 选择分类
    d1 = By.XPATH, "/html/body/div[3]/div[1]/div/div[1]/ul/li/span"
    d2 = By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[1]/label/span[1]/span"

    # 空白区域
    blank_area = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[1]/main/div/div[2]/div/div[1]"

    # 分类名称输入框
    sort_name_input = By.CSS_SELECTOR, "div.el-form-item:nth-child(2) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[1]/main/div/div[2]/div/div[3]/div/button[1]/span"

    # 上下移动按钮
    move_up_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr[2]/td[2]/div/main/main/div/span[2]"
    move_down_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[2]/div/main/main/div/span[2]"

    # 删除按钮
    remove_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr[6]/td[2]/div/main/main/div/span[1]"

    # 删除弹窗的确定按钮
    determine1_btn = By.XPATH, "/html/body/div[2]/div/div[3]/button[2]"

    # 分类名称按钮(点击进入编辑)
    sort_name_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[6]/td[1]/div/div/span"

    # 点击培训管理
    def click_train_manage_btn(self):
        return self.click(self.train_manage_btn)

    # 在第一个搜索框输入内容进行查询
    def input_content_first_search(self, content):
        return self.input(self.first_search, content)

    # 在第二个搜索框输入内容进行查询
    def input_content_second_search(self, content):
        return self.input(self.second_search, content)

    # 点击新建
    def click_new_btn(self):
        return self.click(self.new_btn)

    # 点击父级分类
    def click_parent_sort(self):
        return self.click(self.parent_sort)

    # 选择分类
    def select_sort(self):
        self.click(self.d1)
        return self.click(self.d2)

    # 选择空白区域
    def click_blank_area(self):
        return self.click(self.blank_area)

    # 输入分类名称
    def input_sort_name(self, content):
        return self.input(self.sort_name_input, content)

    # 点击确定按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 点击分类名称进入编辑
    def click_sort_name_btn(self):
        return self.click(self.sort_name_btn)

    # 点击上移按钮
    def click_move_up_btn(self):
        return self.click(self.move_up_btn)

    # 点击下移按钮
    def click_move_down_btn(self):
        return self.click(self.move_down_btn)

    # 点击删除按钮
    def click_remove_btn(self):
        return self.click(self.remove_btn)

    # 点击确定按钮
    def click_determine1_btn(self):
        return self.click(self.determine1_btn)




