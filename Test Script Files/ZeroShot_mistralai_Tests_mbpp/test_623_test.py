import unittest
from mbpp_623_code import nth_nums

class TestNthNums(unittest.TestCase):

    def test_empty_list(self):
        self.assertListEqual(nth_nums([], 2), [])

    def test_single_element(self):
        self.assertListEqual(nth_nums([1], 2), [1])

    def test_single_element_raised_to_zero(self):
        self.assertListEqual(nth_nums([0], 0), [1])

    def test_negative_base(self):
        self.assertListEqual(nth_nums([1, 2, 3], -1), [3, 2, 1])

    def test_positive_base(self):
        self.assertListEqual(nth_nums([1, 2, 3], 2), [1, 8, 27])

    def test_zero_base(self):
        self.assertListEqual(nth_nums([1, 2, 3], 0), [1, 1, 1])

    def test_negative_nums(self):
        self.assertListEqual(nth_nums([-1, -2, -3], 2), [1, 4, 9])
