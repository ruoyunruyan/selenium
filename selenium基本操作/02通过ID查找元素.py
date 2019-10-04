# Time: 2019/9/25  9:20
# Author jzh
# File 02元素.py

import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r'E:/PyCharmProject/%E6%B5%8B%E8%AF%95selenium/source/%E6%B3%A8%E5%86%8CA.html')

# 获取元素
element = driver.find_element_by_id('userA')
# 写入数据
element.send_keys('admin')

# 简写形式
# driver.find_element_by_id('userA').send_keys('admin')

time.sleep(2)

driver.quit()
