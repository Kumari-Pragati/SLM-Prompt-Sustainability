import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessThanK(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([], 0, 0), 0)

    def test_single_element_array(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1], 1, 0), 1)

    def test_two_element_array(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2], 2, 0), 3)

    def test_edge_case_K_zero(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3], 3, 0), 6)

    def test_edge_case_K_one(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3], 3, 1), 3)

    def test_edge_case_K_greater_than_max_diff(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3], 3, 4), 6)

    def test_edge_case_N_one(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1], 1, 0), 1)

    def test_edge_case_N_two(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2], 2, 0), 3)

    def test_edge_case_N_three(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3], 3, 0), 6)

    def test_edge_case_N_greater_than_max_diff(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 0), 9)

    def test_edge_case_N_greater_than_max_diff_K_greater_than_max_diff(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 4), 9)

    def test_edge_case_N_greater_than_max_diff_K_greater_than_max_diff_N_greater_than_max_diff(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5, 6], 6, 4), 12)
