import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual([], add_consecutive_nums([]))

    def test_single_element_list(self):
        self.assertListEqual([], add_consecutive_nums([1]))

    def test_consecutive_numbers(self):
        self.assertListEqual([2, 3, 4], add_consecutive_nums([1, 2, 3, 4]))

    def test_negative_numbers(self):
        self.assertListEqual([-1, -2], add_consecutive_nums([-2, -1]))

    def test_zero_in_middle(self):
        self.assertListEqual([1, 2, 0], add_consecutive_nums([0, 1, 2]))

    def test_duplicate_numbers(self):
        self.assertListEqual([2, 2, 3], add_consecutive_nums([1, 2, 2, 3]))

    def test_large_numbers(self):
        self.assertListEqual([10, 11, 12], add_consecutive_nums(list(range(9, 12))))

    def test_negative_and_positive_numbers(self):
        self.assertListEqual([-3, -2, -1, 0, 1, 2], add_consecutive_nums([-3, -2, -1, 0, 1]))
