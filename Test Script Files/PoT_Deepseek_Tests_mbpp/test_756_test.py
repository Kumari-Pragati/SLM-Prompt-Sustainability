import unittest
from mbpp_756_code import text_match_zero_one

class TestTextMatchZeroOne(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')
        self.assertEqual(text_match_zero_one('a'), 'Not matched!')
        self.assertEqual(text_match_zero_one('b'), 'Not matched!')
        self.assertEqual(text_match_zero_one('abc'), 'Not matched!')

    def test_edge_cases(self):
        self.assertEqual(text_match_zero_one(''), 'Not matched!')
        self.assertEqual(text_match_zero_one('a'*10000), 'Not matched!')

    def test_corner_cases(self):
        self.assertEqual(text_match_zero_one('ababababab'), 'Found a match!')
        self.assertEqual(text_match_zero_one('aab'), 'Not matched!')
        self.assertEqual(text_match_zero_one('bba'), 'Not matched!')
