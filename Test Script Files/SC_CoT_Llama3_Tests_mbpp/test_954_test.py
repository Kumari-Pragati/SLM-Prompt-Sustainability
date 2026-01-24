import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):

    def test_positive_profit(self):
        self.assertEqual(profit_amount(10, 5), 5)

    def test_zero_profit(self):
        self.assertIsNone(profit_amount(5, 5))

    def test_negative_profit(self):
        self.assertEqual(profit_amount(5, 10), 5)

    def test_negative_actual_cost(self):
        with self.assertRaises(TypeError):
            profit_amount(-10, 5)

    def test_negative_sale_amount(self):
        with self.assertRaises(TypeError):
            profit_amount(10, -5)

    def test_equal_actual_cost_and_sale_amount(self):
        self.assertIsNone(profit_amount(5, 5))

    def test_actual_cost_greater_than_sale_amount(self):
        self.assertEqual(profit_amount(10, 5), 5)

    def test_sale_amount_greater_than_actual_cost(self):
        self.assertIsNone(profit_amount(5, 10))
