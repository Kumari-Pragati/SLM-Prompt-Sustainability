import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):
    def test_match_found(self):
        self.assertEqual(text_match_wordz("Hello, world!"), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match_wordz("This is a test"), 'Not matched!')

    def test_match_found_with_punctuation(self):
        self.assertEqual(text_match_wordz("Hello, world!"), 'Found a match!')

    def test_match_found_with_numbers(self):
        self.assertEqual(text_match_wordz("Hello, 123!"), 'Found a match!')

    def test_match_found_with_special_characters(self):
        self.assertEqual(text_match_wordz("Hello, world!@#"), 'Found a match!')

    def test_match_not_found_with_empty_string(self):
        self.assertEqual(text_match_wordz(""), 'Not matched!')
