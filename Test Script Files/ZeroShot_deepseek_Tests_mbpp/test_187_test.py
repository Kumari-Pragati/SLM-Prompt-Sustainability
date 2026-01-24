import unittest
from mbpp_187_code import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):

    def test_empty_strings(self):
        X = ""
        Y = ""
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 0)

    def test_same_strings(self):
        X = "ABCDEF"
        Y = "ABCDEF"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 6)

    def test_different_strings(self):
        X = "ABCDEF"
        Y = "123456"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 0)

    def test_common_subsequence(self):
        X = "ABCDEF"
        Y = "A1B2C3D4EF"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 6)
