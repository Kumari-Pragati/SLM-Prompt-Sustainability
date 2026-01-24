import unittest
from mbpp_747_code import lcs_of_three

class TestLCSOfThree(unittest.TestCase):

    def test_lcs_of_three(self):
        X = "ABCBDAB"
        Y = "BDCAB"
        Z = "BADACB"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 3)

        X = "ABC"
        Y = "ABC"
        Z = "ABC"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 3)

        X = "ABC"
        Y = "DEF"
        Z = "GHI"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 0)
