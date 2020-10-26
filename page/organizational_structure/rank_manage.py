from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 职级管理页面
class RankManagePage(BaseAction):

    # 职级管理按钮
    rank_manage_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[3]"

    # 新建按钮
    new_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[1]/div/button"

    # 职级名称输入框
    rank_name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[1]/div/div/div/div[2]/form/div[1]/div/div[1]/input"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/button[1]"

    # 职级名称按钮(点击编辑职级名称)
    rank_name_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[4]/td[2]/div/span/span"

    # 编辑按钮
    edit_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr[3]/td[4]/div/main/main/div/span[1]"

    # 用户单选框
    user_radio = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[2]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[1]/div/label/span/span"

    # 调整职级按钮
    adjust_rank_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/button"

    # 新职级选择框
    new_rank = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/div/div/div[2]/form/div[2]/div/div/div/div/div/div/input"

    # 选择职级
    select_rank = By.XPATH, "/html/body/div[4]/div[1]/div[1]/ul/li[2]"

    # 确定按钮
    determine1_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/div/div/div[3]/div/button[1]"

    # 上移/下移
    move_up_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr[4]/td[4]/div/main/main/div/span[2]"
    move_down_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr[3]/td[4]/div/main/main/div/span[3]"

    # 删除按钮
    remove_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr[4]/td[4]/div/main/main/div/span[4]"

    # 弹窗的确定按钮
    determine2_btn = By.XPATH, "/html/body/div[2]/div/div[3]/button[2]/span"

    # 点击职级管理
    def click_rank_manage_btn(self):
        return self.click(self.rank_manage_btn)

    # 点击新增按钮
    def click_new_btn(self):
        return self.click(self.new_btn)

    # 输入职级名称
    def input_rank_name(self, content):
        return self.input(self.rank_name_input, content)

    # 点击确定按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 点击职级名称进入编辑
    def click_rank_name_btn(self):
        return self.click(self.rank_name_btn)

    # 清空输入框
    def clear_rank_name_input(self):
        return self.clear(self.rank_name_input)

    # 点击编辑按钮
    def click_edit_btn(self):
        return self.click(self.edit_btn)

    # 点击用户单选框
    def click_user_radio(self):
        return self.click(self.user_radio)

    # 点击调整职级按钮
    def click_adjust_rank_btn(self):
        return self.click(self.adjust_rank_btn)

    # 点击新职级输入框
    def click_new_rank(self):
        return self.click(self.new_rank)

    # 选择职级
    def click_select_rank(self):
        return self.click(self.select_rank)

    # 点击确定
    def click_determine1_btn(self):
        return self.click(self.determine1_btn)

    # 点击上移
    def click_move_up_btn(self):
        return self.click(self.move_up_btn)

    # 点击下移
    def click_move_down_btn(self):
        return self.click(self.move_down_btn)

    # 点击删除按钮
    def click_remove_btn(self):
        return self.click(self.remove_btn)

    # 点击确定按钮
    def click_determine2_btn(self):
        return self.click(self.determine2_btn)
