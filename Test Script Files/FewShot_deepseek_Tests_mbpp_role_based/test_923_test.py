import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):
    def test_typical_case(self):
        X = "AGGTAB"
        Y = "GXTXAYB"
        m = len(X)
        n = len(Y)
        self.assertEqual(super_seq(X, Y, m, n), 6)

    def test_edge_case(self):
        X = ""
        Y = "GXTXAYB"
        m = len(X)
        n = len(Y)
        self.assertEqual(super_seq(X, Y, m, n), len(Y))

    def test_boundary_case(self):
        X = "AGGTAB"
        Y = ""
        m = len(X)
        n = len(Y)
        self.assertEqual(super_seq(X, Y, m, n), len(X))

    def test_typical_case_with_same_chars(self):
        X = "ABCDGH"
        Y = "AEDFHR"
        m = len(X)
        n = len(Y)
        self.assertEqual(super_seq(X, Y, m, n), 6)

    def test_error_handling(self):
        with self.assertRaises(TypeError):
            super_seq("AGGTAB", "GXTXAYB", "len_m", "len_n")
