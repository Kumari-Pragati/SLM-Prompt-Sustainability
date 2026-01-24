import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessThanK(unittest.TestCase):

    def test_max_sum_pair_diff_lessthan_K(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 1), 9)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 2), 10)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 3), 11)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 4), 12)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 5), 15)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 6), 15)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 7), 15)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 8), 15)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 9), 15)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 10), 15)

    def test_max_sum_pair_diff_lessthan_K_edge_cases(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1], 1, 1), 1)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2], 2, 1), 3)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3], 3, 1), 6)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4], 4, 1), 9)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 0), 10)
