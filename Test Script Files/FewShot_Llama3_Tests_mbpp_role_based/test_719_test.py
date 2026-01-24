import unittest
from mbpp_719_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_match_found(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_pattern_with_question_mark(self):
        self.assertEqual(text_match('ab?'), 'Found a match!')

    def test_pattern_with_star(self):
        self.assertEqual(text_match('ab*'), 'Found a match!')

    def test_pattern_with_multiple_characters(self):
        self.assertEqual(text_match('abcde'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_pattern_with_non_matching_characters(self):
        self.assertEqual(text_match('xyz'), 'Not matched!')
