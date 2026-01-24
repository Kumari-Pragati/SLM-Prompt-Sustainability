import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(coin_change([1, 2, 3], 4, 5), 3)
        self.assertEqual(coin_change([1, 2, 3], 3, 5), 2)
        self.assertEqual(coin_change([1, 2, 3], 4, 1), 0)
        self.assertEqual(coin_change([1, 2, 3], 0, 0), 1)

    def test_empty_list(self):
        self.assertEqual(coin_change([], 4, 5), 0)

    def test_negative_input(self):
        self.assertRaises(ValueError, coin_change, [-1, -2, -3], 4, 5)

    def test_zero_input(self):
        self.assertEqual(coin_change([0], 4, 5), 0)

    def test_invalid_input(self):
        self.assertRaises(ValueError, coin_change, [1, 2, 3], -1, 5)
        self.assertRaises(ValueError, coin_change, [1, 2, 3], 4, -1)
