# Time: 2019/9/25  21:17
# Author jzh
# File 22添加cookie.py


import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r'E:/PyCharmProject/%E6%B5%8B%E8%AF%95selenium/source/%E6%B3%A8%E5%86%8CA.html')
# driver.add_cookie({'name' : 'foo', 'value' : 'bar'})
driver.add_cookie({'name': 'cookie', 'value': ''})

# 注意, 需要刷新以下
driver.refresh()

time.sleep(1.5)

driver.quit()