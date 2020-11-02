from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 培训管理->岗位学习页面
class PostLearningPage(BaseAction):

    # 岗位学习按钮
    post_learning_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[6]/span[2]"

    # 岗位名称搜索框
    post_name_search_input = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[1]/main/div/div[1]/div/input"

    # 状态筛选框
    status_filter = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[1]/main/div/div[2]/div/div/div[1]/input"

    # 已发布
    published = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]/span"

    # 未发布
    unpublished = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 新建岗位学习方案按钮
    new_post_learning_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div[1]/button/span"

    # 岗位分类输入框
    post_sort_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div[2]/div/div[2]/div/form/div[1]/div/div[2]/div/div[1]/input"

    # 选择岗位分类
    select_post_sort = By.XPATH, "/html/body/div[4]/div[1]/div/div[1]/ul/li[1]/label/span[1]/span"

    # 空白区域
    blank_area = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div[2]/div/div[1]"

    # 岗位名称选择框
    post_name_select = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div[2]/div/div[2]/div/form/div[2]/div/div[2]/div[1]/input"

    # 选择岗位
    select_post = By.XPATH, "/html/body/div[5]/div[1]/div[1]/ul/li[1]"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div/div[2]/div[1]/div[2]/div/div[3]/div/button[1]/span"

    # 添加阶段按钮
    add_phase_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/span[2]"

    # 阶段名称输入框
    phase_name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[5]/div/div[2]/form/div/div/div[1]/input"

    # 确定按钮
    determine1_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[5]/div/div[3]/div/button[1]"

    # 视频课程按钮
    video_course = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[1]/caption/div/span[2]/button[1]/span"

    # 选择视频
    select_video = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[6]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span[1]/span"

    # 确定按钮
    determine2_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[6]/div/div[3]/div/button[1]"

    # 面授课程按钮
    interaction_course_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[1]/caption/div/span[2]/button[2]/span"

    # 选择面授课程
    select_interaction_course = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[6]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span[1]/span"

    # 确定按钮
    determine3_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[6]/div/div[3]/div/button[1]/span"

    # 考试按钮
    exam_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[1]/caption/div/span[2]/button[3]/span"

    # 所用试卷输入框
    user_paper_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[6]/div/div[2]/div/div/div/form/div[1]/div/div/div/input"

    # 选择试卷
    select_paper = By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span[1]/span"

    # 确定按钮
    determine4_btn = By.XPATH, "/html/body/div[2]/div/div[3]/div/button[1]/span"

    # 考试名称输入框
    exam_name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[6]/div/div[2]/div/div/div/form/div[2]/div/div[1]/div/input"

    # 考试时长输入框
    exam_duration_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[6]/div/div[2]/div/div/div/form/div[4]/div/div[1]/div/div/input"

    # 通过分数输入框
    pass_score_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[6]/div/div[2]/div/div/div/form/div[6]/div/div/div[1]/div/div[1]/div/input"

    # 确定按钮
    determine5_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[6]/div/div[3]/div/button[1]"

    # 上移按钮
    move_up_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[1]/div[3]/div[3]/div/span[3]"

    # 下移按钮
    move_down_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[1]/div[2]/div[3]/div/span[3]"

    # 删除按钮
    delete_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[1]/div[4]/div[3]/div/span[2]"

    # 确定按钮
    determine6_btn = By.XPATH, "/html/body/div[2]/div/div[3]/button[2]"

    # 研修设置
    train_set = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[1]/div[3]/div[2]/div/div/div/input"

    # 选修按钮
    elective = By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[2]"

    # 通关任务输入框
    customs_clearance_task_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[2]/form/div/div/div/div/input"

    # 保存并发布按钮
    save_and_publish = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[4]/button[2]"

    # 点击岗位学习按钮
    def click_post_learning_btn(self):
        return self.click(self.post_learning_btn)

    # 输入岗位名称
    def input_post_name(self, content):
        return self.input(self.post_name_search_input, content)

    # 点击状态筛选框
    def click_status_filter(self):
        return self.click(self.status_filter)

    # 选择已发布
    def select_published(self):
        return self.click(self.published)

    # 选择未发布
    def select_unpublished(self):
        return self.click(self.unpublished)

    # 点击新建岗位学习方案
    def click_new_post_learning_btn(self):
        return self.click(self.new_post_learning_btn)

    # 点击岗位分类输入框
    def click_post_sort_input(self):
        return self.click(self.post_sort_input)

    # 选择岗位分类
    def click_select_post_sort(self):
        return self.click(self.select_post_sort)

    # 点击空白区域
    def click_blank_area(self):
        return self.click(self.blank_area)

    # 点击岗位名称选择框
    def click_post_name_select(self):
        return self.click(self.post_name_select)

    # 选择岗位
    def click_select_post(self):
        return self.click(self.select_post)

    # 点击确定按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 点击添加阶段
    def click_add_phase_btn(self):
        return self.click(self.add_phase_btn)

    # 输入阶段名称
    def input_phase_name_input(self, content):
        return self.input(self.phase_name_input, content)

    # 点击确定按钮
    def click_determine1_btn(self):
        return self.click(self.determine1_btn)

    # 点击视频课程
    def click_video_course(self):
        return self.click(self.video_course)

    # 选择视频
    def click_select_video(self):
        return self.click(self.select_video)

    # 点击确定按钮
    def click_determine2_btn(self):
        return self.click(self.determine2_btn)

    # 点击互动课程
    def click_interaction_course_btn(self):
        return self.click(self.interaction_course_btn)

    # 选择互动课程
    def click_select_interaction_course(self):
        return self.click(self.select_interaction_course)

    # 点击确定按钮
    def click_determine3_btn(self):
        return self.click(self.determine3_btn)

    # 点击考试按钮
    def click_exam_btn(self):
        return self.click(self.exam_btn)

    # 点击所用试卷输入框
    def click_user_paper_input(self):
        return self.click(self.user_paper_input)

    # 选择试卷
    def click_select_paper(self):
        return self.click(self.select_paper)

    # 点击确定按钮
    def click_determine4_btn(self):
        return self.click(self.determine4_btn)

    # 输入考试名称
    def input_exam_name(self, content):
        return self.input(self.exam_name_input, content)

    # 输入考试时长
    def input_exam_duration(self, content):
        return self.input(self.exam_duration_input, content)

    # 输入通过分数
    def input_pass_score(self, content):
        return self.input(self.pass_score_input, content)

    # 点击确定按钮
    def click_determine5_btn(self):
        return self.click(self.determine5_btn)

    # 点击上移按钮
    def click_move_up_btn(self):
        return self.click(self.move_up_btn)

    # 点击下移按钮
    def click_move_down_btn(self):
        return self.click(self.move_down_btn)

    # 点击删除按钮
    def click_delete_btn(self):
        return self.click(self.delete_btn)

    # 点击确定按钮
    def click_determine6_btn(self):
        return self.click(self.determine6_btn)

    # 点击研修设置
    def click_train_set(self):
        return self.click(self.train_set)

    # 点击选修
    def click_elective(self):
        return self.click(self.elective)

    # 输入通关数
    def input_customs_clearance_task(self, content):
        return self.input(self.customs_clearance_task_input, content)

    # 点击保存并发布
    def click_save_and_publish(self):
        return self.click(self.save_and_publish)





