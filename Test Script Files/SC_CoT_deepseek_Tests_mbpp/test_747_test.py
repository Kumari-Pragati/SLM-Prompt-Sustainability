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
        m = 0
        n = 0
        o = 0
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 0)

    def test_corner_case(self):
        X = "A"
        Y = "B"
        Z = "C"
        m = 1
        n = 1
        o = 1
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), 0)

    def test_invalid_input(self):
        X = 123
        Y = "BDCAB"
        Z = "BADACB"
        m = 3
        n = len(Y)
        o = len(Z)
        with self.assertRaises(TypeError):
            lcs_of_three(X, Y, Z, m, n, o)
