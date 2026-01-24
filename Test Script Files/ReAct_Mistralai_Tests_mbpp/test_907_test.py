import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):

    def test_positive_integer(self):
        self.assertListEqual(lucky_num(5), [3, 5])

    def test_zero(self):
        self.assertListEqual(lucky_num(0), [1])

    def test_negative_integer(self):
        self.assertListEqual(lucky_num(-3), [1, 3, 5])

    def test_large_positive_integer(self):
        self.assertListEqual(lucky_num(100), [1, 3, 5, 7, 9, 25, 49, 81, 121, 169, 209, 257, 305, 353, 401, 449, 497, 545, 593, 641, 689, 737, 785, 833, 881, 939])

    def test_large_negative_integer(self):
        self.assertListEqual(lucky_num(-100), [1, 3, 5, 7, 9, 25, 49, 81, 121, 169, 209, 257, 305, 353, 401, 449, 497, 545, 593, 641, 689, 737, 785, 833, 881, 939, -941])

    def test_edge_cases(self):
        self.assertListEqual(lucky_num(1), [1])
        self.assertListEqual(lucky_num(2), [1, 3])
        self.assertListEqual(lucky_num(4), [1, 3, 5])
        self.assertListEqual(lucky_num(9), [1, 3, 5, 7])
