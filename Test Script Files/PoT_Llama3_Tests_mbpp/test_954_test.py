import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):
    def test_positive_profit(self):
        self.assertEqual(profit_amount(10, 5), 5)

    def test_negative_profit(self):
        self.assertEqual(profit_amount(5, 10), 5)

    def test_no_profit(self):
        self.assertIsNone(profit_amount(10, 10))

    def test_loss(self):
        self.assertEqual(profit_amount(15, 10), 5)

    def test_equal_cost_and_sale(self):
        self.assertIsNone(profit_amount(10, 10))

    def test_negative_cost(self):
        with self.assertRaises(TypeError):
            profit_amount(-10, 10)

    def test_negative_sale(self):
        with self.assertRaises(TypeError):
            profit_amount(10, -10)
