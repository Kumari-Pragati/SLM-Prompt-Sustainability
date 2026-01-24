import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(check_String(''))

    def test_all_alphabets(self):
        self.assertTrue(check_String('abcdefghijklmnopqrstuvwxyz'))

    def test_all_numbers(self):
        self.assertTrue(check_String('1234567890'))

    def test_mixed_alphanumeric(self):
        self.assertTrue(check_String('abc123'))

    def test_single_alphabet(self):
        self.assertFalse(check_String('a'))

    def test_single_number(self):
        self.assertFalse(check_String('1'))

    def test_only_special_characters(self):
        self.assertFalse(check_String('!@#$%^&*()'))

    def test_empty_list(self):
        self.assertFalse(check_String(''))

    def test_whitespace(self):
        self.assertFalse(check_String('   '))
