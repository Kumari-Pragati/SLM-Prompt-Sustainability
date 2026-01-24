import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):

    def test_typical_case(self):
        S = [1, 2, 3]
        m = len(S)
        n = 4
        self.assertEqual(coin_change(S, m, n), 4)

    def test_edge_case_n_zero(self):
        S = [1, 2, 3]
        m = len(S)
        n = 0
        self.assertEqual(coin_change(S, m, n), 1)

    def test_boundary_case_n_one(self):
        S = [1, 2, 3]
        m = len(S)
        n = 1
        self.assertEqual(coin_change(S, m, n), 1)

    def test_corner_case_no_coins(self):
        S = []
        m = 0
        n = 10
        self.assertEqual(coin_change(S, m, n), 0)

    def test_corner_case_large_n(self):
        S = [1, 2, 3]
        m = len(S)
        n = 100
        self.assertEqual(coin_change(S, m, n), 242)

    def test_corner_case_large_S(self):
        S = list(range(1, 101))
        m = len(S)
        n = 100
        self.assertEqual(coin_change(S, m, n), 42729)
