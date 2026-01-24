import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):
    def test_positive_profit(self):
        self.assertEqual(profit_amount(10, 5), 5)
        self.assertEqual(profit_amount(20, 15), 5)

    def test_zero_profit(self):
        self.assertEqual(profit_amount(10, 10), 0)

    def test_negative_profit(self):
        self.assertEqual(profit_amount(15, 10), 5)
        self.assertEqual(profit_amount(25, 20), 5)

    def test_negative_sale_amount(self):
        self.assertIsNone(profit_amount(10, -5))
        self.assertIsNone(profit_amount(20, -15))

    def test_zero_actual_cost(self):
        self.assertIsNone(profit_amount(0, 5))
