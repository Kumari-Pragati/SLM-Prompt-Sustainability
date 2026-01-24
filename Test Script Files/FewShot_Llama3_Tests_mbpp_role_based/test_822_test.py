import unittest
from mbpp_822_code import pass_validity

class TestPassValidity(unittest.TestCase):
    def test_valid_password(self):
        self.assertTrue(pass_validity("Password123"))

    def test_invalid_length_too_short(self):
        self.assertFalse(pass_validity("a"))

    def test_invalid_length_too_long(self):
        self.assertFalse(pass_validity("a"*13))

    def test_invalid_characters_no_lowercase(self):
        self.assertFalse(pass_validity("PASSWORD123"))

    def test_invalid_characters_no_uppercase(self):
        self.assertFalse(pass_validity("password123"))

    def test_invalid_characters_no_digits(self):
        self.assertFalse(pass_validity("Password"))

    def test_invalid_characters_no_special_chars(self):
        self.assertFalse(pass_validity("Password123"))

    def test_valid_password_with_special_chars(self):
        self.assertTrue(pass_validity("Password!@#123"))

    def test_invalid_password_with_spaces(self):
        self.assertFalse(pass_validity("Password 123"))
