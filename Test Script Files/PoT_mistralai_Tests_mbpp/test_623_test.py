import unittest
from mbpp_623_code import nth_nums

class TestNthNums(unittest.TestCase):
    def test_typical_case(self):
        self.assertListEqual(nth_nums([1, 2, 3, 4], 2), [1, 4, 9, 16])
        self.assertListEqual(nth_nums([5, 6, 7, 8], 3), [125, 216, 343, 512])

    def test_edge_case_zero(self):
        self.assertListEqual(nth_nums([1], 0), [1])
        self.assertListEqual(nth_nums([1, 2], 0), [1, 1])

    def test_edge_case_negative(self):
        self.assertListEqual(nth_nums([1, 2, 3], -1), [1, 2, 3])
        self.assertListEqual(nth_nums([-1, -2, -3], -1), [1, 4, 9])

    def test_edge_case_empty(self):
        self.assertListEqual(nth_nums([], 2), [])

    def test_corner_case_negative_numbers(self):
        self.assertListEqual(nth_nums([-1, -2, -3], 3), [27, 8, -27])
