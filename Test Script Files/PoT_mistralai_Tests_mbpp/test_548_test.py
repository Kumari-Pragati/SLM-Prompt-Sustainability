import unittest
from mbpp_548_code import longest_increasing_subsequence

class TestLongestIncreasingSubsequence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(longest_increasing_subsequence([3, 4, -1, 0, 6, 2, 3]), 5)
        self.assertEqual(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]), 9)

    def test_edge_case_single_element(self):
        self.assertEqual(longest_increasing_subsequence([1]), 1)

    def test_edge_case_empty_list(self):
        self.assertEqual(longest_increasing_subsequence([]), 0)

    def test_edge_case_decreasing_sequence(self):
        self.assertEqual(longest_increasing_subsequence([6, 5, 4, 3, 2]), 1)

    def test_edge_case_duplicates(self):
        self.assertEqual(longest_increasing_subsequence([1, 1, 1, 1]), 1)
        self.assertEqual(longest_increasing_subsequence([1, 2, 2, 3]), 3)
