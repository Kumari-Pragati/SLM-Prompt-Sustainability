import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):
    def test_found_match(self):
        self.assertEqual(text_match_wordz('HelloZWorld'), 'Found a match!')
        self.assertEqual(text_match_wordz('Z'), 'Found a match!')
        self.assertEqual(text_match_wordz('Z123Z'), 'Found a match!')

    def test_not_found(self):
        self.assertEqual(text_match_wordz('HelloWorld'), 'Not matched!')
        self.assertEqual(text_match_wordz('HelloZ'), 'Not matched!')
        self.assertEqual(text_match_wordz('Z123'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_wordz(''), 'Not matched!')

    def test_special_characters(self):
        self.assertEqual(text_match_wordz('!Z@#$%^&*()'), 'Not matched!')

    def test_numbers(self):
        self.assertEqual(text_match_wordz('123Z456'), 'Not matched!')

    def test_whitespace(self):
        self.assertEqual(text_match_wordz(' HelloZ World '), 'Not matched!')
