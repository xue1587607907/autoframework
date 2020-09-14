import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://test.elearning.learnfuture.com")
driver.maximize_window()
driver.implicitly_wait(5)
time.sleep(2)
driver.find_element_by_class_name("el-input__inner").send_keys("aaa111")
driver.find_element_by_css_selector("div[class = 'bk-form-control with-right-icon'] input").send_keys("aaa111")
driver.find_element_by_css_selector("div[class = 'jw-line-height-login' ] span").click()
driver.find_element_by_class_name("jw-user-face").click()
time.sleep(2)

# 新增
# driver.find_element_by_css_selector("div[class='jw-table-buttons-contain'] span").click()
# element = driver.find_element_by_css_selector("div[class= 'el-input el-input--mini'] input")
# element.send_keys("abc123")
# driver.find_element_by_css_selector(".jw-right-account-form > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)").send_keys("abc123")
# driver.find_element_by_css_selector("div[class='el-cascader el-cascader--mini']").click()
# driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/div[1]/ul/li/label/span[1]/span").click()
# driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[2]/div[1]/ul/li[1]/label/span[1]/span").click()
# driver.find_element_by_xpath("/html/body/div[2]/div[1]/div[3]/div[1]/ul/li[1]/label/span[1]/span").click()
# driver.find_element_by_css_selector("button.el-button--primary:nth-child(1) > span:nth-child(1)").click()

# 修改
# driver.find_element_by_css_selector(".jw-td-cell-self ").click()
# time.sleep(2)
# driver.find_element_by_css_selector("div[class= 'el-input el-input--mini'] input").clear()
# driver.find_element_by_css_selector("div[class= 'el-input el-input--mini'] input").send_keys("123qwe")
# driver.find_element_by_css_selector(".jw-right-account-form > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)").clear()
# driver.find_element_by_css_selector(".jw-right-account-form > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)").send_keys("123qwe")
# time.sleep(2)
# driver.find_element_by_css_selector("button.el-button--primary:nth-child(1) > span:nth-child(1)").click()

# 查询
# driver.find_element_by_css_selector(".jw-tree-data-contain > div:nth-child(1) > input:nth-child(1)").send_keys("技术")
# driver.find_element_by_css_selector("span[class='el-input__suffix-inner'] i").click()

# 禁用

# driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[3]/div[2]/div[2]/div[1]/div/div/"
#                              "div[4]/div[2]/table/tbody/tr[1]/td[8]/div/main/main/div").click()
# driver.implicitly_wait(10)

# driver.find_element_by_xpath("/html/body/ul/li[3]").click()
# driver.find_element_by_xpath("//ur [start-with(@id,'dropdown-menu-')]/li[2]").click()
# driver.find_element_by_xpath("//ur [contains(@id,'dropdown-menu-')]/li[3]").click()
# driver.find_element_by_css_selector("ur[class='el-dropdown-menu el-popper el-dropdown-menu--mini'] li[3]").click()


# time.sleep(3)
# driver.quit()
import random

# i = 0
# str = " "
# while i < 3:
#     num = random.randrange(48, 57)
#     # if (num <= 57) or (num >= 65 and num <= 90) or (num >= 97):
#     str += chr(num)
#     i += 1
element = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[3]/div/div[2]/main/div/div/div[1]/div/div[2]/div/div[1]/div[1]/span[2]/span")
action = ActionChains(driver)
action.move_to_element(element).perform()
time.sleep(3)

driver.quit()
