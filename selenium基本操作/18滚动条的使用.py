# Time: 2019/9/25  16:19
# Author jzh
# File 18滚动条的使用.py

import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

driver.get(r'https://www.douyu.com/g_LOL')
driver.maximize_window()

element = None

while not element:
    try:
        element = driver.find_element_by_xpath('//span[text()="下一页"]')
    except NoSuchElementException as e:
        js = 'window.scrollTo(0, 10000)'
        driver.execute_script(js)

element.click()
time.sleep(12)
driver.quit()
