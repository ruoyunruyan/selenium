# Time: 2019/9/12  16:51
# Author jzh
# File 10键盘操作.py

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get(r'E:\PyCharmProject\测试selenium\source\注册A.html')
try:
    user = driver.find_element_by_id('userAB')
except Exception as e:
    user = None
    print('没有该标签')
if user:
    tel = driver.find_element_by_id('telA')
    user.send_keys('admin123')
    time.sleep(1)
    user.send_keys(Keys.BACKSPACE)
    time.sleep(1)
    user.send_keys(Keys.BACKSPACE)
    time.sleep(1)
    user.send_keys(Keys.CONTROL, 'a')
    time.sleep(1)
    user.send_keys(Keys.CONTROL, 'c')
    time.sleep(1)
    tel.send_keys(Keys.CONTROL, 'v')


time.sleep(2)

driver.quit()



