import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):

    def test_even_length_words(self):
        self.assertTrue(word_len('test word'))
        self.assertTrue(word_len('even length words'))

    def test_odd_length_words(self):
        self.assertFalse(word_len('odd'))
        self.assertFalse(word_len('length'))

    def test_empty_string(self):
        self.assertFalse(word_len(''))

    def test_single_word(self):
        self.assertFalse(word_len('single'))

    def test_special_characters(self):
        self.assertFalse(word_len('special!@#characters'))
