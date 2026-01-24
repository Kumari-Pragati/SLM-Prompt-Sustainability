import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):

    def test_profit_positive(self):
        self.assertEqual(profit_amount(100, 80), 20)

    def test_profit_negative(self):
        self.assertEqual(profit_amount(80, 100), None)

    def test_profit_zero(self):
        self.assertEqual(profit_amount(100, 100), None)

    def test_profit_equal(self):
        self.assertEqual(profit_amount(100, 100), None)

    def test_profit_greater_than_cost(self):
        self.assertEqual(profit_amount(150, 200), 50)

    def test_profit_less_than_cost(self):
        self.assertEqual(profit_amount(200, 150), None)
