import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):
    def test_typical_case(self):
        S = [1, 2, 3]
        m = len(S)
        n = 4
        self.assertEqual(coin_change(S, m, n), 4)

    def test_boundary_case(self):
        S = [1, 2, 3]
        m = len(S)
        n = 0
        self.assertEqual(coin_change(S, m, n), 1)

    def test_edge_case(self):
        S = [1, 2, 3]
        m = len(S)
        n = 1
        self.assertEqual(coin_change(S, m, n), 1)

    def test_invalid_input(self):
        S = [1, 2, 3]
        m = len(S)
        n = -1
        with self.assertRaises(Exception):
            coin_change(S, m, n)
