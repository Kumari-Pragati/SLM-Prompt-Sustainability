import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, -3, 4, -5, 6]
        expected = [1, 2, 4, -3, -5, 6]
        self.assertEqual(re_arrange(arr, len(arr)), expected)

    def test_edge_case_non_negative(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(re_arrange(arr, len(arr)), expected)

    def test_edge_case_non_positive(self):
        arr = [-1, -2, -3, -4, -5]
        expected = [-1, -2, -3, -4, -5]
        self.assertEqual(re_arrange(arr, len(arr)), expected)

    def test_edge_case_mixed(self):
        arr = [1, -2, 3, -4, 5]
        expected = [1, -2, 3, -4, 5]
        self.assertEqual(re_arrange(arr, len(arr)), expected)

    def test_corner_case_zero(self):
        arr = [0, 0, 0, 0, 0]
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(re_arrange(arr, len(arr)), expected)

    def test_corner_case_all_positive(self):
        arr = [1, 2, 3, 4, 5]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(re_arrange(arr, len(arr)), expected)

    def test_corner_case_all_negative(self):
        arr = [-1, -2, -3, -4, -5]
        expected = [-1, -2, -3, -4, -5]
        self.assertEqual(re_arrange(arr, len(arr)), expected)
