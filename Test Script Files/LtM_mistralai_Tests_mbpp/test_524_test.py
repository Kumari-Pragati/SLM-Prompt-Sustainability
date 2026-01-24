import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4], 4), 7)
        self.assertEqual(max_sum_increasing_subsequence([5, 17, 5, 10], 4), 22)

    def test_edge_cases(self):
        self.assertEqual(max_sum_increasing_subsequence([], 0), 0)
        self.assertEqual(max_sum_increasing_subsequence([1], 1), 1)
        self.assertEqual(max_sum_increasing_subsequence([1, 2], 2), 3)
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5], 5), 15)

    def test_boundary_conditions(self):
        self.assertEqual(max_sum_increasing_subsequence([-1, -2, -3, -4], 4), -1)
        self.assertEqual(max_sum_increasing_subsequence([0, 0, 0, 0], 4), 0)
        self.assertEqual(max_sum_increasing_subsequence([1000000000, 1000000000, 1000000000, 1000000000], 4), 4000000000)
