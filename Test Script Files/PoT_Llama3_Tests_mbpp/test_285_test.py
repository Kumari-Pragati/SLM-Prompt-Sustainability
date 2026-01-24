import unittest
from mbpp_285_code import text_match_two_three

class TestTextMatchTwoThree(unittest.TestCase):
    def test_typical_match(self):
        self.assertEqual(text_match_two_three('abab'), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match_two_three('abc'), 'Not matched!')

    def test_edge_match(self):
        self.assertEqual(text_match_two_three('ababab'), 'Found a match!')

    def test_edge_no_match(self):
        self.assertEqual(text_match_two_three('abcabc'), 'Not matched!')

    def test_corner_match(self):
        self.assertEqual(text_match_two_three('ab'), 'Found a match!')

    def test_corner_no_match(self):
        self.assertEqual(text_match_two_three(''), 'Not matched!')
