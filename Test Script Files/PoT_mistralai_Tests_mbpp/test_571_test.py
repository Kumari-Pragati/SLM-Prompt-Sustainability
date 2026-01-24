import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessthanK(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4], 4, 1), 5)
        self.assertEqual(max_sum_pair_diff_lessthan_K([10, 20, 30, 40], 4, 30), 80)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 2), 12)

    def test_edge_case_empty_list(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([], 0, 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1], 1, 0), 1)

    def test_edge_case_two_elements(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2], 2, 1), 3)

    def test_edge_case_K_greater_than_array_sum(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3], 3, 4), 6)

    def test_edge_case_K_less_than_array_sum(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3], 3, 0), 6)

    def test_corner_case_decreasing_array(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([4, 3, 2, 1], 4, 1), 6)

    def test_corner_case_increasing_array(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4], 4, 1), 5)
