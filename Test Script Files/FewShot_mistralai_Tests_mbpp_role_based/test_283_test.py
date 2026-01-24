import unittest
from mbpp_283_code import validate

class TestValidate(unittest.TestCase):
    def test_valid_numbers(self):
        self.assertTrue(validate(123456789))
        self.assertTrue(validate(987654321))

    def test_single_digit_numbers(self):
        self.assertTrue(validate(1))
        self.assertTrue(validate(9))

    def test_zero(self):
        self.assertTrue(validate(0))

    def test_negative_numbers(self):
        self.assertFalse(validate(-1))
        self.assertFalse(validate(-9))

    def test_long_numbers(self):
        self.assertTrue(validate(1234567890123456789))

    def test_short_numbers(self):
        self.assertTrue(validate(12345))
        self.assertTrue(validate(9876))

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, validate, 'abcdefg')
        self.assertRaises(TypeError, validate, 1.23)
        self.assertRaises(TypeError, validate, [1, 2, 3])
