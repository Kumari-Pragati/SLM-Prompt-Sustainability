import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(add_consecutive_nums([]), [])

    def test_single_element_list(self):
        self.assertListEqual(add_consecutive_nums([1]), [])

    def test_consecutive_numbers(self):
        self.assertListEqual(add_consecutive_nums([1, 2, 3, 4]), [2, 3, 4])

    def test_non_consecutive_numbers(self):
        self.assertListEqual(add_consecutive_nums([3, 5, 6, 7, 8]), [4, 6, 7])

    def test_negative_numbers(self):
        self.assertListEqual(add_consecutive_nums([-1, -2, -3]), [-2, -3])

    def test_mixed_numbers(self):
        self.assertListEqual(add_consecutive_nums([1, -2, 3, -4]), [1, -1, 3])
