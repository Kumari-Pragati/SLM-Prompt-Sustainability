import unittest
from mbpp_930_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match('cd'), 'Not matched!')

    def test_empty_input(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_pattern_with_question_mark(self):
        self.assertEqual(text_match('ab?'), 'Found a match!')

    def test_pattern_with_question_mark_and_no_match(self):
        self.assertEqual(text_match('cd?'), 'Not matched!')

    def test_pattern_with_question_mark_and_empty_input(self):
        self.assertEqual(text_match('?'), 'Not matched!')

    def test_pattern_with_question_mark_and_multiple_chars(self):
        self.assertEqual(text_match('ab?cd'), 'Found a match!')

    def test_pattern_with_question_mark_and_multiple_chars_no_match(self):
        self.assertEqual(text_match('ef?gh'), 'Not matched!')
