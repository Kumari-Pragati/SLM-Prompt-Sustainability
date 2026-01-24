import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerstring(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(split_lowerstring("Hello World"), ["Hello", "World"])

    def test_multiple_words(self):
        self.assertEqual(split_lowerstring("This is a test string"), ["This", "is", "a", "test", "string"])

    def test_empty_string(self):
        self.assertEqual(split_lowerstring(""), [])

    def test_single_word(self):
        self.assertEqual(split_lowerstring("Hello"), ["Hello"])

    def test_punctuation(self):
        self.assertEqual(split_lowerstring("Hello, World!"), ["Hello", "World"])

    def test_numbers(self):
        self.assertEqual(split_lowerstring("Hello123 World"), ["Hello123", "World"])

    def test_uppercase(self):
        self.assertEqual(split_lowerstring("HELLO WORLD"), ["HELLO", "WORLD"])
