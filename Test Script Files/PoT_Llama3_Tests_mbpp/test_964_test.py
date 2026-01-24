import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):
    def test_typical_case(self):
        self.assertTrue(word_len("hello world"))

    def test_even_length_word(self):
        self.assertTrue(word_len("hello"))

    def test_odd_length_word(self):
        self.assertFalse(word_len("helloa"))

    def test_multiple_words(self):
        self.assertTrue(word_len("hello world hello"))

    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_single_space(self):
        self.assertFalse(word_len(" "))

    def test_no_words(self):
        self.assertFalse(word_len("   "))
