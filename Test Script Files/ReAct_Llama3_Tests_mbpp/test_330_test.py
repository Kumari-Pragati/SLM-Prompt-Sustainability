import unittest
from mbpp_330_code import find_char

class TestFindChar(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_char("Hello World, this is a test string"), ["Hello", "World", "test"])

    def test_edge_case_empty_string(self):
        self.assertEqual(find_char(""), [])

    def test_edge_case_single_word(self):
        self.assertEqual(find_char("Hello"), ["Hello"])

    def test_edge_case_multiple_words(self):
        self.assertEqual(find_char("Hello World, this is another test string"), ["Hello", "World", "this", "is", "another", "test"])

    def test_edge_case_non_alphanumeric_chars(self):
        self.assertEqual(find_char("Hello! World, this is a test string"), ["Hello", "World", "this", "is", "a", "test"])

    def test_edge_case_punctuation(self):
        self.assertEqual(find_char("Hello... World, this is a test string"), ["Hello", "World", "this", "is", "a", "test"])

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(find_char("Hello   World, this   is   a   test   string"), ["Hello", "World", "this", "is", "a", "test"])

    def test_edge_case_newline(self):
        self.assertEqual(find_char("Hello\nWorld, this is a test string"), ["Hello", "World", "this", "is", "a", "test"])

    def test_edge_case_tab(self):
        self.assertEqual(find_char("Hello\tWorld, this is a test string"), ["Hello", "World", "this", "is", "a", "test"])

    def test_edge_case_multiple_newlines(self):
        self.assertEqual(find_char("Hello\nWorld,\nthis\nis\na\ntest\nstring"), ["Hello", "World", "this", "is", "a", "test"])

    def test_edge_case_multiple_tabs(self):
        self.assertEqual(find_char("Hello\tWorld,\tthis\tis\ta\ttest\tstring"), ["Hello", "World", "this", "is", "a", "test"])
