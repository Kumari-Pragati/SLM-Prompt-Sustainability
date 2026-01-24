import unittest
from mbpp_548_code import longest_increasing_subsequence

class TestLongestIncreasingSubsequence(unittest.TestCase):

    def test_empty_array(self):
        self.assertEqual(longest_increasing_subsequence([]), 0)

    def test_single_element_array(self):
        self.assertEqual(longest_increasing_subsequence([1]), 1)

    def test_increasing_array(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5]), 5)

    def test_decreasing_array(self):
        self.assertEqual(longest_increasing_subsequence([5, 4, 3, 2, 1]), 1)

    def test_mixed_array(self):
        self.assertEqual(longest_increasing_subsequence([1, 3, 2, 4, 5]), 4)

    def test_repeated_elements(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 2, 3, 4, 5]), 5)

    def test_edge_case(self):
        self.assertEqual(longest_increasing_subsequence([1, 1, 1, 1, 1]), 1)

    def test_max_value(self):
        self.assertEqual(longest_increasing_subsequence([10, 9, 8, 7, 6]), 1)

    def test_min_value(self):
        self.assertEqual(longest_increasing_subsequence([-10, -9, -8, -7, -6]), 1)
