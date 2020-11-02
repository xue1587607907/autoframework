import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys(12306)
time.sleep(2)
driver.quit()
