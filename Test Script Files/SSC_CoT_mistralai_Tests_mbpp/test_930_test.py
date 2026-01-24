import unittest
from mbpp_930_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(text_match('abab'), 'Found a match!')
        self.assertEqual(text_match('a'), 'Not matched!')
        self.assertEqual(text_match('abba'), 'Found a match!')
        self.assertEqual(text_match('abbb'), 'Not matched!')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(text_match(''), 'Not matched!')
        self.assertEqual(text_match('ab'), 'Found a match!')
        self.assertEqual(text_match('ababab'), 'Found a match!')
        self.assertEqual(text_match('abababab'), 'Found a match!')
        self.assertEqual(text_match('ababababab'), 'Found a match!')
        self.assertEqual(text_match('abababababab'), 'Found a match!')

    def test_special_cases(self):
        self.assertEqual(text_match('aab'), 'Not matched!')
        self.assertEqual(text_match('ababababab'), 'Found a match!')
        self.assertEqual(text_match('ab*'), 'Found a match!')
        self.assertEqual(text_match('ab**'), 'Found a match!')
        self.assertEqual(text_match('ab***'), 'Found a match!')
