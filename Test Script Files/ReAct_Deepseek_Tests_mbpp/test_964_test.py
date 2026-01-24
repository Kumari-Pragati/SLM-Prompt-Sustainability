import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):

    def test_even_length_word(self):
        self.assertTrue(word_len("hello"))

    def test_odd_length_word(self):
        self.assertFalse(word_len("world"))

    def test_multiple_words_even_length(self):
        self.assertTrue(word_len("hello world"))

    def test_multiple_words_odd_length(self):
        self.assertFalse(word_len("hello there"))

    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_string_with_special_characters(self):
        self.assertTrue(word_len("hello@world"))

    def test_string_with_numbers(self):
        self.assertFalse(word_len("123456"))

    def test_string_with_mixed_case(self):
        self.assertTrue(word_len("Hello"))

    def test_string_with_leading_trailing_spaces(self):
        self.assertFalse(word_len("   hello   "))
