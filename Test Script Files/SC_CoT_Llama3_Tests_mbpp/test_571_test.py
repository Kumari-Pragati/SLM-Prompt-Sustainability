import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessThanK(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 2), 9)

    def test_edge_case_K_is_zero(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 0), 0)

    def test_edge_case_K_is_one(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 1), 2)

    def test_edge_case_N_is_one(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1], 1, 2), 1)

    def test_edge_case_N_is_zero(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([], 0, 2), 0)

    def test_invalid_input_N_is_negative(self):
        with self.assertRaises(ValueError):
            max_sum_pair_diff_lessthan_K([-1, 2, 3, 4, 5], -1, 2)

    def test_invalid_input_K_is_negative(self):
        with self.assertRaises(ValueError):
            max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, -1)

    def test_invalid_input_N_and_K_are_zero(self):
        with self.assertRaises(ValueError):
            max_sum_pair_diff_lessthan_K([], 0, 0)
