import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):
    def test_positive_profit(self):
        self.assertEqual(profit_amount(100, 80), 20)

    def test_zero_profit(self):
        self.assertIsNone(profit_amount(100, 100))

    def test_negative_profit(self):
        self.assertEqual(profit_amount(80, 100), 20)

    def test_negative_actual_cost(self):
        with self.assertRaises(TypeError):
            profit_amount(-100, 80)

    def test_negative_sale_amount(self):
        with self.assertRaises(TypeError):
            profit_amount(100, -80)

    def test_equal_actual_cost_and_sale_amount(self):
        self.assertIsNone(profit_amount(100, 100))

    def test_greater_actual_cost_than_sale_amount(self):
        self.assertEqual(profit_amount(120, 100), 20)

    def test_greater_sale_amount_than_actual_cost(self):
        self.assertIsNone(profit_amount(80, 120))
