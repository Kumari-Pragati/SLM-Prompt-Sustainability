import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):

    def test_profit_amount_positive(self):
        self.assertEqual(profit_amount(100, 80), 20)

    def test_profit_amount_negative(self):
        self.assertEqual(profit_amount(80, 100), None)

    def test_profit_amount_zero(self):
        self.assertEqual(profit_amount(100, 100), None)

    def test_profit_amount_equal(self):
        self.assertEqual(profit_amount(100, 100), None)

    def test_profit_amount_greater(self):
        self.assertEqual(profit_amount(150, 120), 30)

    def test_profit_amount_greater_than_actual_cost(self):
        self.assertEqual(profit_amount(100, 150), None)
