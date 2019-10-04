# Time: 2019/9/25  20:52
# Author jzh
# File 19iframe之间的切换.py

import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r'E:\PyCharmProject\测试selenium\source\注册实例.html')

driver.maximize_window()

# frame之间的切换, 需要先切换到主框架中
driver.find_element_by_id('user').send_keys('admin')

driver.switch_to.frame('myframe1')
driver.find_element_by_id('userA').send_keys('adminA')

# 切换回默认的frame
driver.switch_to.default_content()

# 或者切换回父frame
# driver.switch_to.parent_frame()

driver.switch_to.frame('myframe2')
driver.find_element_by_id('userB').send_keys('adminB')

time.sleep(2)

driver.quit()
