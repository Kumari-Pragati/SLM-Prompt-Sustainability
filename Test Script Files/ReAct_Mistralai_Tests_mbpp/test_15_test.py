import unittest
from mbpp_15_code import split_lowerstring

class TestSplitLowerstring(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(split_lowerstring(''), [])

    def test_single_lowercase_letter(self):
        self.assertEqual(split_lowerstring('a'), ['a'])

    def test_multiple_lowercase_letters(self):
        self.assertEqual(split_lowerstring('abc'), ['abc'])

    def test_mixed_case_string(self):
        self.assertEqual(split_lowerstring('ABCabc123'), ['abc', '123'])

    def test_leading_and_trailing_whitespace(self):
        self.assertEqual(split_lowerstring('   abc   '), ['abc'])

    def test_multiple_words_with_punctuation(self):
        self.assertEqual(split_lowerstring("It's a beautiful day, isn't it?"), ['its', 'a', 'beautiful', 'day', 'isnt', 'it'])

    def test_empty_word_in_middle(self):
        self.assertEqual(split_lowerstring("word1 word2 word3 word4 word5"), ['word1', 'word3', 'word4', 'word5'])

    def test_single_digit(self):
        self.assertEqual(split_lowerstring('1'), [])

    def test_multiple_digits(self):
        self.assertEqual(split_lowerstring('12345'), [])

    def test_digits_with_letters(self):
        self.assertEqual(split_lowerstring('a1b2c3'), ['a', 'b', 'c'])

    def test_special_characters(self):
        self.assertEqual(split_lowerstring('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), [])

    def test_single_uppercase_letter(self):
        self.assertEqual(split_lowerstring('A'), [])

    def test_multiple_uppercase_letters(self):
        self.assertEqual(split_lowerstring('ABC'), [])
