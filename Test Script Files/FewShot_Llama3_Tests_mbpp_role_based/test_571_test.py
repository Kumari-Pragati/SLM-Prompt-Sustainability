import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessThanK(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5]
        N = len(arr)
        K = 2
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 9)

    def test_edge_case_K_zero(self):
        arr = [1, 2, 3, 4, 5]
        N = len(arr)
        K = 0
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 10)

    def test_edge_case_K_negative(self):
        arr = [1, 2, 3, 4, 5]
        N = len(arr)
        K = -1
        self.assertRaises(ValueError, max_sum_pair_diff_lessthan_K, arr, N, K)

    def test_edge_case_N_zero(self):
        arr = []
        N = len(arr)
        K = 2
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 0)

    def test_edge_case_N_one(self):
        arr = [1]
        N = len(arr)
        K = 2
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 1)

    def test_edge_case_N_two(self):
        arr = [1, 2]
        N = len(arr)
        K = 2
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 3)
