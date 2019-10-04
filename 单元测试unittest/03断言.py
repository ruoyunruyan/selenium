# Time: 2019/9/26  8:37
# Author jzh
# File 03断言.py

import unittest

"""
assertEqual(arg1, arg2, msg=None)	    验证arg1=arg2，不等则fail 【掌握】
assertNotEqual(arg1, arg2, msg=None)	验证arg1 != arg2, 相等则fail
assertTrue(expr, msg=None)	            验证expr是true，如果为false，则fail
assertFalse(expr,msg=None)	            验证expr是false，如果为true，则fail
assertIsNone(expr, msg=None)	        验证expr是None，不是则fail
assertIsNotNone(expr, msg=None)	        验证expr不是None，是则fail
assertIn(arg1, arg2, msg=None)	        验证arg1是arg2的子串，不是则fail【掌握】
"""


def add(x, y):
    return x + y


class TestCase01(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_add(self):
        self.assertEqual(2, add(1, 1))

    def test_in(self):
        # 可以用来判断是否登录成功
        self.assertIn(1, [2, 3, 1])


if __name__ == '__main__':
    unittest.main()