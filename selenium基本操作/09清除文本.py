# Time: 2019/9/25  11:07
# Author jzh
# File 09清除文本.py

import time
import numpy
from selenium import webdriver

driver = webdriver.Chrome()

numpy.random.normal()
driver.get(r'E:/PyCharmProject/%E6%B5%8B%E8%AF%95selenium/source/%E6%B3%A8%E5%86%8CA.html')

driver.find_element_by_id('userA').send_keys('admin')

time.sleep(1)
driver.find_element_by_id('userA').clear()

time.sleep(1.5)

driver.quit()
