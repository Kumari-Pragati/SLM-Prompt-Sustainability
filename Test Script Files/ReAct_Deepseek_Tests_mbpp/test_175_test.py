import unittest
from mbpp_175_code import is_valid_parenthese

class TestIsValidParenthese(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_valid_parenthese("()"))
        self.assertTrue(is_valid_parenthese("()[]{}"))
        self.assertTrue(is_valid_parenthese("{[]}"))

    def test_empty_string(self):
        self.assertTrue(is_valid_parenthese(""))

    def test_single_parenthese(self):
        self.assertFalse(is_valid_parenthese("("))
        self.assertFalse(is_valid_parenthese(")"))
        self.assertFalse(is_valid_parenthese("{"))
        self.assertFalse(is_valid_parenthese("}"))
        self.assertFalse(is_valid_parenthese("["))
        self.assertFalse(is_valid_parenthese("]"))

    def test_mismatched_parentheses(self):
        self.assertFalse(is_valid_parenthese("(]"))
        self.assertFalse(is_valid_parenthese("([)]"))
        self.assertFalse(is_valid_parenthese("{[]}("))

    def test_nested_parentheses(self):
        self.assertTrue(is_valid_parenthese("({[]})"))

    def test_extra_characters(self):
        self.assertFalse(is_valid_parenthese("({[]})a"))
        self.assertFalse(is_valid_parenthese("({[]}) "))
