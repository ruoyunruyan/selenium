# Time: 2019/9/25  9:48
# Author jzh
# File 06通过link_txt查找元素.py

import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r'E:/PyCharmProject/%E6%B5%8B%E8%AF%95selenium/source/%E6%B3%A8%E5%86%8CA.html')


# 查找的是 a 标签中的内容
# 报错: selenium.common.exceptions.NoSuchElementException: Message: no such element
# driver.find_element_by_link_text('注册用户A').send_keys('hello world')


# 按照文本查找标签, 适用于 a 标签 (点击事件)
driver.find_element_by_link_text('访问 百度 网站').click()

# list of webelement - a list with elements if any was found.  an empty list if not
# driver.find_elements_by_link_text('')


# 通过 a 标签中的部分内容查找标签
# driver.find_element_by_partial_link_text('AA').click()

# list of webelement - a list with elements if any was found.  an empty list if not
# driver.find_elements_by_partial_link_text('百度')

time.sleep(5)

driver.quit()
