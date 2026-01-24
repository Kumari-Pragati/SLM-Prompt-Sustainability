import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):

    def test_positive_values(self):
        self.assertEqual(profit_amount(100, 50), 50)
        self.assertEqual(profit_amount(200, 250), 0)
        self.assertEqual(profit_amount(500, 400), 100)

    def test_zero_values(self):
        self.assertIsNone(profit_amount(0, 0))
        self.assertIsNone(profit_amount(0, 50))
        self.assertIsNone(profit_amount(50, 0))

    def test_negative_values(self):
        self.assertIsNone(profit_amount(-50, 50))
        self.assertIsNone(profit_amount(50, -50))

    def test_extreme_values(self):
        self.assertEqual(profit_amount(float('inf'), 100), float('inf'))
        self.assertEqual(profit_amount(100, float('inf')), 0)
        self.assertIsNone(profit_amount(float('-inf'), 100))
        self.assertIsNone(profit_amount(100, float('-inf')))
