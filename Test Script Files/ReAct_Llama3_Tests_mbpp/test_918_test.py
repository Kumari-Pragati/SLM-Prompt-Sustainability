import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):

    def test_empty_input(self):
        self.assertRaises(ValueError, coin_change, [], 0, 0)

    def test_single_coin(self):
        self.assertEqual(coin_change([1], 1, 1), 1)

    def test_multiple_coins(self):
        self.assertEqual(coin_change([1, 2, 3], 3, 5), 1)

    def test_no_coins(self):
        self.assertEqual(coin_change([], 0, 5), 0)

    def test_no_change(self):
        self.assertEqual(coin_change([1, 2, 3], 3, 0), 0)

    def test_large_change(self):
        self.assertEqual(coin_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 100), 1)

    def test_edge_case(self):
        self.assertEqual(coin_change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 10), 1)
