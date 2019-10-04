# Time: 2019/9/25  9:59
# Author jzh
# File 07通过css查找元素.py

import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r'E:/PyCharmProject/%E6%B5%8B%E8%AF%95selenium/source/%E6%B3%A8%E5%86%8CA.html')

"""
input[type^='p'] 说明：type属性以p字母开头的元素
input[type$='d'] 说明：type属性以d字母结束的元素
input[type*='w'] 说明：type属性包含w字母的元素
input[type~='value'] 说明: type属性包含value的元素
input[type=value] 说明: type属性是value的所有元素
"""

driver.find_element_by_css_selector('#userA').send_keys('admin')
driver.find_element_by_css_selector('.telA').send_keys('123456789')

driver.find_element_by_css_selector('input').send_keys('hello world')

# driver.find_element_by_css_selector('[name="emailA"]').send_keys('123@163.com')

# driver.find_element_by_css_selector('[name~="emailA"]').send_keys('123@163.com')

driver.find_element_by_css_selector('[name*="email"]').send_keys('123@163.com')

# list of WebElement - a list with elements if any was found.  An empty list if not
# driver.find_elements_by_css_selector('input')

time.sleep(1.5)

driver.quit()
