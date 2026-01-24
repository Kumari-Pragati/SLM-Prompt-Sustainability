import unittest
from mbpp_640_code import remove_parenthesis

class TestRemoveParenthesis(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(remove_parenthesis(["hello (world)", "goodbye (earth)"]),
                         ["hello world", "goodbye earth"])

    def test_edge_case_empty_list(self):
        self.assertEqual(remove_parenthesis([]), [])

    def test_edge_case_single_element(self):
        self.assertEqual(remove_parenthesis(["hello (world)"]), ["hello world"])

    def test_edge_case_multiple_parentheses(self):
        self.assertEqual(remove_parenthesis(["hello (world) (again)", "goodbye (earth) (moon)"]),
                         ["hello world again", "goodbye earth moon"])

    def test_edge_case_no_parentheses(self):
        self.assertEqual(remove_parenthesis(["hello", "goodbye"]), ["hello", "goodbye"])

    def test_edge_case_parentheses_with_spaces(self):
        self.assertEqual(remove_parenthesis(["hello ( world )", "goodbye ( earth )"]),
                         ["hello world", "goodbye earth"])

    def test_edge_case_parentheses_with_newlines(self):
        self.assertEqual(remove_parenthesis(["hello\n(world)", "goodbye\n(earth)"]),
                         ["hello world", "goodbye earth"])

    def test_edge_case_parentheses_with_tabs(self):
        self.assertEqual(remove_parenthesis(["hello\t(world)", "goodbye\t(earth)"]),
                         ["hello world", "goodbye earth"])

    def test_edge_case_parentheses_with_multiple_spaces(self):
        self.assertEqual(remove_parenthesis(["hello   (world)", "goodbye   (earth)"]),
                         ["hello world", "goodbye earth"])

    def test_edge_case_parentheses_with_multiple_newlines(self):
        self.assertEqual(remove_parenthesis(["hello\n\n(world)", "goodbye\n\n(earth)"]),
                         ["hello world", "goodbye earth"])

    def test_edge_case_parentheses_with_multiple_tabs(self):
        self.assertEqual(remove_parenthesis(["hello\t\t(world)", "goodbye\t\t(earth)"]),
                         ["hello world", "goodbye earth"])

    def test_edge_case_parentheses_with_multiple_spaces_and_newlines(self):
        self.assertEqual(remove_parenthesis(["hello   \n\t(world)", "goodbye   \n\t(earth)"]),
                         ["hello world", "goodbye earth"])

    def test_edge_case_parentheses_with_multiple_spaces_and_tabs(self):
        self.assertEqual(remove_parenthesis(["hello   \t(world)", "goodbye   \t(earth)"]),
                         ["hello world", "goodbye earth"])

    def test_edge_case_parentheses_with_multiple_spaces_and_newlines_and_tabs(self):
        self.assertEqual(remove_parenthesis(["hello   \n\t\t(world)", "goodbye   \n\t\t(earth)"]),
                         ["hello world", "goodbye earth"])

    def test_edge_case_parentheses_with_multiple_spaces_and_newlines_and_tabs_and_spaces(self):
        self.assertEqual(remove_parenthesis(["hello   \n\t\t   (world)", "goodbye   \n\t\t   (earth)"]),
                         ["hello world", "goodbye earth"])

    def test_edge_case_parentheses_with_multiple_spaces_and_newlines_and_tabs_and_spaces_and_newlines(self):
        self.assertEqual(remove_parenthesis(["hello   \n\t\t   \n(world)", "goodbye   \n\t\t   \n(earth)"]),
                         ["hello world", "goodbye earth"])

    def test_edge_case_parentheses_with_multiple_spaces_and_newlines_and_tabs_and_spaces_and_newlines_and_tabs(self):
        self.assertEqual(remove_parenthesis(["hello   \n\t\t   \n\t\t   (world)", "goodbye   \n\t\t   \n\t\t   (earth)"]),
                         ["hello world", "goodbye earth"])

    def test_edge_case_parentheses_with_multiple_spaces_and_newlines_and_tabs_and_spaces_and_newlines_and_tabs_and_spaces(self):
        self.assertEqual(remove_parenthesis(["hello   \n\t\t   \n\t\t   \n   (world)", "goodbye   \n\t\t   \n\t\t   \n   (earth)"]),
                         ["hello world", "goodbye earth"])
