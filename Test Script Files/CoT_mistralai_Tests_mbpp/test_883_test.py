import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(div_of_nums([], 3, 4), [])

    def test_single_number(self):
        self.assertListEqual(div_of_nums([12], 3, 4), [12])
        self.assertListEqual(div_of_nums([12], 4, 3), [])

    def test_multiple_numbers(self):
        self.assertListEqual(div_of_nums([12, 18, 24, 36], 3, 4), [12, 18, 24])
        self.assertListEqual(div_of_nums([12, 18, 24, 36], 4, 3), [12])

    def test_negative_numbers(self):
        self.assertListEqual(div_of_nums([-12, -18, -24, -36], 3, 4), [])

    def test_zero(self):
        self.assertListEqual(div_of_nums([0], 3, 4), [])
        self.assertListEqual(div_of_nums([0], 4, 3), [])

    def test_divisible_by_one(self):
        self.assertListEqual(div_of_nums([1], 3, 4), [])

    def test_invalid_input(self):
        self.assertRaises(TypeError, div_of_nums, [1, 2, 3], 'm', 'n')
        self.assertRaises(TypeError, div_of_nums, [1, 2, 3], 0, 'n')
        self.assertRaises(TypeError, div_of_nums, [1, 2, 3], m=3, n='n')
