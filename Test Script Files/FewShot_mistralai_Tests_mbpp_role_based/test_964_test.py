import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):
    def test_even_length_word(self):
        self.assertTrue(word_len("a b c d"))

    def test_odd_length_word(self):
        self.assertFalse(word_len("a b c d e"))

    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_single_word(self):
        self.assertFalse(word_len("word"))

    def test_single_letter(self):
        self.assertFalse(word_len("a"))

    def test_single_digit(self):
        self.assertFalse(word_len("1"))
