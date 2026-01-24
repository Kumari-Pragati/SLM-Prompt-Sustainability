import unittest
from mbpp_548_code import longest_increasing_subsequence

class TestLongestIncreasingSubsequence(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(longest_increasing_subsequence([]), 0)

    def test_single_element_list(self):
        for num in range(10):
            self.assertEqual(longest_increasing_subsequence([num]), 1)

    def test_increasing_list(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(longest_increasing_subsequence(arr), len(arr))

    def test_decreasing_list(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(longest_increasing_subsequence(arr), 1)

    def test_duplicates_in_list(self):
        arr = [1, 1, 2, 3, 4, 4, 5]
        self.assertEqual(longest_increasing_subsequence(arr), 3)

    def test_negative_numbers_in_list(self):
        arr = [-1, -2, -3, 4, 5]
        self.assertEqual(longest_increasing_subsequence(arr), 3)

    def test_zero_in_list(self):
        arr = [0, 1, 2, 3, 4]
        self.assertEqual(longest_increasing_subsequence(arr), 4)
