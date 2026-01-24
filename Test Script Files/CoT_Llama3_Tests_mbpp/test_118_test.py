import unittest
from mbpp_118_code import string_to_list

class TestStringToList(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(string_to_list("Hello World"), ['Hello', 'World'])

    def test_empty_string(self):
        self.assertEqual(string_to_list(""), [])

    def test_single_word(self):
        self.assertEqual(string_to_list("Hello"), ['Hello'])

    def test_multiple_spaces(self):
        self.assertEqual(string_to_list("Hello   World"), ['Hello', 'World'])

    def test_edge_case(self):
        self.assertEqual(string_to_list("   "), [])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            string_to_list(123)
