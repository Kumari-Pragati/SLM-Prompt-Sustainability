import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):

    def test_profit_amount(self):
        self.assertEqual(profit_amount(100, 200), 100)
        self.assertEqual(profit_amount(200, 100), None)
        self.assertEqual(profit_amount(0, 100), 100)
        self.assertEqual(profit_amount(100, 0), None)
        self.assertEqual(profit_amount(100, 100), None)
        self.assertEqual(profit_amount(-100, 200), 300)
        self.assertEqual(profit_amount(200, -100), 300)
        self.assertEqual(profit_amount(-100, -200), -100)
