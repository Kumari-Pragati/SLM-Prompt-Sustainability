import unittest
from mbpp_127_code import multiply_int

class TestMultiplyInt(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(multiply_int(2, 3), 6)

    def test_edge_case_y_zero(self):
        self.assertEqual(multiply_int(2, 0), 0)

    def test_edge_case_y_one(self):
        self.assertEqual(multiply_int(2, 1), 2)

    def test_boundary_case_negative_y(self):
        self.assertEqual(multiply_int(2, -3), -6)

    def test_corner_case_negative_x(self):
        self.assertEqual(multiply_int(-2, 3), -6)

    def test_corner_case_negative_x_and_y(self):
        self.assertEqual(multiply_int(-2, -3), 6)

    def test_invalid_input_y_string(self):
        with self.assertRaises(TypeError):
            multiply_int(2, '3')

    def test_invalid_input_x_string(self):
        with self.assertRaises(TypeError):
            multiply_int('2', 3)

    def test_invalid_input_both_string(self):
        with self.assertRaises(TypeError):
            multiply_int('2', '3')
