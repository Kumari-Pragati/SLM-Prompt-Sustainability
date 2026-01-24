import unittest
from mbpp_434_code import text_match_one

class TestTextMatchOne(unittest.TestCase):
    def test_match_one_character(self):
        self.assertEqual(text_match_one('a'), 'Found a match!')

    def test_match_multiple_characters(self):
        self.assertEqual(text_match_one('abcd'), 'Found a match!')

    def test_match_empty_string(self):
        self.assertEqual(text_match_one(''), 'Not matched!')

    def test_match_no_match(self):
        self.assertEqual(text_match_one('xyz'), 'Not matched!')

    def test_match_with_spaces(self):
        self.assertEqual(text_match_one(' a b c '), 'Not matched!')
