import unittest
from mbpp_548_code import longest_increasing_subsequence

class TestLongestIncreasingSubsequence(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_edge_case_single_element(self):
        self.assertEqual(longest_increasing_subsequence([5]), 1)

    def test_boundary_case_empty_list(self):
        self.assertEqual(longest_increasing_subsequence([]), 0)

    def test_corner_case_decreasing_sequence(self):
        self.assertEqual(longest_increasing_subsequence([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 1)

    def test_corner_case_increasing_sequence(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)

    def test_corner_case_duplicate_elements(self):
        self.assertEqual(longest_increasing_subsequence([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 1)

    def test_corner_case_all_same_elements(self):
        self.assertEqual(longest_increasing_subsequence([5, 5, 5, 5, 5, 5, 5, 5, 5, 5]), 1)
