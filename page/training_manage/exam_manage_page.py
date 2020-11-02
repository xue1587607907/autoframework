from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 考试管理页面
class ExamManagePage(BaseAction):

    # 培训管理按钮
    train_manage_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/ul/li[4]/span"

    # 考试管理按钮
    exam_manage_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[5]"

    # 关键字搜索框
    keyword_search = By.CSS_SELECTOR, "div.jw-inline-block:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 状态筛选框
    status_filter = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[1]/main/div/div[2]/div/div/div[1]/input"

    # 进行中
    have_in_hand_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[3]/span"

    # 未开始
    no_started_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]/span"

    # 考试组织筛选框
    exam_organ_filter = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[1]/main/div/div[3]/div/div/div[1]/input"

    # 直接发起
    direct_initiation = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 项目发起
    project_initiation = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]/span"

    # 新增按钮
    new_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/button"

    # 所用试卷输入框
    papers_used_input = By.CSS_SELECTOR, "div.jw-self-form-item:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 选择试卷
    select_paper = By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span[1]/span"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div[2]/div/div[3]/div/button[1]"

    # 考试名称输入框
    exam_name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/form/div[2]/div/div[1]/div/input"

    # 设置考试期限按钮
    radio_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[2]/div/div/div/div[1]/div[2]/div/form/div[4]/div/div/div/div/div/div[1]/div/label/span[1]/span"

    # 开始日期输入框
    start_time_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/form/div[4]/div/div/div/div/div/i[1]"

    # 选择考试期限
    time1 = By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[5]/td[5]/div/span"
    time2 = By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/table/tbody/tr[5]/td[7]/div/span"

    # 确定按钮
    determine1_btn = By.XPATH, "/html/body/div[3]/div[2]/button[2]/span"

    # 考试时长输入框
    exam_duration = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/form/div[6]/div/div[1]/div/div/input"

    # 通过分数输入框
    pass_score_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/form/div[8]/div/div/div[1]/div/div[1]/div/input"

    # 学分输入框
    credit_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/form/div[8]/div/div/div[2]/div/input"

    # 下一步按钮
    next_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div/div/div[1]/button[1]"

    # 添加用户按钮
    add_user_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[2]/div/div/div[1]/div[2]/button[1]/span"

    # 选择用户复选框
    select_user = By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div[3]/div[2]/div/div/div[2]/table/thead/tr/th[1]/div/label/span/span"

    # 确定按钮
    determine2_btn = By.XPATH, "/html/body/div[4]/div/div[3]/div/button[1]"

    # 保存并发布按钮
    save_and_publish = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[2]/div/div/div[3]/button[1]"

    # 点击培训管理
    def click_train_manage_btn(self):
        return self.click(self.train_manage_btn)

    # 点击考试管理按钮
    def click_exam_manage_btn(self):
        return self.click(self.exam_manage_btn)

    # 输入关键字查询
    def input_keyword_search(self, content):
        return self.input(self.keyword_search, content)

    # 点击状态筛选框
    def click_status_filter(self):
        return self.click(self.status_filter)

    # 点击进行中
    def click_have_in_hand_btn(self):
        return self.click(self.have_in_hand_btn)

    # 点击未开始
    def click_no_started_btn(self):
        return self.click(self.no_started_btn)

    # 点击考试组织筛选框
    def click_exam_organ_filter(self):
        return self.click(self.exam_organ_filter)

    # 点击直接发起
    def click_direct_initiation(self):
        return self.click(self.direct_initiation)

    # 点击项目发起
    def click_project_initiation(self):
        return self.click(self.project_initiation)

    # 点击新增按钮
    def click_new_btn(self):
        return self.click(self.new_btn)

    # 点击所用试卷输入框
    def click_papers_used_input(self):
        return self.click(self.papers_used_input)

    # 点击选择试卷
    def click_select_paper(self):
        return self.click(self.select_paper)

    # 点击确定按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 输入考试名称
    def input_exam_name(self, content):
        return self.input(self.exam_name_input, content)

    # 点击设置考试期限
    def click_radio_btn(self):
        return self.click(self.radio_btn)

    # 点击开始时间输入框
    def click_start_time_input(self):
        return self.click(self.start_time_input)

    # 点击选择考试期限
    def click_select_exam_period(self):
        self.click(self.time1)
        self.click(self.time2)

    # 点击确定按钮
    def click_determine1_btn(self):
        return self.click(self.determine1_btn)

    # 输入考试时长
    def input_exam_duration(self, content):
        return self.input(self.exam_duration, content)

    # 输入通过分数
    def input_pass_score(self, content):
        return self.input(self.pass_score_input, content)

    # 输入学分
    def input_credit(self, content):
        return self.input(self.credit_input, content)

    # 点击下一步
    def click_next_btn(self):
        return self.click(self.next_btn)

    # 点击添加用户按钮
    def click_add_user_btn(self):
        return self.click(self.add_user_btn)

    # 点击选择用户复选框
    def click_select_user(self):
        return self.click(self.select_user)

    # 点击确定按钮
    def click_determine2_btn(self):
        return self.click(self.determine2_btn)

    # 点击保存并发布按钮
    def click_save_and_publish(self):
        return self.click(self.save_and_publish)





