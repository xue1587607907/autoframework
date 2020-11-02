from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 培训需求页面
class TrainNeedsPage(BaseAction):

    # 培训需求按钮
    train_needs_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[3]"

    # 需求名称输入框
    needs_name_search = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[1]/main/div/div/div[1]/input"

    # 状态筛选框
    status_filter = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[1]/main/div/div/div[3]/div[1]/input"

    # 未完成
    no_finished = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 已完成
    finished = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]"

    # 更新时间筛选框
    update_time_filter = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[1]/main/div/div/div[4]/div/div/div/input[1]"

    # 最近一周
    last_week = By.XPATH, "/html/body/div[2]/div[1]/div[1]/button[1]"

    # 最近一个月
    last_month = By.XPATH, "/html/body/div[2]/div[1]/div[1]/button[2]"

    # 新增需求按钮
    new_needs_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/button/span"

    # 需求名称输入框
    needs_name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/div/div[2]/form/div[1]/div/div[1]/input"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/div/div[3]/div/button[1]/span"

    # 设置为已完成
    set_to_completed = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/main/main"

    # 需求名称按钮(点击进入编辑)
    need_name_btn = By.CSS_SELECTOR, ".el-table__body-wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)"

    # 删除按钮
    remove_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[2]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/main/main/span[2]"

    # 确定按钮
    determine1_btn = By.XPATH, "/html/body/div[4]/div/div[3]/button[2]/span"

    # 点击培训需求
    def click_train_needs_btn(self):
        return self.click(self.train_needs_btn)

    # 输入需求名称进行搜索
    def input_needs_name_search(self, content):
        return self.input(self.needs_name_search, content)

    # 点击状态筛选框
    def click_status_filter(self):
        return self.click(self.status_filter)

    # 选择未完成
    def click_no_finished(self):
        return self.click(self.no_finished)

    # 选择已完成
    def click_finished(self):
        return self.click(self.finished)

    # 点击更新时间筛选框
    def click_update_time_filter(self):
        return self.click(self.update_time_filter)

    # 点击最近一周
    def click_last_week(self):
        return self.click(self.last_week)

    # 点击最近一个月
    def click_last_month(self):
        return self.click(self.last_week)

    # 点击新增需求按钮
    def click_new_needs_btn(self):
        return self.click(self.new_needs_btn)

    # 输入需求名称
    def input_needs_name(self, content):
        return self.input(self.needs_name_input, content)

    # 点击确定按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 点击设置已完成
    def click_set_to_completed(self):
        return self.click(self.set_to_completed)

    # 点击需求名称按钮(点击进入编辑)
    def click_need_name_btn(self):
        return self.click(self.need_name_btn)

    # 清空需求名称
    def clear_needs_name_input(self):
        return self.clear(self.needs_name_input)

    # 点击删除按钮
    def click_remove_btn(self):
        return self.click(self.remove_btn)

    # 点击确定按钮
    def click_determine1_btn(self):
        return self.click(self.determine1_btn)
