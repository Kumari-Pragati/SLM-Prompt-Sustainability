import unittest
from mbpp_79_code import word_len

class TestWordLen(unittest.TestCase):

    def test_odd_length_words(self):
        self.assertTrue(word_len("odd length words"))

    def test_even_length_words(self):
        self.assertFalse(word_len("even length words"))

    def test_single_word_odd_length(self):
        self.assertTrue(word_len("odd"))

    def test_single_word_even_length(self):
        self.assertFalse(word_len("even"))

    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_string_with_multiple_spaces(self):
        self.assertTrue(word_len("multiple   spaces"))

    def test_string_with_leading_trailing_spaces(self):
        self.assertTrue(word_len("  leading trailing spaces  "))

    def test_string_with_special_characters(self):
        self.assertTrue(word_len("special!@#characters"))

    def test_string_with_numbers(self):
        self.assertTrue(word_len("1234567890"))
