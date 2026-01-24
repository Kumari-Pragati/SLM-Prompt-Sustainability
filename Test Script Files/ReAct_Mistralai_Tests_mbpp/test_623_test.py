import unittest
from mbpp_623_code import nth_nums

class TestNthNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(nth_nums([], 2), [])

    def test_single_element(self):
        self.assertListEqual(nth_nums([1], 2), [1])

    def test_positive_numbers(self):
        self.assertListEqual(nth_nums([1, 2, 3, 4, 5], 2),
                              [1, 4, 9, 16, 25])

    def test_negative_numbers(self):
        self.assertListEqual(nth_nums([-1, -2, -3, -4, -5], 2),
                              [1, 4, 9, 16, 25])

    def test_zero_base(self):
        self.assertListEqual(nth_nums([0], 0), [0])

    def test_zero_exponent(self):
        self.assertListEqual(nth_nums([1, 2, 3], 0), [1, 1, 1])

    def test_negative_exponent(self):
        self.assertListEqual(nth_nums([1, 2, 3], -2), [1, 4, 9])

    def test_floats(self):
        self.assertListEqual(nth_nums([1.5, 2.5, 3.5], 2),
                              [2.25, 15.625, 56.25])

    def test_list_with_zero(self):
        self.assertListEqual(nth_nums([0, 1, 2, 3], 2),
                              [0, 1, 4, 27])

    def test_list_with_none(self):
        self.assertListEqual(nth_nums([None, 1, 2, 3], 2),
                              [None, 1, 4, 27])

    def test_list_with_string(self):
        self.assertListEqual(nth_nums(["a", "b", "c"], 3),
                              ["a³", "b³", "c³"])
