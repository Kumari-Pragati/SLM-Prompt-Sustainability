import unittest
from mbpp_365_code import count_Digit

class TestCountDigit(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(count_Digit(123), 3)

    def test_edge_case_zero(self):
        self.assertEqual(count_Digit(0), 1)

    def test_edge_case_negative(self):
        self.assertEqual(count_Digit(-123), 3)

    def test_edge_case_single_digit(self):
        self.assertEqual(count_Digit(1), 1)

    def test_edge_case_large_number(self):
        self.assertEqual(count_Digit(123456789), 9)

    def test_edge_case_large_negative_number(self):
        self.assertEqual(count_Digit(-123456789), 9)

    def test_edge_case_max_int(self):
        self.assertEqual(count_Digit(2147483647), 10)

    def test_edge_case_max_negative_int(self):
        self.assertEqual(count_Digit(-2147483648), 10)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            count_Digit('123')

    def test_invalid_input_float(self):
        with self.assertRaises(TypeError):
            count_Digit(123.45)
