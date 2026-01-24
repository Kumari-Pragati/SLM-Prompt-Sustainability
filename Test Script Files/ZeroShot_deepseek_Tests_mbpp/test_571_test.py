import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiff(unittest.TestCase):

    def test_max_sum_pair_diff_lessthan_K(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 2), 10)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5], 5, 1), 9)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 3, 5, 7, 9], 5, 2), 24)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 3, 5, 7, 9], 5, 1), 20)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5, 6], 6, 2), 15)
        self.assertEqual(max_sum_pair_diff_lessthan_K([1, 2, 3, 4, 5, 6], 6, 1), 14)
