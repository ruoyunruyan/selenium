# Time: 2019/9/25  21:27
# Author jzh
# File 23登陆操作.py

import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r'https://mail.163.com/')
driver.maximize_window()

driver.find_element_by_class_name('new-loginFunc').click()

frame = driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
driver.switch_to.frame(frame)

driver.find_element_by_xpath('//input[@name="email"]').send_keys('xxx')

driver.find_element_by_xpath('//input[@name="password"]').send_keys('xxx')

driver.find_element_by_id('dologin').click()

time.sleep(120)

driver.quit()
