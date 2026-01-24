import unittest
from mbpp_175_code import is_valid_parenthese

class TestValidParentheses(unittest.TestCase):

    def test_empty_string(self):
        self.assertTrue(is_valid_parenthese(""))

    def test_single_char(self):
        self.assertTrue(is_valid_parenthese("("))
        self.assertTrue(is_valid_parenthese("{"))
        self.assertTrue(is_valid_parenthese("["))
        self.assertFalse(is_valid_parenthese(")"))
        self.assertFalse(is_valid_parenthese("}"))
        self.assertFalse(is_valid_parenthese("]"))

    def test_valid_parentheses(self):
        self.assertTrue(is_valid_parenthese("()"))
        self.assertTrue(is_valid_parenthese("{}"))
        self.assertTrue(is_valid_parenthese("[]"))
        self.assertTrue(is_valid_parenthese("(())"))
        self.assertTrue(is_valid_parenthese("{}{}"))
        self.assertTrue(is_valid_parenthese("[][]"))
        self.assertTrue(is_valid_parenthese("(()){}[]"))

    def test_invalid_parentheses(self):
        self.assertFalse(is_valid_parenthese("(]"))
        self.assertFalse(is_valid_parenthese("{)}"))
        self.assertFalse(is_valid_parenthese("[(])"))
        self.assertFalse(is_valid_parenthese("(())("))
        self.assertFalse(is_valid_parenthese("{}{}}"))
        self.assertFalse(is_valid_parenthese("[][]]"))
        self.assertFalse(is_valid_parenthese("(()){}[]("))
