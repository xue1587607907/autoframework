from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 试题库页面
class QuestionBankPage(BaseAction):

    # 试卷与试题按钮
    papers_and_questions_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[1]/ul/li[6]"

    # 试题库按钮
    question_bank_btn = By.CSS_SELECTOR, "li.jw-router-child:nth-child(7)"

    # 课程名称搜索框
    course_name_search = By.CSS_SELECTOR, "div.jw-inline-block:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 时间筛选框
    time_filter = By.CSS_SELECTOR, "input.el-range-input:nth-child(2)"

    # 最近一周,最近一个月筛选按钮
    last_week_btn = By.CSS_SELECTOR, "button.el-picker-panel__shortcut:nth-child(1)"
    last_month_btn = By.CSS_SELECTOR, "button.el-picker-panel__shortcut:nth-child(2)"

    # 状态筛选框
    status_filter = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[1]/main/div/div[3]/div/div/div/input"
    # enable_btn = By.CSS_SELECTOR, "div.el-select-dropdown:nth-child(4) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2)"
    enable_btn = By.CSS_SELECTOR, "div.el-select-dropdown:nth-child(4) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > span:nth-child(1)"
    # disable_btn = By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[3]/span"
    disable_btn = By.CSS_SELECTOR, "div.el-select-dropdown:nth-child(4) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2)"

    # 新建按钮
    new_btn = By.CSS_SELECTOR, ".jw-table-buttons-contain > div:nth-child(1) > button:nth-child(1)"

    # 题库名称输入框
    question_bank_name_input = By.CSS_SELECTOR, "div.el-form-item:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)"

    # 分类输入框
    sort_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[1]/main/div/div[5]/div/div[2]/form/div[2]/div/div/div/input"

    # 三级分类按钮
    # d1 = By.XPATH, "/html/body/div[4]/div[1]/div[1]/div[1]/ul/li[3]/span"
    # d2 = By.XPATH, "/html/body/div[4]/div[1]/div[2]/div[1]/ul/li[2]/span"
    # d3 = By.XPATH, "/html/body/div[4]/div[1]/div[3]/div[1]/ul/li[1]/span"
    d1 = By.XPATH, "/html/body/div[3]/div[1]/div/div[1]/ul/li[1]/span"
    d2 = By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[2]/span"
    d3 = By.XPATH, "/html/body/div[3]/div[1]/div[3]/div[1]/ul/li[2]/span"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[1]/main/div/div[5]/div/div[3]/div/div/button[2]"

    # 单选题按钮
    single_choice_questions_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div/ul/li[1]"

    # 题目输入框
    subject_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[4]/div/div[2]/div/div/div[1]/div[2]/div[1]/textarea"

    # 选项A
    optionA_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[4]/div/div[2]/div/div/div[2]/div[2]/div[1]/div[2]/div[1]/textarea"

    # 选项B
    optionB_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[4]/div/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/textarea"

    # 答案选项按钮
    answer_option = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[4]/div/div[2]/div/div/div[3]/div[2]/div[1]/div/label[1]/span[1]/span"

    # 弹窗确定按钮
    determine1_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[4]/div/div[3]/div/button[2]"

    # 外面确定按钮
    determine2_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[5]/button[1]"

    # 题库名称按钮
    question_bank1_btn = By.CSS_SELECTOR, ".el-table__body-wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)"

    # 题库单选框
    question_bank_radio = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span"

    # 删除按钮
    remove_btn = By.CSS_SELECTOR, "button.el-button--mini:nth-child(2)"

    # 弹窗的确定按钮
    determine3_btn = By.CSS_SELECTOR, "button.el-button--default:nth-child(2)"

    # 更多按钮
    more_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[8]/div/main/main/div/button"

    # 更多下的禁用按钮
    disable1_btn = By.XPATH, "/html/body/ul/li[2]"

    # 禁用的确定按钮
    determine4_btn = By.XPATH, "/html/body/div[2]/div/div[3]/button[2]"

    # 更多下的编辑按钮
    edit_btn = By.XPATH, "/html/body/ul/li[1]"

    # 向右翻页
    page_right = By.CSS_SELECTOR, "i.el-icon-arrow-right:nth-child(1)"

    # 向左翻页
    page_left = By.CSS_SELECTOR, ".el-icon-arrow-left"

    # 页数筛选框
    page_num_filter = By.CSS_SELECTOR, ".el-pagination__sizes > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 选择5条/页
    first_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 点击试题与试卷
    def click_papers_and_questions_btn(self):
        return self.click(self.papers_and_questions_btn)

    # 点击试题库
    def click_question_bank_btn(self):
        return self.click(self.question_bank_btn)

    # 点击课程名称搜索框
    def click_course_name_search(self):
        return self.click(self.course_name_search)

    # 输入课程名称
    def input_courses_name(self, content):
        return self.input(self.course_name_search, content)

    # 点击新增时间筛选框
    def click_time_filter(self):
        return self.click(self.time_filter)

    # 点击最近一周
    def click_last_week_btn(self):
        return self.click(self.last_week_btn)

    # 点击最近一个月
    def click_last_month_btn(self):
        return self.click(self.last_month_btn)

    # 点击状态进行筛选
    def click_status_filter(self):
        return self.click(self.status_filter)

    # 点击已启用
    def click_enable_btn(self):
        return self.click(self.enable_btn)

    # 点击已禁用
    def click_disable_btn(self):
        return self.click(self.disable_btn)

    # 点击新建按钮
    def click_new_btn(self):
        return self.click(self.new_btn)

    # 输入题库名称
    def input_question_bank_name(self, content):
        return self.input(self.question_bank_name_input, content)

    # 点击分类输入框
    def click_sort_input(self):
        return self.click(self.sort_input)

    # 选择三级分类
    def select_third_sort(self):
        self.click(self.d1)
        self.click(self.d2)
        return self.click(self.d3)

    # 点击确定按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 点击单选题
    def click_single_choice_questions_btn(self):
        return self.click(self.single_choice_questions_btn)

    # 输入题目
    def input_subject(self, content):
        return self.input(self.subject_input,content)

    # 输入选项A
    def input_option_a(self, content):
        return self.input(self.optionA_input, content)

    # 输入选项A
    def input_option_b(self, content):
        return self.input(self.optionB_input, content)

    # 选择答案
    def select_answer(self):
        return self.click(self.answer_option)

    # 点击弹窗确定按钮
    def click_determine1_btn(self):
        return self.click(self.determine1_btn)

    # 点击外部确定按钮
    def click_determine2_btn(self):
        return self.click(self.determine2_btn)

    # 点击题库名称
    def click_question_bank1_btn(self):
        return self.click(self.question_bank1_btn)

    # 点击更多按钮
    def click_more_btn(self):
        return self.click(self.more_btn)

    # 点击编辑按钮
    def click_edit_btn(self):
        return self.click(self.edit_btn)

    # 点击禁用按钮
    def click_disable1_btn(self):
        return self.click(self.disable1_btn)

    # 禁用弹窗的确定按钮
    def click_determine3_btn(self):
        return self.click(self.determine3_btn)

    # 勾选题库
    def click_question_bank_radio(self):
        return self.click(self.question_bank_radio)

    # 点击删除试题
    def click_remove_btn(self):
        return self.click(self.remove_btn)

    # 点击确定按钮
    def click_determine4_btn(self):
        return self.click(self.determine3_btn)

    # 点击向右翻页
    def click_page_right(self):
        return self.click(self.page_right)

    # 点击向左翻页
    def click_page_left(self):
        return self.click(self.page_left)

    # 点击页数筛选框
    def click_page_num_filter(self):
        return self.click(self.page_num_filter)

    # 点击5条/页
    def click_first_btn(self):
        return self.click(self.first_btn)



