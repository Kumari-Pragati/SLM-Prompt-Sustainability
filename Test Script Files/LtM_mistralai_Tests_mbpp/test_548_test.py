import unittest
from mbpp_548_code import longest_increasing_subsequence

class TestLongestIncreasingSubsequence(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(longest_increasing_subsequence([1, 2, 3]), 3)
        self.assertEqual(longest_increasing_subsequence([3, 2, 1]), 3)
        self.assertEqual(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(longest_increasing_subsequence([]), 0)
        self.assertEqual(longest_increasing_subsequence([1]), 1)
        self.assertEqual(longest_increasing_subsequence([1, 1]), 1)
        self.assertEqual(longest_increasing_subsequence([1, 2, 1]), 2)
        self.assertEqual(longest_increasing_subsequence([2, 1, 2]), 2)
        self.assertEqual(longest_increasing_subsequence([10, 20, 30, 40]), 4)
        self.assertEqual(longest_increasing_subsequence([10, 20, 30, 40, 50]), 5)

    def test_complex_and_corner_cases(self):
        self.assertEqual(longest_increasing_subsequence([10, 20, 10, 30, 20, 50]), 3)
        self.assertEqual(longest_increasing_subsequence([10, 20, 30, 20, 10, 50]), 3)
        self.assertEqual(longest_increasing_subsequence([10, 20, 30, 20, 10, 50, 10]), 4)
        self.assertEqual(longest_increasing_subsequence([10, 20, 30, 20, 10, 50, 10, 10]), 5)
