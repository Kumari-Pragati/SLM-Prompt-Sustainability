import unittest
from mbpp_323_code import re_arrange

class TestReArrange(unittest.TestCase):

    def test_simple_positive_even(self):
        self.assertEqual(re_arrange([1, 2, 3, 4], 4), [1, 4, 2, 3])

    def test_simple_positive_odd(self):
        self.assertEqual(re_arrange([1, 2, 3, 4, 5], 5), [1, 5, 2, 4, 3])

    def test_simple_negative_even(self):
        self.assertEqual(re_arrange([-1, -2, -3, -4], 4), [-1, -4, -2, -3])

    def test_simple_negative_odd(self):
        self.assertEqual(re_arrange([-1, -2, -3, -4, -5], 5), [-1, -5, -2, -4, -3])

    def test_edge_empty_list(self):
        self.assertEqual(re_arrange([], 0), [])

    def test_edge_single_element(self):
        self.assertEqual(re_arrange([1], 1), [1])

    def test_edge_min_positive(self):
        self.assertEqual(re_arrange([0, 1, 2, 3], 4), [1, 2, 3, 0])

    def test_edge_max_negative(self):
        self.assertEqual(re_arrange([-1, -2, -3, -4], 4), [-4, -3, -2, -1])

    def test_edge_min_positive_single(self):
        self.assertEqual(re_arrange([0], 1), [0])

    def test_edge_max_negative_single(self):
        self.assertEqual(re_arrange([-1], 1), [-1])

    def test_edge_min_positive_even(self):
        self.assertEqual(re_arrange([0, 1, 2], 3), [1, 2, 0])

    def test_edge_max_negative_even(self):
        self.assertEqual(re_arrange([-1, -2, -3], 3), [-3, -2, -1])

    def test_edge_min_positive_odd(self):
        self.assertEqual(re_arrange([0, 1, 2, 3], 4), [1, 3, 2, 0])

    def test_edge_max_negative_odd(self):
        self.assertEqual(re_arrange([-1, -2, -3, -4], 4), [-4, -3, -2, -1])

    def test_complex_mixed_positive_negative(self):
        self.assertEqual(re_arrange([1, -2, 3, -4, 5], 5), [1, 5, -4, -2, 3])

    def test_complex_mixed_positive_negative_even_length(self):
        self.assertEqual(re_arrange([1, -2, 3, -4, 5, 6], 6), [1, 6, -4, -2, 3, 5])
