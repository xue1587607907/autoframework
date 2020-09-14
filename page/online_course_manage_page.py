from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 在线课程管理页面
class OnlineCourseManagePage(BaseAction):

    # 在线课程管理
    online_course_manage_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[4]"

    # 课程名称搜索框
    course_name_search = By.CSS_SELECTOR, "div.jw-inline-block:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 时间筛选框
    time_filter = By.CSS_SELECTOR, "input.el-range-input:nth-child(2)"

    # 最近一周,最近一个月筛选按钮
    last_week_btn = By.CSS_SELECTOR, "button.el-picker-panel__shortcut:nth-child(1)"
    last_month_btn = By.CSS_SELECTOR, "button.el-picker-panel__shortcut:nth-child(2)"

    # 状态筛选框
    status_filter = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[1]/main/div/div[3]/div/div/div/input"
    enable_btn = By.CSS_SELECTOR, "div.el-select-dropdown:nth-child(4) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2)"
    disable_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[3]"

    # 新建课程按钮
    new_courses = By.CSS_SELECTOR, ".jw-table-buttons-contain > div:nth-child(1) > button:nth-child(1)"

    # 课程名称输入框
    courses_name_input = By.CSS_SELECTOR, "div.el-form-item:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 资源分类输入框
    resources_sort_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[1]/div/div/form/div[2]/div/div/div/div/input"

    # 选择三级分类
    d1 = By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/ul/li[2]/span"
    d2 = By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/ul/li[1]/span"
    d3 = By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[1]/ul/li[2]/span"

    # 课程封面按钮
    courses_cover_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[1]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/i"

    # 下一步按钮
    next_btn = By.CSS_SELECTOR, "#pane-first > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > button:nth-child(1)"

    # 新增一节按钮
    add_section = By.CSS_SELECTOR, ".jw-add-stage"

    # 小节名称输入框
    section_name_input = By.CSS_SELECTOR, ".el-input--mini > input:nth-child(1)"

    # 确定按钮
    determine1_btn = By.CSS_SELECTOR, ".jw-com-default-content > div:nth-child(4) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)"

    # 添加学习内容按钮
    add_learn_content_btn = By.CSS_SELECTOR, "span.jw-flex-all-center > span:nth-child(2)"

    # 内容类型输入框
    content_type = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[2]/div/div/div[6]/div/div[2]/div/div/form/div[1]/div/div/div/div[1]/input"

    # 视频按钮
    video_btn = By.CSS_SELECTOR, "li.el-select-dropdown__item:nth-child(1)"

    # 学习资料按钮
    learn_data_btn = By.CSS_SELECTOR, "li.el-select-dropdown__item:nth-child(2)"

    # 选择视频按钮
    select_video_btn = By.CSS_SELECTOR, ".el-button--small"

    # 选择资料按钮
    select_data_btn = By.CSS_SELECTOR, ".el-button--small > span:nth-child(1)"

    # 勾选弹窗的资料
    check_data_btn = By.CSS_SELECTOR, "tr.el-table__row:nth-child(2) > td:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(1) > span:nth-child(1)"

    # 勾选弹窗的视频
    check_video_btn = By.CSS_SELECTOR, "tr.el-table__row:nth-child(1) > td:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(1) > span:nth-child(1)"

    # 内容名称输入框
    content_name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[2]/div/div/div[6]/div/div[2]/div/div/form/div[3]/div/div[1]/div/input"

    # 选择视频弹窗的确定按钮
    determine2_btn = By.XPATH, "/html/body/div[4]/div/div[3]/div/button[2]"

    # 新增内容的确定按钮
    determine3_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[2]/div/div/div[6]/div/div[3]/div/div/button[2]"

    # 发布按钮
    release_btn = By.CSS_SELECTOR, "div.jw-flex-all-center:nth-child(4) > button:nth-child(1)"

    # 课程名称按钮
    courses_name_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[2]/div[1]/div/div/div[3]/table/tbody/tr[1]/td[2]/div/span/span"

    # 禁用按钮
    disable1_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/main/main/button[2]"

    # 禁用弹窗的确定按钮
    determine5_btn = By.CSS_SELECTOR, "html body.el-popup-parent--hidden div.el-message-box__wrapper div.el-message-box div.el-message-box__btns button.el-button.el-button--default.el-button--small.el-button--primary"

    # "删除"课程按钮
    remove2_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/table/tbody/tr[1]/td[9]/div/main/main/button[1]"

    # 删除弹窗的确定按钮
    determine6_btn = By.XPATH, "/html/body/div[3]/div/div[3]/button[2]"

    # 课程目录按钮
    courses_content_btn = By.CSS_SELECTOR, "#tab-second > span:nth-child(1)"

    # 上移按钮
    move_up_btn = By.CSS_SELECTOR, ".icon-Move-up"

    # 下移按钮
    move_down_btn = By.CSS_SELECTOR, ".icon-Move-down-copy"

    # 编辑按钮
    edit_btn = By.CSS_SELECTOR, "div.jw-table-row:nth-child(3) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)"

    # 课程小节删除按钮
    remove1_btn = By.CSS_SELECTOR, "div.jw-table-row:nth-child(3) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2)"

    # 删除课程小节弹窗的"确定"按钮
    determine4_btn = By.XPATH, "/html/body/div[2]/div/div[3]/button[2]"

    # 返回按钮
    go_back_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[2]/div[2]/div/div/div[4]/button"

    # 向右翻页
    page_right = By.CSS_SELECTOR, "i.el-icon-arrow-right:nth-child(1)"

    # 向左翻页
    page_left = By.CSS_SELECTOR, ".el-icon-arrow-left"

    # 页数筛选框
    page_num_filter = By.CSS_SELECTOR, ".el-pagination__sizes > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 选择5条/页
    first_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 点击在线课程管理
    def click_online_course_manage_btn(self):
        return self.click(self.online_course_manage_btn)

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
    def click_new_courses(self):
        return self.click(self.new_courses)

    # 点击课程名称
    def click_courses_name_input(self):
        return self.click(self.courses_name_input)

    # 输入课程名称
    def input_courses_name1(self, content):
        return self.input(self.courses_name_input, content)

    # 点击资源分类
    def click_resources_sort_input(self):
        return self.click(self.resources_sort_input)

    # 选择三级分类
    def select_courses_sort(self):
        self.click(self.d1)
        self.click(self.d2)
        return self.click(self.d3)

    # 点击课程封面按钮
    def click_courses_cover_btn(self):
        return self.click(self.courses_cover_btn)

    # 点击下一步
    def click_next_btn(self):
        return self.click(self.next_btn)

    # 点击新增一节
    def click_add_section(self):
        return self.click(self.add_section)

    # 点击小节名称
    def click_section_name_input(self):
        return self.click(self.section_name_input)

    # 输入小节内容
    def input_section_name(self, content):
        return self.input(self.section_name_input, content)

    # 点击确定按钮
    def click_determine1_btn(self):
        return self.click(self.determine1_btn)

    # 点击添加学习内容
    def click_add_learn_content_btn(self):
        return self.click(self.add_learn_content_btn)

    # 点击内容类型输入框
    def click_content_type(self):
        return self.click(self.content_type)

    # 点击视频按钮
    def click_video_btn(self):
        return self.click(self.video_btn)

    # 点击选择视频
    def click_select_video_btn(self):
        return self.click(self.select_video_btn)

    # 勾选弹窗的视频
    def click_check_video_btn(self):
        return self.click(self.check_video_btn)

    # 点击弹窗的确定按钮
    def click_determine2_btn(self):
        return self.click(self.determine2_btn)

    # 点击新增内容的确定按钮
    def click_determine3_btn(self):
        return self.click(self.determine3_btn)

    # 点击学习资料按钮
    def click_learn_data_btn(self):
        return self.click(self.learn_data_btn)

    # 点击选择资料按钮
    def click_select_data_btn(self):
        return self.click(self.select_data_btn)

    # 勾选弹窗的资料
    def click_check_data_btn(self):
        return self.click(self.check_data_btn)

    # 点击内容名称输入框
    def click_content_name_input(self):
        return self.click(self.content_name_input)

    # 在内容名称输入框输入内容
    def input_content_name(self, content):
        return self.input(self.content_name_input, content)

    # 点击发布按钮
    def click_release_btn(self):
        return self.click(self.release_btn)

    # 点击课程名称进入编辑
    def click_courses_name_btn(self):
        return self.click(self.courses_name_btn)

    # 点击课程目录
    def click_courses_content_btn(self):
        return self.click(self.courses_content_btn)

    # 点击上移
    def click_move_up(self):
        return self.click(self.move_up_btn)

    # 点击下移
    def click_move_down(self):
        return self.click(self.move_down_btn)

    # 点击编辑
    def click_edit_btn(self):
        return self.click(self.edit_btn)

    # 点击删除课程小节
    def click_remove1_btn(self):
        return self.click(self.remove1_btn)

    # 点击确定
    def click_determine4_btn(self):
        return self.click(self.determine4_btn)

    # 点击返回按钮
    def click_go_back_btn(self):
        return self.click(self.go_back_btn)

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

    # 点击禁用按钮
    def click_disable1_btn(self):
        return self.click(self.disable1_btn)

    # 点击确定按钮
    def click_determine5_btn(self):
        return self.click(self.determine5_btn)

    # 点击删除该课程
    def click_remove2_btn(self):
        return self.click(self.remove2_btn)






























