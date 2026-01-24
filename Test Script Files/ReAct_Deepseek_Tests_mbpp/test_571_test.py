import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessThanK(unittest.TestCase):

    def test_typical_case(self):
        arr = [1, 2, 3, 4, 5]
        N = len(arr)
        K = 2
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 10)

    def test_edge_case_single_element(self):
        arr = [5]
        N = len(arr)
        K = 10
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 0)

    def test_edge_case_empty_array(self):
        arr = []
        N = len(arr)
        K = 10
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 0)

    def test_error_case_negative_elements(self):
        arr = [-1, -2, -3, -4, -5]
        N = len(arr)
        K = 2
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 0)

    def test_error_case_large_K(self):
        arr = [1, 2, 3, 4, 5]
        N = len(arr)
        K = 10
        self.assertEqual(max_sum_pair_diff_lessthan_K(arr, N, K), 15)
