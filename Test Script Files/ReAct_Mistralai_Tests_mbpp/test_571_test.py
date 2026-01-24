import unittest
from mbpp_571_code import max_sum_pair_diff_lessthan_K

class TestMaxSumPairDiffLessthanK(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(max_sum_pair_diff_lessthan_K([], 0, 1), 0)

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
            self.assertEqual(max_sum_pair_diff_lessthan_K(arr, len(arr), k), 11)

    def test_zero_in_array(self):
        arr = [0, 1, 2, 3, 4]
        for k in range(0, 10):
            self.assertEqual(max_sum_pair_diff_lessthan_K(arr, len(arr), k), 8)

    def test_negative_k(self):
        with self.assertRaises(ValueError):
            max_sum_pair_diff_lessthan_K([1, 2, 3], 3, -1)

    def test_negative_N(self):
        with self.assertRaises(ValueError):
            max_sum_pair_diff_lessthan_K([1, 2, 3], -1, 1)

    def test_empty_K(self):
        with self.assertRaises(ValueError):
            max_sum_pair_diff_lessthan_K([1, 2, 3], 3, 0)
