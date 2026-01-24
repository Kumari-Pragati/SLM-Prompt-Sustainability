import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_wordz_middle('hello z world'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_match_wordz_middle('z'), 'Found a match!')

    def test_boundary_case(self):
        self.assertEqual(text_match_wordz_middle('zhello world'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('hello worldz'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('hello z'), 'Found a match!')

    def test_corner_case(self):
        self.assertEqual(text_match_wordz_middle('hello world'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle(''), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match_wordz_middle(123)
