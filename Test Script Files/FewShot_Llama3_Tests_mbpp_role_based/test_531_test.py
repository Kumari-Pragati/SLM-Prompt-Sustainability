import unittest
from mbpp_531_code import min_coins

class TestMinCoins(unittest.TestCase):
    def test_min_coins_typical_use_case(self):
        coins = [1, 2, 3]
        m = len(coins)
        V = 4
        self.assertEqual(min_coins(coins, m, V), 2)

    def test_min_coins_edge_case_zero_value(self):
        coins = [1, 2, 3]
        m = len(coins)
        V = 0
        self.assertEqual(min_coins(coins, m, V), 0)

    def test_min_coins_edge_case_zero_coins(self):
        coins = []
        m = len(coins)
        V = 4
        self.assertEqual(min_coins(coins, m, V), sys.maxsize)

    def test_min_coins_edge_case_invalid_input(self):
        coins = [1, 2, 3]
        m = len(coins)
        V = -1
        with self.assertRaises(ValueError):
            min_coins(coins, m, V)
