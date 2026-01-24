import unittest
from mbpp_640_code import remove_parenthesis

class TestRemoveParenthesis(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(remove_parenthesis(["hello world (123)"]), ["hello world"])
        self.assertEqual(remove_parenthesis(["(123)"]), [])
        self.assertEqual(remove_parenthesis(["hello (123) world"]), ["hello world"])

    def test_edge(self):
        self.assertEqual(remove_parenthesis([""]), [])
        self.assertEqual(remove_parenthesis(["hello"]), ["hello"])
        self.assertEqual(remove_parenthesis(["(123) (456)"]), [])

    def test_invalid(self):
        with self.assertRaises(TypeError):
            remove_parenthesis(None)
        with self.assertRaises(TypeError):
            remove_parenthesis(123)
