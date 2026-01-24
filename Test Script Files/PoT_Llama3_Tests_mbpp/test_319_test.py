import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_long_word("Hello world this is a test"), ['world', 'test'])

    def test_edge_case_empty_string(self):
        self.assertEqual(find_long_word(""), [])

    def test_edge_case_single_word(self):
        self.assertEqual(find_long_word("Hello"), [])

    def test_edge_case_multiple_words(self):
        self.assertEqual(find_long_word("Hello world this is a test again"), ['world', 'test', 'again'])

    def test_edge_case_no_words(self):
        self.assertEqual(find_long_word("   "), [])

    def test_edge_case_single_word_with_spaces(self):
        self.assertEqual(find_long_word("   Hello   "), [])

    def test_edge_case_multiple_words_with_spaces(self):
        self.assertEqual(find_long_word("   Hello world this is a test again   "), ['world', 'test', 'again'])

    def test_edge_case_punctuation(self):
        self.assertEqual(find_long_word("Hello, world! This is a test."), ['world', 'test'])

    def test_edge_case_punctuation_and_spaces(self):
        self.assertEqual(find_long_word("   Hello, world! This is a test.   "), ['world', 'test'])
