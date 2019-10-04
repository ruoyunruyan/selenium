# Time: 2019/9/12  15:54
# Author jzh
# File 07显式等待.py

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get(r'E:\PyCharmProject\测试selenium\source\注册A.html')

# 执行速度太快, 页面还未加载出来
# selenium.common.exceptions.NoSuchElementException
driver.find_element_by_id('AAA').click()
driver.find_element_by_id('kw').send_keys('风景')
driver.find_element_by_id('su').click()

# 显示等待
element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, '1')))
element.click()

time.sleep(4)

driver.quit()
