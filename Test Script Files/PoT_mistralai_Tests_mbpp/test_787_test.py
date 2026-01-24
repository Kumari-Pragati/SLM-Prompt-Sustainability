import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_match_three('abc'), 'Found a match!')
        self.assertEqual(text_match_three('aab'), 'Found a match!')
        self.assertEqual(text_match_three('abab'), 'Not matched!')

    def test_edge_case(self):
        self.assertEqual(text_match_three('a'), 'Not matched!')
        self.assertEqual(text_match_three('aaa'), 'Not matched!')
        self.assertEqual(text_match_three('ababab'), 'Found a match!')

    def test_boundary_case(self):
        self.assertEqual(text_match_three('ab'), 'Not matched!')
        self.assertEqual(text_match_three('abababab'), 'Found a match!')
        self.assertEqual(text_match_three('ababababab'), 'Found a match!')
