import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(re_arrange([], 0), [])

    def test_single_element(self):
        self.assertEqual(re_arrange([1], 0), [1])
        self.assertEqual(re_arrange([-1], 0), [-1])

    def test_positive_even_length(self):
        self.assertEqual(re_arrange([1, 2, 3, 4], 4), [1, 4, 3, 2])
        self.assertEqual(re_arrange([10, 20, 30, 40], 4), [10, 40, 30, 20])

    def test_positive_odd_length(self):
        self.assertEqual(re_arrange([1, 2, 3], 3), [1, 3, 2])
        self.assertEqual(re_arrange([10, 20, 30], 3), [10, 30, 20])

    def test_negative_even_length(self):
        self.assertEqual(re_arrange([-1, -2, -3, -4], 4), [-1, -4, -3, -2])
        self.assertEqual(re_arrange([-10, -20, -30, -40], 4), [-10, -40, -30, -20])

    def test_negative_odd_length(self):
        self.assertEqual(re_arrange([-1, -2, -3], 3), [-1, -3, -2])
        self.assertEqual(re_arrange([-10, -20, -30], 3), [-10, -30, -20])

    def test_mixed_positive_and_negative(self):
        self.assertEqual(re_arrange([1, -2, 3, -4], 4), [1, -4, 3, -2])
        self.assertEqual(re_arrange([10, -20, 30, -40], 4), [10, -40, 30, -20])

    def test_edge_case_zero_length(self):
        with self.assertRaises(IndexError):
            re_arrange([], 0)

    def test_edge_case_negative_index(self):
        with self.assertRaises(IndexError):
            re_arrange([1, 2, 3], -1)
