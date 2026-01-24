import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sum_increasing_subsequence([], 0), 0)

    def test_single_element(self):
        self.assertEqual(max_sum_increasing_subsequence([1], 1), 1)

    def test_simple_case(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 5, 3, 4, 2], 5), 7)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_increasing_subsequence([-1, -2, -3, -4, -5], 5), -1)

    def test_duplicates(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 1, 1, 1, 1], 5), 5)

    def test_large_numbers(self):
        self.assertEqual(max_sum_increasing_subsequence([1000000001, 1000000002, 1000000003, 1000000004, 1000000005], 5), 2500000015)
