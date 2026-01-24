import unittest
from mbpp_434_code import text_match_one

class TestTextMatchOne(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match_one('a'), 'Found a match!')
        self.assertEqual(text_match_one('ab'), 'Found a match!')
        self.assertEqual(text_match_one('abab'), 'Found a match!')

    def test_edge_cases(self):
        self.assertEqual(text_match_one('aab'), 'Not matched!')
        self.assertEqual(text_match_one(''), 'Not matched!')
        self.assertEqual(text_match_one('ababab'), 'Found a match!')

    def test_complex_cases(self):
        self.assertEqual(text_match_one('ababcdab'), 'Found a match!')
        self.assertEqual(text_match_one('ababababab'), 'Found a match!')
        self.assertEqual(text_match_one('abababababcd'), 'Not matched!')
