import unittest
from mbpp_187_code import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):
    def test_typical_case(self):
        X = "ABCDEF"
        Y = "ACDFE"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 5)

    def test_edge_case(self):
        X = ""
        Y = "ACDFE"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 0)

    def test_boundary_case(self):
        X = "ABCDEF"
        Y = ""
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 0)

    def test_typical_case_2(self):
        X = "AGGTAB"
        Y = "GXTXAYB"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 5)

    def test_invalid_input(self):
        X = "ABCDEF"
        Y = "ACDFE"
        m = -1
        n = len(Y)
        with self.assertRaises(ValueError):
            longest_common_subsequence(X, Y, m, n)
