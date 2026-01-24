import unittest
from mbpp_756_code import text_match_zero_one

class TestTextMatchZeroOne(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_zero_one('ac'), 'Not matched!')

    def test_zero_occurrence(self):
        self.assertEqual(text_match_zero_one('a'), 'Not matched!')

    def test_one_occurrence(self):
        self.assertEqual(text_match_zero_one('ba'), 'Found a match!')

    def test_empty_string(self):
        self.assertEqual(text_match_zero_one(''), 'Not matched!')

    def test_multiple_matches(self):
        self.assertEqual(text_match_zero_one('ababab'), 'Found a match!')

    def test_multiple_no_matches(self):
        self.assertEqual(text_match_zero_one('acacac'), 'Not matched!')
