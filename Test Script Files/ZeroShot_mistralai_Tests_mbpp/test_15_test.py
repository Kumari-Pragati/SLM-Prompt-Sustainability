import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerstring(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(split_lowerstring(''), [])

    def test_single_word(self):
        self.assertListEqual(split_lowerstring('hello'), ['hello', ])

    def test_multiple_words(self):
        self.assertListEqual(split_lowerstring('Hello World'), ['Hello', 'World'])

    def test_mixed_case(self):
        self.assertListEqual(split_lowerstring('HeLlO wOrLd'), ['hello', 'world'])

    def test_punctuation(self):
        self.assertListEqual(split_lowerstring('Hello, World!'), ['hello', 'world'])

    def test_numbers(self):
        self.assertListEqual(split_lowerstring('Hello123 World'), ['hello', 'world'])

    def test_special_characters(self):
        self.assertListEqual(split_lowerstring('Hello@World#'), ['hello', 'world'])

    def test_multiple_spaces(self):
        self.assertListEqual(split_lowerstring(' Hello   World  '), ['hello', 'world'])

    def test_multiple_non_words(self):
        self.assertListEqual(split_lowerstring('123Hello World456'), ['hello', 'world'])
