import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):

    def test_word_len_even_length(self):
        self.assertTrue(word_len("hello world"))

    def test_word_len_odd_length(self):
        self.assertFalse(word_len("hello"))

    def test_word_len_multiple_words(self):
        self.assertTrue(word_len("hello world this is a test"))

    def test_word_len_empty_string(self):
        self.assertFalse(word_len(""))

    def test_word_len_single_word_even_length(self):
        self.assertTrue(word_len("evenlength"))

    def test_word_len_single_word_odd_length(self):
        self.assertFalse(word_len("oddlength"))
