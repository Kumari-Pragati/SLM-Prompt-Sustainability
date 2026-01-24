import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(max_sum_increasing_subsequence([], 0), 0)

    def test_single_element_array(self):
        self.assertEqual(max_sum_increasing_subsequence([1], 1), 1)

    def test_increasing_subsequence(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5], 5), 15)

    def test_decreasing_subsequence(self):
        self.assertEqual(max_sum_increasing_subsequence([5, 4, 3, 2, 1], 5), 1)

    def test_non_increasing_subsequence(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 3, 2, 4, 5], 5), 9)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_increasing_subsequence([-1, -2, -3, -4, -5], 5), -1)

    def test_zero_sum(self):
        self.assertEqual(max_sum_increasing_subsequence([0, 0, 0, 0, 0], 5), 0)
