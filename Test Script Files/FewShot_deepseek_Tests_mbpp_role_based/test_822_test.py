import unittest
from mbpp_822_code import pass_validity

class TestPassValidity(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(pass_validity("Abc123$"))

    def test_short_password(self):
        self.assertFalse(pass_validity("Abc12"))

    def test_long_password(self):
        self.assertFalse(pass_validity("Abcdefghijklmnop"))

    def test_no_lowercase(self):
        self.assertFalse(pass_validity("ABC123$"))

    def test_no_uppercase(self):
        self.assertFalse(pass_validity("abc123$"))

    def test_no_digit(self):
        self.assertFalse(pass_validity("Abcdef$"))

    def test_no_special_char(self):
        self.assertFalse(pass_validity("Abc123"))

    def test_with_whitespace(self):
        self.assertFalse(pass_validity("Abc123 "))
