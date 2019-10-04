# Time: 2019/9/26  13:54
# Author jzh
# File 05ddt的使用.py

import unittest
from ddt import ddt, data, unpack


@ddt
class MyTesting(unittest.TestCase):
    def setUp(self):
        print('this is the setUp')

    # @data(1, 2, 3)  # 将data中的数据分别传入测试用例的参数中
    # def test_1(self, value):
    #     print(value)

    @data([3, 2, 1], [5, 3, 2], [10, 4, 6])
    @unpack
    def test_minus(self, a, b, expected):
        actual = int(a) - int(b)
        expected = int(expected)
        self.assertEqual(actual, expected)

    # @data([3, 3], [5, 5])
    # @unpack  # 使用unpack将[3, 3]拆开, 按照用例中的两个参数传递, 如果不适用, 则将[3, 3]作为整体传入用例的参数中
    # 会抛出缺少参数的错误
    # def test_compare(self, a, b):
    #     self.assertEqual(a, b)

    def tearDown(self):
        print('this is tearDown')


if __name__ == '__main__':
    unittest.main(verbosity=2)
