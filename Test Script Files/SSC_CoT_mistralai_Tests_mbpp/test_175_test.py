import unittest
from mbpp_175_code import is_valid_parenthese

class TestIsValidParenthese(unittest.TestCase):
    def test_valid_parentheses(self):
        self.assertTrue(is_valid_parenthese("()"))
        self.assertTrue(is_valid_parenthese("{}"))
        self.assertTrue(is_valid_parenthese("[]"))
        self.assertTrue(is_valid_parenthese("(())"))
        self.assertTrue(is_valid_parenthese("{}{}"))
        self.assertTrue(is_valid_parenthese("[][]"))

    def test_mixed_parentheses(self):
        self.assertTrue(is_valid_parenthese("(()){}[]"))
        self.assertTrue(is_valid_parenthese("{}()[]"))
        self.assertTrue(is_valid_parenthese("(){}[]"))
        self.assertTrue(is_valid_parenthese("{}()[]("))
        self.assertTrue(is_valid_parenthese("(){}[]}"))
        self.assertTrue(is_valid_parenthese("()[]{}"))

    def test_empty_string(self):
        self.assertTrue(is_valid_parenthese(""))

    def test_single_parenthesis(self):
        self.assertFalse(is_valid_parenthese("("))
        self.assertFalse(is_valid_parenthese(")"))
        self.assertFalse(is_valid_parenthese("{"))
        self.assertFalse(is_valid_parenthese("}"))
        self.assertFalse(is_valid_parenthese("["))
        self.assertFalse(is_valid_parenthese("]"))

    def test_invalid_parentheses(self):
        self.assertFalse(is_valid_parenthese("(}"))
        self.assertFalse(is_valid_parenthese("{)"))
        self.assertFalse(is_valid_parenthese("]["))
        self.assertFalse(is_valid_parenthese("][("))
        self.assertFalse(is_valid_parenthese(")(("))
        self.assertFalse(is_valid_parenthese("}{{"))
