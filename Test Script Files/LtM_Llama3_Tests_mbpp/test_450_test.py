import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(extract_string("", 3), [])

    def test_single_char_string(self):
        self.assertEqual(extract_string("a", 1), ["a"])

    def test_single_word_string(self):
        self.assertEqual(extract_string("hello", 5), ["hello"])

    def test_multiple_word_string(self):
        self.assertEqual(extract_string("hello world", 5), ["hello", "world"])

    def test_string_with_no_matches(self):
        self.assertEqual(extract_string("hello world", 7), [])

    def test_string_with_single_match(self):
        self.assertEqual(extract_string("hello world", 3), ["hel"])

    def test_string_with_multiple_matches(self):
        self.assertEqual(extract_string("hello world", 2), ["he", "lo", "or", "ld"])

    def test_string_with_no_matches_and_max_length(self):
        self.assertEqual(extract_string("hello world", 10), [])

    def test_string_with_single_match_and_max_length(self):
        self.assertEqual(extract_string("hello world", 10), ["hel"])

    def test_string_with_multiple_matches_and_max_length(self):
        self.assertEqual(extract_string("hello world", 10), ["he", "hel", "lo", "lor", "ld"])
