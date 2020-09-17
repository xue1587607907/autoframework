from selenium.webdriver.common.by import By
from base.base_action import BaseAction


# 学习资源管理页面
class StudyResourcesManagePage(BaseAction):

    # 资源管理按钮
    resources_btn = By.XPATH, "/html/body/div/div/div[3]/div[2]/ul/li[2]/span"

    # 学习资源管理按钮
    study_resources_manage_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[1]/ul/li[3]"

    # 资源名称输入框
    resources_name_search = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[1]/div[1]/main/div/div[1]/div/input"

    # 状态筛选框
    status_filter = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[1]/div[1]/main/div/div[2]/div/div/div/input"

    # 状态下的转码成功按钮
    transcoding_successful = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]"

    # 状态下的转码失败按钮
    transcoding_fail = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[3]"

    # 编辑按钮
    edit_btn = By.CSS_SELECTOR, "tr.el-table__row:nth-child(1) > td:nth-child(6) > div:nth-child(1) > main:nth-child(1) > span:nth-child(1)"

    # 资源分类选择框
    resources_sort_select = By.CSS_SELECTOR, ".el-cascader > div:nth-child(1) > input:nth-child(1)"

    d1 = By.XPATH, "/html/body/div[3]/div[1]/div[1]/div[1]/ul/li[1]/span"
    d2 = By.XPATH, "/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[1]/span"
    d3 = By.XPATH, "/html/body/div[3]/div[1]/div[3]/div[1]/ul/li[1]/span"

    # 资源名称按钮
    resources_sort_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div/div[1]/main/div/div[4]/div/div[2]/div[2]/form/div[2]/div[1]/div/div/span"

    # 编辑资源名称输入框
    edit_resources_name_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div/div[1]/main/div/div[4]/div/div[2]/div[2]/form/div[2]/div[1]/div/div/p/div/input"

    # 确定按钮
    determine_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div/div[1]/main/div/div[4]/div/div[3]/div/button[1]"

    # 删除按钮
    remove_btn = By.CSS_SELECTOR, "tr.el-table__row:nth-child(1) > td:nth-child(6) > div:nth-child(1) > main:nth-child(1) > span:nth-child(2)"

    # 弹窗的确定按钮
    determine1_btn = By.CSS_SELECTOR, "button.el-button:nth-child(2)"

    # 向右翻页---------------------------------------------------------------------------
    page_right = By.CSS_SELECTOR, "i.el-icon-arrow-right:nth-child(1)"

    # 向左翻页
    page_left = By.CSS_SELECTOR, ".el-icon-arrow-left"

    # 点击数字翻页
    num_btn_page = By.CSS_SELECTOR, "li.number:nth-child(3)"

    # 选择页面数量筛选框
    select_page_size = By.CSS_SELECTOR, ".el-pagination__sizes > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 翻页区域
    turn_the_page_area = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul"

    # 5条/每页按钮---------------------------------------------------------------------------
    third_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"
    # third_btn = By.CSS_SELECTOR, ".hover > span:nth-child(1)"

    # 资料库页面元素和操作方法
    # 课程资料库按钮
    database_btn = By.CSS_SELECTOR, "#tab-courseLib > span:nth-child(1)"

    # 类型筛选框---------------------------------------------------------------------------
    type_filter = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[2]/div[1]/div[1]/main/div[2]/div/div/div/input"

    # 选择类型
    first_type_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]"
    second_type_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[4]"

    # 上传时间筛选框
    time_filter = By.CSS_SELECTOR, "input.el-range-input:nth-child(2)"
    # time_filter = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[2]/div[1]/div[1]/main/div[3]/div/div/input[1]"

    # 通过上传时间筛选
    first_time_filter = By.CSS_SELECTOR, "button.el-picker-panel__shortcut:nth-child(1)"
    second_time_filter = By.CSS_SELECTOR, "button.el-picker-panel__shortcut:nth-child(2)"

    # 状态筛选
    # status_btn = By.CSS_SELECTOR, ".is-focus > input:nth-child(1)"
    status_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[2]/div[1]/div[1]/main/div[4]/div/div/div/input"

    # 选择启用
    enable_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"
    # enable_btn = By.CSS_SELECTOR, "div.el-select-dropdown:nth-child(4) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1)"

    # 选择禁用---------------------------------------------------------------------------
    disable_btn = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]/span"
    # disable_btn = By.CSS_SELECTOR, "div.el-select-dropdown:nth-child(4) > div:nth-child(1) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(2)"

    # "更多"按钮
    more_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[4]/div[2]/table/tbody/tr[1]/td[7]/div/main/div/button"
    # more_btn = By.CSS_SELECTOR, ".el-table__fixed-body-wrapper > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(7) > div:nth-child(1) > main:nth-child(1) > div:nth-child(1) > button:nth-child(1)"

    # 关联课程按钮
    related_courses = By.XPATH, "/html/body/ul/li[1]"

    # 课程复选框
    cources_check_box = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/div/div[2]/div[1]/label/span[2]"

    # 课程复选框的"确定"按钮
    cources_check_box_determine = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[2]/div[2]/div/div[3]/div/button[1]"

    # 下载按钮
    download_btn = By.XPATH, "/html/body/ul/li[2]"

    # 删除按钮
    more_remove_btn = By.XPATH, "/html/body/ul/li[3]"

    # 点击删除弹窗的确定按钮
    determine2_btn = By.XPATH, "/html/body/div[3]/div/div[3]/button[2]"

    # 启用(禁用)按钮
    more_enable_btn = By.XPATH, "/html/body/ul/li[4]"

    # 点击资源管理
    def click_resources_manage(self):
        return self.click(self.resources_btn)

    # 点击学习资源管理
    def click_study_resources_manage(self):
        return self.click(self.study_resources_manage_btn)

    # 点击搜索框
    def click_search(self):
        return self.click(self.resources_name_search)

    # 在搜索框输入内容
    def input_search_content(self, content):
        return self.input(self.resources_name_search, content)

    # 点击状态筛选框
    def click_status_filter1(self):
        return self.click(self.status_filter)

    # 点击转码成功
    def click_transcoding_successful(self):
        return self.click(self.transcoding_successful)

    # 点击转码失败
    def click_transcoding_fail(self):
        return self.click(self.transcoding_fail)

    # 点击编辑按钮
    def click_edit_btn(self):
        return self.click(self.edit_btn)

    # 点击资源分类选择框
    def click_resources_sort_select(self):
        return self.click(self.resources_sort_select)

    # 选择三级分类
    def select_third_sort(self):
        self.click(self.d1)
        self.click(self.d2)
        return self.click(self.d3)

    # 点击资源名称按钮
    def click_resources_sort_btn(self):
        return self.click(self.resources_sort_btn)

    # 弹窗下的资源名称输入框
    def click_resources_name_input(self):
        return self.click_resources_name_input()

    # 点击"确定"按钮
    def click_determine_btn(self):
        return self.click(self.determine_btn)

    # 点击删除按钮
    def click_remove_btn(self):
        return self.click(self.remove_btn)

    # 点击确定按钮
    def click_determine1_btn(self):
        return self.click(self.determine1_btn)

    # 点击向左翻页
    def click_page_right(self):
        return self.click(self.page_right)

    # 点击向左翻页
    def click_page_left(self):
        return self.click(self.page_left)

    # 点击数字翻页
    def click_num_btn_page(self):
        return self.click(self.num_btn_page)

    # 点击页数筛选框
    def click_page_size(self):
        return self.click(self.select_page_size)

    # 点击5条/页按钮
    def click_third_btn(self):
        return self.click(self.third_btn)

    # 点击资料库
    def click_database_btn(self):
        return self.click(self.database_btn)

    # 点击类型筛选框
    def click_type_filter(self):
        return self.click(self.type_filter)

    # 选择第一个类型
    def click_first_type_btn(self):
        return self.click(self.first_type_btn)

    # 选择第二个类型
    def click_second_type_btn(self):
        return self.click(self.second_type_btn)

    # 点击上传时间输入框
    def click_time_filter(self):
        return self.click(self.time_filter)

    # 点击第一个按钮
    def click_first_time_filter(self):
        return self.click(self.first_time_filter)

    # 点击第二个按钮
    def click_second_time_filter(self):
        return self.click(self.second_time_filter)

    # 点击状态筛选
    def click_status_filter2(self):
        return self.click(self.status_btn)

    # 点击启用
    def click_enable_btn(self):
        return self.click(self.enable_btn)

    # 点击禁用
    def click_disable_btn(self):
        return self.click(self.disable_btn)

    # 点击"更多"按钮
    def click_more_btn(self):
        return self.click(self.more_btn)

    # 点击关联课程
    def click_related_courses(self):
        return self.click(self.related_courses)

    # 选择关联课程
    def select_related_courses(self):
        return self.click(self.cources_check_box)

    # 点击确定按钮
    def click_related_courses_determine(self):
        return self.click(self.cources_check_box_determine)

    # 点击下载
    def click_download_btn(self):
        return self.click(self.download_btn)

    # 点击删除
    def click_more_remove_btn(self):
        return self.click(self.more_remove_btn)

    # 点击确定
    def click_determine2_btn(self):
        return self.click(self.determine2_btn)

    # 点击启用/禁用
    def click_more_enable(self):
        return self.click(self.more_enable_btn)










