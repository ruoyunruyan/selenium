# Time: 2019/9/25  21:09
# Author jzh
# File 21窗口截图.py

import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r'E:/PyCharmProject/%E6%B5%8B%E8%AF%95selenium/source/%E6%B3%A8%E5%86%8CA.html')
driver.maximize_window()
driver.save_screenshot('images/截图.png')

time.sleep(1.5)

driver.quit()
