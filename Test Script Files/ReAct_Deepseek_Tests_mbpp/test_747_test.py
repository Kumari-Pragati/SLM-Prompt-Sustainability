import unittest
from mbpp_747_code import lcs_of_three

class TestLCSOfThree(unittest.TestCase):

    def test_typical_case(self):
        X = "ABCBDAB"
        Y = "BDCAB"
        Z = "BADACB"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 2)

    def test_edge_case(self):
        X = ""
        Y = ""
        Z = ""
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 0)

    def test_error_case(self):
        X = "ABC"
        Y = "DEF"
        Z = "GHI"
        m = len(X)
        n = len(Y)
        o = len(Z)
        with self.assertRaises(Exception):
            lcs_of_three(X, Y, Z, m, n, o)
