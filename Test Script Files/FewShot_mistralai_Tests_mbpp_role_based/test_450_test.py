import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(extract_string("abcdefg", 3), ["abc", "def", "gh"])

    def test_empty_string(self):
        self.assertEqual(extract_string("", 3), [])

    def test_string_shorter_than_length(self):
        self.assertEqual(extract_string("ab", 3), [])

    def test_string_longer_than_length(self):
        self.assertEqual(extract_string("abcdefg", 5), [])

    def test_string_with_only_one_word(self):
        self.assertEqual(extract_string("word", 1), ["w"])

    def test_string_with_only_one_word_and_length_zero(self):
        self.assertEqual(extract_string("word", 0), [])
