import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(div_of_nums([], 3, 4), [])

    def test_single_number(self):
        self.assertListEqual(div_of_nums([10], 3, 4), [])
        self.assertListEqual(div_of_nums([12], 3, 4), [])
        self.assertListEqual(div_of_nums([15], 3, 5), [15])

    def test_multiple_numbers(self):
        self.assertListEqual(div_of_nums([10, 12, 15, 20], 3, 4), [15, 20])
        self.assertListEqual(div_of_nums([10, 12, 15, 20], 3, 5), [15])
        self.assertListEqual(div_of_nums([10, 12, 15, 20], 4, 5), [])

    def test_negative_numbers(self):
        self.assertListEqual(div_of_nums([-10, -12, -15, -20], 3, 4), [])
        self.assertListEqual(div_of_nums([-10, -12, -15, -20], 3, -4), [-10, -15, -20])
        self.assertListEqual(div_of_nums([-10, -12, -15, -20], -3, 4), [])

    def test_zero(self):
        self.assertListEqual(div_of_nums([0, 10, 12, 15, 20], 3, 4), [])
        self.assertListEqual(div_of_nums([0, 0, 15, 20], 3, 4), [0])
