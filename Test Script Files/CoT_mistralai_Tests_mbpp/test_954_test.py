import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):
    def test_positive_values(self):
        self.assertEqual(profit_amount(10, 5), 5)
        self.assertEqual(profit_amount(20, 15), 5)
        self.assertEqual(profit_amount(30, 25), 5)

    def test_zero_or_negative_values(self):
        self.assertIsNone(profit_amount(0, 5))
        self.assertIsNone(profit_amount(-10, 5))
        self.assertIsNone(profit_amount(0, 0))

    def test_sale_amount_greater_than_actual_cost(self):
        self.assertIsNone(profit_amount(5, 10))
        self.assertIsNone(profit_amount(5, 20))
        self.assertIsNone(profit_amount(5, 30))
