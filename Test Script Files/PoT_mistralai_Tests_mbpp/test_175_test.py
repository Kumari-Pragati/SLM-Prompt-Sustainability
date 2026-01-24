import unittest
from mbpp_175_code import is_valid_parenthese

class TestIsValidParenthese(unittest.TestCase):

    def test_typical_cases(self):
        self.assertTrue(is_valid_parenthese("()"))
        self.assertTrue(is_valid_parenthese("{}"))
        self.assertTrue(is_valid_parenthese("[]"))
        self.assertTrue(is_valid_parenthese("(())"))
        self.assertTrue(is_valid_parenthese("{}{}"))
        self.assertTrue(is_valid_parenthese("[][]"))

    def test_edge_and_boundary_cases(self):
        self.assertTrue(is_valid_parenthese("(())("))
        self.assertTrue(is_valid_parenthese("{}(){}"))
        self.assertTrue(is_valid_parenthese("[]()[]"))
        self.assertTrue(is_valid_parenthese("(())(())"))
        self.assertTrue(is_valid_parenthese("{}(){}(){}"))
        self.assertTrue(is_valid_parenthese("[]()[]()[]"))
        self.assertTrue(is_valid_parenthese("(())(())(())"))
        self.assertTrue(is_valid_parenthese("{}(){}(){}(){}"))
        self.assertTrue(is_valid_parenthese("[]()[]()[][]"))

        self.assertFalse(is_valid_parenthese("(("))
        self.assertFalse(is_valid_parenthese("{}}"))
        self.assertFalse(is_valid_parenthese("[[")
        self.assertFalse(is_valid_parenthese("())"))
        self.assertFalse(is_valid_parenthese("{}}")))
        self.assertFalse(is_valid_parenthese("[]]"))
        self.assertFalse(is_valid_parenthese("(()))"))
        self.assertFalse(is_valid_parenthese("{}(){}()"))
        self.assertFalse(is_valid_parenthese("[][]]"))
