import unittest
from mbpp_756_code import text_match_zero_one

class TestTextMatchZeroOne(unittest.TestCase):
    def test_match_ab(self):
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')

    def test_match_empty_string(self):
        self.assertEqual(text_match_zero_one(''), 'Not matched!')

    def test_match_ab_multiple_times(self):
        self.assertEqual(text_match_zero_one('abab'), 'Found a match!')

    def test_match_abab(self):
        self.assertEqual(text_match_zero_one('abab'), 'Not matched!')

    def test_match_ab_with_other_characters(self):
        self.assertEqual(text_match_zero_one('abcab'), 'Not matched!')
