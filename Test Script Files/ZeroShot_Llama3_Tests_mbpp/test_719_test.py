import unittest
from mbpp_719_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_match_found(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_match_found_with_wildcard(self):
        self.assertEqual(text_match('abba'), 'Found a match!')

    def test_match_not_found_with_wildcard(self):
        self.assertEqual(text_match('abcde'), 'Not matched!')

    def test_match_found_with_multiple_occurrences(self):
        self.assertEqual(text_match('abab'), 'Found a match!')

    def test_match_not_found_with_multiple_occurrences(self):
        self.assertEqual(text_match('abcabc'), 'Not matched!')
