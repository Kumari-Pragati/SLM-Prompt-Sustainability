import unittest
from mbpp_930_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_typical_match(self):
        self.assertEqual(text_match('ab'), 'Found a match!')
        self.assertEqual(text_match('aba'), 'Found a match!')
        self.assertEqual(text_match('abab'), 'Found a match!')
        self.assertEqual(text_match('ababab'), 'Found a match!')

    def test_edge_cases(self):
        self.assertEqual(text_match('a'), 'Not matched!')
        self.assertEqual(text_match('abaa'), 'Not matched!')
        self.assertEqual(text_match('abababab'), 'Found a match!')
        self.assertEqual(text_match(''), 'Not matched!')
        self.assertEqual(text_match(' '), 'Not matched!')
        self.assertEqual(text_match('ab?'), 'Not matched!')
        self.assertEqual(text_match('ab**'), 'Found a match!')
        self.assertEqual(text_match('ab*'), 'Found a match!')
        self.assertEqual(text_match('ab*a'), 'Found a match!')
        self.assertEqual(text_match('ab*ab'), 'Found a match!')
