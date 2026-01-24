import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(text_match_wordz_middle('zoo'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('zap'), 'Not matched!')

    def test_edge_cases(self):
        self.assertEqual(text_match_wordz_middle('z'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('zzz'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('zZz'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('Zz'), 'Not matched!')

    def test_complex_cases(self):
        self.assertEqual(text_match_wordz_middle('zAaZ'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('zAaZz'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('ZzZ'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('ZzZz'), 'Found a match!')
