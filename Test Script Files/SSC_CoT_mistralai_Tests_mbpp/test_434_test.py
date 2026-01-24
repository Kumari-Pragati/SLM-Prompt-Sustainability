import unittest
from mbpp_434_code import text_match_one

class TestTextMatchOne(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(text_match_one('abab'), 'Found a match!')
        self.assertEqual(text_match_one('aab'), 'Not matched!')

    def test_edge_cases(self):
        self.assertEqual(text_match_one(''), 'Not matched!')
        self.assertEqual(text_match_one('ab'), 'Found a match!')
        self.assertEqual(text_match_one('ababab'), 'Found a match!')

    def test_boundary_cases(self):
        self.assertEqual(text_match_one('a'), 'Not matched!')
        self.assertEqual(text_match_one('abaaaa'), 'Found a match!')
        self.assertEqual(text_match_one('abababab'), 'Found a match!')

    def test_invalid_input(self):
        self.assertRaises(TypeError, text_match_one, 123)
        self.assertRaises(TypeError, text_match_one, None)
