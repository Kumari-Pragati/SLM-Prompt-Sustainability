import unittest

from mbpp_187_code import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):

    def test_typical_case(self):
        X = "ABCDEF"
        Y = "ZBCDGHF"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 5)

    def test_edge_case(self):
        X = ""
        Y = "ZBCDGHF"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 0)

    def test_corner_case(self):
        X = "ABCDEF"
        Y = "ABCDEF"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 6)

    def test_invalid_input(self):
        X = "ABCDEF"
        Y = "ZBCDGHF"
        m = -1
        n = len(Y)
        with self.assertRaises(Exception):
            longest_common_subsequence(X, Y, m, n)
