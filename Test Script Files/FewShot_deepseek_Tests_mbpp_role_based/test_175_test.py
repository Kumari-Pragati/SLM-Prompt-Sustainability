import unittest
from mbpp_175_code import is_valid_parenthese

class TestIsValidParenthese(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(is_valid_parenthese("()"))
        self.assertTrue(is_valid_parenthese("()[]{}"))
        self.assertTrue(is_valid_parenthese("{[]}"))

    def test_edge_conditions(self):
        self.assertFalse(is_valid_parenthese("("))
        self.assertFalse(is_valid_parenthese(")"))
        self.assertFalse(is_valid_parenthese(""))

    def test_boundary_conditions(self):
        self.assertTrue(is_valid_parenthese("("*10000 + ")"*10000))
        self.assertFalse(is_valid_parenthese("("*10001 + ")"*10000))
        self.assertFalse(is_valid_parenthese("("*10000 + ")"*9999))

    def test_invalid_inputs(self):
        self.assertFalse(is_valid_parenthese("(]"))
        self.assertFalse(is_valid_parenthese("([)]"))
        self.assertFalse(is_valid_parenthese("{"))
        self.assertFalse(is_valid_parenthese("}"))
        self.assertFalse(is_valid_parenthese("["))
        self.assertFalse(is_valid_parenthese("]"))
