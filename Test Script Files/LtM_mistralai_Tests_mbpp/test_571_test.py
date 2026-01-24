import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessthanK(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3], 3, 1), 4)
        self.assertEqual(max_sum_pair_diff_lessthan_K([4, 6, 10], 3, 3), 13)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4], 4, 1), 8)

    def test_edge_and_boundary(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([], 0, 1), 0)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1], 1, 1), 1)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2], 2, 0), 3)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3], 3, 4), 6)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3], 1, 2), 4)
