import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(text_match_wordz_middle('hello z world'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('z is a letter'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('no match here'), 'Not matched!')

    def test_edge_cases(self):
        self.assertEqual(text_match_wordz_middle('z'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle(''), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('zhello zworld'), 'Not matched!')

    def test_error_cases(self):
        with self.assertRaises(TypeError):
            text_match_wordz_middle(123)
        with self.assertRaises(TypeError):
            text_match_wordz_middle(None)
        with self.assertRaises(TypeError):
            text_match_wordz_middle(True)
