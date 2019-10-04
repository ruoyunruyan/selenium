# Time: 2019/9/26  14:25
# Author jzh
# File mail_test_01.py

import os
import time
import unittest
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


class TestCaseMail(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """
        这个只有在开始和结束的时候执行一次，即执行第一个用例之前
        :return:
        """
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        """
        这个只有在开始和结束的时候执行一次，即执行最后一个用例之后
        :return:
        """
        pass

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()

    def test_login(self, username, password):
        self.assertEqual(1, login(self.driver, username, password))

    @staticmethod
    def getTestFunc(arg1, arg2):
        def func(self):
            self.test_login(arg1, arg2)
        return func

    def tearDown(self) -> None:
        self.driver.quit()


# 读取测试用例
test_cases = []
file = open('测试用例.txt', 'r')
for line in file:
    test_cases.append(line.replace('\n', '').strip().split())


def __generate_test_cases():
    for args in test_cases:
        # setattr  参数2 设置属性的名称  参数3 设置属性的值
        setattr(TestCaseMail, 'test_func_%s' % args[0], TestCaseMail.getTestFunc(*args))


__generate_test_cases()
