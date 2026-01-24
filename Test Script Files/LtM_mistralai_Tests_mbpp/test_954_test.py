import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):

    def test_simple_positive(self):
        self.assertEqual(profit_amount(10, 5), 5)

    def test_simple_negative(self):
        self.assertEqual(profit_amount(5, 10), -5)

    def test_zero_sale_amount(self):
        self.assertEqual(profit_amount(10, 0), 10)

    def test_edge_case_zero_cost(self):
        self.assertIsNone(profit_amount(0, 10))

    def test_large_positive(self):
        self.assertEqual(profit_amount(1000000, 999999), 1)

    def test_large_negative(self):
        self.assertEqual(profit_amount(-1000000, -999999), 1000000)
