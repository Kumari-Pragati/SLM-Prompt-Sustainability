import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_profit([], 1), 0)

    def test_single_transaction(self):
        self.assertEqual(max_profit([1, 2, 3, 4], 1), 3)

    def test_multiple_transactions(self):
        self.assertEqual(max_profit([1, 2, 3, 4], 2), 4)

    def test_negative_prices(self):
        self.assertEqual(max_profit([-1, -2, -3, -4], 1), 6)

    def test_zero_prices(self):
        self.assertEqual(max_profit([0, 0, 0, 0], 1), 0)

    def test_invalid_k(self):
        with self.assertRaises(ValueError):
            max_profit([1, 2, 3, 4], 0)

    def test_invalid_price_list(self):
        with self.assertRaises(TypeError):
            max_profit('1, 2, 3, 4', 1)
