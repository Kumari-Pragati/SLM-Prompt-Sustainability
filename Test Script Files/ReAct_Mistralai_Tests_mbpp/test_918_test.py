import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):

    def test_empty_input(self):
        self.assertEqual(coin_change([], 1, 1), 1)
        self.assertEqual(coin change([], 0, 0), 0)

    def test_single_coin(self):
        self.assertEqual(coin_change([1], 1, 1), 1)
        self.assertEqual(coin_change([5], 1, 1), 0)

    def test_multiple_coins(self):
        self.assertEqual(coin_change([1, 2, 3], 4, 3), 3)
        self.assertEqual(coin_change([1, 2, 3], 5, 3), 4)
        self.assertEqual(coin_change([1, 2, 3], 6, 3), 5)

    def test_large_input(self):
        self.assertEqual(coin_change([1, 5, 10, 25], 30, 3), 6)
        self.assertEqual(coin_change([1, 5, 10, 25], 50, 3), 10)

    def test_negative_coins(self):
        self.assertEqual(coin_change([-1, 2, 3], 4, 3), 0)

    def test_zero_amount(self):
        self.assertEqual(coin_change([1, 2, 3], 0, 3), 0)

    def test_negative_amount(self):
        self.assertEqual(coin_change([1, 2, 3], -1, 3), 0)
        self.assertEqual(coin_change([1, 2, 3], -4, 3), 0)
