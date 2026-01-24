import unittest
from mbpp_956_code import split_list

class TestSplitList(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(split_list("HelloWorld"), ["Hello", "World"])

    def test_edge_case_uppercase(self):
        self.assertEqual(split_list("WORLD"), ["WORLD"])

    def test_edge_case_lowercase(self):
        self.assertEqual(split_list("world"), [])

    def test_edge_case_empty_string(self):
        self.assertEqual(split_list(""), [])

    def test_edge_case_single_char(self):
        self.assertEqual(split_list("a"), [])

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(split_list("Hello   World"), ["Hello", "World"])

    def test_edge_case_non_alphabetic_chars(self):
        self.assertEqual(split_list("Hello123World"), ["Hello", "World"])

    def test_edge_case_multiple_consecutive_chars(self):
        self.assertEqual(split_list("HelloWorldHello"), ["Hello", "World", "Hello"])

    def test_edge_case_multiple_consecutive_spaces(self):
        self.assertEqual(split_list("Hello   World   Hello"), ["Hello", "World", "Hello"])

    def test_edge_case_newline(self):
        self.assertEqual(split_list("Hello\nWorld"), ["Hello", "World"])

    def test_edge_case_tab(self):
        self.assertEqual(split_list("Hello\tWorld"), ["Hello", "World"])

    def test_edge_case_multiple_newlines(self):
        self.assertEqual(split_list("Hello\nWorld\nHello"), ["Hello", "World", "Hello"])

    def test_edge_case_multiple_tabs(self):
        self.assertEqual(split_list("Hello\tWorld\tHello"), ["Hello", "World", "Hello"])

    def test_edge_case_newline_and_tab(self):
        self.assertEqual(split_list("Hello\n\tWorld"), ["Hello", "World"])

    def test_edge_case_multiple_newlines_and_tabs(self):
        self.assertEqual(split_list("Hello\n\tWorld\n\tHello"), ["Hello", "World", "Hello"])

    def test_edge_case_non_ascii_chars(self):
        self.assertEqual(split_list("HelloWorld"), ["Hello", "World"])

    def test_edge_case_non_ascii_chars_with_spaces(self):
        self.assertEqual(split_list("Hello   World"), ["Hello", "World"])

    def test_edge_case_non_ascii_chars_with_newlines(self):
        self.assertEqual(split_list("Hello\nWorld"), ["Hello", "World"])

    def test_edge_case_non_ascii_chars_with_tabs(self):
        self.assertEqual(split_list("Hello\tWorld"), ["Hello", "World"])
