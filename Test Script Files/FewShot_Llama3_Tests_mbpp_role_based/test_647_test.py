import unittest
from mbpp_647_code import split_upperstring

class TestSplitUpperstring(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(split_upperstring(""), [])

    def test_single_word(self):
        self.assertEqual(split_upperstring("HELLO"), ["HELLO"])

    def test_multiple_words(self):
        self.assertEqual(split_upperstring("HELLO WORLD"), ["HELLO", "WORLD"])

    def test_punctuation(self):
        self.assertEqual(split_upperstring("HELLO, WORLD!"), ["HELLO", "WORLD"])

    def test_numbers(self):
        self.assertEqual(split_upperstring("HELLO123 WORLD"), ["HELLO", "WORLD"])

    def test_non_ascii_characters(self):
        self.assertEqual(split_upperstring("HELLO ABCD"), ["HELLO", "ABCD"])

    def test_mixed_case(self):
        self.assertEqual(split_upperstring("HeLlO wOrLd"), ["HeLlO", "wOrLd"])

    def test_spaces(self):
        self.assertEqual(split_upperstring("   HELLO   WORLD   "), ["HELLO", "WORLD"])
