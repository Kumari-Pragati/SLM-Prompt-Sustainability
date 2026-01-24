import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerstring(unittest.TestCase):
    def test_empty_input(self):
        self.assertEqual(split_lowerstring(""), [])

    def test_single_word(self):
        self.assertEqual(split_lowerstring("hello"), ['hello'])

    def test_multiple_words(self):
        self.assertEqual(split_lowerstring("hello world"), ['hello', 'world'])

    def test_punctuation(self):
        self.assertEqual(split_lowerstring("hello, world!"), ['hello', 'world'])

    def test_numbers(self):
        self.assertEqual(split_lowerstring("hello123 world"), ['hello', 'world'])

    def test_uppercase(self):
        self.assertEqual(split_lowerstring("HELLO world"), ['world'])

    def test_mixed_case(self):
        self.assertEqual(split_lowerstring("HeLlO world"), ['world'])

    def test_non_alphabetic_characters(self):
        self.assertEqual(split_lowerstring("hello! world"), ['hello', 'world'])

    def test_long_string(self):
        self.assertEqual(split_lowerstring("hello world this is a test"), ['hello', 'world', 'this', 'is', 'a', 'test'])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            split_lowerstring(123)
