import unittest
from mbpp_118_code import string_to_list

class TestStringToList(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(string_to_list("Hello World"), ["Hello", "World"])

    def test_edge_case_empty_string(self):
        self.assertEqual(string_to_list(""), [])

    def test_edge_case_single_word(self):
        self.assertEqual(string_to_list("Hello"), ["Hello"])

    def test_edge_case_single_space(self):
        self.assertEqual(string_to_list("   "), [])

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(string_to_list("Hello   World"), ["Hello", "World"])

    def test_edge_case_multiple_spaces_with_trailing(self):
        self.assertEqual(string_to_list("Hello   World   "), ["Hello", "World"])

    def test_edge_case_multiple_spaces_with_leading(self):
        self.assertEqual(string_to_list("   Hello   World"), ["Hello", "World"])

    def test_edge_case_multiple_spaces_with_leading_and_trailing(self):
        self.assertEqual(string_to_list("   Hello   World   "), ["Hello", "World"])

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            string_to_list(123)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            string_to_list(None)
