import unittest
from mbpp_623_code import nth_nums

class TestNthNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(nth_nums([1, 2, 3], 2), [1, 4, 9])

    def test_edge_case_negative(self):
        self.assertEqual(nth_nums([-1, -2, -3], 2), [1, 4, 9])

    def test_edge_case_zero(self):
        self.assertEqual(nth_nums([1, 2, 3], 0), [1, 2, 3])

    def test_edge_case_one(self):
        self.assertEqual(nth_nums([1, 2, 3], 1), [1, 2, 3])

    def test_edge_case_empty_list(self):
        self.assertEqual(nth_nums([], 2), [])

    def test_edge_case_single_element(self):
        self.assertEqual(nth_nums([1], 2), [1])

    def test_edge_case_negative_power(self):
        self.assertEqual(nth_nums([1, 2, 3], -2), [1, 1/4, 1/9])
