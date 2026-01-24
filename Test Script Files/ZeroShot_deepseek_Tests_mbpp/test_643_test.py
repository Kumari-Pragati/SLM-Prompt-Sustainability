import unittest
from mbpp_643_code import text_match_wordz_middle

class TestTextMatchWordzMiddle(unittest.TestCase):

    def test_text_match_wordz_middle_positive(self):
        self.assertEqual(text_match_wordz_middle('hello z world'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('z is in the middle'), 'Found a match!')
        self.assertEqual(text_match_wordz_middle('z is not at the end'), 'Found a match!')

    def test_text_match_wordz_middle_negative(self):
        self.assertEqual(text_match_wordz_middle('hello world'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z is not in the middle'), 'Not matched!')
        self.assertEqual(text_match_wordz_middle('z is at the end z'), 'Not matched!')
