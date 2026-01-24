import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):
    def test_single_word_even_length(self):
        self.assertTrue(word_len("hello"))

    def test_single_word_odd_length(self):
        self.assertFalse(word_len("helloo"))

    def test_multiple_words_even_length(self):
        self.assertTrue(word_len("hello world"))

    def test_multiple_words_odd_length(self):
        self.assertFalse(word_len("hello worldo"))

    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_single_space(self):
        self.assertFalse(word_len(" "))

    def test_multiple_spaces(self):
        self.assertFalse(word_len("   "))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            word_len(123)
