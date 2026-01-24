import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(profit_amount(100, 150), 50)

    def test_boundary_condition(self):
        self.assertEqual(profit_amount(0, 0), None)

    def test_edge_case(self):
        self.assertEqual(profit_amount(200, 150), 50)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            profit_amount('100', 150)
