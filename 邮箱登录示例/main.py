# Time: 2019/9/26  9:45
# Author jzh
# File main.py

import os
import unittest
from utils.HTMLTestRunner import HTMLTestRunner
# from mail_test_case import TestCaseMail
from mail_test_cases01 import TestCaseMail

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestCaseMail))

BASIC_DIR = os.path.dirname(os.path.abspath(__file__))
reports_dir = os.path.join(BASIC_DIR, 'reports')
images_dir = os.path.join(BASIC_DIR, 'screen_shorts')

with open(os.path.join(reports_dir, '测试报告.html'), 'wb') as f:
    runner = HTMLTestRunner(stream=f, title='test report', description='测试报告')
    runner.run(suite)
