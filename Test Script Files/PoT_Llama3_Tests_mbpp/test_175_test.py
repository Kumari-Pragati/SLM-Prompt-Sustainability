import unittest
from mbpp_175_code import is_valid_parenthese

class TestIsValidParenthese(unittest.TestCase):

    def test_typical_valid(self):
        self.assertTrue(is_valid_parenthese("()"))
        self.assertTrue(is_valid_parenthese("()()"))
        self.assertTrue(is_valid_parenthese("({[]})"))

    def test_typical_invalid(self):
        self.assertFalse(is_valid_parenthese(")()("))
        self.assertFalse(is_valid_parenthese("({[)}"))
        self.assertFalse(is_valid_parenthese("([)]"))

    def test_edge_opening(self):
        self.assertTrue(is_valid_parenthese("("))
        self.assertTrue(is_valid_parenthese("{"))
        self.assertTrue(is_valid_parenthese("["))

    def test_edge_closing(self):
        self.assertTrue(is_valid_parenthese(")"))
        self.assertTrue(is_valid_parenthese("}"))
        self.assertTrue(is_valid_parenthese("]"))

    def test_edge_opening_closing(self):
        self.assertTrue(is_valid_parenthese("()"))
        self.assertTrue(is_valid_parenthese("()"))
        self.assertTrue(is_valid_parenthese("({[]})"))

    def test_edge_opening_closing_invalid(self):
        self.assertFalse(is_valid_parenthese(")(("))
        self.assertFalse(is_valid_parenthese("({[)}"))
        self.assertFalse(is_valid_parenthese("([)]"))

    def test_edge_empty(self):
        self.assertTrue(is_valid_parenthese(""))
