import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):
    def test_found_match(self):
        self.assertEqual(text_match_wordz("Hello, world!"), 'Found a match!')

    def test_not_found_match(self):
        self.assertEqual(text_match_wordz("Hello"), 'Not matched!')

    def test_found_match_with_punctuation(self):
        self.assertEqual(text_match_wordz("Hello, world!"), 'Found a match!')

    def test_found_match_with_numbers(self):
        self.assertEqual(text_match_wordz("Hello, 123!"), 'Found a match!')

    def test_found_match_with_punctuation_and_numbers(self):
        self.assertEqual(text_match_wordz("Hello, 123!"), 'Found a match!')

    def test_empty_string(self):
        self.assertEqual(text_match_wordz(""), 'Not matched!')

    def test_none_input(self):
        self.assertEqual(text_match_wordz(None), 'Not matched!')
