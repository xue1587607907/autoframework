from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 操作日志页面
class OperationLogPage(BaseAction):

    # 操作日志按钮
    operation_log_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[2]/span[2]"

    # 账号搜索框
    account_search = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/main/div[1]/div[1]/div[1]/div/input"

    # 操作类型筛选框
    operation_type_filter = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/main/div[1]/div[1]/div[2]/div/div[1]/input"

    # 选择"新增"
    add_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 选择"编辑"
    edit_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]/span"

    # 模块筛选框
    module_filter = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/main/div[1]/div[1]/div[3]/div/div/input"

    # 选择"系统管理"
    system_manage_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]/span"

    # 选择"培训管理"
    train_manage_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[4]/span"

    # 功能筛选框
    function_filter = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/main/div[1]/div[1]/div[4]/div/div[1]/input"

    # 选择"培训分类"
    train_sort_btn = By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[1]/span"

    # 选择"岗位学习"
    post_learn = By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[5]/span"

    # 时间筛选框
    time_filter = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/main/div[1]/div[1]/div[5]/div/div/i[1]"

    # 选择"最近一周"
    last_week_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/button[1]"

    # 选择"最近一月"
    last_month_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/button[2]"

    # 点击操作日志
    def click_operation_log_btn(self):
        return self.click(self.operation_log_btn)

    # 输入账号名称搜索
    def input_account_search(self, content):
        return self.input(self.account_search, content)

    # 点击类型筛选框
    def click_operation_type_filter(self):
        return self.click(self.operation_type_filter)

    # 选择"新增"
    def click_add_btn(self):
        return self.click(self.add_btn)

    # 选择"编辑"
    def click_edit_btn(self):
        return self.click(self.edit_btn)

    # 点击模块筛选框
    def click_module_filter(self):
        return self.click(self.module_filter)

    # 选择系统管理
    def click_system_manage_btn(self):
        return self.click(self.system_manage_btn)

    # 选择培训管理
    def click_train_manage_btn(self):
        return self.click(self.train_manage_btn)

    # 点击功能筛选框
    def click_function_filter(self):
        return self.click(self.function_filter)

    # 选择培训分类
    def click_train_sort_btn(self):
        return self.click(self.train_sort_btn)

    # 选择岗位学习
    def click_post_learn(self):
        return self.click(self.post_learn)

    # 点击时间筛选框
    def click_time_filter(self):
        return self.click(self.time_filter)

    # 选择最近一周
    def click_last_week_btn(self):
        return self.click(self.last_week_btn)

    # 选择最近一个月
    def click_last_month_btn(self):
        return self.click(self.last_month_btn)


