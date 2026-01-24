import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):

    def test_typical_match(self):
        self.assertEqual(text_match_three('ababab'), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match_three('abc'), 'Not matched!')

    def test_edge_match(self):
        self.assertEqual(text_match_three('abababab'), 'Found a match!')

    def test_edge_no_match(self):
        self.assertEqual(text_match_three(''), 'Not matched!')

    def test_corner_match(self):
        self.assertEqual(text_match_three('ababababab'), 'Found a match!')

    def test_corner_no_match(self):
        self.assertEqual(text_match_three('ab'), 'Not matched!')
