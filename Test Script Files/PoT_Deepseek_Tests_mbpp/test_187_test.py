import unittest
from mbpp_187_code import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):

    def test_typical_case(self):
        X = "ABCDGH"
        Y = "AEDFHR"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 3)

    def test_edge_case(self):
        X = ""
        Y = "AEDFHR"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 0)

    def test_boundary_case(self):
        X = "ABCDGH"
        Y = ""
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 0)

    def test_corner_case(self):
        X = "ABCDEF"
        Y = "ABCDEF"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 6)

    def test_tricky_case(self):
        X = "ABCDEF"
        Y = "FECBAD"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 6)
