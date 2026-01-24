import unittest
from mbpp_543_code import count_digits

class TestCountDigits(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_digits(123, 456), 6)

    def test_edge_case_single_digit(self):
        self.assertEqual(count_digits(0, 0), 1)

    def test_boundary_case_max_int(self):
        self.assertEqual(count_digits(2147483647, 2147483647), 10)

    def test_boundary_case_min_int(self):
        self.assertEqual(count_digits(-2147483648, -2147483648), 10)

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            count_digits("123", 456)

    def test_invalid_input_float(self):
        with self.assertRaises(TypeError):
            count_digits(123.5, 456)
