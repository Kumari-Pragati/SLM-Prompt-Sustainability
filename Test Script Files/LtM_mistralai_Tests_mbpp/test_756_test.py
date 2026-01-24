import unittest
from mbpp_756_code import text_match_zero_one

class TestTextMatchZeroOne(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match_zero_one('a'), 'Found a match!')
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')
        self.assertEqual(text_match_zero_one('aba'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_zero_one(''), 'Not matched!')
        self.assertEqual(text_match_zero_one('b'), 'Not matched!')
        self.assertEqual(text_match_zero_one('abab'), 'Not matched!')

    def test_edge_cases(self):
        self.assertEqual(text_match_zero_one('a.'), 'Found a match!')
        self.assertEqual(text_match_zero_one('ab.'), 'Not matched!')
        self.assertEqual(text_match_zero_one('ab\n'), 'Found a match!')
        self.assertEqual(text_match_zero_one('\nab'), 'Not matched!')
