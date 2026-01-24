import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerstring(unittest.TestCase):
    def test_empty_string(self):
        self.assertListEqual(split_lowerstring(''), [])

    def test_single_word(self):
        self.assertListEqual(split_lowerstring('hello'), ['hello'])

    def test_multiple_words(self):
        self.assertListEqual(split_lowerstring('hello world'), ['hello', 'world'])

    def test_mixed_case(self):
        self.assertListEqual(split_lowerstring('Hello World'), ['hello', 'world'])

    def test_punctuation(self):
        self.assertListEqual(split_lowerstring('hello, world!'), ['hello', 'world'])

    def test_numbers(self):
        self.assertListEqual(split_lowerstring('hello123world'), ['hello', 'world'])

    def test_multiple_punctuation(self):
        self.assertListEqual(split_lowerstring('hello,world!'), ['hello', 'world'])

    def test_multiple_spaces(self):
        self.assertListEqual(split_lowerstring('hello   world'), ['hello', 'world'])

    def test_leading_trailing_spaces(self):
        self.assertListEqual(split_lowerstring(' hello world '), ['hello', 'world'])

    def test_leading_trailing_punctuation(self):
        self.assertListEqual(split_lowerstring('.,hello world.!'), ['hello', 'world'])

    def test_empty_words(self):
        self.assertListEqual(split_lowerstring(' ,  ,  '), [])

    def test_non_alphabetic_characters(self):
        self.assertListEqual(split_lowerstring('$%^&*()_+-=@!#hello world$%^&*()_+-='), ['hello', 'world'])
