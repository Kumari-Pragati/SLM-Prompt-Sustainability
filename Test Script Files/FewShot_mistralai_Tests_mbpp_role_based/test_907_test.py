import unittest
from mbpp_907_code import lucky_num

class TestLuckyNum(unittest.TestCase):
    def test_positive_small_numbers(self):
        self.assertListEqual(lucky_num(1), [1])
        self.assertListEqual(lucky_num(2), [1, 3])
        self.assertListEqual(lucky_num(3), [1, 3, 5])

    def test_large_numbers(self):
        self.assertListEqual(lucky_num(10), [1, 3, 5, 7, 9])
        self.assertListEqual(lucky_num(100), [1, 3, 5, 7, 9, 21, 23, 25, 27, 29, 41, 43, 45, 47, 49, 61, 63, 65, 67, 69, 81, 83, 85, 87, 89, 101, 103, 105, 107, 109])

    def test_negative_numbers(self):
        self.assertListEqual(lucky_num(-1), [])
        self.assertListEqual(lucky_num(-2), [1])

    def test_zero(self):
        self.assertListEqual(lucky_num(0), [])

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            lucky_num(3.14)
