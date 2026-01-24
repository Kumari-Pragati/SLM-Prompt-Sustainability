import unittest
from mbpp_930_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_typical_match(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match('xyz'), 'Not matched!')

    def test_edge_match_at_start(self):
        self.assertEqual(text_match('abxyz'), 'Found a match!')

    def test_edge_match_at_end(self):
        self.assertEqual(text_match('xyzab'), 'Found a match!')

    def test_edge_no_match_at_start(self):
        self.assertEqual(text_match('xyz'), 'Not matched!')

    def test_edge_no_match_at_end(self):
        self.assertEqual(text_match('abxyz'), 'Not matched!')

    def test_corner_match_at_middle(self):
        self.assertEqual(text_match('axb'), 'Found a match!')

    def test_corner_no_match_at_middle(self):
        self.assertEqual(text_match('axyz'), 'Not matched!')
