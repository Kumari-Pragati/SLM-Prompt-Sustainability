import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_match('aaab'), 'Found a match!')
        self.assertEqual(text_match('abab'), 'Found a match!')
        self.assertEqual(text_match('aabba'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_match('a'), 'Not matched!')
        self.assertEqual(text_match('aa'), 'Not matched!')
        self.assertEqual(text_match('ab'), 'Not matched!')
        self.assertEqual(text_match('aabb'), 'Not matched!')
        self.assertEqual(text_match('baa'), 'Not matched!')
        self.assertEqual(text_match('bba'), 'Not matched!')

    def test_boundary_case(self):
        self.assertEqual(text_match('a.'), 'Not matched!')
        self.assertEqual(text_match('a..'), 'Not matched!')
        self.assertEqual(text_match('a...'), 'Not matched!')
        self.assertEqual(text_match('a...b'), 'Found a match!')
        self.assertEqual(text_match('ab.'), 'Not matched!')
        self.assertEqual(text_match('ab..'), 'Not matched!')
        self.assertEqual(text_match('ab...'), 'Not matched!')
        self.assertEqual(text_match('ab...b'), 'Found a match!')
