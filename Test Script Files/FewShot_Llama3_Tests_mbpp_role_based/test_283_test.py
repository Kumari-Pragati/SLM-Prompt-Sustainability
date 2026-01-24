import unittest
from mbpp_283_code import validate

class TestValidate(unittest.TestCase):
    def test_valid_number(self):
        self.assertTrue(validate(1234567890))

    def test_invalid_number(self):
        self.assertFalse(validate(1234567891))

    def test_single_digit_number(self):
        self.assertTrue(validate(1))

    def test_zero(self):
        self.assertFalse(validate(0))

    def test_negative_number(self):
        self.assertFalse(validate(-1234567890))

    def test_large_number(self):
        self.assertTrue(validate(9876543210))

    def test_edge_case(self):
        self.assertTrue(validate(1111111111))
