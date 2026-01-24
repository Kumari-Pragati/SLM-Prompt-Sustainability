import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match_wordz("Hello worldz"), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_wordz("Hello world"), 'Not matched!')

    def test_empty_input(self):
        self.assertEqual(text_match_wordz(""), 'Not matched!')

    def test_pattern_with_spaces(self):
        self.assertEqual(text_match_wordz("Hello world z"), 'Found a match!')

    def test_pattern_with_punctuation(self):
        self.assertEqual(text_match_wordz("Hello world! z"), 'Found a match!')

    def test_pattern_with_numbers(self):
        self.assertEqual(text_match_wordz("Hello world123 z"), 'Found a match!')

    def test_pattern_with_special_chars(self):
        self.assertEqual(text_match_wordz("Hello world@ z"), 'Found a match!')
