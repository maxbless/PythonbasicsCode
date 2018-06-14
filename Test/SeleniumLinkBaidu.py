#coding=UTF-8
#使用selenium连接百度
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
driver.find_element_by_id("kw").send_keys("testing")
driver.find_element_by_id("su").click()
driver.quit()