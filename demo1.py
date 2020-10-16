import time
from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get("http://test.elearning.learnfuture.com")
driver.maximize_window()
driver.implicitly_wait(5)


