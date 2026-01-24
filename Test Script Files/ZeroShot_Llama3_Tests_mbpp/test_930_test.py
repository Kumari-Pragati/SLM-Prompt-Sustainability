import unittest
from mbpp_930_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_match(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_match_with_wildcard(self):
        self.assertEqual(text_match('abba'), 'Found a match!')

    def test_no_match_with_wildcard(self):
        self.assertEqual(text_match('abcde'), 'Not matched!')

    def test_match_with_multiple_wildcards(self):
        self.assertEqual(text_match('abbaabba'), 'Found a match!')

    def test_no_match_with_multiple_wildcards(self):
        self.assertEqual(text_match('abcdeabcde'), 'Not matched!')
