import unittest
from mbpp_531_code import min_coins

class TestMinCoins(unittest.TestCase):

    def test_min_coins(self):
        coins = [1, 2, 5]
        m = len(coins)
        V = 11
        self.assertEqual(min_coins(coins, m, V), 3)

        coins = [9, 6, 5, 1]
        m = len(coins)
        V = 11
        self.assertEqual(min_coins(coins, m, V), 2)

        coins = [1, 2, 5]
        m = len(coins)
        V = 0
        self.assertEqual(min_coins(coins, m, V), 0)

        coins = [1, 2, 5]
        m = len(coins)
        V = 3
        self.assertEqual(min_coins(coins, m, V), 2)

        coins = [1, 2, 5]
        m = len(coins)
        V = 7
        self.assertEqual(min_coins(coins, m, V), 3)
