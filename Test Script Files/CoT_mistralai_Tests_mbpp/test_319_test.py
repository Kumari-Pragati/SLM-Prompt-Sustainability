import unittest
from mbpp_319_code import find_long_word

class TestFindLongWord(unittest.TestCase):
    def test_empty_string(self):
        self.assertListEqual(find_long_word(''), [])

    def test_single_word(self):
        self.assertListEqual(find_long_word('one'), ['one'])
        self.assertListEqual(find_long_word('Two'), ['Two'])

    def test_multiple_words(self):
        self.assertListEqual(find_long_word('This is a test'), ['test'])
        self.assertListEqual(find_long_word('The quick brown fox jumps over the lazy dog'), ['brown', 'fox', 'lazy'])

    def test_longer_words(self):
        self.assertListEqual(find_long_word('Supercalifragilisticexpialidocious'), ['Supercalifragilisticexpialidocious'])

    def test_short_words(self):
        self.assertListEqual(find_long_word('one two three'), [])
        self.assertListEqual(find_long_word('a b c d e'), [])

    def test_punctuation(self):
        self.assertListEqual(find_long_word('This, is, a, test.'), ['test'])
        self.assertListEqual(find_long_word("It's a test!"), ['test'])

    def test_numbers(self):
        self.assertListEqual(find_long_word('12345'), [])
        self.assertListEqual(find_long_word('one two three four five'), ['five'])

    def test_special_characters(self):
        self.assertListEqual(find_long_word('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), [])
        self.assertListEqual(find_long_word('This_is_a_test'), ['test'])
