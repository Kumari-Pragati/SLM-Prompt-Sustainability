import unittest
from mbpp_747_code import lcs_of_three

class TestLCSofThree(unittest.TestCase):

    def test_lcs_of_three_typical_case(self):
        X = "ABC"
        Y = "BCD"
        Z = "BCD"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 2)

    def test_lcs_of_three_edge_case(self):
        X = "A"
        Y = "B"
        Z = "C"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 0)

    def test_lcs_of_three_error_case(self):
        X = "ABC"
        Y = "BCD"
        Z = "BCD"
        m = len(X)
        n = len(Y)
        o = 0
        with self.assertRaises(IndexError):
            lcs_of_three(X, Y, Z, m, n, o)

    def test_lcs_of_three_zero_length(self):
        X = ""
        Y = "BCD"
        Z = "BCD"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 0)

    def test_lcs_of_three_all_equal(self):
        X = "ABC"
        Y = "ABC"
        Z = "ABC"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 3)
