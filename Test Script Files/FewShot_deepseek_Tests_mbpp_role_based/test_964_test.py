import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):
    def test_even_length_word(self):
        self.assertTrue(word_len("hello world"))

    def test_odd_length_word(self):
        self.assertFalse(word_len("hello world"))

    def test_single_word_even_length(self):
        self.assertTrue(word_len("python"))

    def test_single_word_odd_length(self):
        self.assertFalse(word_len("java"))

    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_whitespace_only(self):
        self.assertFalse(word_len(" "))

    def test_special_characters(self):
        self.assertFalse(word_len("!@#$%^&*"))

    def test_numbers_only(self):
        self.assertFalse(word_len("123456"))
