import unittest
from mbpp_956_code import split_list

class TestSplitList(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(split_list("HelloWorld"), ["Hello", "World"])

    def test_edge_case_empty_string(self):
        self.assertEqual(split_list(""), [])

    def test_edge_case_single_word(self):
        self.assertEqual(split_list("Hello"), ["Hello"])

    def test_edge_case_single_character(self):
        self.assertEqual(split_list("A"), ["A"])

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(split_list("Hello   World"), ["Hello", "World"])

    def test_edge_case_punctuation(self):
        self.assertEqual(split_list("Hello,World"), ["Hello", "World"])

    def test_edge_case_numbers(self):
        self.assertEqual(split_list("Hello123World"), ["Hello", "123", "World"])

    def test_edge_case_punctuation_and_numbers(self):
        self.assertEqual(split_list("Hello,123World"), ["Hello", "123", "World"])

    def test_invalid_input_non_string(self):
        with self.assertRaises(TypeError):
            split_list(123)
