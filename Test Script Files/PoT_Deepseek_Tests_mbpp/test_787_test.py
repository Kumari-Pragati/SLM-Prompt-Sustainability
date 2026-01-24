import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(text_match_three('abbb'), 'Found a match!')
        self.assertEqual(text_match_three('ab'), 'Not matched!')

    def test_edge_cases(self):
        self.assertEqual(text_match_three(''), 'Not matched!')
        self.assertEqual(text_match_three('a'), 'Not matched!')
        self.assertEqual(text_match_three('abbbbb'), 'Found a match!')

    def test_corner_cases(self):
        self.assertEqual(text_match_three('abbbbbbb'), 'Found a match!')
        self.assertEqual(text_match_three('abbbbbbbb'), 'Not matched!')
