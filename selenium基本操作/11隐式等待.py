# Time: 2019/9/25  14:51
# Author jzh
# File 11隐式等待.py

import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r'E:/PyCharmProject/%E6%B5%8B%E8%AF%95selenium/source/%E6%B3%A8%E5%86%8CA.html')

driver.find_element_by_id('AAA').click()
driver.find_element_by_id('kw').send_keys('风景')
driver.find_element_by_id('su').click()

# 隐式等待
driver.implicitly_wait(5)
driver.find_element_by_id('1').click()

time.sleep(10)

driver.quit()
