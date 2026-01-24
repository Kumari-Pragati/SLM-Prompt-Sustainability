import unittest
from mbpp_79_code import word_len

class TestWordLen(unittest.TestCase):

    def test_simple_words(self):
        self.assertTrue(word_len("abc"))
        self.assertFalse(word_len("abcd"))

    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_single_word_with_even_length(self):
        self.assertFalse(word_len("abcdef"))

    def test_multiple_words(self):
        self.assertTrue(word_len("abc def"))
        self.assertFalse(word_len("abc defg"))

    def test_special_characters(self):
        self.assertTrue(word_len("abc!@#"))
        self.assertFalse(word_len("abc!@#$"))
