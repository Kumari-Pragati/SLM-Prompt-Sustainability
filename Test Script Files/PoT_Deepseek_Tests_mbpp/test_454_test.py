import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(text_match_wordz('hello world'), 'Not matched!')
        self.assertEqual(text_match_wordz('zoo zoo'), 'Found a match!')
        self.assertEqual(text_match_wordz('the quick brown fox jumps over the lazy dog'), 'Not matched!')
        self.assertEqual(text_match_wordz('the quick brown fox jumps over the lazy zzz'), 'Found a match!')

    def test_edge_cases(self):
        self.assertEqual(text_match_wordz(''), 'Not matched!')
        self.assertEqual(text_match_wordz('z'), 'Found a match!')
        self.assertEqual(text_match_wordz(' '), 'Not matched!')
        self.assertEqual(text_match_wordz('z '), 'Found a match!')

    def test_corner_cases(self):
        self.assertEqual(text_match_wordz('the quick brown fox jumps over the lazy dog z'), 'Found a match!')
        self.assertEqual(text_match_wordz('the quick brown fox jumps over the lazy dog zz'), 'Found a match!')
        self.assertEqual(text_match_wordz('the quick brown fox jumps over the lazy dog zzz'), 'Found a match!')
