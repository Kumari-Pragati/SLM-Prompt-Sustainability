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
        self.assertEqual(max_profit([-1, -2, -3, -4], 1), 3)

    def test_k_greater_than_len(self):
        self.assertEqual(max_profit([1, 2, 3, 4], 5), 0)

    def test_k_zero(self):
        self.assertEqual(max_profit([1, 2, 3, 4], 0), 0)
