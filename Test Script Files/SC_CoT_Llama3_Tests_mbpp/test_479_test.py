import unittest
from mbpp_479_code import first_Digit

class TestFirstDigit(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(first_Digit(123), 1)

    def test_edge_case_zero(self):
        self.assertEqual(first_Digit(0), 0)

    def test_edge_case_single_digit(self):
        self.assertEqual(first_Digit(5), 5)

    def test_edge_case_negative(self):
        self.assertEqual(first_Digit(-123), -1)

    def test_edge_case_large_number(self):
        self.assertEqual(first_Digit(123456789), 1)

    def test_edge_case_zero_with_leading_zeros(self):
        self.assertEqual(first_Digit(0000), 0)

    def test_edge_case_single_digit_with_leading_zeros(self):
        self.assertEqual(first_Digit(0005), 5)

    def test_edge_case_negative_with_leading_zeros(self):
        self.assertEqual(first_Digit(-0001), -1)

    def test_edge_case_large_number_with_leading_zeros(self):
        self.assertEqual(first_Digit(000123456789), 1)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            first_Digit('abc')

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(TypeError):
            first_Digit([1, 2, 3])
