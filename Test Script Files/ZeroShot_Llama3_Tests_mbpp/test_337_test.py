import unittest
from mbpp_337_code import text_match_word

class TestTextMatchWord(unittest.TestCase):

    def test_match(self):
        self.assertEqual(text_match_word("Hello World!"), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_word("Hello"), 'Not matched!')

    def test_match_with_punctuation(self):
        self.assertEqual(text_match_word("Hello, World!"), 'Found a match!')

    def test_no_match_with_punctuation(self):
        self.assertEqual(text_match_word("Hello, World"), 'Not matched!')

    def test_match_with_numbers(self):
        self.assertEqual(text_match_word("Hello 123 World!"), 'Found a match!')

    def test_no_match_with_numbers(self):
        self.assertEqual(text_match_word("Hello 123"), 'Not matched!')
