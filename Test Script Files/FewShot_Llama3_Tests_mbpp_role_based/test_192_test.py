import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_String("Hello123"))

    def test_string_with_only_letters(self):
        self.assertTrue(check_String("HelloWorld"))

    def test_string_with_only_numbers(self):
        self.assertTrue(check_String("123456"))

    def test_string_with_letters_and_numbers(self):
        self.assertTrue(check_String("Hello123World"))

    def test_string_with_no_letters_or_numbers(self):
        self.assertFalse(check_String(""))

    def test_string_with_no_letters(self):
        self.assertFalse(check_String("1234567890"))

    def test_string_with_no_numbers(self):
        self.assertFalse(check_String("abcdefghijklmnopqrstuvwxyz"))

    def test_string_with_mixed_case(self):
        self.assertTrue(check_String("Hello123World"))

    def test_string_with_spaces(self):
        self.assertFalse(check_String("Hello 123 World"))
