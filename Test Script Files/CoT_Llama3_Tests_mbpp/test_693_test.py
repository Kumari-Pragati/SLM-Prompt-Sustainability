import unittest
from mbpp_693_code import remove_multiple_spaces

class TestRemoveMultipleSpaces(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(remove_multiple_spaces("Hello   World"), "Hello World")

    def test_edge_case_empty_string(self):
        self.assertEqual(remove_multiple_spaces(""), "")

    def test_edge_case_single_space(self):
        self.assertEqual(remove_multiple_spaces("Hello World"), "Hello World")

    def test_edge_case_no_spaces(self):
        self.assertEqual(remove_multiple_spaces("HelloWorld"), "HelloWorld")

    def test_edge_case_multiple_spaces_at_start(self):
        self.assertEqual(remove_multiple_spaces("   Hello World"), "Hello World")

    def test_edge_case_multiple_spaces_at_end(self):
        self.assertEqual(remove_multiple_spaces("Hello World   "), "Hello World")

    def test_edge_case_multiple_spaces_in_between(self):
        self.assertEqual(remove_multiple_spaces("Hello   World  !"), "Hello World!")

    def test_edge_case_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_multiple_spaces(123)

    def test_edge_case_non_string_input_with_spaces(self):
        with self.assertRaises(TypeError):
            remove_multiple_spaces("Hello World 123")
