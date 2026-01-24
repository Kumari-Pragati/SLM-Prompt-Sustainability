import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 5, 2, 9, 4, 5, 6, 3], 8), 18)
        self.assertEqual(max_sum_increasing_subsequence([-1, -2, -3, -4, -5], 5), -1)
        self.assertEqual(max_sum_increasing_subsequence([0, 3, 2, 1], 4), 6)

    def test_edge_case_empty_list(self):
        self.assertEqual(max_sum_increasing_subsequence([], 0), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(max_sum_increasing_subsequence([1], 1), 1)

    def test_edge_case_decreasing_sequence(self):
        self.assertEqual(max_sum_increasing_subsequence([5, 4, 3, 2, 1], 5), 6)

    def test_corner_case_duplicates(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 1, 2, 3, 4], 5), 7)
