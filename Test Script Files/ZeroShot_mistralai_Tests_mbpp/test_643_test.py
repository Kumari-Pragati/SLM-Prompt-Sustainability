import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(text_match_wordz_middle(''), 'Not matched!')

    def test_single_word(self):
        self.assertEqual(text_match_wordz_middle('z'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('Z'), 'Not matched!')

    def test_multiple_words(self):
        self.assertEqual(text_match_wordz_middle('zap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('zapz'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('zapZ'), 'Not matched!')

    def test_multiple_occurrences(self):
        self.assertEqual(text_match_wordz_middle('zzapzz'), 'Found a match!')

    def test_punctuation(self):
        self.assertEqual(text_match_wordz_middle('z,ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z.ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z;ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z:ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('za?p'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z!ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z@ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z#ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z$ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z%ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z&ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z*ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z+ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z-ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z_ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z^ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z|ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z~ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z`ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z\'ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z"ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z\''), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z\\ap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z\bap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z\nap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z\rap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z\tap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z\vap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z\rap'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z\fap'), 'Not matched!')
