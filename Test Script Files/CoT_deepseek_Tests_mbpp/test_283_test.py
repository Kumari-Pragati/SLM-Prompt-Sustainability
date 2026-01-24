import unittest
from mbpp_283_code import validate

class TestValidateFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(validate(12321))
        self.assertTrue(validate(12345))

    def test_single_digit_number(self):
        self.assertTrue(validate(0))
        self.assertTrue(validate(9))

    def test_large_number(self):
        self.assertTrue(validate(1234567890))

    def test_edge_case_with_same_digits(self):
        self.assertTrue(validate(11111))
        self.assertTrue(validate(22222))

    def test_edge_case_with_increasing_digits(self):
        self.assertTrue(validate(123456))
        self.assertTrue(validate(123456789))

    def test_edge_case_with_decreasing_digits(self):
        self.assertTrue(validate(987654321))

    def test_invalid_input_negative_number(self):
        self.assertFalse(validate(-12321))

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            validate("12321")

    def test_invalid_input_large_number(self):
        self.assertFalse(validate(12345678901))
