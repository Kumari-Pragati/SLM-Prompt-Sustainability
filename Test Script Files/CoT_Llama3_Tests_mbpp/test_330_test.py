import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(find_char("Hello world, this is a test string"), ["world", "test"])

    def test_edge_case_empty_string(self):
        self.assertEqual(find_char(""), [])

    def test_edge_case_single_word(self):
        self.assertEqual(find_char("Hello"), [])

    def test_edge_case_multiple_words(self):
        self.assertEqual(find_char("Hello world, this is another test string"), ["world", "test"])

    def test_edge_case_non_alphanumeric_chars(self):
        self.assertEqual(find_char("Hello! world, this is a test string"), ["world", "test"])

    def test_edge_case_punctuation(self):
        self.assertEqual(find_char("Hello, world! this is a test string"), ["world", "test"])

    def test_edge_case_numbers(self):
        self.assertEqual(find_char("Hello 123, world! this is a test string"), ["world", "test"])

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(find_char("Hello   world, this is a test string"), ["world", "test"])

    def test_edge_case_newline(self):
        self.assertEqual(find_char("Hello\nworld, this is a test string"), ["world", "test"])

    def test_edge_case_tabs(self):
        self.assertEqual(find_char("Hello\tworld, this is a test string"), ["world", "test"])

    def test_edge_case_multiple_newlines(self):
        self.assertEqual(find_char("Hello\nworld\nthis is a test string"), ["world", "test"])

    def test_edge_case_tabs_and_newlines(self):
        self.assertEqual(find_char("Hello\tworld\nthis is a test string"), ["world", "test"])
