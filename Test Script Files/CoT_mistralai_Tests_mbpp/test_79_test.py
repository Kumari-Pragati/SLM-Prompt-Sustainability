import unittest
from79_code import word_len

class TestWordLen(unittest.TestCase):
    def test_even_length_words(self):
        self.assertFalse(word_len("this is a test"))

    def test_odd_length_word(self):
        self.assertTrue(word_len("unevenWord"))

    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_single_word(self):
        self.assertFalse(word_len("word"))

    def test_single_character(self):
        self.assertFalse(word_len("a"))

    def test_whitespace_only(self):
        self.assertFalse(word_len("   "))

    def test_mixed_even_odd_length_words(self):
        self.assertFalse(word_len("oddEvenWord"))

    def test_invalid_input(self):
        self.assertRaises(TypeError, word_len, 123)
        self.assertRaises(TypeError, word_len, [1, 2, 3])
        self.assertRaises(TypeError, word_len, (1, 2, 3))
        self.assertRaises(TypeError, word_len, {"key": "value"})
