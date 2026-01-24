import unittest
from mbpp_548_code import longest_increasing_subsequence

class TestLongestIncreasingSubsequence(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]), 5)

    def test_edge_case(self):
        self.assertEqual(longest_increasing_subsequence([1]), 1)

    def test_boundary_case(self):
        self.assertEqual(longest_increasing_subsequence([]), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            longest_increasing_subsequence("10, 22, 9, 33, 21, 50, 41, 60, 80")

        with self.assertRaises(TypeError):
            longest_increasing_subsequence(10)

        with self.assertRaises(TypeError):
            longest_increasing_subsequence(None)
