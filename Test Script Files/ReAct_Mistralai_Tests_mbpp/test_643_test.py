import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(text_match_wordz_middle(''), 'Not matched!')

    def test_single_word(self):
        self.assertEqual(text_match_wordz_middle('z'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('Z'), 'Not matched!')

    def test_multiple_words(self):
        self.assertEqual(text_match_wordz_middle('az'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('zxz'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('Zyz'), 'Not matched!')

    def test_word_at_beginning(self):
        self.assertEqual(text_match_wordz_middle('zabc'), 'Not matched!')

    def test_word_at_end(self):
        self.assertEqual(text_match_wordz_middle('az'), 'Not matched!')

    def test_word_in_middle(self):
        self.assertEqual(text_match_wordz_middle('zxzy'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('ZxZy'), 'Not matched!')

    def test_multiple_matches(self):
        self.assertEqual(text_match_wordz_middle('zxzxz'), 'Found a match!')

    def test_non_word_characters(self):
        self.assertEqual(text_match_wordz_middle('z1z'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z_z'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z-z'), 'Not matched!')
