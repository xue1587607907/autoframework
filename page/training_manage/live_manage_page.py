from selenium.webdriver.common.by import By

from base.base_action import BaseAction


# 直播管理页面
class LiveManagePage(BaseAction):

    # 直播管理按钮
    live_manage_btn = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[1]/ul/li[5]/div/span[2]"

    # 直播名称搜索框
    live_name_search = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[1]/main/div/div[1]/div/input"

    # 直播类型筛选框
    live_type_filter = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[1]/main/div/div[2]/div/div/div[1]/input"

    # 选择课程直播
    select_course_live = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 选择自定义直播
    select_custom_live = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]/span"

    # 组织形式筛选框
    organizational_form = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[1]/main/div/div[3]/div/div/div[1]/input"

    # 选择直接发起
    select_direct_initiation = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 选择间接发起
    select_indirect_initiation = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[2]/span"

    # 状态筛选框
    status_filter = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[1]/main/div/div[4]/div/div/div[1]/input"

    # 选择未发布
    select_unpublished = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span"

    # 选择已结束
    select_end = By.XPATH, "/html/body/div[2]/div[1]/div[1]/ul/li[4]/span"

    # 新建直播按钮
    add_live_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[1]/div/button/span"

    # 直播名称输入框
    live_name_input = By.CSS_SELECTOR, "#pane-setting_liveBroadcast > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > input:nth-child(1)"

    # 选择互动课程
    select_interaction_course = By.CSS_SELECTOR, "tr.el-table__row:nth-child(1) > td:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(1) > span:nth-child(1)"

    # 点击确定
    determine_btn1 = By.CSS_SELECTOR, "div.el-dialog__footer:nth-child(3) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1) > span:nth-child(1)"

    # 培训分类输入框
    train_sort_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div/div/div[2]/div/form/div[2]/div/div/div[1]/input"

    # 选择培训分类
    select_train_sort = By.XPATH, "/html/body/div[3]/div[1]/div[1]/div[1]/ul/li[1]/label/span[1]/span"

    # 选择空白区域
    select_blank_area = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[1]/div/div"

    # 授课讲师输入框
    lecturer_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div/div/div[2]/div/form/div[6]/div/div[1]/input"

    # 选择授课讲师
    select_lecturer = By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span[1]/span"

    # 确定按钮
    determine_btn2 = By.XPATH, "/html/body/div[4]/div/div[3]/div/div/button[1]"

    # 小节名称输入框
    section_name_input = By.CSS_SELECTOR, "div.jw-table-row:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)"

    # 直播日期输入框
    live_date_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div/div/div[4]/form/div/div[2]/div[2]/div/div/div/div/div/span[1]/i"

    # 点击下一个月,选择日期
    next_month_btn = By.XPATH, "/html/body/div[5]/div[1]/div/div[1]/button[4]"
    select_date = By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[2]/div/span"

    # 直播时间输入框
    live_time_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div/div/div[4]/form/div/div[2]/div[3]/div/div/div/div/div/i[1]"

    # 选择直播时间
    select_live_time = By.XPATH, "/html/body/div[5]/div[1]/div[1]/div[2]/div/div[1]/div[1]/ul/li[18]"
    select_live_time1 = By.XPATH, "/html/body/div[5]/div[1]/div[2]/div[2]/div/div[1]/div[1]/ul/li[19]"

    # 弹窗的确定按钮
    determine_btn3 = By.XPATH, "/html/body/div[5]/div[2]/button[2]"

    # 下一步按钮
    next_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div/div/div[5]/button[1]/span"

    # 添加用户按钮
    add_user_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div[2]/div/div[1]/div[2]/button[1]"

    # 全选按钮
    select_all = By.XPATH, "/html/body/div[5]/div/div[2]/div/div/div[3]/div[2]/div/div/div[2]/table/thead/tr/th[1]/div/label/span/span"

    # 确定按钮
    determine_btn4 = By.XPATH, "/html/body/div[5]/div/div[3]/div/button[1]/span"

    # 发布按钮
    publish_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div[2]/div/div[4]/button[1]/span"

    # 管理按钮
    manage_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div/div[2]/div[1]/div/button/span"

    # 删除按钮
    remove_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div/div[1]/div[2]/button[2]/span"

    # 确定按钮
    determine_btn5 = By.XPATH, "/html/body/div[2]/div/div[3]/button[2]/span"

    # 自定义直播按钮
    custom_live_btn = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div/div/div[1]/div[2]/label[2]/span[1]/span"

    # 学分输入框
    credit_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div/div/div[3]/div/form/div[4]/div/div/div/input"

    # 学时输入框
    class_hour = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div/div/div[3]/div/form/div[5]/div/div/div/input"

    # 点击直播管理
    def click_live_manage_btn(self):
        return self.click(self.live_manage_btn)

    # 输入直播名称
    def input_live_name_search(self, content):
        return self.input(self.live_name_search, content)

    # 点击直播类型筛选框
    def click_live_type_filter(self):
        return self.click(self.live_type_filter)

    # 选择直播课程
    def click_select_course_live(self):
        return self.click(self.select_course_live)

    # 选择自定义直播
    def click_select_custom_live(self):
        return self.click(self.select_custom_live)

    # 点击组织形式筛选框
    def click_organizational_form(self):
        return self.click(self.organizational_form)

    # 选择直接发起
    def click_select_direct_initiation(self):
        return self.click(self.select_direct_initiation)

    # 选择间接发起
    def click_select_indirect_initiation(self):
        return self.click(self.select_indirect_initiation)

    # 点击状态筛选框
    def click_status_filter(self):
        return self.click(self.status_filter)

    # 选择未发布
    def click_select_unpublished(self):
        return self.click(self.select_unpublished)

    # 选择已结束
    def click_select_end(self):
        return self.click(self.select_end)

    # 点击新建直播按钮
    def click_add_live_btn(self):
        return self.click(self.add_live_btn)

    # 点击直播名称输入框
    def click_live_name_input(self):
        return self.click(self.live_name_input)

    # 选择互动课程
    def click_select_interaction_course(self):
        return self.click(self.select_interaction_course)

    # 点击确定按钮
    def click_determine_btn1(self):
        return self.click(self.determine_btn1)

    # 点击培训分类输入框
    def click_train_sort_input(self):
        return self.click(self.train_sort_input)

    # 选择培训分类
    def click_select_train_sort(self):
        return self.click(self.select_train_sort)

    # 点击空白区域
    def click_select_blank_area(self):
        return self.click(self.select_blank_area)

    # 点击授课讲师输入框
    def click_lecturer_input(self):
        return self.click(self.lecturer_input)

    # 选择授课讲师
    def click_select_lecturer(self):
        return self.click(self.select_lecturer)

    # 点击确定按钮
    def click_determine_btn2(self):
        return self.click(self.determine_btn2)

    # 输入小节名称
    def input_section_name(self, content):
        return self.input(self.section_name_input, content)

    # 点击直播日期输入框
    def click_live_date_input(self):
        return self.click(self.live_date_input)

    # 点击选择日期
    def click_select_date(self):
        self.click(self.next_month_btn)
        return self.click(self.select_date)

    # 点击直播时间输入框
    def click_live_time_input(self):
        return self.click(self.live_time_input)

    # 选择直播时间
    def click_select_live_time(self):
        self.click(self.select_live_time)
        return self.click(self.select_live_time1)

    # 点击弹窗的确定按钮
    def click_determine_btn3(self):
        return self.click(self.determine_btn3)

    # 点击下一步
    def click_next_btn(self):
        return self.click(self.next_btn)

    # 点击添加用户按钮
    def click_add_user_btn(self):
        return self.click(self.add_user_btn)

    # 点击全选
    def click_select_all(self):
        return self.click(self.select_all)

    # 点击确定按钮
    def click_determine_btn4(self):
        return self.click(self.determine_btn4)

    # 点击发布按钮
    def click_publish_btn(self):
        return self.click(self.publish_btn)

    # 点击管理按钮
    def click_manage_btn(self):
        return self.click(self.manage_btn)

    # 点击删除按钮
    def click_remove_btn(self):
        return self.click(self.remove_btn)

    # 点击确定按钮
    def click_determine_btn5(self):
        return self.click(self.determine_btn5)

    # 点击自定义直播
    def click_custom_live_btn(self):
        return self.click(self.custom_live_btn)

    # 直播名称输入框
    live_name_input1 = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div/div/div[3]/div/form/div[1]/div/div/input"

    # 培训分类输入框
    train_sort_input1 = By.XPATH, "/html/body/div/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div/div/div[3]/div/form/div[2]/div/div/div[1]/input"

    # 选择培训分类
    select_train_sort1 = By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/ul/li[1]/label/span[1]/span"

    # 点击空白区域
    blank_area1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[1]/div/div"

    # 学分输入框
    credit_input1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div/div/div[3]/div/form/div[4]/div/div/div/input"

    # 学时输入框
    class_hour_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div/div/div[3]/div/form/div[5]/div/div/div/input"

    # 授课讲师输入框
    lecturer_input1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div/div/div[3]/div/form/div[6]/div/div/input"

    # 选择授课讲师
    select_lecturer1 = By.XPATH, "/html/body/div[3]/div/div[2]/div/div/div/div[2]/div/div/div[3]/table/tbody/tr[1]/td[1]/div/label/span[1]/span"

    # 确定按钮
    determine_btn6 = By.XPATH, "/html/body/div[3]/div/div[3]/div/div/button[1]"

    # 小节输入框
    section_input = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div/div/div[4]/form/div/div[2]/div[1]/div/div/div/div/div/input"

    # 直播日期输入框
    live_date_input1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div/div/div[4]/form/div/div[2]/div[2]/div/div/div/div/div/input"

    # 点击下一个月,选择日期
    next_month_btn1 = By.XPATH, "/html/body/div[4]/div[1]/div/div[1]/button[4]"
    select_live_date = By.XPATH, "/html/body/div[4]/div[1]/div/div[2]/table[1]/tbody/tr[6]/td[1]/div/span"

    # 直播时间输入框
    live_time_input1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div/div/div[4]/form/div/div[2]/div[3]/div/div/div/div/div/i[1]"

    # 选择直播时间
    select_live_time2 = By.XPATH, "/html/body/div[4]/div[1]/div[1]/div[2]/div/div[1]/div[1]/ul/li[17]"
    select_live_time3 = By.XPATH, "/html/body/div[4]/div[1]/div[2]/div[2]/div/div[1]/div[1]/ul/li[18]"

    # 确定按钮
    determine_btn7 = By.XPATH, "/html/body/div[4]/div[2]/button[2]"

    # 下一步按钮
    next_btn1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div/div/div[5]/button[1]/span"

    # 添加用户按钮
    add_user_btn1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div[2]/div/div[1]/div[2]/button[1]/span"

    # 全选
    select_all1 = By.XPATH, "/html/body/div[4]/div/div[2]/div/div/div[3]/div[2]/div/div/div[2]/table/thead/tr/th[1]/div/label/span/span"

    # 确定按钮
    determine_btn8 = By.XPATH, "/html/body/div[4]/div/div[3]/div/button[1]"

    # 发布按钮
    publish_btn1 = By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/main/div/div/div[2]/div[2]/div/div[4]/button[1]"

    # 输入直播名称
    def input_live_name(self, content):
        return self.input(self.live_name_input1, content)

    # 点击培训分类
    def click_train_sort_input1(self):
        return self.click(self.train_sort_input1)

    # 选择培训分类
    def click_select_train_sort1(self):
        return self.click(self.select_train_sort1)

    # 点击空白区域
    def click_blank_area1(self):
        return self.click(self.blank_area1)

    # 输入学分
    def input_credit(self, content):
        return self.input(self.credit_input1, content)

    # 输入学时
    def input_class_hour(self, content):
        return self.input(self.class_hour_input, content)

    # 点击授课讲师输入框
    def click_lecturer_input1(self):
        return self.click(self.lecturer_input1)

    # 选择授课讲师
    def click_select_lecturer1(self):
        return self.click(self.select_lecturer1)

    # 点击确定按钮
    def click_determine_btn6(self):
        return self.click(self.determine_btn6)

    # 输入小节名称
    def input_section(self, content):
        return self.input(self.section_input, content)

    # 点击直播日期输入框
    def click_live_date_input1(self):
        return self.click(self.live_date_input1)

    # 选择直播日期
    def click_select_live_date(self):
        self.click(self.next_month_btn1)
        return self.click(self.select_live_date)

    # 点击直播时间输入框
    def click_live_time_input1(self):
        return self.click(self.live_time_input1)

    # 选择直播时间
    def click_select_live_time2(self):
        self.click(self.select_live_time2)
        return self.click(self.select_live_time3)

    # 点击确定按钮
    def click_determine_btn7(self):
        return self.click(self.determine_btn7)

    # 点击下一步
    def click_next_btn1(self):
        return self.click(self.next_btn1)

    # 点击添加用户
    def click_add_user_btn1(self):
        return self.click(self.add_user_btn1)

    # 点击全选
    def click_select_all1(self):
        return self.click(self.select_all1)

    # 点击确定
    def click_determine_btn8(self):
        return self.click(self.determine_btn8)

    # 点击发布按钮
    def click_publish_btn1(self):
        return self.click(self.publish_btn1)

