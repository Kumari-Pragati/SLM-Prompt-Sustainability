import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_match_wordz_middle('hello world'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('hello zorld'), 'Found a match!')

    def test_edge_case(self):
        self.assertEqual(text_match_wordz_middle('z'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle(''), 'Not matched!')

    def test_boundary_case(self):
        self.assertEqual(text_match_wordz_middle('zello worl'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('hello worl'), 'Not matched!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_match_wordz_middle(123)
