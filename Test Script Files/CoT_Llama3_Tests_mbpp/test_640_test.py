import unittest
from mbpp_640_code import remove_parenthesis

class TestRemoveParenthesis(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(remove_parenthesis(["Hello (world)"]), ["Hello world"])

    def test_multiple_items(self):
        self.assertEqual(remove_parenthesis(["Hello (world)", "Goodbye (earth)"]), ["Hello world", "Goodbye earth"])

    def test_no_parenthesis(self):
        self.assertEqual(remove_parenthesis(["Hello", "Goodbye"]), ["Hello", "Goodbye"])

    def test_no_items(self):
        self.assertEqual(remove_parenthesis([]), [])

    def test_parenthesis_in_middle(self):
        self.assertEqual(remove_parenthesis(["Hello (world) foo (bar)"]), ["Hello world foo bar"])

    def test_parenthesis_at_start(self):
        self.assertEqual(remove_parenthesis(["(hello) world", "Goodbye (earth)"]), ["hello world", "Goodbye earth"])

    def test_parenthesis_at_end(self):
        self.assertEqual(remove_parenthesis(["Hello world (foo)", "Goodbye (earth)"]), ["Hello world foo", "Goodbye earth"])

    def test_parenthesis_in_multiple_places(self):
        self.assertEqual(remove_parenthesis(["Hello (world) foo (bar) baz (qux)"]), ["Hello world foo bar baz qux"])
