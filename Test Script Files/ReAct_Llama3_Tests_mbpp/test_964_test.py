import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(word_len("Hello World"))

    def test_even_length_word(self):
        self.assertTrue(word_len("abcdef"))

    def test_odd_length_word(self):
        self.assertFalse(word_len("abcde"))

    def test_multiple_words(self):
        self.assertTrue(word_len("Hello World abc def"))

    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_single_word(self):
        self.assertFalse(word_len("abc"))

    def test_no_words(self):
        self.assertFalse(word_len("   "))
