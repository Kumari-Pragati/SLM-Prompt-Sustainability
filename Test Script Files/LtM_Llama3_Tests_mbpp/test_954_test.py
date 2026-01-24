import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):
    def test_profit_amount_positive(self):
        self.assertEqual(profit_amount(10, 5), 5)

    def test_profit_amount_negative(self):
        self.assertEqual(profit_amount(5, 10), None)

    def test_profit_amount_equal(self):
        self.assertEqual(profit_amount(5, 5), None)

    def test_profit_amount_zero(self):
        self.assertEqual(profit_amount(0, 0), None)

    def test_profit_amount_zero_cost(self):
        self.assertEqual(profit_amount(0, 5), None)

    def test_profit_amount_zero_sale(self):
        self.assertEqual(profit_amount(5, 0), None)

    def test_profit_amount_negative_cost(self):
        self.assertEqual(profit_amount(-5, 5), None)

    def test_profit_amount_negative_sale(self):
        self.assertEqual(profit_amount(5, -5), None)
