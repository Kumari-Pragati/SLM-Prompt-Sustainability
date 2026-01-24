import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):
    def test_allowed_string(self):
        self.assertTrue(is_allowed_specific_char("HelloWorld."))
        self.assertTrue(is_allowed_specific_char("HelloWorld123"))
        self.assertTrue(is_allowed_specific_char("HelloWorld.123"))

    def test_disallowed_string(self):
        self.assertFalse(is_allowed_specific_char("Hello!World"))
        self.assertFalse(is_allowed_specific_char("Hello,World"))
        self.assertFalse(is_allowed_specific_char("Hello@World"))

    def test_empty_string(self):
        self.assertTrue(is_allowed_specific_char(""))

    def test_single_character(self):
        self.assertTrue(is_allowed_specific_char("a"))
        self.assertTrue(is_allowed_specific_char("0"))
        self.assertTrue(is_allowed_specific_char("."))

    def test_multiple_characters(self):
        self.assertTrue(is_allowed_specific_char("Hello"))
        self.assertTrue(is_allowed_specific_char("World"))
        self.assertTrue(is_allowed_specific_char("123"))
