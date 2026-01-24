import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessthanK(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 1), 10)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 2), 12)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 3), 15)

    def test_edge_input(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 1, 1), 2)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 2, 1), 6)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 0), 10)
        self.assertEqual(max_sum_pair_diff_lessthan_K([], 0, 1), 0)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1], 1, 1), 1)

    def test_boundary_input(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3], 3, 1), 9)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3], 2, 1), 7)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3], 1, 1), 4)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3], 0, 1), 3)
