import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):

    def test_allowed_characters(self):
        self.assertTrue(is_allowed_specific_char("abc123.@"))
        self.assertTrue(is_allowed_specific_char("ABC_123.@"))
        self.assertTrue(is_allowed_specific_char("abc.123@"))
        self.assertTrue(is_allowed_specific_char("ABC_123@"))

    def test_disallowed_characters(self):
        self.assertFalse(is_allowed_specific_char("!abc123.@"))
        self.assertFalse(is_allowed_specific_char("abc!123.@"))
        self.assertFalse(is_allowed_specific_char("abc123!@"))
        self.assertFalse(is_allowed_specific_char("abc123@!"))
        self.assertFalse(is_allowed_specific_char("abc123_"))
        self.assertFalse(is_allowed_specific_char("abc123-"))
        self.assertFalse(is_allowed_specific_char("abc123_@"))
        self.assertFalse(is_allowed_specific_char("abc123-@"))
        self.assertFalse(is_allowed_specific_char("abc123"))
        self.assertFalse(is_allowed_specific_char(""))
        self.assertFalse(is_allowed_specific_char(None))
