import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):
    def test_allowed_chars(self):
        self.assertTrue(is_allowed_specific_char("hello"))
        self.assertTrue(is_allowed_specific_char("hello123"))
        self.assertTrue(is_allowed_specific_char("hello.123"))

    def test_disallowed_chars(self):
        self.assertFalse(is_allowed_specific_char("hello!"))
        self.assertFalse(is_allowed_specific_char("hello,"))
        self.assertFalse(is_allowed_specific_char("hello?"))

    def test_empty_string(self):
        self.assertTrue(is_allowed_specific_char(""))

    def test_single_char(self):
        self.assertTrue(is_allowed_specific_char("a"))
        self.assertTrue(is_allowed_specific_char("0"))
        self.assertTrue(is_allowed_specific_char("."))

    def test_multiple_chars(self):
        self.assertFalse(is_allowed_specific_char("abc!"))
        self.assertFalse(is_allowed_specific_char("123,"))
        self.assertFalse(is_allowed_specific_char("hello?world"))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            is_allowed_specific_char(123)
