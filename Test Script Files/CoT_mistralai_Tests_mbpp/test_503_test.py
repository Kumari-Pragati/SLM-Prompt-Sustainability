import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):
    def test_empty_list(self):
        self.assertListEqual([], add_consecutive_nums([]))

    def test_single_element_list(self):
        self.assertListEqual([], add_consecutive_nums([1]))

    def test_consecutive_numbers(self):
        self.assertListEqual([2, 4, 6], add_consecutive_nums([1, 2, 3, 4]))

    def test_negative_numbers(self):
        self.assertListEqual([-1, -3, -5], add_consecutive_nums([0, -1, -2, -3]))

    def test_zero_as_first_element(self):
        self.assertListEqual([0, 2], add_consecutive_nums([0, 2]))

    def test_zero_as_last_element(self):
        self.assertListEqual([1, 3], add_consecutive_nums([1, 2, 3]))

    def test_mixed_numbers(self):
        self.assertListEqual([2, 4, 6, 8], add_consecutive_nums([1, 3, 5, 7, 9]))

    def test_duplicate_numbers(self):
        self.assertListEqual([2, 4, 6, 8, 10], add_consecutive_nums([1, 3, 5, 7, 9, 7, 5, 3]))

    def test_invalid_input(self):
        self.assertRaises(TypeError, add_consecutive_nums, 'abc')
