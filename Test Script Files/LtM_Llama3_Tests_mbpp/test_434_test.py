import unittest
from mbpp_434_code import text_match_one

class TestTextMatchOne(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match_one('ab'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_one(''), 'Not matched!')

    def test_edge_case(self):
        self.assertEqual(text_match_one('a'), 'Not matched!')

    def test_pattern_match(self):
        self.assertEqual(text_match_one('abab'), 'Found a match!')

    def test_pattern_no_match(self):
        self.assertEqual(text_match_one('abc'), 'Not matched!')

    def test_pattern_edge_case(self):
        self.assertEqual(text_match_one('a'), 'Not matched!')
