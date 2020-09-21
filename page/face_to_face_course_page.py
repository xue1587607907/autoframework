from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 面授课程管理页面
class FaceToFaceCoursePage(BaseAction):

    # 面授课程管理按钮
    face_to_face_course_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[1]/ul/li[5]"

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
    disable_btn = By.XPATH, "/html/body/div[3]/div[1]/div[1]/ul/li[3]/span"

    # 新建课程按钮
    new_courses = By.CSS_SELECTOR, ".jw-table-buttons-contain > div:nth-child(1) > button:nth-child(1)"

    # 课程名称输入框
    courses_name_input = By.CSS_SELECTOR, "div.el-form-item:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 资源分类输入框
    resources_sort_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/form/div[2]/div/div/div/div/input"

    # 选择三级分类
    d1 = By.XPATH, "/html/body/div[2]/div[1]/div/div[1]/ul/li/span"
    d2 = By.XPATH, "/html/body/div[2]/div[1]/div[2]/div[1]/ul/li/span"
    d3 = By.XPATH, "/html/body/div[2]/div[1]/div[3]/div[1]/ul/li[1]/span"

    # 学分输入框
    credit_input = By.CSS_SELECTOR, "div.jw-el-form-item-inline:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > input:nth-child(1)"

    # 学时输入框
    class_hours = By.CSS_SELECTOR, "div.jw-offline-lesson-base-info-duration:nth-child(1) > div:nth-child(1) > div:nth-child(3) > input:nth-child(1)"

    # 保存并发布按钮
    save_and_publish = By.CSS_SELECTOR, "button.el-button--mini:nth-child(2)"

    # 课程名称按钮
    course_name_btn = By.CSS_SELECTOR, ".el-table__body-wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(1) > div:nth-child(1) > span:nth-child(1) > span:nth-child(1)"

    # 禁用按钮
    disable1_btn = By.CSS_SELECTOR, ".el-table__fixed-body-wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(8) > div:nth-child(1) > main:nth-child(1) > main:nth-child(1) > button:nth-child(2)"

    # 禁用/删除 弹窗的确定按钮
    determine_btn = By.CSS_SELECTOR, "button.el-button--default:nth-child(2)"

    # 删除按钮
    remove_btn = By.CSS_SELECTOR, ".el-table__fixed-body-wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(8) > div:nth-child(1) > main:nth-child(1) > main:nth-child(1) > button:nth-child(1)"

    # 向右翻页
    page_right = By.CSS_SELECTOR, "i.el-icon-arrow-right:nth-child(1)"

    # 向左翻页
    page_left = By.CSS_SELECTOR, ".el-icon-arrow-left"

    # 页数筛选框
    page_num_filter = By.CSS_SELECTOR, ".el-pagination__sizes > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 选择5条/页
    first_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 点击面授课程管理
    def click_face_to_face_course_btn(self):
        return self.click(self.face_to_face_course_btn)

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

    # 输入学分
    def input_credit(self, content):
        return self.input(self.credit_input, content)

    # 输入学时
    def input_class_hours(self, content):
        return self.input(self.class_hours, content)

    # 点击保存并发布
    def click_save_and_publish(self):
        return self.click(self.save_and_publish)

    # 点击课程名称
    def click_course_name_btn(self):
        return self.click(self.course_name_btn)

    # 清空课程名称输入框
    def clear_courses_name_input(self):
        return self.clear(self.courses_name_input)

    # 点击禁用
    def click_disable1_btn(self):
        return self.click(self.disable1_btn)

    # 禁用/删除弹窗的确定按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 删除课程
    def click_remove_btn(self):
        return self.click(self.remove_btn)

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




