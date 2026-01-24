import unittest
from mbpp_822_code import pass_validity

class TestPassValidity(unittest.TestCase):

    def test_valid_pass(self):
        self.assertTrue(pass_validity("Password123"))

    def test_invalid_pass_length(self):
        self.assertFalse(pass_validity("short"))
        self.assertFalse(pass_validity("verylong"))

    def test_invalid_pass_characters(self):
        self.assertFalse(pass_validity("abc"))
        self.assertFalse(pass_validity("123"))
        self.assertFalse(pass_validity("ABC"))
        self.assertFalse(pass_validity("$@#"))

    def test_invalid_pass_spaces(self):
        self.assertFalse(pass_validity("abc def"))
        self.assertFalse(pass_validity("abc def 123"))

    def test_valid_pass_with_special_characters(self):
        self.assertTrue(pass_validity("Password123$"))

    def test_valid_pass_with_uppercase(self):
        self.assertTrue(pass_validity("Password123ABC"))

    def test_valid_pass_with_numbers(self):
        self.assertTrue(pass_validity("Password123456"))

    def test_invalid_pass_with_no_characters(self):
        self.assertFalse(pass_validity(""))

    def test_invalid_pass_with_no_numbers(self):
        self.assertFalse(pass_validity("abcABC$@#"))

    def test_invalid_pass_with_no_special_characters(self):
        self.assertFalse(pass_validity("abcABC123"))
