import unittest
from mbpp_640_code import remove_parenthesis

class TestRemoveParenthesis(unittest.TestCase):

    def test_typical_case(self):
        items = ["Hello (world)", "Python (3.8)"]
        expected_output = ["Hello ", "Python "]
        self.assertEqual(remove_parenthesis(items), expected_output)

    def test_edge_case(self):
        items = ["(Edge case)"]
        expected_output = [""]
        self.assertEqual(remove_parenthesis(items), expected_output)

    def test_boundary_case(self):
        items = ["(Boundary case)"]
        expected_output = [""]
        self.assertEqual(remove_parenthesis(items), expected_output)

    def test_special_case(self):
        items = ["Special (characters!)", "Another (one)"]
        expected_output = ["Special characters!", "Another "]
        self.assertEqual(remove_parenthesis(items), expected_output)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_parenthesis(123)
