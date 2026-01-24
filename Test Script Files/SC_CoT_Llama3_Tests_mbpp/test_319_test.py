import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(find_long_word("Hello world this is a test"), ["world", "this"])

    def test_edge_case_empty_string(self):
        self.assertEqual(find_long_word(""), [])

    def test_edge_case_single_word(self):
        self.assertEqual(find_long_word("Hello"), [])

    def test_edge_case_multiple_words(self):
        self.assertEqual(find_long_word("Hello world this is a test"), ["world", "this"])

    def test_edge_case_long_word(self):
        self.assertEqual(find_long_word("Hello world this is a very long word"), ["world", "this", "very", "long", "word"])

    def test_edge_case_non_word_characters(self):
        self.assertEqual(find_long_word("Hello! world this is a test"), ["world", "this"])

    def test_edge_case_non_ascii_characters(self):
        self.assertEqual(find_long_word("Hello world this is a test with non-ascii characters"), ["world", "this"])

    def test_edge_case_mixed_case(self):
        self.assertEqual(find_long_word("Hello WORLD this is a test"), ["WORLD", "this"])

    def test_edge_case_punctuation(self):
        self.assertEqual(find_long_word("Hello, world! this is a test."), ["world", "this"])

    def test_edge_case_numbers(self):
        self.assertEqual(find_long_word("Hello 123 world this is a test"), ["world", "this"])

    def test_edge_case_special_characters(self):
        self.assertEqual(find_long_word("Hello!@# world this is a test"), ["world", "this"])

    def test_edge_case_multiple_spaces(self):
        self.assertEqual(find_long_word("Hello  world  this  is  a  test"), ["world", "this"])

    def test_edge_case_tab_characters(self):
        self.assertEqual(find_long_word("Hello\tworld this is a test"), ["world", "this"])

    def test_edge_case_newline_characters(self):
        self.assertEqual(find_long_word("Hello\nworld this is a test"), ["world", "this"])

    def test_edge_case_carriage_return_characters(self):
        self.assertEqual(find_long_word("Hello\rworld this is a test"), ["world", "this"])

    def test_edge_case_multiple_newline_characters(self):
        self.assertEqual(find_long_word("Hello\nworld\nthis is a test"), ["world", "this"])
