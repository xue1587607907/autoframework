from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 问卷模板页面
class QuestionnaireTemplatePage(BaseAction):

    # 资源管理按钮
    resources_manage_btn = By.XPATH, "/html/body/div/div/div[3]/div[2]/ul/li[3]/span"

    # 问卷模板按钮
    questionnaire_template_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[8]/div/span[2]"

    # 关键字搜索框
    keyword_search = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[1]/div[1]/div[1]/input"

    # 时间筛选框
    time_filter_box = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[1]/div[1]/div[2]/div/div/i[1]"

    # 最近一周
    last_week_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/button[1]"

    # 最近一个月
    last_month_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/button[2]"

    # 状态筛选框
    status_filter = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[1]/div[1]/div[3]/div[1]/input"

    # 已启用按钮
    enable_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 已禁用按钮
    disable_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]/span"

    # 新建按钮
    add_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[1]/div[2]/button/span"

    # 模板名称输入框
    template_name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[1]/div[2]/div/div/div[2]/form/div/div/div/input"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[1]/div[2]/div/div/div[3]/div/button[1]/span"

    # 再次确定按钮
    determine_btn1 = By.XPATH, "/html/body/div[3]/div/div[3]/button[2]/span"

    # 单选题按钮
    single_choice_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/div[1]"

    # 题目输入框
    topic_input = By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[1]/div/div/textarea"

    # 第一个选项输入框
    option_input = By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[4]/div/div[2]/div/div/div/div[1]/div/div/div/input"

    # 新增选项按钮
    add_option_btn = By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[5]/div/div/div[1]"

    # 第二个选项输入框
    option_input2 = By.XPATH, "/html/body/div[3]/div/div[2]/div/form/div[4]/div/div[3]/div/div/div/div[1]/div/div/div[1]/input"

    # 确定按钮
    determine_btn2 = By.XPATH, "/html/body/div[3]/div/div[3]/div/button[1]/span"

    # 禁用按钮
    disable_btn1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div/div/div[5]/div[2]/table/tbody/tr[1]/td[7]/div/main/div/span[1]"

    # 确定按钮(与删除的确定按钮复用)
    determine_btn3 = By.XPATH, "/html/body/div[2]/div/div[3]/button[2]"

    # 删除按钮
    remove_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div/div/div[5]/div[2]/table/tbody/tr[1]/td[7]/div/main/div/span[2]"

    # 点击资源管理
    def click_resources_manage_btn(self):
        return self.click(self.resources_manage_btn)

    # 点击问卷模板
    def click_questionnaire_template_btn(self):
        return self.click(self.questionnaire_template_btn)

    # 输入关键字进行查询
    def input_keyword(self, content):
        return self.input(self.keyword_search, content)

    # 点击时间筛选框
    def click_time_filter_box(self):
        return self.click(self.time_filter_box)

    # 点击最近一周
    def click_last_week_btn(self):
        return self.click(self.last_week_btn)

    # 点击最近一个月
    def click_last_month_btn(self):
        return self.click(self.last_month_btn)

    # 点击状态筛选框
    def click_status_filter(self):
        return self.click(self.status_filter)

    # 点击已启用
    def click_enable_btn(self):
        return self.click(self.enable_btn)

    # 点击已禁用
    def click_disable_btn(self):
        return self.click(self.disable_btn)

    # 点击新建按钮
    def click_add_btn(self):
        return self.click(self.add_btn)

    # 输入模板名称
    def input_template_name(self, content):
        return self.input(self.template_name_input, content)

    # 点击确定按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 再次点击外面的确定按钮
    def click_determine_btn1(self):
        return self.click(self.determine_btn1)

    # 点击单选题按钮
    def click_single_choice_btn(self):
        return self.click(self.single_choice_btn)

    # 输入题目名称
    def input_topic(self, content):
        return self.input(self.topic_input, content)

    # 输入选项内容
    def input_option_input(self, content):
        return self.input(self.option_input, content)

    # 点击新增选项按钮
    def click_add_option_btn(self):
        return self.click(self.add_option_btn)

    # 输入选项内容
    def input_option_input2(self, content):
        return self.input(self.option_input2, content)

    # 点击确定按钮
    def click_determine_btn2(self):
        return self.click(self.determine_btn2)

    # 点击禁用按钮
    def click_disable_btn1(self):
        return self.click(self.disable_btn1)

    # 点击确定按钮
    def click_determine_btn3(self):
        return self.click(self.determine_btn3)

    # 点击删除按钮
    def click_remove_btn(self):
        return self.click(self.remove_btn)



