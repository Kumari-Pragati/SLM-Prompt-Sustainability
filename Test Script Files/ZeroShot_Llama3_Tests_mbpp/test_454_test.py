import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):

    def test_found_match(self):
        self.assertEqual(text_match_wordz("Hello worldz"), 'Found a match!')

    def test_not_found_match(self):
        self.assertEqual(text_match_wordz("Hello world"), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_wordz(""), 'Not matched!')

    def test_no_match(self):
        self.assertEqual(text_match_wordz("Hello"), 'Not matched!')