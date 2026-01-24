import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(text_match_three('ababab'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_match_three('a'), 'Not matched!')
        self.assertEqual(text_match_three('aba'), 'Found a match!')
        self.assertEqual(text_match_three('abab'), 'Found a match!')
        self.assertEqual(text_match_three('ababa'), 'Found a match!')

    def test_boundary_case(self):
        self.assertEqual(text_match_three('ab'), 'Not matched!')
        self.assertEqual(text_match_three('abab'), 'Found a match!')
        self.assertEqual(text_match_three('ababab'), 'Found a match!')
        self.assertEqual(text_match_three('abababab'), 'Not matched!')

    def test_invalid_input(self):
        self.assertRaises(TypeError, text_match_three, 123)
        self.assertRaises(TypeError, text_match_three, [])
        self.assertRaises(TypeError, text_match_three, ())
        self.assertRaises(TypeError, text_match_three, None)
        self.assertRaises(TypeError, text_match_three, {})
