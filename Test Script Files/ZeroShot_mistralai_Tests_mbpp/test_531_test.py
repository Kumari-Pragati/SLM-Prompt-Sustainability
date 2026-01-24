import unittest
from mbpp_531_code import min_coins

class TestMinCoins(unittest.TestCase):

    def test_min_coins_empty_coins(self):
        self.assertEqual(min_coins([], 3, 4), 0)

    def test_min_coins_single_coin(self):
        self.assertEqual(min_coins([1], 3, 4), 4 if 4 % 1 == 0 else -1)
        self.assertEqual(min_coins([1], 3, 5), 1)
        self.assertEqual(min_coins([1], 3, 1), 0)

    def test_min_coins_multiple_coins(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 4), 4)
        self.assertEqual(min_coins([1, 2, 3], 3, 5), 2)
        self.assertEqual(min_coins([1, 2, 3], 3, 6), 2)
        self.assertEqual(min_coins([1, 2, 3], 3, 7), 3)
        self.assertEqual(min_coins([1, 2, 3], 3, 10), 4)

    def test_min_coins_large_input(self):
        self.assertEqual(min_coins([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3, 495), 9)
