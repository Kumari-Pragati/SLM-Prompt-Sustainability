import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):
    def test_allowed_chars(self):
        self.assertTrue(is_allowed_specific_char("hello"))
        self.assertTrue(is_allowed_specific_char("hello123"))
        self.assertTrue(is_allowed_specific_char("hello.123"))

    def test_disallowed_chars(self):
        self.assertFalse(is_allowed_specific_char("hello!"))
        self.assertFalse(is_allowed_specific_char("hello@"))
        self.assertFalse(is_allowed_specific_char("hello#"))

    def test_edge_cases(self):
        self.assertTrue(is_allowed_specific_char(""))
        self.assertTrue(is_allowed_specific_char("a"))
        self.assertTrue(is_allowed_specific_char("a."))
        self.assertTrue(is_allowed_specific_char("123"))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_allowed_specific_char(None)
        with self.assertRaises(TypeError):
            is_allowed_specific_char(123)
