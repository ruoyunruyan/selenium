# Time: 2019/9/25  9:36
# Author jzh
# File 05通过tag_name查找元素.py

import time
from selenium import webdriver


driver = webdriver.Chrome()

driver.get(r'E:/PyCharmProject/%E6%B5%8B%E8%AF%95selenium/source/%E6%B3%A8%E5%86%8CA.html')

# WebElement - the element if it was found, NoSuchElementException - if the element wasn't found
# 如果有, 返回第一个, 如果没有, 抛出错误
# element = driver.find_element_by_tag_name('input')

# element.send_keys('admin123')


# list of WebElement - a list with elements if any was found.  An empty list if not
# 如果有, 返回列表, 如果没有, 返回空列表
elements = driver.find_elements_by_tag_name('input')

print(len(elements))

elements[3].send_keys('hello world')

time.sleep(2)

driver.quit()

