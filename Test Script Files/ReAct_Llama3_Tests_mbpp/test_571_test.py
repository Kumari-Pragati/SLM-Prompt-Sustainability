import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessThanK(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        N = len(arr)
        K = 2
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 9)

    def test_edge_case_K_zero(self):
        arr = [1, 2, 3, 4, 5]
        N = len(arr)
        K = 0
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 0)

    def test_edge_case_K_large(self):
        arr = [1, 2, 3, 4, 5]
        N = len(arr)
        K = 100
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 14)

    def test_edge_case_N_one(self):
        arr = [1]
        N = len(arr)
        K = 2
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 1)

    def test_edge_case_N_zero(self):
        arr = []
        N = len(arr)
        K = 2
        with self.assertRaises(IndexError):
            max_sum_pair_diff_lessthan_K(arr, N, K)

    def test_edge_case_K_negative(self):
        arr = [1, 2, 3, 4, 5]
        N = len(arr)
        K = -2
        with self.assertRaises(ValueError):
            max_sum_pair_diff_lessthan_K(arr, N, K)
