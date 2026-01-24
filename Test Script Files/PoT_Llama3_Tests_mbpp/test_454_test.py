import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):
    def test_typical_match(self):
        self.assertEqual(text_match_wordz("Hello worldz"), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match_wordz("Hello world"), 'Not matched!')

    def test_edge_match_at_start(self):
        self.assertEqual(text_match_wordz("worldz hello"), 'Found a match!')

    def test_edge_match_at_end(self):
        self.assertEqual(text_match_wordz("hello worldz"), 'Found a match!')

    def test_edge_no_match_at_start(self):
        self.assertEqual(text_match_wordz("hello world"), 'Not matched!')

    def test_edge_no_match_at_end(self):
        self.assertEqual(text_match_wordz("Hello world"), 'Not matched!')

    def test_corner_match_with_punctuation(self):
        self.assertEqual(text_match_wordz("Hello worldz!"), 'Found a match!')

    def test_corner_no_match_with_punctuation(self):
        self.assertEqual(text_match_wordz("Hello world!"), 'Not matched!')
