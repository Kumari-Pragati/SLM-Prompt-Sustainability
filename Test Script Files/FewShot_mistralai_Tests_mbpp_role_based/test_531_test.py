import unittest
from mbpp_531_code import min_coins

class TestMinCoins(unittest.TestCase):
    def test_empty_coins(self):
        self.assertEqual(min_coins([], 1, 1), sys.maxsize)

    def test_single_coin(self):
        self.assertEqual(min_coins([1], 1, 1), 1)
        self.assertEqual(min_coins([5], 1, 5), 1)
        self.assertEqual(min_coins([10], 1, 10), 1)

    def test_multiple_coins(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 4), 2)
        self.assertEqual(min_coins([1, 2, 3], 3, 5), 2)
        self.assertEqual(min_coins([1, 2, 3], 3, 6), 3)
        self.assertEqual(min_coins([1, 2, 3], 3, 7), 4)

    def test_large_coins(self):
        self.assertEqual(min_coins([10, 25, 50], 3, 100), 3)
        self.assertEqual(min_coins([10, 25, 50], 3, 200), 4)
        self.assertEqual(min_coins([10, 25, 50], 3, 300), 5)

    def test_zero_value(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 0), 0)

    def test_negative_value(self):
        self.assertEqual(min_coins([1, 2, 3], 3, -1), sys.maxsize)
