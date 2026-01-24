import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):
    def test_string_only_letters(self):
        self.assertTrue(check_String("abcdefg"))

    def test_string_only_numbers(self):
        self.assertTrue(check_String("123456"))

    def test_string_empty(self):
        self.assertFalse(check_String(""))

    def test_string_mixed_letters_and_numbers(self):
        self.assertTrue(check_String("abc123"))

    def test_string_only_special_characters(self):
        self.assertFalse(check_String("!@#$%^&*()"))

    def test_string_only_spaces(self):
        self.assertFalse(check_String("   "))
