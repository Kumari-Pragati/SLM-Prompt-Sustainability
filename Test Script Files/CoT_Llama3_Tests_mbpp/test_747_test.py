import unittest
from mbpp_747_code import lcs_of_three

class TestLcsOfThree(unittest.TestCase):

    def test_lcs_of_three_typical(self):
        X = "abc"
        Y = "bca"
        Z = "abc"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 3)

    def test_lcs_of_three_edge(self):
        X = "a"
        Y = "a"
        Z = "a"
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 1)

    def test_lcs_of_three_invalid_input(self):
        X = "abc"
        Y = "bca"
        Z = ""
        m = len(X)
        n = len(Y)
        o = len(Z)
        with self.assertRaises(IndexError):
            lcs_of_three(X, Y, Z, m, n, o)

    def test_lcs_of_three_empty_input(self):
        X = ""
        Y = ""
        Z = ""
        m = len(X)
        n = len(Y)
        o = len(Z)
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 0)
