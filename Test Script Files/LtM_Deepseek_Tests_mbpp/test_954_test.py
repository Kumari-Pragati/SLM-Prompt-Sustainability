import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(profit_amount(100, 150), 50)

    def test_edge_case_sale_greater_than_cost(self):
        self.assertIsNone(profit_amount(100, 50))

    def test_boundary_case_sale_equal_to_cost(self):
        self.assertIsNone(profit_amount(100, 100))

    def test_edge_case_negative_cost(self):
        self.assertEqual(profit_amount(-50, 0), 50)

    def test_edge_case_negative_sale(self):
        self.assertIsNone(profit_amount(100, -50))

    def test_edge_case_zero_cost(self):
        self.assertIsNone(profit_amount(0, 100))

    def test_edge_case_zero_sale(self):
        self.assertIsNone(profit_amount(100, 0))
