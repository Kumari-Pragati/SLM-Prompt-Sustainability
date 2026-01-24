import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):

    def test_typical_case(self):
        X = "AGGTAB"
        Y = "GXTXAYB"
        m = len(X)
        n = len(Y)
        self.assertEqual(super_seq(X, Y, m, n), 6)

    def test_edge_case_X_empty(self):
        X = ""
        Y = "GXTXAYB"
        m = len(X)
        n = len(Y)
        self.assertEqual(super_seq(X, Y, m, n), len(Y))

    def test_edge_case_Y_empty(self):
        X = "AGGTAB"
        Y = ""
        m = len(X)
        n = len(Y)
        self.assertEqual(super_seq(X, Y, m, n), len(X))

    def test_edge_case_both_empty(self):
        X = ""
        Y = ""
        m = len(X)
        n = len(Y)
        self.assertEqual(super_seq(X, Y, m, n), 0)

    def test_explicitly_handled_error_case(self):
        X = "AGGTAB"
        Y = "GXTXAYB"
        m = 0
        n = len(Y)
        with self.assertRaises(IndexError):
            super_seq(X, Y, m, n)
