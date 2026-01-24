import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(remove_multiple_spaces("Hello   World"), "Hello World")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_multiple_spaces(""), "")

    def test_edge_case_single_space(self):
        self.assertEqual(remove_multiple_spaces("Hello World"), "Hello World")

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(remove_multiple_spaces("Hello   World   this   is   a   test"), "Hello World this is a test")

    def test_edge_case_leading_spaces(self):
        self.assertEqual(remove_multiple_spaces("   Hello World"), "Hello World")

    def test_edge_case_trailing_spaces(self):
        self.assertEqual(remove_multiple_spaces("Hello World   "), "Hello World")

    def test_edge_case_multiple_leading_and_trailing_spaces(self):
        self.assertEqual(remove_multiple_spaces("   Hello   World   "), "Hello World")

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            remove_multiple_spaces(123)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            remove_multiple_spaces(None)
