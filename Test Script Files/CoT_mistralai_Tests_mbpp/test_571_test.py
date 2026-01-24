import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessthanK(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([], 0, 0), 0)

    def test_single_element_array(self):
        for k in range(0, 10):
            self.assertEqual(max_sum_pair_diff_lessthan_K([1], 1, k), 1)

    def test_positive_numbers(self):
        arr = [1, 2, 3, 4, 5]
        for k in range(0, 10):
            self.assertEqual(max_sum_pair_diff_lessthan_K(arr, len(arr), k), 9)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        for k in range(0, 10):
            self.assertEqual(max_sum_pair_diff_lessthan_K(arr, len(arr), k), 9)

    def test_mixed_numbers(self):
        arr = [1, -2, 3, -4, 5]
        for k in range(0, 10):
            self.assertEqual(max_sum_pair_diff_lessthan_K(arr, len(arr), k), 10)

    def test_zero(self):
        arr = [0, 0]
        for k in range(0, 10):
            self.assertEqual(max_sum_pair_diff_lessthan_K(arr, len(arr), k), 0)

    def test_large_difference(self):
        arr = [1, 1000000000]
        for k in range(0, 1000000001):
            self.assertEqual(max_sum_pair_diff_lessthan_K(arr, len(arr), k), 1000000001)

    def test_invalid_k(self):
        arr = [1, 2]
        with self.assertRaises(ValueError):
            max_sum_pair_diff_lessthan_K(arr, 2, -1)

    def test_invalid_array(self):
        with self.assertRaises(TypeError):
            max_sum_pair_diff_lessthan_K(1, 2, 3)
