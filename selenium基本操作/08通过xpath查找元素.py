# Time: 2019/9/25  10:00
# Author jzh
# File 08通过xpath查找元素.py

import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r'E:/PyCharmProject/%E6%B5%8B%E8%AF%95selenium/source/%E6%B3%A8%E5%86%8CA.html')

"""
//*[text()="xxx"]                           文本内容是xxx的元素

//*[starts-with(@attribute,'xxx')]          属性以xxx开头的元素

//*[contains(@attribute,'Sxxx')]            属性中含有xxx的元素
"""

# driver.find_element_by_xpath('//input[@id="userA"]').send_keys('admin')

# driver.find_element_by_xpath('//a[text()="访问 百度 网站"]').click()

# driver.find_element_by_xpath('//input[starts-with(@name, "user")]').send_keys('admin')

driver.find_element_by_xpath('//input[contains(@name, "user")]').send_keys('admin')

time.sleep(5)

driver.quit()
