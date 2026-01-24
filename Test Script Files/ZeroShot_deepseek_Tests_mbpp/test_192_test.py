import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):

    def test_alpha_and_digit(self):
        self.assertTrue(check_String('abc123'))

    def test_only_alpha(self):
        self.assertFalse(check_String('abc'))

    def test_only_digit(self):
        self.assertFalse(check_String('123'))

    def test_empty_string(self):
        self.assertFalse(check_String(''))

    def test_special_characters(self):
        self.assertFalse(check_String('abc@123'))
