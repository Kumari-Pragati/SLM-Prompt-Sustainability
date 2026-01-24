import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):
    def test_empty_price(self):
        self.assertEqual(max_profit([], 1), None)

    def test_single_price(self):
        self.assertEqual(max_profit([10], 1), 0)

    def test_two_prices(self):
        self.assertEqual(max_profit([10, 20], 1), 10)

    def test_k_transactions(self):
        self.assertEqual(max_profit([1, 5, 3, 5], 2), 4)

    def test_k_transactions_with_negative_prices(self):
        self.assertEqual(max_profit([-1, -5, 3, -5], 2), 2)

    def test_k_transactions_with_zero_price(self):
        self.assertEqual(max_profit([0, 0, 0, 0], 2), 0)

    def test_k_transactions_with_all_zero_prices(self):
        self.assertEqual(max_profit([0, 0, 0, 0], 3), 0)

    def test_k_transactions_with_all_negative_prices(self):
        self.assertEqual(max_profit([-1, -5, -3, -5], 2), -4)
