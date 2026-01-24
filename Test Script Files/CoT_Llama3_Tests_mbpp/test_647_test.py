import unittest
from mbpp_647_code import split_upperstring

class TestSplitUpperstring(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(split_upperstring("HelloWorld"), ["Hello", "World"])

    def test_edge_case_empty_string(self):
        self.assertEqual(split_upperstring(""), [])

    def test_edge_case_single_uppercase_character(self):
        self.assertEqual(split_upperstring("A"), ["A"])

    def test_edge_case_single_lowercase_character(self):
        self.assertEqual(split_upperstring("a"), [])

    def test_edge_case_multiple_uppercase_characters(self):
        self.assertEqual(split_upperstring("ABC"), ["ABC"])

    def test_edge_case_multiple_uppercase_and_lowercase_characters(self):
        self.assertEqual(split_upperstring("AbcDef"), ["Abc", "Def"])

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            split_upperstring(123)

    def test_invalid_input_non_string_list(self):
        with self.assertRaises(TypeError):
            split_upperstring(["Hello", "World"])
