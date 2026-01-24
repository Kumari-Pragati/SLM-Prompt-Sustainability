import unittest
from mbpp_640_code import remove_parenthesis

class TestRemoveParenthesis(unittest.TestCase):

    def test_remove_parenthesis(self):
        self.assertEqual(remove_parenthesis(["Hello (world)"]), ["Hello world"])
        self.assertEqual(remove_parenthesis(["Hello (world) foo (bar)"]), ["Hello world foo bar"])
        self.assertEqual(remove_parenthesis(["Hello (world) foo (bar) baz (qux)"]), ["Hello world foo bar baz qux"])
        self.assertEqual(remove_parenthesis(["Hello (world) foo (bar) baz (qux) qux (xyz)"]), ["Hello world foo bar baz qux qux"])
        self.assertEqual(remove_parenthesis(["Hello (world) foo (bar) baz (qux) qux (xyz) qux (abc)"]), ["Hello world foo bar baz qux qux qux"])

    def test_remove_parenthesis_empty(self):
        self.assertEqual(remove_parenthesis([]), [])

    def test_remove_parenthesis_single(self):
        self.assertEqual(remove_parenthesis(["Hello (world)"]), ["Hello world"])

    def test_remove_parenthesis_multiple(self):
        self.assertEqual(remove_parenthesis(["Hello (world)", "foo (bar)", "baz (qux)"]), ["Hello world", "foo bar", "baz qux"])
