# Time: 2019/9/26  8:53
# Author jzh
# File 04生成测试报告.py

import os
import unittest

from utils.HTMLTestRunner import HTMLTestRunner

BASIC_DIR = os.path.dirname(os.path.abspath(__file__))
start_dir = os.path.join(BASIC_DIR, 'test_cases')
report_dir = os.path.join(BASIC_DIR, '测试报告')

suite = unittest.defaultTestLoader.discover(start_dir=start_dir, pattern='case*')


if __name__ == '__main__':
    with open(os.path.join(report_dir, '测试报告.html'), 'wb') as f:
        runner = HTMLTestRunner(stream=f, title='测试报告', description='测试用例')
        runner.run(suite)

