# Time: 2019/9/26  7:56
# Author jzh
# File 02Testsuite的使用.py

import unittest

from unittest_simple01 import TestCase01, TestCase02

# 创展测试组
suite = unittest.TestSuite()

# 方法1: 添加测试方法
# suite.addTest(TestCase01.test_add)
# suite.addTest(TestCase02.test_add)
# suite.addTest(TestCase01.test_division)
# suite.addTest(TestCase02.test_division)

# 方法2: 添加测试方法
# suite.addTests([TestCase02.test_add, TestCase02.test_division, TestCase01.test_add, TestCase01.test_division])

# 方法3: 添加测试方法
suite.addTest(unittest.makeSuite(TestCase01))
suite.addTest(unittest.makeSuite(TestCase02))


# 推荐使用这种运行方式
runner = unittest.TextTestRunner()
runner.run(suite)

# if __name__ == '__main__':
#     # 使用这种方式运行, 结果会乱
#     unittest.main()
