import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):
    def test_profit_positive(self):
        self.assertEqual(profit_amount(100, 120), 20)

    def test_profit_negative(self):
        self.assertEqual(profit_amount(150, 120), 30)

    def test_profit_zero(self):
        self.assertEqual(profit_amount(100, 100), 0)

    def test_profit_none(self):
        self.assertIsNone(profit_amount(100, 100))

    def test_profit_invalid_input(self):
        with self.assertRaises(TypeError):
            profit_amount("a", 100)
