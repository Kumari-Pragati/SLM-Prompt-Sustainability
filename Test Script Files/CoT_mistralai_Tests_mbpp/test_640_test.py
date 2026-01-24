import unittest
from mbpp_640_code import remove_parenthesis

class TestRemoveParenthesis(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(remove_parenthesis(""), "")

    def test_single_char(self):
        for char in "!@#$%^&*()_+-=[]{};':\"|,.<>/? ":
            self.assertEqual(remove_parenthesis(char), char)

    def test_single_parenthesis(self):
        self.assertEqual(remove_parenthesis("("), "")
        self.assertEqual(remove_parenthesis(")"), "")

    def test_multiple_parentheses(self):
        self.assertEqual(remove_parenthesis("()"), "")
        self.assertEqual(remove_parenthesis("()()"), "")
        self.assertEqual(remove_parenthesis("(())"), "")
        self.assertEqual(remove_parenthesis("(())()"), "")

    def test_nested_parentheses(self):
        self.assertEqual(remove_parenthesis("((()))"), "")
        self.assertEqual(remove_parenthesis("((()))((()))"), "")
        self.assertEqual(remove_parenthesis("((()))((()))((()))"), "")

    def test_mixed_string(self):
        self.assertEqual(remove_parenthesis("Hello, World! (This is a test)"), "Hello, World! This is a test")
        self.assertEqual(remove_parenthesis("(1 + 2) * (3 + 4)"), "1 + 2 * 3 + 4")
        self.assertEqual(remove_parenthesis("(1 + 2)(3 + 4)"), "1 + 23 + 4")
        self.assertEqual(remove_parenthesis("(1 + 2)(3 + 4)(5 + 6)"), "1 + 23 + 45 + 6")

    def test_invalid_parenthesis(self):
        self.assertRaises(ValueError, remove_parenthesis, "(())(")
        self.assertRaises(ValueError, remove_parenthesis, "((()))((()))((()))((()))")
