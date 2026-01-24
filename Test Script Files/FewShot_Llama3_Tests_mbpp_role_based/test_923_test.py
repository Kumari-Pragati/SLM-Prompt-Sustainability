import unittest
from mbpp_923_code import super_seq

class TestSuperSeq(unittest.TestCase):
    def test_typical_use_case(self):
        X = [1, 2, 3]
        Y = [4, 5, 6]
        m = 3
        n = 3
        self.assertEqual(super_seq(X, Y, m, n), 3)

    def test_edge_case_m_zero(self):
        X = [1, 2, 3]
        Y = [4, 5, 6]
        m = 0
        n = 3
        self.assertEqual(super_seq(X, Y, m, n), 3)

    def test_edge_case_n_zero(self):
        X = [1, 2, 3]
        Y = [4, 5, 6]
        m = 3
        n = 0
        self.assertEqual(super_seq(X, Y, m, n), 3)

    def test_edge_case_m_and_n_zero(self):
        X = [1, 2, 3]
        Y = [4, 5, 6]
        m = 0
        n = 0
        self.assertEqual(super_seq(X, Y, m, n), 0)

    def test_edge_case_m_and_n_one(self):
        X = [1]
        Y = [4]
        m = 1
        n = 1
        self.assertEqual(super_seq(X, Y, m, n), 1)

    def test_edge_case_m_and_n_equal(self):
        X = [1, 2, 3]
        Y = [1, 2, 3]
        m = 3
        n = 3
        self.assertEqual(super_seq(X, Y, m, n), 3)
