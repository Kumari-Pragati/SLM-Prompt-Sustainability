import unittest
from mbpp_822_code import pass_validity

class TestPassValidity(unittest.TestCase):
    def test_valid_pass(self):
        self.assertTrue(pass_validity("P@ssw0rd123"))

    def test_invalid_pass_length(self):
        self.assertFalse(pass_validity("short"))
        self.assertFalse(pass_validity("verylong"))

    def test_invalid_pass_characters(self):
        self.assertFalse(pass_validity("abc"))
        self.assertFalse(pass_validity("123"))
        self.assertFalse(pass_validity("ABC"))
        self.assertFalse(pass_validity("special"))

    def test_invalid_pass_spaces(self):
        self.assertFalse(pass_validity("P@ssw0rd 123"))
        self.assertFalse(pass_validity("P@ssw0rd123 "))

    def test_valid_pass_with_uppercase(self):
        self.assertTrue(pass_validity("P@ssw0rd123ABC"))

    def test_valid_pass_with_numbers(self):
        self.assertTrue(pass_validity("P@ssw0rd123456"))

    def test_valid_pass_with_special_chars(self):
        self.assertTrue(pass_validity("P@ssw0rd123!@#"))
