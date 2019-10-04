# Time: 2019/9/26  9:22
# Author jzh
# File mail_test.py

import os
import time
import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

BASIC_DIR = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(BASIC_DIR, 'screen_shorts')


def login(driver, username, password):
    driver.get(r'https://mail.163.com/')
    driver.maximize_window()
    driver.find_element_by_class_name('new-loginFunc').click()
    frame = driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
    driver.switch_to.frame(frame)
    driver.find_element_by_xpath('//input[@name="email"]').send_keys(username)
    driver.find_element_by_xpath('//input[@name="password"]').send_keys(password)
    driver.find_element_by_id('dologin').click()

    # time.sleep(2)

    # 隐式等待
    driver.implicitly_wait(5)

    try:
        driver.find_element_by_id('spnUid')
    except NoSuchElementException as e:
        driver.save_screenshot(os.path.join(images_dir, username + '登录失败.png'))
        return 0
    else:
        driver.save_screenshot(os.path.join(images_dir, username + '登录成功.png'))
        return 1


# 读取测试用例
test_cases = []
file = open('测试用例.txt', 'r')
for line in file:
    test_cases.append(line.replace('\n', '').strip().split())


@ddt
class TestCaseMail(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    @data(*test_cases)
    @unpack
    def test_login(self, username, password):
        self.assertEqual(1, login(self.driver, username, password))

    def tearDown(self) -> None:
        self.driver.quit()
