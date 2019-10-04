# Time: 2019/9/26  8:25
# Author jzh
# File 03defaultTestLoader的使用.py

import os
import unittest

BASIC_DIR = os.path.dirname(os.path.abspath(__file__))
start_dir = os.path.join(BASIC_DIR, 'test_cases')

# 返回测试套件
suite = unittest.defaultTestLoader.discover(start_dir=start_dir, pattern='case*')
# suite = unittest.defaultTestLoader.discover(start_dir='./test_cases', pattern='case*')

runner = unittest.TextTestRunner()

runner.run(suite)
