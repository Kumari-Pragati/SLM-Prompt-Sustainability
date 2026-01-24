import unittest
from mbpp_930_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match('ac'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_pattern_at_start(self):
        self.assertEqual(text_match('abab'), 'Found a match!')

    def test_pattern_at_end(self):
        self.assertEqual(text_match('bba'), 'Found a match!')

    def test_pattern_multiple_times(self):
        self.assertEqual(text_match('ababab'), 'Found a match!')

    def test_pattern_no_times(self):
        self.assertEqual(text_match('ba'), 'Not matched!')
