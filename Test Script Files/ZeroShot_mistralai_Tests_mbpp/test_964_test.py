import unittest
from964_code import word_len

class TestWordLen(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(word_len(''))

    def test_single_word(self):
        self.assertFalse(word_len('word'))
        self.assertTrue(word_len('evenWord'))

    def test_multiple_words(self):
        self.assertFalse(word_len('word1 word2'))
        self.assertTrue(word_len('evenWord1 oddWord2'))

    def test_mixed_case(self):
        self.assertFalse(word_len('Word1 Word2'))
        self.assertTrue(word_len('evenWord1 oddWord2'))

    def test_punctuation(self):
        self.assertFalse(word_len('word,word'))
        self.assertTrue(word_len('evenWord,oddWord'))

    def test_numbers(self):
        self.assertFalse(word_len('word123word'))
        self.assertTrue(word_len('evenWord123oddWord'))
