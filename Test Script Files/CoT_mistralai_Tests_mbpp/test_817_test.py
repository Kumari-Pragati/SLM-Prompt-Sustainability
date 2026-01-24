import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual(div_of_nums([], 2, 3), [])

    def test_single_number(self):
        self.assertListEqual(div_of_nums([4], 2, 2), [4])
        self.assertListEqual(div_of_nums([5], 2, 3), [])

    def test_multiple_numbers(self):
        self.assertListEqual(div_of_nums([4, 8, 15, 16, 20], 4, 8), [4, 8, 16, 20])
        self.assertListEqual(div_of_nums([5, 9, 15, 16, 20], 4, 3), [15, 20])

    def test_negative_numbers(self):
        self.assertListEqual(div_of_nums([-4, -8, -15, -16, -20], 4, 8), [-4, -8, -16, -20])
        self.assertListEqual(div_of_nums([-5, -9, -15, -16, -20], 4, 3), [-15, -20])

    def test_zero(self):
        self.assertListEqual(div_of_nums([0], 2, 2), [0])
        self.assertListEqual(div_of_nums([0], 2, 3), [])

    def test_m_equals_n(self):
        self.assertListEqual(div_of_nums([4, 8, 15, 16, 20], 4, 4), [4, 8, 16, 20])

    def test_invalid_m(self):
        self.assertRaises(TypeError, div_of_nums, [4, 8, 15, 16, 20], 0, 3)
        self.assertRaises(TypeError, div_of_nums, [4, 8, 15, 16, 20], "m", 3)

    def test_invalid_n(self):
        self.assertRaises(TypeError, div_of_nums, [4, 8, 15, 16, 20], 2, 0)
        self.assertRaises(TypeError, div_of_nums, [4, 8, 15, 16, 20], 2, "n")
