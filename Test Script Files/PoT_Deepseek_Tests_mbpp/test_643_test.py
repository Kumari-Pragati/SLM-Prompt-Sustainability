import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(text_match_wordz_middle('hello z world'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('z is a letter'), 'Found a match!')

    def test_edge_cases(self):
        self.assertEqual(text_match_wordz_middle('z'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('without z'), 'Not matched!')

    def test_boundary_conditions(self):
        self.assertEqual(text_match_wordz_middle(''), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z' * 10000), 'Found a match!')

    def test_corner_cases(self):
        self.assertEqual(text_match_wordz_middle('z at the beginning'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('z at the end'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('z in the middle'), 'Found a match!')

    def test_invalid_inputs(self):
        # The function does not handle invalid inputs, so we don't need to test this case.
        pass
