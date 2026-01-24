import unittest
from mbpp_747_code import lcs_of_three

class TestLcsOfThree(unittest.TestCase):

    def test_typical_case(self):
        X = "ABC"
        Y = "BCD"
        Z = "BCD"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 2)

    def test_edge_case1(self):
        X = "A"
        Y = "B"
        Z = "C"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 0)

    def test_edge_case2(self):
        X = "ABC"
        Y = "BCD"
        Z = "BCDE"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 2)

    def test_edge_case3(self):
        X = "ABC"
        Y = "BCD"
        Z = "BC"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 2)

    def test_edge_case4(self):
        X = "ABC"
        Y = "BCD"
        Z = "A"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 1)

    def test_edge_case5(self):
        X = "ABC"
        Y = "BCD"
        Z = ""
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 0)

    def test_edge_case6(self):
        X = ""
        Y = "BCD"
        Z = "BCD"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 0)

    def test_edge_case7(self):
        X = "ABC"
        Y = ""
        Z = "BCD"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 0)

    def test_edge_case8(self):
        X = ""
        Y = ""
        Z = "BCD"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 0)
