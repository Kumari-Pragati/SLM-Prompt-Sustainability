import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessThanK(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 2), 9)

    def test_edge_case_K_zero(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 0), 0)

    def test_edge_case_N_one(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1], 1, 2), 1)

    def test_edge_case_N_two(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2], 2, 2), 3)

    def test_edge_case_K_greater_than_max_diff(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 10), 10)

    def test_edge_case_K_equal_to_max_diff(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 3), 6)

    def test_edge_case_N_zero(self):
        with self.assertRaises(IndexError):
            max_sum_pair_diff_lessthan_K([], 0, 2)

    def test_edge_case_N_negative(self):
        with self.assertRaises(IndexError):
            max_sum_pair_diff_lessthan_K([-1, 2, 3, 4, 5], -1, 2)

    def test_edge_case_K_negative(self):
        with self.assertRaises(IndexError):
            max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, -2)
