import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):

    def test_max_sum_increasing_subsequence(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5], 5), 9)
        self.assertEqual(max_sum_increasing_subsequence([5, 6, 9, 10, 17, 12, 15], 7), 25)
        self.assertEqual(max_sum_increasing_subsequence([10, 22, 9, 10, 5, 12, 7, 9, 2], 9), 36)
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9], 9), 18)
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10), 18)

    def test_max_sum_increasing_subsequence_edge_cases(self):
        self.assertEqual(max_sum_increasing_subsequence([1], 1), 1)
        self.assertEqual(max_sum_increasing_subsequence([1, 1], 2), 1)
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 1], 3), 3)
