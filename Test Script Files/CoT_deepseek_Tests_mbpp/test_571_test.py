import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessThanK(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        N = len(arr)
        K = 2
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 10)

    def test_edge_case_with_small_k(self):
        arr = [1, 2, 3, 4, 5]
        N = len(arr)
        K = 0
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 9)

    def test_edge_case_with_large_k(self):
        arr = [1, 2, 3, 4, 5]
        N = len(arr)
        K = 10
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 0)

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
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 0)

    def test_invalid_input_empty_array(self):
        arr = []
        N = 0
        K = 2
        with self.assertRaises(Exception):
            max_sum_pair_diff_lessthan_K(arr, N, K)
