import unittest
from mbpp_548_code import longest_increasing_subsequence

class TestLongestIncreasingSubsequence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(longest_increasing_subsequence([]), 0)

    def test_single_element(self):
        self.assertEqual(longest_increasing_subsequence([1]), 1)

    def test_increasing_sequence(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5]), 5)

    def test_decreasing_sequence(self):
        self.assertEqual(longest_increasing_subsequence([5, 4, 3, 2, 1]), 1)

    def test_random_sequence(self):
        self.assertEqual(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]), 5)
