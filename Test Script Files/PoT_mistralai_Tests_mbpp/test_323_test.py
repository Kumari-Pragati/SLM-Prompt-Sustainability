import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):

    def test_typical_case_positive_numbers(self):
        self.assertEqual(re_arrange([1, 2, 3, -1, -2, -3], 6), [1, 3, -1, 2, -3, -2])
        self.assertEqual(re_arrange([-1, 2, 3, -1, -2, -3], 6), [3, -1, 2, -3, -1, -2])
        self.assertEqual(re_arrange([1, -1, 2, -1, 3, -1], 6), [1, 3, -1, 2, -1, -1])

    def test_typical_case_negative_numbers(self):
        self.assertEqual(re_arrange([-1, -2, -3, 1, 2, 3], 6), [-3, -1, -2, 1, 2, 3])
        self.assertEqual(re_arrange([3, -2, -1, -3, 1, 2], 6), [-1, -3, -2, 3, 1, 2])
        self.assertEqual(re_arrange([-3, 1, -2, 3, -1, 2], 6), [-2, -3, 1, -1, 3, 2])

    def test_edge_case_even_length(self):
        self.assertEqual(re_arrange([1, 2, 3, -1], 4), [1, 3, -1, 2])
        self.assertEqual(re_arrange([-1, 2, 3, -1], 4), [3, -1, 2, -1])

    def test_edge_case_odd_length(self):
        self.assertEqual(re_arrange([1, 2, 3, -1], 5), [1, 3, -1, 2, -1])
        self.assertEqual(re_arrange([-1, 2, 3, -1], 5), [3, -1, 2, -1, 1])

    def test_corner_case_all_positive(self):
        self.assertEqual(re_arrange([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_corner_case_all_negative(self):
        self.assertEqual(re_arrange([-1, -2, -3, -4, -5], 5), [-5, -4, -3, -2, -1])

    def test_corner_case_empty_list(self):
        self.assertEqual(re_arrange([], 0), [])

    def test_corner_case_single_element(self):
        self.assertEqual(re_arrange([1], 1), [1])
