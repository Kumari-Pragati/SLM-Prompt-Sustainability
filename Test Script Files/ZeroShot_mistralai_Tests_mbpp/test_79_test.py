import unittest
from79_code import word_len

class TestWordLen(unittest.TestCase):

    def test_empty_string(self):
        self.assertFalse(word_len(''))

    def test_single_word(self):
        self.assertTrue(word_len('odd word'))
        self.assertFalse(word_len('even word'))

    def test_multiple_words(self):
        self.assertTrue(word_len('odd word1 odd word2'))
        self.assertFalse(word_len('even word1 even word2'))

    def test_mixed_words(self):
        self.assertTrue(word_len('even word odd word'))
        self.assertFalse(word_len('odd word even word'))
