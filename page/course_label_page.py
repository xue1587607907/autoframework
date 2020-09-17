from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 课程标签页面
class CourseLabelPage(BaseAction):

    # 课程标签按钮
    course_label_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[2]"

    # 资源分类输入框
    resources_sort_input = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[1]/main/form/div/div/div/div[1]/input"

    # 选择三级分类
    d1 = By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/ul/li[1]/span"
    d2 = By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/ul/li[2]/span"
    d3 = By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[1]/ul/li[2]/span"

    # 新建按钮
    new_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[2]/div[1]/button"

    # 标签分类输入框
    label_sort_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[2]/div[1]/div/div/div[2]/form/div[1]/div/div[1]/input"

    # 标签名称输入框
    label_name_input1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[2]/div[1]/div/div/div[2]/form/div[2]/div/div[1]/div/div/div[1]/input"
    label_name_input2 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[2]/div[1]/div/div/div[2]/form/div[2]/div/div[2]/div/div[1]/div[1]/input"

    # 新增标签按钮
    add_label_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[2]/div[1]/div/div/div[2]/form/div[2]/div/div/div/div[1]/div[2]/span[1]"

    # 删除标签名称按钮
    remove_label_btn = By.CSS_SELECTOR, "div.tag:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > span:nth-child(2)"

    # 上移按钮
    move_up_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[2]/div[1]/div/div/div[2]/form/div[2]/div/div[2]/div/div/div[2]/span[3]"

    # 下移按钮
    move_down_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[2]/div[1]/div/div/div[2]/form/div[2]/div/div[1]/div/div/div[2]/span[4]"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[2]/div[1]/div/div/div[3]/div/button[1]"

    # 编辑标签按钮
    edit_label_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr/td[4]/div/main/main/div/span[1]"

    # 删除标签分类按钮
    remove1_label_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr/td[4]/div/main/main/div/span[2]"

    # 点击删除弹窗的确定按钮
    determine1_btn = By.XPATH, "/html/body/div[3]/div/div[3]/button[2]/span"

    # 点击课程标签按钮
    def click_course_label_btn(self):
        return self.click(self.course_label_btn)

    # 点击资源分类输入框
    def click_resources_sort_input(self):
        return self.click(self.resources_sort_input)

    # 选择三级分类
    def select_third_sort(self):
        self.click(self.d1)
        self.click(self.d2)
        return self.click(self.d3)

    # 点击新建按钮
    def click_new_btn(self):
        return self.click(self.new_btn)

    # 输入标签分类
    def input_label_sort(self, content):
        return self.input(self.label_sort_input, content)

    # 输入标签名称1
    def input_label_name1(self, content):
        return self.input(self.label_name_input1, content)

    # 输入标签名称2
    def input_label_name2(self, content):
        return self.input(self.label_name_input2, content)

    # 点击新增
    def click_add_label_btn(self):
        return self.click(self.add_label_btn)

    # 点击上移
    def click_move_up_btn(self):
        return self.click(self.move_up_btn)

    # 点击下移
    def click_move_down_btn(self):
        return self.click(self.move_down_btn)

    # 点击删除
    def click_remove_label_btn(self):
        return self.click(self.remove_label_btn)

    # 点击确定
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 点击编辑标签按钮
    def click_edit_label_btn(self):
        return self.click(self.edit_label_btn)

    # 点击删除标签分类按钮
    def click_remove1_label_btn(self):
        return self.click(self.remove1_label_btn)

    # 点击删除弹窗的确定按钮
    def click_determine1_btn(self):
        return self.click(self.determine1_btn)




