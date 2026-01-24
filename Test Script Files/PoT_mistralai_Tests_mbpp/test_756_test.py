import unittest
from mbpp_756_code import text_match_zero_one

class TestTextMatchZeroOne(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')
        self.assertEqual(text_match_zero_one('a'), 'Not matched!')
        self.assertEqual(text_match_zero_one('abab'), 'Found a match!')
        self.assertEqual(text_match_zero_one('ababab'), 'Found a match!')
        self.assertEqual(text_match_zero_one(''), 'Not matched!')

    def test_edge_case(self):
        self.assertEqual(text_match_zero_one('a '), 'Not matched!')
        self.assertEqual(text_match_zero_one(' ab '), 'Found a match!')
        self.assertEqual(text_match_zero_one(' aba '), 'Not matched!')
