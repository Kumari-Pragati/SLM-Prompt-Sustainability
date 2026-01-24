import unittest
from mbpp_310_code import string_to_tuple

class TestStringToTuple(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(string_to_tuple("Hello World"), ('Hello', 'World'))

    def test_edge_case_empty_string(self):
        self.assertEqual(string_to_tuple(""), ())

    def test_edge_case_single_space(self):
        self.assertEqual(string_to_tuple(" "), (''))

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(string_to_tuple("   "), (''))

    def test_edge_case_non_space_characters(self):
        self.assertEqual(string_to_tuple("HelloWorld"), ('Hello', 'World'))

    def test_edge_case_mixed_spaces_and_characters(self):
        self.assertEqual(string_to_tuple("Hello World!"), ('Hello', 'World', '!'))

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            string_to_tuple(123)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            string_to_tuple(None)
