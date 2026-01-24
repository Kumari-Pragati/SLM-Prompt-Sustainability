import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(extract_string("", 1), [])

    def test_single_word(self):
        self.assertListEqual(extract_string("word", 3), ["word"])

    def test_multiple_words(self):
        self.assertListEqual(extract_string("apple banana cherry", 4), ["apple", "banana"])

    def test_longer_words(self):
        self.assertListEqual(extract_string("antidisestablishmentarianism", 10), ["antidisestablishmentarianism"])

    def test_shorter_words(self):
        self.assertListEqual(extract_string("antidisestablishmentarianism", 5), [])

    def test_single_letter_words(self):
        self.assertListEqual(extract_string("abcdefg", 1), ["a", "b", "c", "d", "e", "f", "g"])

    def test_empty_list(self):
        self.assertListEqual(extract_string([], 1), [])

    def test_negative_length(self):
        self.assertRaises(ValueError, extract_string, "test", -1)

    def test_non_string_input(self):
        self.assertRaises(TypeError, extract_string, 123, 1)
