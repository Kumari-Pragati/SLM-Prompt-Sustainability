import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):
    def test_match_wordz_middle_with_z(self):
        self.assertEqual(text_match_wordz_middle('z'), 'Found a match!')

    def test_match_wordz_middle_with_multiple_zs(self):
        self.assertEqual(text_match_wordz_middle('zz'), 'Found a match!')

    def test_match_wordz_middle_with_z_at_beginning(self):
        self.assertEqual(text_match_wordz_middle('zText'), 'Not matched!')

    def test_match_wordz_middle_with_z_at_end(self):
        self.assertEqual(text_match_wordz_middle('Textz'), 'Not matched!')

    def test_match_wordz_middle_with_multiple_words(self):
        self.assertEqual(text_match_wordz_middle('TextZText'), 'Not matched!')

    def test_match_wordz_middle_with_no_z(self):
        self.assertEqual(text_match_wordz_middle('Text'), 'Not matched!')
