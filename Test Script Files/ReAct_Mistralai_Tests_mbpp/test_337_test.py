import unittest
from mbpp_337_code import text_match_word

class TestTextMatchWord(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(text_match_word(''), 'Not matched!')

    def test_single_word(self):
        self.assertEqual(text_match_word('word'), 'Found a match!')

    def test_multiple_words(self):
        self.assertEqual(text_match_word('multiple words'), 'Not matched!')

    def test_word_with_suffix(self):
        self.assertEqual(text_match_word('wordSuffix'), 'Found a match!')

    def test_word_with_prefix(self):
        self.assertEqual(text_match_word('prefixWord'), 'Found a match!')

    def test_word_with_prefix_and_suffix(self):
        self.assertEqual(text_match_word('prefixWordSuffix'), 'Found a match!')

    def test_word_with_leading_spaces(self):
        self.assertEqual(text_match_word(' word'), 'Found a match!')

    def test_word_with_trailing_spaces(self):
        self.assertEqual(text_match_word('word '), 'Found a match!')

    def test_word_with_leading_and_trailing_spaces(self):
        self.assertEqual(text_match_word(' word '), 'Found a match!')

    def test_non_word_string(self):
        self.assertEqual(text_match_word('12345'), 'Not matched!')

    def test_empty_pattern(self):
        with self.assertRaises(ValueError):
            text_match_word(text='word', patterns='')
