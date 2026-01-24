import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):
    def test_allowed_characters(self):
        self.assertTrue(is_allowed_specific_char("abc123.@"))
        self.assertTrue(is_allowed_specific_char("ABC_123.@"))
        self.assertTrue(is_allowed_specific_char("abc123.ABC"))

    def test_empty_string(self):
        self.assertTrue(is_allowed_specific_char(""))

    def test_only_special_characters(self):
        self.assertFalse(is_allowed_specific_char("!@#$%^&*()"))

    def test_only_numbers(self):
        self.assertFalse(is_allowed_specific_char("1234567890"))

    def test_only_uppercase_letters(self):
        self.assertFalse(is_allowed_specific_char("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    def test_only_lowercase_letters(self):
        self.assertFalse(is_allowed_specific_char("abcdefghijklmnopqrstuvwxyz"))
