import unittest
from mbpp_756_code import text_match_zero_one

class TestTextMatchZeroOne(unittest.TestCase):

    def test_typical_match(self):
        self.assertEqual(text_match_zero_one("ab"), 'Found a match!')

    def test_typical_no_match(self):
        self.assertEqual(text_match_zero_one("xyz"), 'Not matched!')

    def test_edge_match(self):
        self.assertEqual(text_match_zero_one("a"), 'Found a match!')

    def test_edge_no_match(self):
        self.assertEqual(text_match_zero_one(""), 'Not matched!')

    def test_edge_pattern_empty(self):
        self.assertEqual(text_match_zero_one(""), 'Not matched!')

    def test_edge_pattern_single_char(self):
        self.assertEqual(text_match_zero_one("a"), 'Found a match!')

    def test_edge_pattern_multiple_chars(self):
        self.assertEqual(text_match_zero_one("abc"), 'Found a match!')

    def test_edge_pattern_multiple_chars_no_match(self):
        self.assertEqual(text_match_zero_one("def"), 'Not matched!')

    def test_edge_pattern_multiple_chars_with_question_mark(self):
        self.assertEqual(text_match_zero_one("ab?"), 'Found a match!')

    def test_edge_pattern_multiple_chars_with_question_mark_no_match(self):
        self.assertEqual(text_match_zero_one("def?"), 'Not matched!')

    def test_edge_pattern_multiple_chars_with_question_mark_and_chars(self):
        self.assertEqual(text_match_zero_one("ab?c"), 'Found a match!')

    def test_edge_pattern_multiple_chars_with_question_mark_and_chars_no_match(self):
        self.assertEqual(text_match_zero_one("def?ghi"), 'Not matched!')

    def test_edge_pattern_multiple_chars_with_question_mark_and_chars_and_question_mark(self):
        self.assertEqual(text_match_zero_one("ab?c?"), 'Found a match!')

    def test_edge_pattern_multiple_chars_with_question_mark_and_chars_and_question_mark_no_match(self):
        self.assertEqual(text_match_zero_one("def?ghi?"), 'Not matched!')
