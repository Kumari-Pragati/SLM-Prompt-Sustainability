import unittest
from mbpp_337_code import text_match_word

class TestTextMatchWord(unittest.TestCase):
    def test_match_single_word(self):
        self.assertEqual(text_match_word("Hello World"), "Found a match!")

    def test_match_multiple_words(self):
        self.assertEqual(text_match_word("Hello World Goodbye"), "Found a match!")

    def test_match_word_at_end(self):
        self.assertEqual(text_match_word("World"), "Found a match!")

    def test_match_empty_string(self):
        self.assertEqual(text_match_word(""), "Not matched!")

    def test_match_no_word(self):
        self.assertEqual(text_match_word("12345"), "Not matched!")

    def test_match_word_with_punctuation(self):
        self.assertEqual(text_match_word("Hello, World!"), "Not matched!")
