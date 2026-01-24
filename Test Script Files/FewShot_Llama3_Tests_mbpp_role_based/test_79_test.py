import unittest
from mbpp_79_code import word_len

class TestWordLen(unittest.TestCase):
    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_single_word(self):
        self.assertFalse(word_len("hello"))

    def test_multiple_words(self):
        self.assertTrue(word_len("hello world"))

    def test_empty_string_with_spaces(self):
        self.assertFalse(word_len("   "))

    def test_single_word_with_spaces(self):
        self.assertFalse(word_len("   hello   "))

    def test_multiple_words_with_spaces(self):
        self.assertTrue(word_len("   hello   world   "))

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            word_len(123)
