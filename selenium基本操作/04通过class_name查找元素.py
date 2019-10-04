# Time: 2019/9/25  9:30
# Author jzh
# File 04通过class_name查找元素.py

import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r'E:/PyCharmProject/%E6%B5%8B%E8%AF%95selenium/source/%E6%B3%A8%E5%86%8CA.html')

element = driver.find_element_by_class_name('telA')

# html 的 class用可以继承多个class用空格分开
# element = driver.find_element_by_class_name('haha')

element.send_keys('123456')

time.sleep(1.5)

driver.quit()
