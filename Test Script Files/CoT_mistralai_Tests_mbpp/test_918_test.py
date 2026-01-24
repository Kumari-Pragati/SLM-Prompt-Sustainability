import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):

    def test_empty_target_amount(self):
        self.assertEqual(coin_change([1, 2, 3], 0, 3), [1, 0, 0])

    def test_single_coin(self):
        self.assertEqual(coin_change([1], 1, 1), [1])
        self.assertEqual(coin_change([5], 1, 1), [1])

    def test_multiple_coins(self):
        self.assertEqual(coin_change([1, 2, 3], 4, 3), [1, 1, 2])
        self.assertEqual(coin_change([1, 5, 10], 10, 1), [1, 0, 0])

    def test_invalid_target_amount(self):
        self.assertRaises(ValueError, lambda: coin_change([1, 2, 3], 5, 3))
        self.assertRaises(ValueError, lambda: coin_change([1, 2, 3], -1, 3))
        self.assertRaises(ValueError, lambda: coin_change([], 4, 3))

    def test_invalid_coin_values(self):
        self.assertRaises(ValueError, lambda: coin_change([-1, 0, 1], 1, 3))
        self.assertRaises(ValueError, lambda: coin_change([1, 0, 1], 1, 3))
