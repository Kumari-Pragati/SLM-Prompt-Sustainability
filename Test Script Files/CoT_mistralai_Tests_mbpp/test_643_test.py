import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_match_wordz_middle('zebra'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('Zebra'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('ZebraZ'), 'Not matched!')

    def test_edge_cases(self):
        self.assertEqual(text_match_wordz_middle('z'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('zebrAz'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('zebraZ'), 'Not matched!')

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, text_match_wordz_middle, 123)
        self.assertRaises(TypeError, text_match_wordz_middle, None)
        self.assertRaises(TypeError, text_match_wordz_middle, [])
        self.assertRaises(TypeError, text_match_wordz_middle, {})
