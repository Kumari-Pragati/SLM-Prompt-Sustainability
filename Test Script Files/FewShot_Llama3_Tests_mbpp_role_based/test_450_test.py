import unittest
from mbpp_450_code import extract_string

class TestExtractString(unittest.TestCase):
    def test_extract_single_character(self):
        self.assertEqual(extract_string("hello", 2), ["he", "ll", "lo"])

    def test_extract_multiple_characters(self):
        self.assertEqual(extract_string("hello", 3), ["hel", "llo"])

    def test_extract_single_character_from_empty_string(self):
        self.assertEqual(extract_string("", 2), [])

    def test_extract_non_existent_characters(self):
        self.assertEqual(extract_string("hello", 5), [])

    def test_extract_characters_from_string_with_spaces(self):
        self.assertEqual(extract_string("hello world", 2), ["he", "ll", "wo", "rl", "ld"])

    def test_extract_characters_from_string_with_punctuation(self):
        self.assertEqual(extract_string("hello, world!", 2), ["he", "ll", "wo", "rl", "ld", "o", ","])
