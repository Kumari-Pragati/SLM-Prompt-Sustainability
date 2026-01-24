import unittest
from mbpp_756_code import text_match_zero_one

class TestTextMatchZeroOne(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(text_match_zero_one(''), 'Not matched!')

    def test_single_character(self):
        self.assertEqual(text_match_zero_one('a'), 'Not matched!')
        self.assertEqual(text_match_zero_one('b'), 'Not matched!')
        self.assertEqual(text_match_zero_one('c'), 'Not matched!')

    def test_two_characters(self):
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')
        self.assertEqual(text_match_zero_one('ba'), 'Found a match!')
        self.assertEqual(text_match_zero_one('ac'), 'Not matched!')
        self.assertEqual(text_match_zero_one('bc'), 'Not matched!')

    def test_three_characters(self):
        self.assertEqual(text_match_zero_one('aba'), 'Found a match!')
        self.assertEqual(text_match_zero_one('bab'), 'Found a match!')
        self.assertEqual(text_match_zero_one('abc'), 'Not matched!')

    def test_longer_strings(self):
        self.assertEqual(text_match_zero_one('ababab'), 'Found a match!')
        self.assertEqual(text_match_zero_one('abcdab'), 'Not matched!')
        self.assertEqual(text_match_zero_one('abcdefg'), 'Not matched!')
