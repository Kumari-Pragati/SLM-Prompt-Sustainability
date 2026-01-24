import unittest
from mbpp_879_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(text_match('aaab'), 'Found a match!')
        self.assertEqual(text_match('abab'), 'Found a match!')
        self.assertEqual(text_match('aaaaab'), 'Found a match!')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(text_match('a'), 'Not matched!')
        self.assertEqual(text_match('aa'), 'Not matched!')
        self.assertEqual(text_match('ab'), 'Not matched!')
        self.assertEqual(text_match('aabb'), 'Found a match!')
        self.assertEqual(text_match('abbb'), 'Not matched!')
        self.assertEqual(text_match('aabba'), 'Not matched!')
        self.assertEqual(text_match('aabbb'), 'Not matched!')

    def test_invalid_input(self):
        self.assertNotEqual(text_match(123), 'Found a match!')
        self.assertNotEqual(text_match(None), 'Found a match!')
        self.assertNotEqual(text_match(''), 'Found a match!')
        self.assertNotEqual(text_match(' '), 'Found a match!')
        self.assertNotEqual(text_match('a.'), 'Found a match!')
        self.assertNotEqual(text_match('ab$'), 'Found a match!')
