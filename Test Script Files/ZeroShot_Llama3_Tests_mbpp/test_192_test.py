import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):

    def test_check_string_alpha_and_digit(self):
        self.assertTrue(check_String("Hello123"))

    def test_check_string_alpha(self):
        self.assertFalse(check_String("Hello"))

    def test_check_string_digit(self):
        self.assertFalse(check_String("123"))

    def test_check_string_alpha_and_space(self):
        self.assertFalse(check_String("Hello World"))

    def test_check_string_digit_and_space(self):
        self.assertFalse(check_String("123 456"))

    def test_check_string_alpha_and_digit_and_space(self):
        self.assertFalse(check_String("Hello123 World"))

    def test_check_string_empty(self):
        self.assertFalse(check_String(""))

    def test_check_string_non_alpha_and_non_digit(self):
        self.assertFalse(check_String("!@#"))
