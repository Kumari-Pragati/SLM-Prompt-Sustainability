import unittest
from mbpp_756_code import text_match_zero_one

class TestTextMatchZeroOne(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(text_match_zero_one(''), 'Not matched!')

    def test_single_a(self):
        self.assertEqual(text_match_zero_one('a'), 'Found a match!')

    def test_single_b(self):
        self.assertEqual(text_match_zero_one('b'), 'Not matched!')

    def test_multiple_a(self):
        self.assertEqual(text_match_zero_one('aa'), 'Found a match!')

    def test_multiple_ab(self):
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')

    def test_multiple_abab(self):
        self.assertEqual(text_match_zero_one('abab'), 'Found a match!')

    def test_multiple_abab_with_other_chars(self):
        self.assertEqual(text_match_zero_one('ababcd'), 'Found a match!')

    def test_multiple_abab_with_repeated_a(self):
        self.assertEqual(text_match_zero_one('aaaaabbbb'), 'Not matched!')
