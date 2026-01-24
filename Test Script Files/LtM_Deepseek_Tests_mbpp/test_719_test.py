import unittest
from mbpp_719_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match('ac'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_single_character(self):
        self.assertEqual(text_match('a'), 'Not matched!')

    def test_multiple_matches(self):
        self.assertEqual(text_match('ababab'), 'Found a match!')

    def test_pattern_at_end(self):
        self.assertEqual(text_match('ba'), 'Found a match!')

    def test_pattern_at_start(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_pattern_in_middle(self):
        self.assertEqual(text_match('acb'), 'Found a match!')

    def test_pattern_with_spaces(self):
        self.assertEqual(text_match('ab '), 'Found a match!')

    def test_pattern_with_numbers(self):
        self.assertEqual(text_match('ab1'), 'Found a match!')

    def test_pattern_with_special_chars(self):
        self.assertEqual(text_match('ab!'), 'Found a match!')
