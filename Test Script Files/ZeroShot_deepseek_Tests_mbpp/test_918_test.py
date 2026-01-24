import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):

    def test_coin_change(self):
        S = [1, 2, 3]
        m = len(S)
        n = 5
        self.assertEqual(coin_change(S, m, n), 5)

        S = [2, 5, 3, 6]
        m = len(S)
        n = 10
        self.assertEqual(coin_change(S, m, n), 4)

        S = [1, 2, 5]
        m = len(S)
        n = 11
        self.assertEqual(coin_change(S, m, n), 3)

        S = [1, 2, 3, 4]
        m = len(S)
        n = 10
        self.assertEqual(coin_change(S, m, n), 4)

        S = [1, 2, 3, 4, 5]
        m = len(S)
        n = 15
        self.assertEqual(coin_change(S, m, n), 6)
