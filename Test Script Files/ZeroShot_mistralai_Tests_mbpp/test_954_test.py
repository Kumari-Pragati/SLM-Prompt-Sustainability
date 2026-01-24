import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):

    def test_profit_when_actual_cost_greater_than_sale_amount(self):
        self.assertEqual(profit_amount(100, 50), 50)
        self.assertEqual(profit_amount(200, 150), 50)
        self.assertEqual(profit_amount(300, 200), 100)

    def test_profit_when_actual_cost_less_than_or_equal_to_sale_amount(self):
        self.assertIsNone(profit_amount(50, 100))
        self.assertIsNone(profit_amount(100, 100))
        self.assertIsNone(profit_amount(150, 200))
