import unittest
from mbpp_434_code import text_match_one

class TestTextMatchOne(unittest.TestCase):

    def test_typical_match(self):
        self.assertEqual(text_match_one('abab'), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match_one('abc'), 'Not matched!')

    def test_edge_match(self):
        self.assertEqual(text_match_one('a'), 'Found a match!')

    def test_edge_no_match(self):
        self.assertEqual(text_match_one(''), 'Not matched!')

    def test_corner_match(self):
        self.assertEqual(text_match_one('ababab'), 'Found a match!')

    def test_corner_no_match(self):
        self.assertEqual(text_match_one('ab'), 'Not matched!')
