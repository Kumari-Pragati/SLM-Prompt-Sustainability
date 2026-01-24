import unittest
from mbpp_892_code import remove_spaces

class TestRemoveSpaces(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(remove_spaces("Hello   World"), "Hello World")

    def test_multiple_spaces(self):
        self.assertEqual(remove_spaces("Hello    World"), "Hello World")

    def test_single_space(self):
        self.assertEqual(remove_spaces("Hello World"), "Hello World")

    def test_no_spaces(self):
        self.assertEqual(remove_spaces("HelloWorld"), "HelloWorld")

    def test_edge_case_leading_spaces(self):
        self.assertEqual(remove_spaces("   Hello World"), "Hello World")

    def test_edge_case_trailing_spaces(self):
        self.assertEqual(remove_spaces("Hello World   "), "Hello World")

    def test_edge_case_multiple_leading_trailing_spaces(self):
        self.assertEqual(remove_spaces("   Hello   World   "), "Hello World")

    def test_error_case_non_string_input(self):
        with self.assertRaises(TypeError):
            remove_spaces(123)

    def test_error_case_non_string_input_with_message(self):
        with self.assertRaises(TypeError) as e:
            remove_spaces(123)
        self.assertEqual(str(e.exception), "Input must be a string")
