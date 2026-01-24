import unittest
from mbpp_501_code import num_comm_div

class TestNumCommDiv(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(num_comm_div(12, 15), 2)

    def test_edge_case_gcd_1(self):
        self.assertEqual(num_comm_div(1, 1), 2)

    def test_edge_case_gcd_x(self):
        self.assertEqual(num_comm_div(12, 12), 1)

    def test_edge_case_gcd_y(self):
        self.assertEqual(num_comm_div(12, 15), 2)

    def test_edge_case_gcd_x_y(self):
        self.assertEqual(num_comm_div(12, 24), 2)

    def test_edge_case_gcd_x_y_negative(self):
        self.assertEqual(num_comm_div(-12, -24), 2)

    def test_edge_case_gcd_x_y_zero(self):
        self.assertEqual(num_comm_div(0, 0), 0)

    def test_edge_case_gcd_x_y_one(self):
        self.assertEqual(num_comm_div(1, 1), 2)

    def test_edge_case_gcd_x_y_large(self):
        self.assertEqual(num_comm_div(1000000, 2000000), 4)

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            num_comm_div("abc", 12)
