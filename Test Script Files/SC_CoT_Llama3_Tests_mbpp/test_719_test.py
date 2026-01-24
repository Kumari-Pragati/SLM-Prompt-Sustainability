import unittest
from mbpp_719_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_typical_match(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match('cd'), 'Not matched!')

    def test_edge_match_at_start(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_edge_match_at_end(self):
        self.assertEqual(text_match('ba'), 'Found a match!')

    def test_edge_no_match_at_start(self):
        self.assertEqual(text_match('cd'), 'Not matched!')

    def test_edge_no_match_at_end(self):
        self.assertEqual(text_match('dc'), 'Not matched!')

    def test_pattern_with_multiple_occurrences(self):
        self.assertEqual(text_match('abab'), 'Found a match!')

    def test_pattern_with_no_occurrences(self):
        self.assertEqual(text_match('cdcd'), 'Not matched!')

    def test_pattern_with_multiple_occurrences_and_non_matching_chars(self):
        self.assertEqual(text_match('ababxy'), 'Found a match!')

    def test_pattern_with_no_occurrences_and_non_matching_chars(self):
        self.assertEqual(text_match('cdcdxy'), 'Not matched!')

    def test_pattern_with_non_matching_chars(self):
        self.assertEqual(text_match('axy'), 'Not matched!')

    def test_pattern_with_non_matching_chars_and_non_matching_chars(self):
        self.assertEqual(text_match('axyz'), 'Not matched!')
