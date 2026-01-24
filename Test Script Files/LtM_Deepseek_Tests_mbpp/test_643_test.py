import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(text_match_wordz_middle('hello z world'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_wordz_middle('hello world'), 'Not matched!')

    def test_edge_case_empty_string(self):
        self.assertEqual(text_match_wordz_middle(''), 'Not matched!')

    def test_edge_case_single_character(self):
        self.assertEqual(text_match_wordz_middle('a'), 'Not matched!')

    def test_edge_case_two_characters_no_z(self):
        self.assertEqual(text_match_wordz_middle('ab'), 'Not matched!')

    def test_edge_case_two_characters_with_z(self):
        self.assertEqual(text_match_wordz_middle('az'), 'Found a match!')

    def test_complex_case_multiple_words_with_z(self):
        self.assertEqual(text_match_wordz_middle('the quick brown fox jumps over the lazy dog z'), 'Found a match!')

    def test_complex_case_multiple_words_no_z(self):
        self.assertEqual(text_match_wordz_middle('the quick brown fox jumps over the lazy dog'), 'Not matched!')
