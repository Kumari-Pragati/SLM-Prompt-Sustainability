import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(find_long_word("Hello world this is a test"), ['world', 'test'])

    def test_edge_case_empty_string(self):
        self.assertEqual(find_long_word(""), [])

    def test_edge_case_single_word(self):
        self.assertEqual(find_long_word("Hello"), [])

    def test_edge_case_multiple_words(self):
        self.assertEqual(find_long_word("Hello world this is a test"), ['world', 'test'])

    def test_edge_case_long_word(self):
        self.assertEqual(find_long_word("Hello world this is a very long word"), ['world', 'test','very', 'long', 'word'])

    def test_edge_case_non_word_characters(self):
        self.assertEqual(find_long_word("Hello! world this is a test"), ['world', 'test'])

    def test_edge_case_punctuation(self):
        self.assertEqual(find_long_word("Hello, world! this is a test."), ['world', 'test'])

    def test_edge_case_numbers(self):
        self.assertEqual(find_long_word("Hello 123 world this is a test"), ['world', 'test'])

    def test_edge_case_special_characters(self):
        self.assertEqual(find_long_word("Hello@ world this is a test"), ['world', 'test'])
