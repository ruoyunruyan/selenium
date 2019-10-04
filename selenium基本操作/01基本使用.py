# Time: 2019/9/12  10:34
# Author jzh
# File 01基本使用.py

import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r'E:/PyCharmProject/%E6%B5%8B%E8%AF%95selenium/source/%E6%B3%A8%E5%86%8CA.html')

"""
1. maximize_window()                   最大化 --> 模拟浏览器最大化按钮
2. set_window_size(100,100)            浏览器大小 --> 设置浏览器宽、高(像素点)
3. set_window_position(300,200)        浏览器位置 --> 设置浏览器位置
4. back()                              后退 --> 模拟浏览器后退按钮
5. forward()                           前进 --> 模拟浏览器前进按钮
6. refresh()                           刷新 --> 模拟浏览器F5刷新
7. close()                             关闭 --> 模拟浏览器关闭按钮(关闭单个窗口)
8. quit()                              关闭 --> 关闭所有WebDriver启动的窗口
"""

# 窗口最大化
# driver.maximize_window()

# 设置窗口大小
# driver.set_window_size(400, 400)

# time.sleep(1)

# 设置窗口位置
# driver.set_window_position(100, 100)
"""
driver.find_element_by_id('AAA').click()

time.sleep(1)

driver.back()

time.sleep(1)
driver.forward()
time.sleep(1)
driver.refresh()
"""

"""
1. size                    返回元素大小
2. text                    获取元素的文本
3. title                   获取页面title
4. current_url             获取当前页面URL
5. get_attribute()         获取属性值
6. is_display()            判断元素是否可见
7. is_enabled()            判断元素是否可用
"""

# {'height': 29, 'width': 183}
# print(driver.find_element_by_id('userA').size)

# 访问 百度 网站
# print(driver.find_element_by_id('fwA').text)

# 注册A
# print(driver.title)

# file:///E:/PyCharmProject/%E6%B5%8B%E8%AF%95selenium/source/%E6%B3%A8%E5%86%8CA.html
# print(driver.current_url)

# http://www.baidu.com/
# print(driver.find_element_by_id('fwA').get_attribute('href'))

# True
# print(driver.find_element_by_xpath('//button[@value="注册A"]').is_enabled())

# True
# print(driver.find_element_by_xpath('//input[@name="userA"]').is_displayed())

# False
print(driver.find_element_by_id('cancelA').is_enabled())

time.sleep(2)
# 关闭当前页
# driver.close()
# 关闭浏览器
driver.quit()
