import unittest
from mbpp_434_code import text_match_one

class TestTextMatchOne(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(text_match_one('ab'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_one('a'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_one(''), 'Not matched!')

    def test_multiple_matches(self):
        self.assertEqual(text_match_one('abb'), 'Found a match!')

    def test_pattern_with_other_characters(self):
        self.assertEqual(text_match_one('acb'), 'Not matched!')

    def test_pattern_with_numbers(self):
        self.assertEqual(text_match_one('ab1'), 'Found a match!')
