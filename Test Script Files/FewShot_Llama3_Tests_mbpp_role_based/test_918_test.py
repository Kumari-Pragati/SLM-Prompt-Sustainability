import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):
    def test_typical_use_case(self):
        S = [1, 2, 3]
        m = 3
        n = 4
        self.assertEqual(coin_change(S, m, n), 1)

    def test_edge_case_zero(self):
        S = []
        m = 0
        n = 1
        self.assertEqual(coin_change(S, m, n), 0)

    def test_edge_case_one(self):
        S = [1]
        m = 1
        n = 1
        self.assertEqual(coin_change(S, m, n), 1)

    def test_edge_case_m_zero(self):
        S = [1, 2, 3]
        m = 0
        n = 4
        self.assertEqual(coin_change(S, m, n), 0)

    def test_edge_case_n_zero(self):
        S = [1, 2, 3]
        m = 3
        n = 0
        self.assertEqual(coin_change(S, m, n), 0)

    def test_invalid_input(self):
        S = [1, 2, 3]
        m = -1
        n = 4
        with self.assertRaises(IndexError):
            coin_change(S, m, n)
