import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_allowed_specific_char("abc123.def"))
        self.assertTrue(is_allowed_specific_char(""))
        self.assertTrue(is_allowed_specific_char("123456"))
        self.assertTrue(is_allowed_specific_char("abcdefghijklmnopqrstuvwxyz"))
        self.assertTrue(is_allowed_specific_char("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    def test_edge_cases(self):
        self.assertTrue(is_allowed_specific_char("."))
        self.assertTrue(is_allowed_specific_char("a."))
        self.assertTrue(is_allowed_specific_char(".a"))
        self.assertTrue(is_allowed_specific_char("a.b"))
        self.assertTrue(is_allowed_specific_char("123.456"))
        self.assertTrue(is_allowed_specific_char("a1b2c3.d4e5f6"))

    def test_explicitly_handled_error_cases(self):
        self.assertFalse(is_allowed_specific_char("@#$%^&*()"))
        self.assertFalse(is_allowed_specific_char("a@b"))
        self.assertFalse(is_allowed_specific_char("a#b"))
        self.assertFalse(is_allowed_specific_char("a$b"))
        self.assertFalse(is_allowed_specific_char("a%b"))
        self.assertFalse(is_allowed_specific_char("a^b"))
        self.assertFalse(is_allowed_specific_char("a&b"))
        self.assertFalse(is_allowed_specific_char("a*b"))
        self.assertFalse(is_allowed_specific_char("a(b"))
        self.assertFalse(is_allowed_specific_char("a)b"))
