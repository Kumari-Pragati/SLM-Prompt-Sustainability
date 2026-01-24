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
        self.assertEqual(profit_amount(200, 150), 50)

    def test_invalid_input_sale_negative(self):
        with self.assertRaises(TypeError):
            profit_amount(100, -100)

    def test_invalid_input_cost_negative(self):
        with self.assertRaises(TypeError):
            profit_amount(-100, 150)

    def test_invalid_input_sale_non_numeric(self):
        with self.assertRaises(TypeError):
            profit_amount(100, 'abc')

    def test_invalid_input_cost_non_numeric(self):
        with self.assertRaises(TypeError):
            profit_amount('abc', 150)
