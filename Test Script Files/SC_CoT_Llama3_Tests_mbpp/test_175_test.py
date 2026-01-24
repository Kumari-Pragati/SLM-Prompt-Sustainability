import unittest
from mbpp_175_code import is_valid_parenthese

class TestIsValidParenthese(unittest.TestCase):
    def test_valid_parenthese(self):
        self.assertTrue(is_valid_parenthese("()"))
        self.assertTrue(is_valid_parenthese("()[]{}"))
        self.assertTrue(is_valid_parenthese("({[]})"))

    def test_invalid_parenthese(self):
        self.assertFalse(is_valid_parenthese("([)]"))
        self.assertFalse(is_valid_parenthese("({)}"))
        self.assertFalse(is_valid_parenthese("([)]"))

    def test_empty_string(self):
        self.assertTrue(is_valid_parenthese(""))

    def test_single_char(self):
        self.assertTrue(is_valid_parenthese("("))
        self.assertTrue(is_valid_parenthese(")"))
        self.assertTrue(is_valid_parenthese("{"))
        self.assertTrue(is_valid_parenthese("}"))
        self.assertTrue(is_valid_parenthese("["))
        self.assertTrue(is_valid_parenthese("]"))

    def test_multiple_chars(self):
        self.assertTrue(is_valid_parenthese("()"))
        self.assertTrue(is_valid_parenthese("()[]{}"))
        self.assertTrue(is_valid_parenthese("({[]})"))

    def test_mixed_chars(self):
        self.assertTrue(is_valid_parenthese("({[]})"))
        self.assertTrue(is_valid_parenthese("({[()]}"))
        self.assertTrue(is_valid_parenthese("({[()]}"))

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            is_valid_parenthese(123)
