import unittest
from mbpp_719_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(text_match('ab'), 'Found a match!')
        self.assertEqual(text_match('aba'), 'Found a match!')
        self.assertEqual(text_match('abab'), 'Found a match!')

    def test_edge_and_boundary_cases(self):
        self.assertEqual(text_match('a'), 'Not matched!')
        self.assertEqual(text_match('abba'), 'Not matched!')
        self.assertEqual(text_match('ababab'), 'Found a match!')
        self.assertEqual(text_match(''), 'Not matched!')
        self.assertEqual(text_match('ab**'), 'Found a match!')
        self.assertEqual(text_match('**ab'), 'Not matched!')

    def test_invalid_input(self):
        self.assertRaises(TypeError, text_match, 123)
        self.assertRaises(TypeError, text_match, None)
        self.assertRaises(TypeError, text_match, [])
