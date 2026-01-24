import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessThanK(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4], 4, 2), 6)

    def test_edge_condition_empty_input(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([], 0, 2), 0)

    def test_edge_condition_single_element(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([5], 1, 10), 0)

    def test_edge_condition_K_equals_0(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4], 4, 0), 0)

    def test_complex_input(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 3, 1, 2], 4, 2), 5)

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            max_sum_pair_diff_lessthan_K([1, 2, 3, 4], 4, -1)
