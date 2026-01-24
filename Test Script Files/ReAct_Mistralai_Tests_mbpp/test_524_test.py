import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sum_increasing_subsequence([], 0), 0)

    def test_single_element(self):
        for num in range(-100, 101):
            self.assertEqual(max_sum_increasing_subsequence([num], 1), num)

    def test_positive_numbers(self):
        arr = [1, 5, 7, 9, 15, 23, 31]
        self.assertEqual(max_sum_increasing_subsequence(arr, len(arr)), 59)

    def test_negative_numbers(self):
        arr = [-1, -5, -7, -9, -15, -23, -31]
        self.assertEqual(max_sum_increasing_subsequence(arr, len(arr)), -31)

    def test_mixed_numbers(self):
        arr = [1, -5, 7, -9, 15, -23, 31]
        self.assertEqual(max_sum_increasing_subsequence(arr, len(arr)), 31)

    def test_duplicates(self):
        arr = [1, 1, 5, 7, 7, 9, 15, 15, 23, 23, 31]
        self.assertEqual(max_sum_increasing_subsequence(arr, len(arr)), 46)

    def test_zero(self):
        self.assertEqual(max_sum_increasing_subsequence([0], 1), 0)
        self.assertEqual(max_sum_increasing_subsequence([0, 0], 2), 0)
        self.assertEqual(max_sum_increasing_subsequence([0, 0, 0], 3), 0)

    def test_negative_zero(self):
        self.assertEqual(max_sum_increasing_subsequence([-0], 1), 0)
        self.assertEqual(max_sum_increasing_subsequence([-0, -0], 2), 0)
        self.assertEqual(max_sum_increasing_subsequence([-0, -0, -0], 3), 0)

    def test_large_input(self):
        arr = [1] * 1000
        self.assertEqual(max_sum_increasing_subsequence(arr, len(arr)), sum(arr))
