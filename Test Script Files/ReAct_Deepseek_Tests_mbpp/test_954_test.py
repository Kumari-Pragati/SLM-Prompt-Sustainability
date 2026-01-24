import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(profit_amount(100, 150), 50)

    def test_edge_case_sale_greater_than_cost(self):
        self.assertIsNone(profit_amount(100, 200))

    def test_edge_case_sale_equal_to_cost(self):
        self.assertIsNone(profit_amount(100, 100))

    def test_edge_case_sale_less_than_cost(self):
        self.assertEqual(profit_amount(200, 100), 100)

    def test_negative_cost(self):
        self.assertEqual(profit_amount(-100, 50), 150)

    def test_negative_sale(self):
        self.assertEqual(profit_amount(100, -50), 150)

    def test_zero_cost(self):
        self.assertIsNone(profit_amount(0, 100))

    def test_zero_sale(self):
        self.assertIsNone(profit_amount(100, 0))

    def test_negative_cost_and_sale(self):
        self.assertEqual(profit_amount(-100, -50), 50)
