from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 问卷管理页面
class QuestionnaireManagementPage(BaseAction):

    # 问卷管理按钮
    questionnaire_management_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[6]/div/span[2]"

    # 关键字搜索框
    keyword_search = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[1]/div[1]/div[1]/input"

    # 组织形式筛选框
    organizational_form_filter = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[1]/div[1]/div[2]/div[1]/input"

    # 选择学习项目
    select_learn_project = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 选择直接发起
    select_directly_by = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]/span"

    # 状态筛选框
    status_filter = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[1]/div[1]/div[3]/div[1]/input"

    # 选择待发布
    select_unpublished = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 选择进行中
    select_under_way = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[3]/span"

    # 新建问卷按钮
    add_questionnaire_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[1]/div[2]/div/button/span"

    # 复制模板按钮
    copy_template_btn = By.XPATH, "/html/body/ul/li[1]"

    # 问卷模板选择框
    questionnaire_template_select = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/form/div[1]/div/div/input"

    # 选择模板
    select_template = By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span[1]/span"

    # 点击确定
    determine_btn = By.XPATH, "/html/body/div[2]/div/div[3]/div/button[1]"

    # 问卷名称输入框
    questionnaire_name_input = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/form/div[2]/div/div[1]/input"

    # 富文本输入框
    rich_text_input = By.CLASS_NAME, "w-e-text"

    # 开始时间选择框
    start_time_select = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/form/div[4]/div/div/div[1]/span[1]/i"
    # 选择开始时间
    select_start_time = By.XPATH, "/html/body/div[2]/div[2]/button[1]/span"

    # 结束时间选择框
    end_time_select = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/form/div[5]/div/div/span[1]/i"
    # 选择结束时间
    select_end_time1 = By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/button[4]"
    select_end_time2 = By.XPATH, "/html/body/div[3]/div[1]/div/div[3]/table[1]/tbody/tr[4]/td[1]/div/span"

    # 回收上限输入框
    upper_bound_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/form/div[6]/div/div[1]/div[1]/div[1]/div/input"

    # 下一步按钮
    next_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div[1]/button[1]/span"

    # 问卷内容页面下一步按钮
    next_btn1 = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/button[1]/span"

    # 指定人员填写复选框
    checkbox = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[3]/div/div[1]/div/label[3]/span[1]/span"

    # 添加用户按钮
    add_user_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[3]/div/div[2]/div[1]/div[2]/div[1]/button[1]/span"

    # 弹窗的姓名输入框
    name_input = By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[3]/div[1]/div/div/div/input"

    # 全选框
    select_all = By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[3]/div[2]/div/div/div[2]/table/thead/tr/th[1]/div/label/span/span"

    # 确定按钮
    determine_btn1 = By.XPATH, "/html/body/div[2]/div/div[3]/div/button[1]"

    # 发布按钮
    publish_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[3]/div/div[3]/button[1]"

    # 直接新建
    new_direct = By.XPATH, "/html/body/ul/li[2]"

    # 问卷名称输入框
    questionnaire_name_input1 = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/form/div[1]/div/div[1]/input"

    # 富文本框
    rich_text_input1 = By.CLASS_NAME, "w-e-text"

    # 开始时间输入框
    start_time_input = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/form/div[3]/div/div/div[1]/span[1]/i"

    # 点击此刻
    at_the_moment = By.XPATH, "/html/body/div[2]/div[2]/button[1]/span"

    # 结束时间输入框
    end_time_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/form/div[4]/div/div/span[1]/i"

    # 选择结束时间
    next_month_btn = By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/button[4]"
    time_btn = By.XPATH, "/html/body/div[3]/div[1]/div/div[3]/table[1]/tbody/tr[4]/td[1]/div/span"

    # 上限输入框
    upper_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/form/div[5]/div/div[1]/div[1]/div[1]/div/input"

    # 下一步按钮
    next_btn2 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div[1]/button[1]/span"

    # 单选题按钮
    single_choice_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[2]/div/div/div[1]/div/div[1]/div[2]/div[1]"

    # 题目输入框
    subject_input = By.XPATH, "/html/body/div[2]/div/div[2]/div/form/div[1]/div/div[1]/textarea"

    # 选项输入框
    option_input = By.XPATH, "/html/body/div[2]/div/div[2]/div/form/div[4]/div/div[2]/div/div/div/div[1]/div/div/div[1]/input"

    # 确定按钮
    determine_btn2 = By.XPATH, "/html/body/div[2]/div/div[3]/div/button[1]"

    # 下一步按钮
    next_btn3 = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/button[1]"

    # 发布按钮
    publish_btn1 = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[3]/div/div[2]/button[1]"

    # 点击问卷管理
    def click_questionnaire_management_btn(self):
        return self.click(self.questionnaire_management_btn)

    # 输入问卷名称进行搜索
    def input_questionnaire_name(self, content):
        return self.input(self.keyword_search, content)

    # 点击组织形式筛选框
    def click_organizational_form_filter(self):
        return self.click(self.organizational_form_filter)

    # 选择学习项目
    def click_select_learn_project(self):
        return self.click(self.select_learn_project)

    # 选择直接发起
    def click_select_directly_by(self):
        return self.click(self.select_directly_by)

    # 点击状态筛选框
    def click_status_filter(self):
        return self.click(self.status_filter)

    # 选择待发布
    def click_select_unpublished(self):
        return self.click(self.select_unpublished)

    # 选择进行中
    def click_select_under_way(self):
        return self.click(self.select_under_way)

    # 点击新建问卷
    def click_add_questionnaire_btn(self):
        return self.click(self.add_questionnaire_btn)

    # 点击复制模板
    def click_copy_template_btn(self):
        return self.click(self.copy_template_btn)

    # 点击问卷模板输入框
    def click_questionnaire_template_select(self):
        return self.click(self.questionnaire_template_select)

    # 选择模板
    def click_select_template(self):
        return self.click(self.select_template)

    # 点击确定
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 输入问卷名称
    def input_questionnaire_name_input(self, content):
        return self.input(self.questionnaire_name_input, content)

    # 输入问卷说明
    def input_questionnaire_declare(self, content):
        return self.input(self.rich_text_input, content)

    # 选择开始时间输入框
    def click_start_time_select(self):
        self.click(self.start_time_select)
        return self.click(self.select_start_time)

    # 选择结束时间
    def click_end_time_select(self):
        self.click(self.end_time_select)
        self.click(self.select_end_time1)
        return self.click(self.select_end_time2)

    # 输入回收上限
    def input_upper_bound(self, content):
        return self.input(self.upper_bound_input, content)

    # 点击下一步按钮
    def click_next_btn(self):
        return self.click(self.next_btn)

    # 问卷内容页面的下一步按钮
    def click_next_btn1(self):
        return self.click(self.next_btn1)

    # 勾选指定人员填写
    def click_checkbox(self):
        return self.click(self.checkbox)

    # 点击添加用户按钮
    def click_add_user_btn(self):
        return self.click(self.add_user_btn)

    # 输入姓名进行搜索
    def input_name_search(self, content):
        return self.input(self.name_input, content)

    # 全选框
    def click_select_all(self):
        return self.click(self.select_all)

    # 点击确定按钮
    def click_determine_btn1(self):
        return self.click(self.determine_btn1)

    # 点击发布按钮
    def click_publish_btn(self):
        return self.click(self.publish_btn)

    # 点击直接新建
    def click_new_direct(self):
        return self.click(self.new_direct)

    # 点击问卷名称输入框
    def input_questionnaire_name1(self, content):
        return self.input(self.questionnaire_name_input1, content)

    # 输入问卷说明
    def input_questionnaire_declare1(self, content):
        return self.input(self.rich_text_input1, content)

    # 选择开始时间
    def click_start_time_input(self):
        self.click(self.start_time_input)
        return self.click(self.at_the_moment)

    # 选择结束时间
    def click_end_time_input(self):
        self.click(self.end_time_input)
        self.click(self.next_month_btn)
        return self.click(self.time_btn)

    # 输入上限
    def input_upper(self, content):
        return self.input(self.upper_input, content)

    # 点击下一步
    def click_next_btn2(self):
        return self.click(self.next_btn2)

    # 点击单选题按钮
    def click_single_choice_btn(self):
        return self.click(self.single_choice_btn)

    # 输入单选题题目
    def input_subject(self, content):
        return self.input(self.subject_input, content)

    # 输入选项
    def input_option_input(self, content):
        return self.input(self.option_input, content)

    # 点击确定
    def click_determine_btn2(self):
        return self.click(self.determine_btn2)

    # 点击下一步(跳转到人员范围页面)
    def click_next_btn3(self):
        return self.click(self.next_btn3)

    # 点击发布按钮
    def click_publish_btn1(self):
        return self.click(self.publish_btn1)

