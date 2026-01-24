import unittest
from mbpp_719_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_match_with_ab_pattern(self):
        self.assertEqual(text_match('ab'), 'Found a match!')
        self.assertEqual(text_match('aab'), 'Found a match!')
        self.assertEqual(text_match('abab'), 'Found a match!')

    def test_match_with_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_match_with_single_a(self):
        self.assertEqual(text_match('a'), 'Not matched!')

    def test_match_with_multiple_b(self):
        self.assertEqual(text_match('bb'), 'Not matched!')

    def test_match_with_multiple_non_a_non_b(self):
        self.assertEqual(text_match('xyz'), 'Not matched!')
