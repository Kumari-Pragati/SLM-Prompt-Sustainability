import unittest
from mbpp_531_code import min_coins

class TestMinCoins(unittest.TestCase):
    def test_empty_coins(self):
        self.assertEqual(min_coins([], 1, 1), 0)

    def test_single_coin(self):
        self.assertEqual(min_coins([1], 1, 1), 1)
        self.assertEqual(min_coins([5], 1, 5), 1)
        self.assertEqual(min_coins([10], 1, 10), 1)

    def test_multiple_coins(self):
        self.assertEqual(min_coins([1, 2, 3], 1, 4), 2)
        self.assertEqual(min_coins([1, 2, 3], 1, 5), 3)
        self.assertEqual(min_coins([1, 2, 3], 1, 6), 2)
        self.assertEqual(min_coins([1, 2, 3], 1, 7), 3)
        self.assertEqual(min_coins([1, 2, 3], 1, 8), 2)

    def test_large_coins(self):
        self.assertEqual(min_coins([10, 25, 50], 1, 100), 2)
        self.assertEqual(min_coins([10, 25, 50], 1, 101), 3)
        self.assertEqual(min_coins([10, 25, 50], 1, 200), 2)

    def test_invalid_coins(self):
        self.assertRaises(ValueError, min_coins, [1, 2, 3], 0, 1)
        self.assertRaises(ValueError, min_coins, [1, 2, 3], 2, 0)
