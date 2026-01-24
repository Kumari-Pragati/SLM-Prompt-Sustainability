import unittest
from mbpp_187_code import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):

    def test_typical_case(self):
        X = "ABCBDAB"
        Y = "BDCAB"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 4)

    def test_edge_case_zero_m(self):
        X = "ABCBDAB"
        Y = "BDCAB"
        m = 0
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 0)

    def test_edge_case_zero_n(self):
        X = "ABCBDAB"
        Y = "BDCAB"
        m = len(X)
        n = 0
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 0)

    def test_edge_case_m_equal_n(self):
        X = "ABCBDAB"
        Y = "BDCAB"
        m = len(X)
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 4)

    def test_edge_case_m_greater_than_n(self):
        X = "ABCBDAB"
        Y = "BDCAB"
        m = len(X) + 1
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 4)

    def test_edge_case_n_greater_than_m(self):
        X = "ABCBDAB"
        Y = "BDCAB"
        m = len(X)
        n = len(Y) + 1
        self.assertEqual(longest_common_subsequence(X, Y, m, n), 4)

    def test_edge_case_m_equal_zero(self):
        X = ""
        Y = "BDCAB"
        n = len(Y)
        self.assertEqual(longest_common_subsequence(X, Y, m=0, n=n), 0)

    def test_edge_case_n_equal_zero(self):
        X = "ABCBDAB"
        Y = ""
        m = len(X)
        self.assertEqual(longest_common_subsequence(X, Y, m, n=0), 0)

    def test_invalid_input_type(self):
        X = "ABCBDAB"
        Y = "BDCAB"
        m = len(X)
        n = len(Y)
        with self.assertRaises(TypeError):
            longest_common_subsequence(X, Y, m, 'n')

    def test_invalid_input_value(self):
        X = "ABCBDAB"
        Y = "BDCAB"
        m = len(X)
        n = len(Y)
        with self.assertRaises(ValueError):
            longest_common_subsequence(X, Y, m, n=-1)
