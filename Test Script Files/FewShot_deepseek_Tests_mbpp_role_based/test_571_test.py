import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessThanK(unittest.TestCase):
    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        N = len(arr)
        K = 2
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 10)

    def test_edge_case_small_k(self):
        arr = [1, 2, 3, 4, 5]
        N = len(arr)
        K = 0
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 9)

    def test_boundary_case_k_equals_max_diff(self):
        arr = [1, 2, 3, 4, 5]
        N = len(arr)
        K = 5
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 9)

    def test_invalid_input_negative_k(self):
        arr = [1, 2, 3, 4, 5]
        N = len(arr)
        K = -1
        with self.assertRaises(Exception):
            max_sum_pair_diff_lessthan_K(arr, N, K)

    def test_invalid_input_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        N = len(arr)
        K = 2
        with self.assertRaises(Exception):
            max_sum_pair_diff_lessthan_K(arr, N, K)
