import unittest
from mbpp_482_code import match

class TestMatchFunction(unittest.TestCase):

    def test_match_uppercase_and_lowercase_words(self):
        self.assertEqual(match('UppercaseAndLowercase'), 'Yes')
        self.assertEqual(match('lowercaseanduppercase'), 'Yes')

    def test_match_single_uppercase_word(self):
        self.assertEqual(match('Uppercase'), 'Yes')

    def test_match_single_lowercase_word(self):
        self.assertEqual(match('lowercase'), 'No')

    def test_match_empty_string(self):
        self.assertEqual(match(''), 'No')

    def test_match_only_numbers(self):
        self.assertEqual(match('123456'), 'No')

    def test_match_special_characters(self):
        self.assertEqual(match('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), 'No')

    def test_match_mixed_case_with_punctuation(self):
        self.assertEqual(match('Uppercase,AndLowercase.'), 'No')

    def test_match_all_uppercase_with_punctuation(self):
        self.assertEqual(match('UPPERCASE,ANDLOWERCASE.'), 'No')

    def test_match_all_lowercase_with_punctuation(self):
        self.assertEqual(match('lowercase,andlowercase.'), 'No')
