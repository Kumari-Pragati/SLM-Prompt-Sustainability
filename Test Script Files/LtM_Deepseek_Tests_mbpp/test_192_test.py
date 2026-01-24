import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(check_String('abc123'))

    def test_empty_string(self):
        self.assertFalse(check_String(''))

    def test_string_without_digit(self):
        self.assertFalse(check_String('abcABC'))

    def test_string_without_letter(self):
        self.assertFalse(check_String('123456'))

    def test_string_with_special_characters(self):
        self.assertFalse(check_String('abc123!'))

    def test_string_with_mixed_case(self):
        self.assertTrue(check_String('abc123ABC'))
