import unittest
from mbpp_538_code import string_list_to_tuple

class TestStringListToTuple(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(string_list_to_tuple(['hello', 'world', 'python']), ('hello', 'world', 'python'))

    def test_edge_case_empty_input(self):
        self.assertEqual(string_list_to_tuple([]), ())

    def test_edge_case_single_element_input(self):
        self.assertEqual(string_list_to_tuple(['hello']), ('hello',))

    def test_edge_case_multiple_spaces_input(self):
        self.assertEqual(string_list_to_tuple(['hello   world']), ('hello', 'world'))

    def test_edge_case_single_space_input(self):
        self.assertEqual(string_list_to_tuple(['hello world']), ('hello', 'world'))

    def test_edge_case_multiple_spaces_and_newlines_input(self):
        self.assertEqual(string_list_to_tuple(['hello   world\n   python']), ('hello', 'world', 'python'))

    def test_invalid_input_non_string_input(self):
        with self.assertRaises(TypeError):
            string_list_to_tuple([1, 2, 3])

    def test_invalid_input_non_list_input(self):
        with self.assertRaises(TypeError):
            string_list_to_tuple('hello world')
