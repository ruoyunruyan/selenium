# Time: 2019/9/25  15:58
# Author jzh
# File 17滚动条.py

import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get(r'E:/PyCharmProject/%E6%B5%8B%E8%AF%95selenium/source/%E6%B3%A8%E5%86%8CA.html')

driver.maximize_window()

driver.find_element_by_id('AAA').click()
driver.find_element_by_id('kw').send_keys('风景')
driver.find_element_by_id('su').click()

# 使用隐式等待会与滚动操作冲突
# driver.implicitly_wait(5)

# 使用time.sleep强制等待
# time.sleep(2)

# 使用显式等待
WebDriverWait(driver, 5).until(ec.presence_of_element_located((By.ID, '10')))

js = 'window.scrollTo(0, 10000)'
driver.execute_script(js)

time.sleep(2)

driver.quit()
