import unittest
from mbpp_531_code import min_coins

class TestMinCoins(unittest.TestCase):
    def test_typical_use_case(self):
        coins = [1, 2, 5]
        m = len(coins)
        V = 11
        self.assertEqual(min_coins(coins, m, V), 3)

    def test_boundary_condition(self):
        coins = [1, 2, 5]
        m = len(coins)
        V = 0
        self.assertEqual(min_coins(coins, m, V), 0)

    def test_edge_condition(self):
        coins = [1, 2, 5]
        m = len(coins)
        V = 1
        self.assertEqual(min_coins(coins, m, V), 1)

    def test_invalid_input(self):
        coins = [1, 2, 5]
        m = len(coins)
        V = -1
        with self.assertRaises(Exception):
            min_coins(coins, m, V)
