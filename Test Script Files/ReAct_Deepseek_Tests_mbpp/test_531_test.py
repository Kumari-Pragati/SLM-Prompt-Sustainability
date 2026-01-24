import unittest
from mbpp_531_code import min_coins

class TestMinCoins(unittest.TestCase):

    def test_typical_case(self):
        coins = [1, 2, 5]
        m = len(coins)
        V = 11
        self.assertEqual(min_coins(coins, m, V), 3)

    def test_edge_case_zero_value(self):
        coins = [1, 2, 5]
        m = len(coins)
        V = 0
        self.assertEqual(min_coins(coins, m, V), 0)

    def test_edge_case_single_coin(self):
        coins = [1]
        m = len(coins)
        V = 10
        self.assertEqual(min_coins(coins, m, V), 10)

    def test_edge_case_no_coins(self):
        coins = []
        m = len(coins)
        V = 10
        self.assertEqual(min_coins(coins, m, V), sys.maxsize)

    def test_explicitly_handled_error_case(self):
        coins = [1, 2, 5]
        m = len(coins)
        V = -10
        with self.assertRaises(Exception):
            min_coins(coins, m, V)
