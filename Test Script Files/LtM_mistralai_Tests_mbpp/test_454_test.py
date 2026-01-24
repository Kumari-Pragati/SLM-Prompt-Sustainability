import unittest
from mbpp_454_code import text_match_wordz

class TestTextMatchWordz(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match_wordz('wordz'), 'Found a match!')
        self.assertEqual(text_match_wordz('wordz123'), 'Found a match!')
        self.assertEqual(text_match_wordz('wordzWord'), 'Found a match!')

    def test_edge_cases(self):
        self.assertEqual(text_match_wordz('word'), 'Not matched!')
        self.assertEqual(text_match_wordz('wordz.'), 'Found a match!')
        self.assertEqual(text_match_wordz('wordz123z'), 'Found a match!')
        self.assertEqual(text_match_wordz('wordzWordz'), 'Found a match!')
        self.assertEqual(text_match_wordz('wordz123Wordz'), 'Found a match!')

    def test_complex_cases(self):
        self.assertEqual(text_match_wordz('wordz123_'), 'Not matched!')
        self.assertEqual(text_match_wordz('wordz123_z'), 'Found a match!')
        self.assertEqual(text_match_wordz('wordz123_z123'), 'Not matched!')
        self.assertEqual(text_match_wordz('wordz123_z123z'), 'Found a match!')
