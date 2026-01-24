import unittest
from mbpp_537_code import first_repeated_word

class TestFirstRepeatedWord(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(first_repeated_word(''), 'None')

    def test_single_word(self):
        self.assertEqual(first_repeated_word('word'), 'word')

    def test_multiple_words_no_repeats(self):
        self.assertEqual(first_repeated_word('apple banana cherry'), 'None')

    def test_multiple_words_with_repeats(self):
        self.assertEqual(first_repeated_word('apple apple banana cherry'), 'apple')

    def test_case_sensitivity(self):
        self.assertEqual(first_repeated_word('Apple Apple Banana Cherry'), 'Apple')

    def test_whitespace_handling(self):
        self.assertEqual(first_repeated_word(' apple Apple Banana cherry '), 'Apple')

    def test_punctuation_handling(self):
        self.assertEqual(first_repeated_word("apple, Apple! Banana@ cherry#"), 'Apple')

    def test_special_characters(self):
        self.assertEqual(first_repeated_word("apple_ Apple- Banana^ cherry~"), 'Apple')
