import unittest
from mbpp_954_code import profit_amount

class TestProfitAmount(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(profit_amount(100, 150), 50)

    def test_edge_case(self):
        self.assertEqual(profit_amount(200, 200), None)

    def test_boundary_case(self):
        self.assertEqual(profit_amount(0, 100), 100)
        self.assertEqual(profit_amount(100, 0), 100)

    def test_negative_numbers(self):
        self.assertEqual(profit_amount(-100, -50), 50)
        self.assertEqual(profit_amount(-100, 0), 100)
        self.assertEqual(profit_amount(0, -50), 50)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            profit_amount("100", 150)
        with self.assertRaises(TypeError):
            profit_amount(100, "150")
        with self.assertRaises(TypeError):
            profit_amount("100", "150")
