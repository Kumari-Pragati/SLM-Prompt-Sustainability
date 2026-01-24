import unittest
from mbpp_640_code import remove_parenthesis

class TestRemoveParenthesis(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(remove_parenthesis(["Hello (World)"]) , ["Hello "])

    def test_edge_condition_empty_input(self):
        self.assertEqual(remove_parenthesis([]) , [])

    def test_boundary_condition_single_item(self):
        self.assertEqual(remove_parenthesis(["(Test)"]) , [""])

    def test_complex_input(self):
        self.assertEqual(remove_parenthesis(["Hello (World)", "Test (123)"]) , ["Hello ", "Test "])

    def test_multiple_parenthesis(self):
        self.assertEqual(remove_parenthesis(["(Hello) (World)"]) , [" "])

    def test_no_parenthesis(self):
        self.assertEqual(remove_parenthesis(["Hello World"]) , ["Hello World"])
