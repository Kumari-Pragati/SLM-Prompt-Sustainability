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
        expected_output = 2
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), expected_output)

    def test_edge_case(self):
        X = ""
        Y = ""
        Z = ""
        m = 0
        n = 0
        o = 0
        expected_output = 0
        self.assertEqual(lcs_of_three(X, Y, Z, m, n, o), expected_output)

    def test_invalid_input(self):
        X = "ABCBDAB"
        Y = "BDCAB"
        Z = "BADACB"
        m = len(X)
        n = len(Y)
        o = len(Z)
        with self.assertRaises(TypeError):
            lcs_of_three(X, Y, Z, m, "invalid", o)
