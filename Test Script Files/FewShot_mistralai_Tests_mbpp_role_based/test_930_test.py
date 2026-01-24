import unittest
from mbpp_930_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_match_with_ab_pattern(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_match_with_multiple_ab(self):
        self.assertEqual(text_match('abab'), 'Found a match!')

    def test_match_with_ab_and_other_chars(self):
        self.assertEqual(text_match('abcdab'), 'Found a match!')

    def test_no_match_with_no_ab(self):
        self.assertEqual(text_match('xyz'), 'Not matched!')

    def test_no_match_with_ab_at_beginning(self):
        self.assertEqual(text_match('abX'), 'Not matched!')

    def test_no_match_with_ab_at_end(self):
        self.assertEqual(text_match('Xab'), 'Not matched!')

    def test_no_match_with_ab_in_middle(self):
        self.assertEqual(text_match('XabY'), 'Not matched!')
