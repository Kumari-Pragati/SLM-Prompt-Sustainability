import unittest
from mbpp_548_code import longest_increasing_subsequence

class TestLongestIncreasingSubsequence(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(longest_increasing_subsequence([3, 4, -1, 0, 6, 2, 3]), 4)
        self.assertEqual(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]), 6)

    def test_edge_cases(self):
        self.assertEqual(longest_increasing_subsequence([]), 0)
        self.assertEqual(longest_increasing_subsequence([1]), 1)
        self.assertEqual(longest_increasing_subsequence([1, 1]), 2)
        self.assertEqual(longest_increasing_subsequence([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
        self.assertEqual(longest_increasing_subsequence([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]), 10)
        self.assertEqual(longest_increasing_subsequence([-1, -2, -3]), 1)
        self.assertEqual(longest_increasing_subsequence([0, 0, 0]), 1)

    def test_decreasing_input(self):
        self.assertEqual(longest_increasing_subsequence([5, 4, 3, 2, 1]), 1)

    def test_duplicate_input(self):
        self.assertEqual(longest_increasing_subsequence([1, 1, 2, 3, 4, 4, 5, 6]), 6)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            longest_increasing_subsequence(1.5)
        with self.assertRaises(TypeError):
            longest_increasing_subsequence(("str",))
