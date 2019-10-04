# Time: 2019/9/25  9:25
# Author jzh
# File 03通过name查找元素.py


import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r'E:/PyCharmProject/%E6%B5%8B%E8%AF%95selenium/source/%E6%B3%A8%E5%86%8CA.html')

element = driver.find_element_by_name('userA')
element.send_keys('admin')

time.sleep(2)
driver.quit()
