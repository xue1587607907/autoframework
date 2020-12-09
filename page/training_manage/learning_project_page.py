from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 学习项目页面
class LearningProjectPage(BaseAction):

    # 培训管理按钮
    train_manage_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/ul/li[4]/span"

    # 培训组织按钮
    train_organization_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[2]/div/span[2]"

    # 学习项目按钮
    learn_project_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[2]/li/div/span[2]"

    # 关键字搜索框
    keyword_search = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[1]/main/div/div[1]/div/input"

    # 时间筛选框
    time_filter = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[1]/main/div/div[2]/div/div/input[1]"

    # 最近一周,最近一个月筛选按钮
    last_week_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/button[1]"
    last_month_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/button[2]"

    # 状态筛选框
    status_filter = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[1]/main/div/div[3]/div/div/div[1]/input"
    have_in_hand_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[4]/span"
    finished_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[3]/span"

    # 新建按钮
    new_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[1]/div/button/span"

    # 项目名称输入框
    project_name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/form/div/div[1]/div[2]/div/div/div[1]/input"

    # 项目分类输入框
    project_sort_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/form/div/div[3]/div[2]/div/div/div/div/input"

    # 选择三级分类
    d1 = By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/ul/li[1]/label/span[1]/span"
    d2 = By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/ul/li[2]/label/span[1]/span"
    d3 = By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[1]/ul/li/label/span[1]/span"

    # 空白区域
    blank_area = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/ul"

    # 开始时间输入框
    start_time_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/form/div/div[5]/div[2]/div/div/div[1]/div/span[1]/i"

    # 选择开始时间
    select_start_time = By.CSS_SELECTOR, "tr.el-date-table__row:nth-child(2) > td:nth-child(5) > div:nth-child(1) > span:nth-child(1)"

    # 结束时间输入框
    end_time_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/form/div/div[7]/div[2]/div/div/div[1]/div/span[1]/i"

    # 选择结束时间
    select_end_time = By.CSS_SELECTOR, "div.el-picker-panel:nth-child(6) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(1) > tr:nth-child(6) > td:nth-child(7) > div:nth-child(1) > span:nth-child(1)"

    # 下一步按钮
    next_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div/button[1]/span"

    # 新增阶段按钮
    new_stage_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[2]"

    # 阶段名称输入框
    stage_name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[3]/div/div[2]/div/div/form/div/div/div[1]/input"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[3]/div/div[3]/div/button[1]"

    # 面授课程按钮
    face_to_face_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div[2]/button[1]/span"

    # 课程名称输入框
    course_name = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[2]/div/div/div/div[1]/div[1]/form/div[1]/div/div[1]/div/input"

    # 选择课程
    select_course = By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span[1]/span"

    # 确定按钮
    determine1_btn = By.XPATH, "/html/body/div[2]/div/div[3]/div/button[1]/span"

    # 内容名称输入框
    content_name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[1]/div/div/div/div/div/input"

    # 开始时间输入框
    start_time_input1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[2]/div/div/div/div/div/input"

    # 选择开始时间
    select_start_time1 = By.XPATH, "/html/body/div[4]/div[1]/div/div[3]/table[1]/tbody/tr[5]/td[6]/div/span"

    # 点击确定按钮
    determine11_btn = By.XPATH, "/html/body/div[4]/div[2]/button[2]/span"
    determine12_btn = By.XPATH, "/html/body/div[3]/div[2]/button[2]/span"

    # 结束时间输入框
    end_time_input1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[2]/div/div/div/div[2]/form/div/div[2]/div[3]/div/div/div/div/div/input"

    # 选择结束时间
    select_end_time1 = By.XPATH, "/html/body/div[4]/div[1]/div/div[3]/table[1]/tbody/tr[5]/td[6]/div/span"

    # 确定按钮
    determine2_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[3]/div/button[1]"

    # 直播课程按钮
    live_course_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div[2]/button[2]"

    # 直播名称输入框
    live_name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[2]/div/div/main/div/div/div[2]/div/div/div[2]/div/form/div[1]/div/div/input"

    # 选择互动课程
    select_interaction_course = By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span[1]/span"

    # 点击确定按钮
    determine_btn15 = By.XPATH, "/html/body/div[2]/div/div[3]/div/div/button[1]/span"

    # 培训分类输入框
    train_sort_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[2]/div/div/main/div/div/div[2]/div/div/div[2]/div/form/div[2]/div/div/div[1]/input"

    # 选择培训分类
    select_train_sort = By.XPATH, "/html/body/div[4]/div[1]/div[1]/div[1]/ul/li[1]/label/span[1]/span"

    # 空白区域
    blank_area1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[1]"

    # 学分输入框
    credit_input1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[1]"

    # 学时输入框
    class_hour = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[2]/div/div/main/div/div/div[2]/div/div/div[2]/div/form/div[5]/div/div/div/input"

    # 授课讲师输入框
    lecturer_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[2]/div/div/main/div/div/div[2]/div/div/div[2]/div/form/div[6]/div/div/input"

    # 选择讲师
    select_lecturer = By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span[1]/span"

    # 确定按钮
    determine_btn12 = By.XPATH, "/html/body/div[4]/div/div[3]/div/div/button[1]/span"

    # 小节名称输入框
    section_name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[2]/div/div/main/div/div/div[2]/div/div/div[4]/form/div/div[2]/div[1]/div/div/div/div/div/input"

    # 直播日期输入框
    live_date_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[2]/div/div/main/div/div/div[2]/div/div/div[4]/form/div/div[2]/div[2]/div/div/div/div/div/span[1]/i"

    # 选择日期
    select_date = By.XPATH, "/html/body/div[6]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[5]/div/span"

    # 直播时间输入框
    live_time_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[2]/div/div/main/div/div/div[2]/div/div/div[4]/form/div/div[2]/div[3]/div/div/div/div/div/i[1]"

    # 选择直播时间
    select_live_time = By.XPATH, "/html/body/div[6]/div[1]/div[1]/div[2]/div/div[1]/div[1]/ul/li[16]"
    select_live_time1 = By.XPATH, "/html/body/div[6]/div[1]/div[2]/div[2]/div/div[1]/div[1]/ul/li[17]"

    # 弹窗的确定按钮
    determine_btn13 = By.XPATH, "/html/body/div[6]/div[2]/button[2]"

    # 外面的确定按钮
    determine_btn14 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[3]/div/button[1]/span"

    # 自定义直播按钮
    custom_live_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[2]/div/div/main/div/div/div[2]/div/div/div[1]/div[2]/label[2]/span[1]/span"

    # 视频课程按钮
    video_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div[2]/button[3]/span"

    # 课程名称输入框
    course_name1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[2]/div/div/div/div[1]/form/div[1]/div/div/div/input"

    # 选择课程
    select_course1 = By.XPATH, "/html/body/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span[1]/span"

    # 弹窗的确定按钮
    determine3_btn = By.XPATH, "/html/body/div[2]/div/div[3]/div/button[1]/span"

    # 外面的确定按钮
    determine4_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[3]/div/button[1]"

    # 添加考试按钮
    add_test_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[2]/div[1]/div[2]/button[4]/span"

    # 所用试卷输入框
    papers_used_input = By.CSS_SELECTOR, "div.jw-self-form-item:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 选择试卷
    select_paper = By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span[1]/span"

    # 确定按钮
    determine5_btn = By.XPATH, "/html/body/div[2]/div/div[3]/div/button[1]"

    # 考试名称输入框
    exam_name_input = By.CSS_SELECTOR, "div.jw-self-form-item:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 设置考试期限按钮
    radio_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[2]/div/div/div/form/div[4]/div/div/label/span[1]/span"

    # 开始日期输入框
    start_time_input2 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[2]/div/div/div/form/div[4]/div/div/div/div/div/i[1]"

    # 选择考试期限
    time1 = By.XPATH, "/html/body/div[4]/div[1]/div/div[2]/table/tbody/tr[5]/td[5]/div/span"
    time2 = By.XPATH, "/html/body/div[4]/div[1]/div/div[2]/table/tbody/tr[5]/td[7]/div/span"

    # 确定按钮
    determine6_btn = By.XPATH, "/html/body/div[4]/div[2]/button[2]/span"

    # 考试时长输入框
    exam_duration = By.CSS_SELECTOR, "div.el-form-item:nth-child(6) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 通过分数输入框
    pass_score_input = By.CSS_SELECTOR, "div.jw-el-form-item-inline:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 学分输入框
    credit_input = By.CSS_SELECTOR, "div.el-input-number:nth-child(4) > div:nth-child(1) > input:nth-child(1)"

    # 确定按钮
    determine7_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div/div[3]/div/button[1]"

    # 上移/下移
    move_up_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[2]/td[5]/div/main/div/span[3]"
    move_down_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[5]/div/main/div/span[3]"

    # 删除按钮
    remove_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[2]/td[5]/div/main/div/span[2]"

    # 确定按钮
    determine8_btn = By.XPATH, "/html/body/div[2]/div/div[3]/button[2]/span"

    # 研修设置框
    research_settings = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[2]/div[2]/div/div/div[3]/table/tbody/tr[2]/td[4]/div/div/div/div/div/input"

    # 选择选修
    select_elective = By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[2]"

    # 下一步按钮
    next1_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[6]/button[1]/span"

    # 添加用户按钮
    add_user_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[1]/div[2]/button[1]/span"

    # 选择用户复选框
    select_user = By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div[3]/div[2]/div/div/div[2]/table/thead/tr/th[1]/div/label/span/span"

    # 确定按钮
    determine9_btn = By.XPATH, "/html/body/div[3]/div/div[3]/div/button[1]/span"

    # 下一步按钮
    next2_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[4]/button[1]/span"

    # 选修任务输入框
    elective_input = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div[5]/div[2]/div[2]/form/div/div/div[1]/div/input"

    # 保存并发布按钮
    save_and_publish = By.CSS_SELECTOR, "button.el-button--primary:nth-child(2)"

    # 项目名称按钮
    project_name_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/span/span"

    # 页数选择框
    pagesize = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[2]/div[2]/div/div/span/div/div/input"

    # 选择5条/页
    first_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 点击培训管理按钮
    def click_train_manage_btn(self):
        return self.click(self.train_manage_btn)

    # 点击培训组织
    def click_train_organization_btn(self):
        return self.click(self.train_organization_btn)

    # 点击学习项目按钮
    def click_learn_project_btn(self):
        return self.click(self.learn_project_btn)

    # 输入项目名称进行搜索
    def input_keyword_search(self, content):
        return self.input(self.keyword_search, content)

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

    # 点击进行中
    def click_have_in_hand_btn(self):
        return self.click(self.have_in_hand_btn)

    # 点击已结束
    def click_finished_btn(self):
        return self.click(self.finished_btn)

    # 点击创建按钮
    def click_new_btn(self):
        return self.click(self.new_btn)

    # 输入项目名称
    def input_project_name(self, content):
        return self.input(self.project_name_input, content)

    # 点击项目分类输入框
    def click_project_sort_input(self):
        return self.click(self.project_sort_input)

    # 选择三级分类
    def select_third_sort(self):
        self.click(self.d1)
        self.click(self.d2)
        # self.click(self.d3)
        return self.click(self.blank_area)

    # 点击开始时间输入框
    def click_start_time_input(self):
        return self.click(self.start_time_input)

    # 选择开始时间
    def click_select_start_time(self):
        return self.click(self.select_start_time)

    # 点击结束时间输入框
    def click_end_time_input(self):
        return self.click(self.end_time_input)

    # 选择结束时间
    def click_select_end_time(self):
        return self.click(self.select_end_time)

    # 点击下一步
    def click_next_btn(self):
        return self.click(self.next_btn)

    # 点击新增阶段按钮
    def click_new_stage_btn(self):
        return self.click(self.new_stage_btn)

    # 输入阶段名称
    def input_stage_name(self, content):
        return self.input(self.stage_name_input, content)

    # 点击确定按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 点击面授课程
    def click_face_to_face_btn(self):
        return self.click(self.face_to_face_btn)

    # 点击课程名称
    def click_course_name(self):
        return self.click(self.course_name)

    # 选择课程
    def click_select_course(self):
        return self.click(self.select_course)

    # 点击确定按钮
    def click_determine1_btn(self):
        return self.click(self.determine1_btn)

    # 输入内容名称
    def input_content_name_input(self, content):
        return self.input(self.content_name_input, content)

    # 点击开始时间输入框
    def click_start_time_input1(self):
        return self.click(self.start_time_input1)

    # 选择开始时间
    def click_select_start_time1(self):
        return self.click(self.select_start_time1)

    # 点击确定
    def click_determine11_btn(self):
        return self.click(self.determine11_btn)

    # 点击结束时间输入框
    def click_end_time_input1(self):
        return self.click(self.end_time_input1)

    # 选择结束时间
    def click_select_end_time1(self):
        return self.click(self.select_end_time1)

    # 点击确定
    def click_determine12_btn(self):
        return self.click(self.determine12_btn)

    # 点击确定按钮
    def click_determine2_btn(self):
        return self.click(self.determine2_btn)

    # 点击直播课程按钮
    def click_live_course_btn(self):
        return self.click(self.live_course_btn)

    # 点击直播名称输入框
    def click_live_name_input(self):
        return self.click(self.live_name_input)

    # 选择互动课程
    def click_select_interaction_course(self):
        return self.click(self.select_interaction_course)

    # 点击确定
    def click_determine_btn15(self):
        return self.click(self.determine_btn15)

    # 点击培训分类输入框
    def click_train_sort_input(self):
        return self.click(self.train_sort_input)

    # 选择培训分类
    def click_select_train_sort(self):
        return self.click(self.select_train_sort)

    # 点击空白区域
    def click_blank_area1(self):
        return self.click(self.blank_area1)

    # 点击授课讲师输入框
    def click_lecturer_input(self):
        return self.click(self.lecturer_input)

    # 选择授课讲师
    def click_select_lecturer(self):
        return self.click(self.select_lecturer)

    # 点击确定按钮
    def click_determine_btn12(self):
        return self.click(self.determine_btn12)

    # 点击小节名称输入框
    def input_section_name(self, content):
        return self.input(self.section_name_input, content)

    # 点击直播日期输入框
    def click_live_date_input(self):
        return self.click(self.live_date_input)

    # 选择日期
    def click_select_date(self):
        return self.click(self.select_date)

    # 直播时间输入框
    def click_live_time_input(self):
        return self.click(self.live_time_input)

    # 选择直播时间
    def click_select_live_time(self):
        self.click(self.select_live_time)
        return self.click(self.select_live_time1)

    # 点击弹窗的确定按钮
    def click_determine_btn13(self):
        return self.click(self.determine_btn13)

    # 点击外面的确定按钮
    def click_determine_btn14(self):
        return self.click(self.determine_btn14)

    # 点击视频课程按钮
    def click_video_btn(self):
        return self.click(self.video_btn)

    # 点击课程名称输入框
    def click_course_name1(self):
        return self.click(self.course_name1)

    # 选择课程
    def click_select_course1(self):
        return self.click(self.select_course1)

    # 点击弹窗的确定按钮
    def click_determine3_btn(self):
        return self.click(self.determine3_btn)

    # 点击外面的确定按钮
    def click_determine4_btn(self):
        return self.click(self.determine4_btn)

    # 点击添加考试按钮
    def click_add_test_btn(self):
        return self.click(self.add_test_btn)

    # 点击所用试卷输入框
    def click_papers_used_input(self):
        return self.click(self.papers_used_input)

    # 选择试卷
    def click_select_paper(self):
        return self.click(self.select_paper)

    # 点击确定按钮
    def click_determine5_btn(self):
        return self.click(self.determine5_btn)

    # 输入考试名称
    def input_exam_name(self, content):
        return self.input(self.exam_name_input, content)

    # 点击设置考试期限按钮
    def click_radio_btn(self):
        return self.click(self.radio_btn)

    # 点击开始时间输入框
    def click_start_time_input2(self):
        return self.click(self.start_time_input2)

    # 选择开始/结束时间
    def select_start_and_end_time(self):
        self.click(self.time1)
        return self.click(self.time2)

    # 点击确定按钮
    def click_determine6_btn(self):
        return self.click(self.determine6_btn)

    # 输入考试时长
    def input_exam_duration(self, content):
        return self.input(self.exam_duration, content)

    # 输入通过分数
    def input_pass_score_input(self, content):
        return self.input(self.pass_score_input, content)

    # 输入学分
    def input_credit_input(self, content):
        return self.input(self.credit_input, content)

    # 点击确定按钮
    def click_determine7_btn(self):
        return self.click(self.determine7_btn)

    # 点击上下移动按钮
    def click_move_up_down(self):
        self.click(self.move_up_btn)
        return self.click(self.move_down_btn)

    # 点击删除按钮
    def click_remove_btn(self):
        return self.click(self.remove_btn)

    # 点击确定按钮
    def click_determine8_btn(self):
        return self.click(self.determine8_btn)

    # 点击研修设置框
    def click_research_settings(self):
        return self.click(self.research_settings)

    # 选择选修
    def click_select_elective(self):
        return self.click(self.select_elective)

    # 点击下一步按钮
    def click_next1_btn(self):
        return self.click(self.next1_btn)

    # 点击添加用户按钮
    def click_add_user_btn(self):
        return self.click(self.add_user_btn)

    # 选择用户复选框
    def click_select_user(self):
        return self.click(self.select_user)

    # 点击确定按钮
    def click_determine9_btn(self):
        return self.click(self.determine9_btn)

    # 点击下一步按钮
    def click_next2_btn(self):
        return self.click(self.next2_btn)

    # 输入选修任务数量
    def input_elective(self, content):
        return self.input(self.elective_input, content)

    # 点击保存并发布
    def click_save_and_publish(self):
        return self.click(self.save_and_publish)

    # 点击项目名称输入框
    def click_project_name_btn(self):
        return self.click(self.project_name_btn)

    # 清空项目名称
    def clear_project_name_input(self):
        return self.clear(self.project_name_input)

    # 保存按钮
    determine = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[2]/div/button[2]"

    # 点击保存
    def click_determine(self):
        return self.click(self.determine)

    # 点击页面大小筛选框
    def click_pagesize(self):
        return self.click(self.pagesize)

    # 点击选择5条/页
    def click_first_btn(self):
        return self.click(self.first_btn)

