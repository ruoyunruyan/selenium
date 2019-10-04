# Time: 2019/9/25  15:52
# Author jzh
# File 16警告框.py

import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r'E:\PyCharmProject\测试selenium\source\css_example.html')

"""
1. text                     --> 返回alert/confirm/prompt中的文字信息
2. accept()                 --> 接受对话框选项
3. dismiss()                --> 取消对话框选项
"""

inputs = driver.find_elements_by_tag_name('input')
# inputs[0].click()
inputs[1].click()

alert = driver.switch_to.alert
# print(alert.text)

time.sleep(1)
# 确定
# alert.accept()
# 取消
alert.dismiss()

time.sleep(1.5)

driver.quit()
