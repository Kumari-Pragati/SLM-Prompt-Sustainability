import unittest
from mbpp_175_code import is_valid_parenthese

class TestIsValidParenthese(unittest.TestCase):

    def test_valid_parenthese(self):
        self.assertTrue(is_valid_parenthese("()"))
        self.assertTrue(is_valid_parenthese("()[]{}"))
        self.assertTrue(is_valid_parenthese("(a+b)-(c+d)"))

    def test_invalid_parenthese(self):
        self.assertFalse(is_valid_parenthese("(("))
        self.assertFalse(is_valid_parenthese("({["))
        self.assertFalse(is_valid_parenthese("([)]"))

    def test_empty_string(self):
        self.assertTrue(is_valid_parenthese(""))

    def test_single_parenthese(self):
        self.assertTrue(is_valid_parenthese("("))
        self.assertTrue(is_valid_parenthese(")"))
        self.assertTrue(is_valid_parenthese("{"))
        self.assertTrue(is_valid_parenthese("}"))
        self.assertTrue(is_valid_parenthese("["))
        self.assertTrue(is_valid_parenthese("]"))

    def test_multiple_parenthese(self):
        self.assertTrue(is_valid_parenthese("()()"))
        self.assertTrue(is_valid_parenthese("({[})"))
        self.assertTrue(is_valid_parenthese("([{}])"))

    def test_parenthese_with_spaces(self):
        self.assertTrue(is_valid_parenthese("( a + b )"))
        self.assertTrue(is_valid_parenthese("({ [ } )"))
