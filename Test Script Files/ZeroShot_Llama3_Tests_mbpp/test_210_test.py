import unittest
from mbpp_210_code import is_allowed_specific_char

class TestIsAllowedSpecificChar(unittest.TestCase):

    def test_valid_string(self):
        self.assertTrue(is_allowed_specific_char("HelloWorld."))
        self.assertTrue(is_allowed_specific_char("HelloWorld123"))
        self.assertTrue(is_allowed_specific_char("HelloWorld123."))
        self.assertTrue(is_allowed_specific_char("HelloWorld123456"))

    def test_invalid_string(self):
        self.assertFalse(is_allowed_specific_char("Hello!World"))
        self.assertFalse(is_allowed_specific_char("Hello@World"))
        self.assertFalse(is_allowed_specific_char("Hello#World"))
        self.assertFalse(is_allowed_specific_char("Hello$World"))

    def test_empty_string(self):
        self.assertTrue(is_allowed_specific_char(""))

    def test_single_character(self):
        self.assertTrue(is_allowed_specific_char("a"))
        self.assertTrue(is_allowed_specific_char("1"))
        self.assertTrue(is_allowed_specific_char("."))

    def test_multiple_characters(self):
        self.assertTrue(is_allowed_specific_char("abc"))
        self.assertTrue(is_allowed_specific_char("123"))
        self.assertTrue(is_allowed_specific_char("abc.123"))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            is_allowed_specific_char(123)
        with self.assertRaises(TypeError):
            is_allowed_specific_char([1, 2, 3])
