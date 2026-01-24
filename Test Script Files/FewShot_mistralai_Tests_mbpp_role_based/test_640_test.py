import unittest
from mbpp_640_code import remove_parenthesis

class TestRemoveParenthesis(unittest.TestCase):
    def test_simple_string(self):
        self.assertEqual(remove_parenthesis("Hello (world)!"), "Hello world!")

    def test_multiple_parentheses(self):
        self.assertEqual(remove_parenthesis("(a) (b) (c)"), "a b c")

    def test_empty_string(self):
        self.assertEqual(remove_parenthesis(""), "")

    def test_string_with_only_parentheses(self):
        self.assertEqual(remove_parenthesis("(a)"), "")

    def test_string_with_mixed_characters(self):
        self.assertEqual(remove_parenthesis("Hello (world)!, (how) are (you)?"), "Hello world!, how are you?")

    def test_string_with_nested_parentheses(self):
        self.assertEqual(remove_parenthesis("((a) (b))"), "a b")
