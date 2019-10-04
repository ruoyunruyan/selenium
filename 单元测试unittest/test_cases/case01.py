# Time: 2019/9/26  8:23
# Author jzh
# File case01.py

import unittest


def add(x, y):
    return x + y


def division(x, y):
    return x / y


class TestCase01(unittest.TestCase):

    def setUp(self) -> None:
        # 用于初始化测试环境
        print('测试开始...')

    def tearDown(self) -> None:
        # 用户收尾
        print('测试结束...')

    def test_add(self):
        print('1 + 1', add(1, 1))

    def test_division(self):
        print('1 / 0', division(1, 0))

