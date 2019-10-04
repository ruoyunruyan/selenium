# Time: 2019/9/25  15:03
# Author jzh
# File 13鼠标拖拽.py

import time
import numpy
import random

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

driver.get(r'E:\PyCharmProject\测试selenium\source\drag.html')

action = ActionChains(driver)

div1 = driver.find_element_by_id('div1')
div2 = driver.find_element_by_id('div2')

# 拖拽
# action.drag_and_drop(div1, div2).perform()

# 生成拖拽的距离列表
# 正态分布前距离的前 3/4 , 均匀分布生成后 1/4, 预计在 0.8s -- 1s 之间完成
x1 = numpy.random.normal(3, 2, 100)[50:]
x1 = [x for x in x1 if x > 0]
x2 = numpy.random.uniform(1, 2, 100)[50:]

x = list(x1) + list(x2)

done_time = random.uniform(0.8, 1)
time_step = done_time / len(x)
print(sum(x))
action.click_and_hold(div1).perform()

for distance in x:
    action.move_by_offset(xoffset=distance, yoffset=0).perform()
    # time.sleep(time_step)

action.release(div2).perform()

# 方法拆解
# action.click_and_hold(div1).perform()
# action.release(div2).perform()

time.sleep(1.5)

driver.quit()
