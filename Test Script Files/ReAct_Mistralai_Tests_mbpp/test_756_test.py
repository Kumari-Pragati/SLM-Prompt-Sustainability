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

    def test_multiple_non_matching(self):
        self.assertEqual(text_match_zero_one('ac'), 'Not matched!')

    def test_long_string(self):
        long_string = 'a' * 100 + 'b' * 100
        self.assertEqual(text_match_zero_one(long_string), 'Found a match!')
