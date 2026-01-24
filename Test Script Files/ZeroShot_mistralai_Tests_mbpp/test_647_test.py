import unittest
from mbpp_647_code import findall

def split_upperstring(text):
    return findall('[A-Z][^A-Z]*', text)

class TestSplitUpperstring(unittest.TestCase):

    def test_empty_string(self):
        self.assertListEqual(split_upperstring(''), [])

    def test_single_uppercase_letter(self):
        self.assertListEqual(split_upperstring('A'), ['A'])

    def test_single_word(self):
        self.assertListEqual(split_upperstring('Hello'), ['Hello'])

    def test_multiple_words(self):
        self.assertListEqual(split_upperstring('Hello World'), ['Hello', 'World'])

    def test_mixed_case(self):
        self.assertListEqual(split_upperstring('HeLlO wOrLd'), ['HeLlO', 'wOrLd'])

    def test_multiple_spaces(self):
        self.assertListEqual(split_upperstring(' HeLlO   wOrLd  '), ['HeLlO', 'wOrLd'])

    def test_punctuation(self):
        self.assertListEqual(split_upperstring('HeLlO, wOrLd!'), ['HeLlO', 'wOrLd'])

    def test_numbers(self):
        self.assertListEqual(split_upperstring('HeLlO123 World'), ['HeLlO', 'World'])
