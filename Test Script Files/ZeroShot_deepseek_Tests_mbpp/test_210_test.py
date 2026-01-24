import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):

    def test_allowed_chars(self):
        self.assertTrue(is_allowed_specific_char("abc123.def"))
        self.assertTrue(is_allowed_specific_char("ABC123.DEF"))
        self.assertTrue(is_allowed_specific_char("123.456"))
        self.assertTrue(is_allowed_specific_char("a.b"))
        self.assertTrue(is_allowed_specific_char("a1.b2"))

    def test_disallowed_chars(self):
        self.assertFalse(is_allowed_specific_char("abc123@def"))
        self.assertFalse(is_allowed_specific_char("ABC!@#"))
        self.assertFalse(is_allowed_specific_char("123$%^"))
        self.assertFalse(is_allowed_specific_char("a@.b"))
        self.assertFalse(is_allowed_specific_char("a1@b2"))
