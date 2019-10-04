# Time: 2019/9/25  15:22
# Author jzh
# File 15下拉框.py

import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get(r'E:/PyCharmProject/%E6%B5%8B%E8%AF%95selenium/source/%E6%B3%A8%E5%86%8CA.html')

"""
1. select_by_index()                    --> 根据option索引来定位，从0开始
2. select_by_value()                    --> 根据option属性 value值来定位
3. select_by_visible_text()             --> 根据option显示文本来定位
"""
cities = driver.find_element_by_id('selectA')

select = Select(cities)

select.select_by_index(3)
time.sleep(1)

select.select_by_value('sh')
time.sleep(1)

select.select_by_visible_text('A北京')

for option in select.options:
    time.sleep(0.5)
    option.click()

time.sleep(1.5)

driver.quit()
