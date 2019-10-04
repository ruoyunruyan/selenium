# Time: 2019/9/25  21:00
# Author jzh
# File 20多窗口之间的切换.py

import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r'E:/PyCharmProject/%E6%B5%8B%E8%AF%95selenium/source/%E6%B3%A8%E5%86%8CA.html')
driver.maximize_window()
# 当前窗口的唯一标识
print(driver.current_window_handle)
print(driver.window_handles)
print(driver.title)

driver.find_element_by_id('fwA').click()

print(driver.current_window_handle)
print(driver.window_handles)

driver.switch_to.window(driver.window_handles[1])
print(driver.title)

time.sleep(3)

driver.quit()
