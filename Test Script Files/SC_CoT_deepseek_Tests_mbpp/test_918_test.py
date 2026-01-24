import unittest

from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):

    def test_typical_case(self):
        S = [1, 2, 3]
        m = len(S)
        n = 4
        self.assertEqual(coin_change(S, m, n), 4)

    def test_edge_case_n_equals_0(self):
        S = [1, 2, 3]
        m = len(S)
        n = 0
        self.assertEqual(coin_change(S, m, n), 1)

    def test_edge_case_m_equals_1(self):
        S = [1]
        m = len(S)
        n = 5
        self.assertEqual(coin_change(S, m, n), 1)

    def test_corner_case_no_coins(self):
        S = []
        m = 0
        n = 5
        self.assertEqual(coin_change(S, m, n), 0)

    def test_invalid_input_negative_n(self):
        S = [1, 2, 3]
        m = len(S)
        n = -1
        with self.assertRaises(Exception):
            coin_change(S, m, n)

    def test_invalid_input_negative_coin_values(self):
        S = [-1, 2, 3]
        m = len(S)
        n = 4
        with self.assertRaises(Exception):
            coin_change(S, m, n)
