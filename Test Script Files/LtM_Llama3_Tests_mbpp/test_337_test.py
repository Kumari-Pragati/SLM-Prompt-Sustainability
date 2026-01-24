import unittest
from mbpp_337_code import text_match_word

class TestTextMatchWord(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match_word("Hello World!"), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_word("Hello"), 'Not matched!')

    def test_empty_input(self):
        self.assertEqual(text_match_word(""), 'Not matched!')

    def test_single_word(self):
        self.assertEqual(text_match_word("Hello"), 'Not matched!')

    def test_multiple_words(self):
        self.assertEqual(text_match_word("Hello World! Foo Bar"), 'Found a match!')

    def test_punctuation(self):
        self.assertEqual(text_match_word("Hello, World!"), 'Found a match!')

    def test_numbers(self):
        self.assertEqual(text_match_word("Hello 123!"), 'Found a match!')

    def test_special_chars(self):
        self.assertEqual(text_match_word("Hello @# World!"), 'Found a match!')
