import unittest
from mbpp_187_code import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):

    def test_typical_case(self):
        X = "AGGTAB"
        Y = "GXTXAYB"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 5)

    def test_edge_case_empty_string(self):
        X = ""
        Y = "GXTXAYB"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 0)

    def test_edge_case_one_char_string(self):
        X = "A"
        Y = "GXTXAYB"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 0)

    def test_error_case_non_string_input(self):
        X = 123
        Y = "GXTXAYB"
        m = len(X)
        n = len(Y)
        with self.assertRaises(TypeError):
            longest_common_subsequence(X, Y, m, n)
