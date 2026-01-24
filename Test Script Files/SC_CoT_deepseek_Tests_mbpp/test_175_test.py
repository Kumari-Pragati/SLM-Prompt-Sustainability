import unittest
from mbpp_175_code import is_valid_parenthese

class TestIsValidParenthese(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_valid_parenthese("()"))
        self.assertTrue(is_valid_parenthese("()[]{}"))
        self.assertTrue(is_valid_parenthese("{[]}"))

    def test_edge_cases(self):
        self.assertFalse(is_valid_parenthese("("))
        self.assertFalse(is_valid_parenthese(")"))
        self.assertFalse(is_valid_parenthese(""))

    def test_corner_cases(self):
        self.assertFalse(is_valid_parenthese(")("))
        self.assertFalse(is_valid_parenthese("({[]})]"))
        self.assertFalse(is_valid_parenthese("({[]})("))

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            is_valid_parenthese(123)
        with self.assertRaises(TypeError):
            is_valid_parenthese(None)
        with self.assertRaises(TypeError):
            is_valid_parenthese([])
