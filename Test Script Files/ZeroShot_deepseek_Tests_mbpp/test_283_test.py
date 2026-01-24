import unittest
from mbpp_283_code import validate

class TestValidate(unittest.TestCase):

    def test_single_digit(self):
        self.assertTrue(validate(0))
        self.assertTrue(validate(1))
        self.assertTrue(validate(2))
        self.assertTrue(validate(3))
        self.assertTrue(validate(4))
        self.assertTrue(validate(5))
        self.assertTrue(validate(6))
        self.assertTrue(validate(7))
        self.assertTrue(validate(8))
        self.assertTrue(validate(9))

    def test_multiple_digits(self):
        self.assertTrue(validate(11))
        self.assertTrue(validate(22))
        self.assertTrue(validate(33))
        self.assertTrue(validate(44))
        self.assertTrue(validate(55))
        self.assertTrue(validate(66))
        self.assertTrue(validate(77))
        self.assertTrue(validate(88))
        self.assertTrue(validate(99))

    def test_large_numbers(self):
        self.assertTrue(validate(1234567890))
        self.assertTrue(validate(9876543210))

    def test_invalid_numbers(self):
        self.assertFalse(validate(1234567891))
        self.assertFalse(validate(1234567892))
        self.assertFalse(validate(1234567893))
        self.assertFalse(validate(1234567894))
        self.assertFalse(validate(1234567895))
        self.assertFalse(validate(1234567896))
        self.assertFalse(validate(1234567897))
        self.assertFalse(validate(1234567898))
        self.assertFalse(validate(1234567899))
