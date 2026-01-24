import unittest
from mbpp_643_code import str
from 643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(text_match_wordz_middle('zebra'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('Zebra'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('ZebraZ'), 'Not matched!')

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(text_match_wordz_middle(''), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('zz'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('zZ'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('Zz'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('ZzZ'), 'Not matched!')

    def test_special_cases(self):
        self.assertEqual(text_match_wordz_middle('ZebrAz'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('ZebrAzZ'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('ZebrAzZebra'), 'Found a match!')
