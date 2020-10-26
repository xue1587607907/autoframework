from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 试卷库页面
class PaperLibraryPage(BaseAction):

    # 试卷与试题按钮
    papers_and_questions_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[1]/ul/li[5]"

    # 试卷库按钮
    paper_btn = By.CSS_SELECTOR, "li.jw-router-child:nth-child(8)"

    # 课程名称搜索框
    course_name_search = By.CSS_SELECTOR, "div.jw-inline-block:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 时间筛选框
    time_filter = By.CSS_SELECTOR, "input.el-range-input:nth-child(2)"

    # 最近一周,最近一个月筛选按钮
    last_week_btn = By.CSS_SELECTOR, "button.el-picker-panel__shortcut:nth-child(1)"
    last_month_btn = By.CSS_SELECTOR, "button.el-picker-panel__shortcut:nth-child(2)"

    # 状态筛选框
    status_filter = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[1]/main/div/div[3]/div/div/div/input"
    enable_btn = By.CSS_SELECTOR, "div.el-select-dropdown:nth-child(4) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2)"
    disable_btn = By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[3]/span"

    # 新建按钮
    new_btn = By.CSS_SELECTOR, ".jw-table-buttons-contain > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)"

    # 固定试卷按钮
    fixed_papers_btn = By.XPATH, "/html/body/ul/li[1]"

    # 固定试卷名称输入框
    paper_name_input = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[1]/div[1]/div/div/div/form/div/div/div[1]/input"

    # 从题库中选择题目按钮
    question_bank_select_btn = By.CSS_SELECTOR, ".jw-new-side-cong > p:nth-child(1)"

    # 搜索题库输入框
    search_question_bank_input = By.CSS_SELECTOR, "div.el-form-item__content:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 搜索框按钮
    search_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/form/div/div/div/span/span/i"

    # 选择题库按钮
    question_bank1_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[1]/div[1]/div[3]/table/tbody/tr[1]/td/div"

    # 全选题目复选框
    select_all = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[1]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/table/thead/tr/th[1]/div/label/span/span"

    # 确定按钮
    determine_btn = By.CSS_SELECTOR, ".dialog-footer > button:nth-child(1)"

    # 试题删除按钮
    remove_btn = By.CSS_SELECTOR, "div.jw-new-newfixed-ti:nth-child(2) > div:nth-child(3) > form:nth-child(1) > div:nth-child(2) > div:nth-child(1) > p:nth-child(1) > span:nth-child(3) > img:nth-child(1)"

    # 提示确定按钮
    determine1_btn = By.XPATH, "/html/body/div[2]/div/div[3]/button[2]/span"

    # 分值输入框
    score_input = By.CSS_SELECTOR, "div.el-input:nth-child(2) > input:nth-child(1)"

    # 保存按钮
    save_btn = By.CSS_SELECTOR, "button.el-button--mini:nth-child(1)"

    # 随机试卷按钮--------------------------------------------------------------
    random_papers_btn = By.XPATH, "/html/body/ul/li[2]"

    # 随机试卷名称输入框
    random_paper_input = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[1]/div/div[1]/form/div/div/div[1]/input"

    # 添加题库按钮
    add_question_bank_btn = By.CSS_SELECTOR, ".jw-new-side-cong > p:nth-child(1)"

    # 全选题库
    select_all1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/table/thead/tr/th[1]/div/label/span/span"

    # 确定按钮
    determine2_btn = By.CSS_SELECTOR, ".dialog-footer > button:nth-child(1)"

    # 抽题数量输入框
    select_question_input1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[1]/div/div[3]/div[1]/p[2]/div/input"
    select_question_input2 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[1]/div/div[3]/div[2]/p[2]/div/input"
    select_question_input3 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[1]/div/div[3]/div[3]/p[2]/div/input"
    select_question_input4 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[1]/div/div[3]/div[4]/p[2]/div/input"
    select_question_input5 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[1]/div/div[3]/div[5]/p[2]/div/input"

    # 分值输入框
    score_input1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[1]/div/div[3]/div[1]/p[3]/div/input"
    score_input2 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[1]/div/div[3]/div[2]/p[3]/div/input"
    score_input3 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[1]/div/div[3]/div[3]/p[3]/div/input"
    score_input4 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[1]/div/div[3]/div[4]/p[3]/div/input"
    score_input5 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[1]/div/div[3]/div[5]/p[3]/div/input"

    # 确定按钮
    determine3_btn = By.CSS_SELECTOR, "button.el-button--mini:nth-child(1)"

    # 更多按钮
    more_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/main/main/div/button"

    # 编辑按钮
    edit_btn = By.XPATH, "/html/body/ul/li[1]"

    # 禁用按钮
    disable1_btn = By.XPATH, "/html/body/ul/li[2]"

    # 禁用的确定按钮
    determine4_btn = By.XPATH, "/html/body/div[2]/div/div[3]/button[2]"

    # 选择试卷单选框
    radio = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span/span"

    # 试卷删除按钮
    remove1_btn = By.CSS_SELECTOR, "button.el-button--mini:nth-child(2)"

    # 弹窗的确定按钮
    determine5_btn = By.CSS_SELECTOR, "button.el-button--default:nth-child(2)"

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

    # 点击试卷库
    def click_paper_btn(self):
        return self.click(self.paper_btn)

    # 点击课程名称搜索框
    def click_course_name_search(self):
        return self.click(self.course_name_search)

    # 输入课程名称
    def input_courses_name(self, content):
        return self.input(self.course_name_search, content)

    # 点击时间筛选框
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

    # 点击新建按钮 ---------------------------------------------
    def click_new_btn(self):
        return self.click(self.new_btn)

    # 点击固定试卷
    def click_fixed_papers_btn(self):
        return self.click(self.fixed_papers_btn)

    # 输入固定试卷名称
    def input_paper_name(self, content):
        return self.input(self.paper_name_input, content)

    # 点击从题库中选择试题--------------------------------
    def click_question_bank_select_btn(self):
        return self.click(self.question_bank_select_btn)

    # 搜索框输入试卷名称
    def input_question_bank(self, content):
        return self.input(self.search_question_bank_input, content)

    # 搜索框按钮
    def click_search_btn(self):
        return self.click(self.search_btn)

    # 点击搜索出来的题库
    def select_question_bank1_btn(self):
        return self.click(self.question_bank1_btn)

    # 全选按钮
    def click_select_all(self):
        return self.click(self.select_all)

    # 点击确定按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 点击删除试题按钮
    def click_remove_btn(self):
        return self.click(self.remove_btn)

    # 点击确定按钮
    def click_determine1_btn(self):
        return self.click(self.determine1_btn)

    # 输入分值
    def input_score(self, content):
        return self.input(self.score_input, content)

    # 点击保存
    def click_save_btn(self):
        return self.click(self.save_btn)

    # 点击随机试卷
    def click_random_papers_btn(self):
        return self.click(self.random_papers_btn)

    # 输入随机试卷名称
    def input_random_paper(self, content):
        return self.input(self.random_paper_input, content)

    # 点击添加题库
    # 点击全选题库
    def click_select_all1(self):
        return self.click(self.select_all1)

    # 点击确定按钮
    def click_determine2_btn(self):
        return self.click(self.determine2_btn)

    # 输入抽题数量
    def input_select_question(self, content):
        self.input(self.select_question_input1, content)
        self.input(self.select_question_input2, content)
        return self.input(self.select_question_input3, content)

    # 输入分值
    def input_score1(self, content):
        self.input(self.score_input1, content)
        self.input(self.score_input2, content)
        return self.input(self.score_input3, content)

    # 点击确定
    def click_determine3_btn(self):
        return self.click(self.determine3_btn)

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
    def click_determine4_btn(self):
        return self.click(self.determine4_btn)

    # 点击选择试卷单选框
    def click_radio(self):
        return self.click(self.radio)

    # 点击删除试卷
    def click_remove1_btn(self):
        return self.click(self.remove1_btn)

    # 点击确定按钮
    def click_determine5_btn(self):
        return self.click(self.determine5_btn)

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













