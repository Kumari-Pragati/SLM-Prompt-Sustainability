import unittest
from mbpp_531_code import min_coins

class TestMinCoins(unittest.TestCase):
    def test_zero_coins(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 0), 0)

    def test_single_coin(self):
        self.assertEqual(min_coins([1], 1, 1), 1)

    def test_multiple_coins(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 4), 2)

    def test_exceeds_max_value(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 10), sys.maxsize)

    def test_exceeds_max_value_with_zero_coins(self):
        self.assertEqual(min_coins([1, 2, 3], 3, 11), sys.maxsize)

    def test_coins_greater_than_max_value(self):
        self.assertEqual(min_coins([10, 20, 30], 3, 5), sys.maxsize)

    def test_coins_greater_than_max_value_with_zero_coins(self):
        self.assertEqual(min_coins([10, 20, 30], 3, 6), sys.maxsize)

    def test_coins_greater_than_max_value_with_max_coins(self):
        self.assertEqual(min_coins([10, 20, 30], 3, 30), sys.maxsize)
