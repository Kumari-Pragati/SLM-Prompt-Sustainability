import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):

    def test_typical_case(self):
        S = [1, 2, 3]
        m = len(S)
        n = 4
        self.assertEqual(coin_change(S, m, n), 4)

    def test_edge_case_zero_amount(self):
        S = [1, 2, 3]
        m = len(S)
        n = 0
        self.assertEqual(coin_change(S, m, n), 1)

    def test_edge_case_zero_coins(self):
        S = []
        m = 0
        n = 10
        self.assertEqual(coin_change(S, m, n), 0)

    def test_edge_case_negative_amount(self):
        S = [1, 2, 3]
        m = len(S)
        n = -5
        with self.assertRaises(Exception):
            coin_change(S, m, n)

    def test_edge_case_negative_coins(self):
        S = [-1, 2, 3]
        m = len(S)
        n = 5
        with self.assertRaises(Exception):
            coin_change(S, m, n)

    def test_edge_case_negative_amount_and_coins(self):
        S = [-1, -2, -3]
        m = len(S)
        n = -5
        with self.assertRaises(Exception):
            coin_change(S, m, n)
