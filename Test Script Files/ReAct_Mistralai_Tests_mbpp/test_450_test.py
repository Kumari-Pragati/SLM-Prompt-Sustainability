import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(extract_string("", 1), [])

    def test_single_word(self):
        self.assertListEqual(extract_string("word", 3), ["word"])

    def test_multiple_words(self):
        self.assertListEqual(extract_string("apple banana cherry", 5), ["apple", "banana"])

    def test_single_word_with_spaces(self):
        self.assertListEqual(extract_string(" apple ", 3), ["apple"])

    def test_longer_word(self):
        self.assertListEqual(extract_string("bananarama", 4), ["banana", "arama"])

    def test_shorter_word(self):
        self.assertListEqual(extract_string("bananarama", 6), [])

    def test_punctuation(self):
        self.assertListEqual(extract_string("apple, banana! cherry.", 5), ["apple", "banana"])

    def test_error_negative_length(self):
        with self.assertRaises(ValueError):
            extract_string("apple", -1)

    def test_error_zero_length(self):
        with self.assertRaises(ValueError):
            extract_string("apple", 0)
