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

    def test_boundary_case_max_size(self):
        coins = [sys.maxsize]
        m = 1
        V = sys.maxsize
        self.assertEqual(min_coins(coins, m, V), 1)

    def test_corner_case_invalid_coin(self):
        coins = [-1, 2, 5]
        m = len(coins)
        V = 6
        self.assertEqual(min_coins(coins, m, V), sys.maxsize)

    def test_corner_case_no_coins(self):
        coins = []
        m = 0
        V = 10
        self.assertEqual(min_coins(coins, m, V), sys.maxsize)
