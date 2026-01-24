import unittest
from mbpp_548_code import longest_increasing_subsequence

class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(longest_increasing_subsequence([]), 0)

    def test_single_element_list(self):
        self.assertEqual(longest_increasing_subsequence([1]), 1)

    def test_increasing_list(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5]), 5)

    def test_decreasing_list(self):
        self.assertEqual(longest_increasing_subsequence([5, 4, 3, 2, 1]), 1)

    def test_duplicate_elements(self):
        self.assertEqual(longest_increasing_subsequence([1, 1, 2, 3, 4, 4, 5]), 3)

    def test_negative_numbers(self):
        self.assertEqual(longest_increasing_subsequence([-1, -2, -3, -4, -5]), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            longest_increasing_subsequence(1.5)
