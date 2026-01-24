import unittest
from mbpp_964_code import word_len

class TestWordLen(unittest.TestCase):

    def test_even_word_length(self):
        self.assertTrue(word_len('hello world'))

    def test_odd_word_length(self):
        self.assertFalse(word_len('python'))

    def test_single_word_even_length(self):
        self.assertTrue(word_len('even'))

    def test_single_word_odd_length(self):
        self.assertFalse(word_len('odd'))

    def test_empty_string(self):
        self.assertFalse(word_len(''))

    def test_string_with_multiple_spaces(self):
        self.assertTrue(word_len('this   is a test'))

    def test_string_with_leading_trailing_spaces(self):
        self.assertTrue(word_len('  leading trailing  '))

    def test_string_with_special_characters(self):
        self.assertTrue(word_len('special#characters'))

    def test_string_with_numbers(self):
        self.assertFalse(word_len('123456'))
