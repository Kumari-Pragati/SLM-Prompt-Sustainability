import unittest
from mbpp_531_code import min_coins

class TestMinCoins(unittest.TestCase):

    def test_typical_case(self):
        coins = [1, 2, 5]
        m = len(coins)
        V = 11
        self.assertEqual(min_coins(coins, m, V), 3)

    def test_edge_case_zero(self):
        coins = [1, 2, 5]
        m = len(coins)
        V = 0
        self.assertEqual(min_coins(coins, m, V), 0)

    def test_edge_case_maxsize(self):
        coins = [1, 2, 5]
        m = len(coins)
        V = 1000
        self.assertEqual(min_coins(coins, m, V), 20)

    def test_invalid_input_negative_value(self):
        coins = [1, 2, 5]
        m = len(coins)
        V = -1
        with self.assertRaises(Exception):
            min_coins(coins, m, V)

    def test_invalid_input_negative_coin(self):
        coins = [-1, 2, 5]
        m = len(coins)
        V = 11
        with self.assertRaises(Exception):
            min_coins(coins, m, V)
