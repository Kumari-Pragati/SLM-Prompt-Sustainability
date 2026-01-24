import unittest
from mbpp_434_code import text_match_one

class TestTextMatchOne(unittest.TestCase):
    def test_match_found(self):
        self.assertEqual(text_match_one('abab'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match_one('hello'), 'Not matched!')

    def test_pattern_match(self):
        self.assertEqual(text_match_one('ababab'), 'Found a match!')

    def test_pattern_not_match(self):
        self.assertEqual(text_match_one('hello world'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_one(''), 'Not matched!')

    def test_none_input(self):
        self.assertEqual(text_match_one(None), 'Not matched!')
