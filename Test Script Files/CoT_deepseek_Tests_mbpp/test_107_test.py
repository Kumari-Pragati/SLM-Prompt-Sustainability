import unittest
from mbpp_107_code import count_Hexadecimal

class TestCountHexadecimal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Hexadecimal(10, 15), 2)

    def test_edge_case_L_greater_than_R(self):
        self.assertEqual(count_Hexadecimal(16, 15), 0)

    def test_boundary_case_L_equals_10(self):
        self.assertEqual(count_Hexadecimal(10, 10), 1)

    def test_boundary_case_R_equals_15(self):
        self.assertEqual(count_Hexadecimal(14, 15), 1)

    def test_boundary_case_R_equals_16(self):
        self.assertEqual(count_Hexadecimal(15, 16), 2)

    def test_invalid_input_negative_number(self):
        with self.assertRaises(Exception):
            count_Hexadecimal(-1, 10)

    def test_invalid_input_string(self):
        with self.assertRaises(Exception):
            count_Hexadecimal("10", 15)
