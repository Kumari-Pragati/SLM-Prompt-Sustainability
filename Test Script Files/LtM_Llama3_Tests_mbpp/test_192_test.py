import unittest
from mbpp_192_code import check_String

class TestCheckString(unittest.TestCase):
    def test_simple_valid(self):
        self.assertTrue(check_String("Hello123"))
        self.assertTrue(check_String("abc456"))

    def test_empty_input(self):
        self.assertFalse(check_String(""))

    def test_alpha_only(self):
        self.assertFalse(check_String("abcdef"))

    def test_digit_only(self):
        self.assertFalse(check_String("123456"))

    def test_mixed_alpha_digit(self):
        self.assertTrue(check_String("abc123"))

    def test_mixed_alpha_digit_with_spaces(self):
        self.assertTrue(check_String("abc 123"))

    def test_mixed_alpha_digit_with_punctuation(self):
        self.assertTrue(check_String("abc!123"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            check_String(123)
