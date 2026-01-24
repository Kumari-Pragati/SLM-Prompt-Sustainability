import unittest
from mbpp_640_code import remove_parenthesis

class TestRemoveParenthesis(unittest.TestCase):

    def test_typical_case(self):
        items = ["Hello (World)", "Python (Programming)"]
        expected_output = ["Hello ", "Python "]
        self.assertEqual(remove_parenthesis(items), expected_output)

    def test_empty_string(self):
        items = ["", ""]
        expected_output = ["", ""]
        self.assertEqual(remove_parenthesis(items), expected_output)

    def test_no_parenthesis(self):
        items = ["Hello World", "Python Programming"]
        expected_output = ["Hello World", "Python Programming"]
        self.assertEqual(remove_parenthesis(items), expected_output)

    def test_single_parenthesis(self):
        items = ["Hello (World", "Python ("]
        expected_output = ["Hello (World", "Python ("]
        self.assertEqual(remove_parenthesis(items), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_parenthesis(123)
