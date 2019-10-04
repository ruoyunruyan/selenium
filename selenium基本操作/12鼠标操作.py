# Time: 2019/9/25  14:57
# Author jzh
# File 12鼠标操作.py


import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get(r'E:/PyCharmProject/%E6%B5%8B%E8%AF%95selenium/source/%E6%B3%A8%E5%86%8CA.html')
"""
1. context_click()            右击 --> 此方法模拟鼠标右键点击效果
2. double_click()             双击 --> 此方法模拟双标双击效果
3. drag_and_drop()            拖动 --> 此方法模拟双标拖动效果
4. move_to_element()          悬停 --> 此方法模拟鼠标悬停效果
5. perform()                  执行 --> 此方法用来执行以上所有鼠标方法
"""

action = ActionChains(driver)
# user = driver.find_element_by_id('userA')
# 鼠标右键
# action.context_click(user)

# 显示效果
# action.perform()

# 简写
# action.context_click(user).perform()

driver.find_element_by_id('AAA').click()

driver.implicitly_wait(6)

element = driver.find_element_by_class_name('soutu-btn')

# 鼠标悬停
action.move_to_element(element).perform()

time.sleep(2)

driver.quit()