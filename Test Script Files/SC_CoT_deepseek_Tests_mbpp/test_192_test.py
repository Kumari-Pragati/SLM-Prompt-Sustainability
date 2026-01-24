import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_String('a1'))

    def test_no_alpha(self):
        self.assertFalse(check_String('1234567890'))

    def test_no_digit(self):
        self.assertFalse(check_String('abcdefghijklmnopqrstuvwxyz'))

    def test_empty_string(self):
        self.assertFalse(check_String(''))

    def test_special_characters(self):
        self.assertFalse(check_String('!@#$%^&*()'))

    def test_whitespace(self):
        self.assertFalse(check_String(' '))

    def test_string_with_special_characters_and_digits(self):
        self.assertFalse(check_String('a1!@#$%^&*()'))

    def test_string_with_special_characters_and_alphabets(self):
        self.assertFalse(check_String('a!@#$%^&*()1'))

    def test_string_with_only_special_characters(self):
        self.assertFalse(check_String('!@#$%^&*()'))

    def test_string_with_only_spaces(self):
        self.assertFalse(check_String('   '))
