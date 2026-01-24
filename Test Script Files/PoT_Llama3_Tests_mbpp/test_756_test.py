import unittest
from mbpp_756_code import text_match_zero_one

class TestTextMatchZeroOne(unittest.TestCase):
    def test_typical_match(self):
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match_zero_one('xyz'), 'Not matched!')

    def test_edge_match(self):
        self.assertEqual(text_match_zero_one('a'), 'Found a match!')

    def test_edge_no_match(self):
        self.assertEqual(text_match_zero_one(''), 'Not matched!')

    def test_corner_match(self):
        self.assertEqual(text_match_zero_one('ab?'), 'Found a match!')

    def test_corner_no_match(self):
        self.assertEqual(text_match_zero_one('abc'), 'Not matched!')
