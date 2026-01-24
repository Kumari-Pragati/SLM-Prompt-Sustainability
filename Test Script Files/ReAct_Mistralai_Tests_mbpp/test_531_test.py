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
        self.assertEqual(min_coins([1, 2, 3], 1, 7), 2)
        self.assertEqual(min_coins([1, 2, 3], 1, 8), 3)

    def test_large_amount(self):
        self.assertEqual(min_coins([1, 2, 3], 1, 1000000), 100000)

    def test_negative_coins(self):
        self.assertRaises(ValueError, min_coins, [-1], 1, 1)

    def test_negative_amount(self):
        self.assertRaises(ValueError, min_coins, [1], 1, -1)

    def test_zero_amount(self):
        self.assertEqual(min_coins([1], 1, 0), 0)
