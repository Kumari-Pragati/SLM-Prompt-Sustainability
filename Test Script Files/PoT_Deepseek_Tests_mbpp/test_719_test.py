import unittest
from mbpp_719_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(text_match('ab'), 'Found a match!')
        self.assertEqual(text_match('a'), 'Not matched!')
        self.assertEqual(text_match('abb'), 'Found a match!')
        self.assertEqual(text_match('abbb'), 'Found a match!')

    def test_edge_cases(self):
        self.assertEqual(text_match(''), 'Not matched!')
        self.assertEqual(text_match('aab'), 'Found a match!')
        self.assertEqual(text_match('abab'), 'Found a match!')

    def test_corner_cases(self):
        self.assertEqual(text_match('ababab'), 'Found a match!')
        self.assertEqual(text_match('abababab'), 'Found a match!')
        self.assertEqual(text_match('ababababab'), 'Found a match!')
