import unittest
from mbpp_175_code import is_valid_parenthese

class TestIsValidParenthese(unittest.TestCase):

    def test_simple_valid_cases(self):
        self.assertTrue(is_valid_parenthese("()"))
        self.assertTrue(is_valid_parenthese("()[]{}"))
        self.assertTrue(is_valid_parenthese("{[]}"))

    def test_edge_and_boundary_conditions(self):
        self.assertTrue(is_valid_parenthese(""))
        self.assertFalse(is_valid_parenthese("("))
        self.assertFalse(is_valid_parenthese(")"))
        self.assertFalse(is_valid_parenthese("({[]})]"))
        self.assertFalse(is_valid_parenthese("({[]})["))

    def test_complex_and_corner_cases(self):
        self.assertFalse(is_valid_parenthese("({[]})"))
        self.assertFalse(is_valid_parenthese("({[]})"))
        self.assertFalse(is_valid_parenthese("({[]})"))
