import unittest
from mbpp_524_code import max_sum_increasing_subsequence

class TestMaxSumIncreasingSubsequence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_sum_increasing_subsequence([], 0), 0)

    def test_single_element(self):
        self.assertEqual(max_sum_increasing_subsequence([1], 1), 1)

    def test_increasing_sequence(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 2, 3, 4, 5], 5), 15)

    def test_decreasing_sequence(self):
        self.assertEqual(max_sum_increasing_subsequence([5, 4, 3, 2, 1], 5), 6)

    def test_mixed_sequence(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 5, 2, 3, 4], 5), 9)

    def test_negative_numbers(self):
        self.assertEqual(max_sum_increasing_subsequence([-1, -2, -3, -4, -5], 5), -1)

    def test_duplicates(self):
        self.assertEqual(max_sum_increasing_subsequence([1, 1, 2, 3, 4], 5), 7)

    def test_invalid_input_empty_list(self):
        with self.assertRaises(ValueError):
            max_sum_increasing_subsequence([], 'not_an_integer')

    def test_invalid_input_negative_list(self):
        with self.assertRaises(ValueError):
            max_sum_increasing_subsequence([-1, -2, -3], 'not_an_integer')
