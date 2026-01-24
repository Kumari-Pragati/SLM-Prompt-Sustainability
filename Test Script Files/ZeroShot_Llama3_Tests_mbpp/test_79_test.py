import unittest
from mbpp_79_code import word_len

class TestWordLen(unittest.TestCase):

    def test_word_len(self):
        self.assertTrue(word_len("Hello World"))
        self.assertFalse(word_len("Hello"))
        self.assertTrue(word_len("Hello World Hello"))
        self.assertFalse(word_len("Hello World Hello World"))
        self.assertTrue(word_len("Hello World Hello World Hello"))
        self.assertFalse(word_len("Hello World Hello World Hello World"))

    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_single_word(self):
        self.assertFalse(word_len("Hello"))

    def test_multiple_words(self):
        self.assertTrue(word_len("Hello World Hello"))

    def test_multiple_words_with_even_length(self):
        self.assertFalse(word_len("Hello World Hello World"))

    def test_multiple_words_with_mixed_length(self):
        self.assertTrue(word_len("Hello World Hello World Hello"))
