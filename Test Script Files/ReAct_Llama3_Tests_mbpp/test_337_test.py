import unittest
from mbpp_337_code import text_match_word

class TestTextMatchWord(unittest.TestCase):

    def test_match_word(self):
        self.assertEqual(text_match_word("Hello World!"), 'Found a match!')

    def test_no_match_word(self):
        self.assertEqual(text_match_word("Hello"), 'Not matched!')

    def test_match_word_at_end(self):
        self.assertEqual(text_match_word("Hello World! World"), 'Found a match!')

    def test_no_match_word_at_end(self):
        self.assertEqual(text_match_word("Hello World!"), 'Found a match!')

    def test_match_word_with_punctuation(self):
        self.assertEqual(text_match_word("Hello World!."), 'Found a match!')

    def test_no_match_word_with_punctuation(self):
        self.assertEqual(text_match_word("Hello World"), 'Not matched!')

    def test_match_word_with_numbers(self):
        self.assertEqual(text_match_word("Hello 123 World!"), 'Found a match!')

    def test_no_match_word_with_numbers(self):
        self.assertEqual(text_match_word("Hello 123"), 'Not matched!')
