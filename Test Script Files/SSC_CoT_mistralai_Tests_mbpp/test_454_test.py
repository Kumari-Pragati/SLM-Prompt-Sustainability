import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(text_match_wordz("abcxyzdef"), 'Found a match!')
        self.assertEqual(text_match_wordz("xyz"), 'Found a match!')
        self.assertEqual(text_match_wordz("z"), 'Found a match!')

    def test_edge_cases(self):
        self.assertEqual(text_match_wordz("abcxyz"), 'Not matched!')
        self.assertEqual(text_match_wordz("xyzdef"), 'Found a match!')
        self.assertEqual(text_match_wordz("abcxyzdef"), 'Not matched!')
        self.assertEqual(text_match_wordz("xyz123"), 'Not matched!')
        self.assertEqual(text_match_wordz("xyz.z"), 'Found a match!')
        self.assertEqual(text_match_wordz("z.xyz"), 'Found a match!')

    def test_invalid_inputs(self):
        self.assertNotEqual(text_match_wordz(123), 'Found a match!')
        self.assertNotEqual(text_match_wordz(None), 'Found a match!')
        self.assertNotEqual(text_match_wordz(""), 'Found a match!')
        self.assertNotEqual(text_match_wordz(" "), 'Found a match!')
