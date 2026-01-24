import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):

    def test_max_sum_increasing_subsequence(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 101, 100, 2, 3, 100, 4, 5], 8), 305)
        self.assertEqual(max_sum_increasing_subsequence([10, 5, 4, 3], 4), 10)
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5], 5), 15)
        self.assertEqual(max_sum_increasing_subsequence([5, 4, 3, 2, 1], 5), 5)
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 55)
