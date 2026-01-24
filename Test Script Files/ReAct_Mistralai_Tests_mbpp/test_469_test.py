import unittest
from mbpp_469_code import max_profit

class TestMaxProfit(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(max_profit([], 1), 0)

    def test_single_transaction(self):
        self.assertEqual(max_profit([1], 1), 0)
        self.assertEqual(max_profit([-1], 1), 0)
        self.assertEqual(max_profit([1], 2), 0)
        self.assertEqual(max_profit([-1], 2), 0)

    def test_multiple_transactions(self):
        self.assertEqual(max_profit([1, 2, 3, 4, 5], 1), 4)
        self.assertEqual(max_profit([1, 2, 3, 4, 5], 2), 7)
        self.assertEqual(max_profit([1, 2, 3, -4, 5], 1), 3)
        self.assertEqual(max_profit([1, 2, 3, -4, 5], 2), 4)
        self.assertEqual(max_profit([-1, -2, -3, -4, -5], 1), 0)
        self.assertEqual(max_profit([-1, -2, -3, -4, -5], 2), 0)

    def test_k_greater_than_n(self):
        self.assertEqual(max_profit([1, 2, 3], 4), 0)

    def test_negative_k(self):
        self.assertRaises(ValueError, max_profit, [1, 2, 3], -1)

    def test_negative_price(self):
        self.assertRaises(TypeError, max_profit, [-1, -2, -3], 1)
