import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):
    def test_positive_numbers(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(max_sum_increasing_subsequence(arr, len(arr)), 15)

    def test_empty_list(self):
        arr = []
        self.assertEqual(max_sum_increasing_subsequence(arr, len(arr)), 0)

    def test_negative_numbers(self):
        arr = [-1, -2, -3, -4, -5]
        self.assertEqual(max_sum_increasing_subsequence(arr, len(arr)), -15)

    def test_mixed_numbers(self):
        arr = [1, -2, 3, -4, 5]
        self.assertEqual(max_sum_increasing_subsequence(arr, len(arr)), 11)

    def test_single_element(self):
        arr = [1]
        self.assertEqual(max_sum_increasing_subsequence(arr, len(arr)), 1)

    def test_zero(self):
        arr = [0]
        self.assertEqual(max_sum_increasing_subsequence(arr, len(arr)), 0)

    def test_negative_zero(self):
        arr = [-0]
        self.assertEqual(max_sum_increasing_subsequence(arr, len(arr)), 0)
