import unittest
from mbpp_918_code import coin_change

class TestCoinChange(unittest.TestCase):

    def test_coin_change_empty_list(self):
        self.assertEqual(coin_change([], 3, 3), 1)

    def test_coin_change_single_coin(self):
        self.assertEqual(coin_change([1], 3, 3), 3)

    def test_coin_change_multiple_coins(self):
        self.assertEqual(coin_change([1, 2, 3], 4, 4), 4)

    def test_coin_change_large_amount(self):
        self.assertEqual(coin_change([1, 5, 10, 25], 30, 2), 2)

    def test_coin_change_no_solution(self):
        self.assertEqual(coin_change([1, 2, 3], 4, 1), 0)
