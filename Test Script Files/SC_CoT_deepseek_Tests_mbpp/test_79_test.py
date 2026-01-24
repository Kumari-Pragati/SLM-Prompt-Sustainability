import unittest
from mbpp_79_code import word_len

class TestWordLen(unittest.TestCase):

    def test_typical_case(self):
        self.assertTrue(word_len("hello world"))

    def test_odd_length_word(self):
        self.assertTrue(word_len("odd length"))

    def test_even_length_word(self):
        self.assertFalse(word_len("even length"))

    def test_single_word(self):
        self.assertFalse(word_len("word"))

    def test_empty_string(self):
        self.assertFalse(word_len(""))

    def test_special_characters(self):
        self.assertTrue(word_len("!@#$%^&*"))

    def test_numbers(self):
        self.assertTrue(word_len("1234567890"))

    def test_whitespace_only(self):
        self.assertFalse(word_len(" "))

    def test_special_case_with_multiple_words(self):
        self.assertTrue(word_len("odd length word"))
