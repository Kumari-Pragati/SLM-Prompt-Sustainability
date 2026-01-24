import unittest
from mbpp_756_code import text_match_zero_one

class TestTextMatchZeroOne(unittest.TestCase):

    def test_match_found(self):
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match_zero_one('xyz'), 'Not matched!')

    def test_match_found_with_question_mark(self):
        self.assertEqual(text_match_zero_one('ab?'), 'Found a match!')

    def test_match_found_with_question_mark_and_characters(self):
        self.assertEqual(text_match_zero_one('ab?c'), 'Found a match!')

    def test_match_found_with_question_mark_and_characters_and_digits(self):
        self.assertEqual(text_match_zero_one('ab?c123'), 'Found a match!')

    def test_match_found_with_question_mark_and_characters_and_digits_and_punctuation(self):
        self.assertEqual(text_match_zero_one('ab?c123!'), 'Found a match!')

    def test_match_found_with_question_mark_and_characters_and_digits_and_punctuation_and_spaces(self):
        self.assertEqual(text_match_zero_one('ab? c123!'), 'Found a match!')

    def test_match_found_with_question_mark_and_characters_and_digits_and_punctuation_and_spaces_and_newline(self):
        self.assertEqual(text_match_zero_one('ab? c123!\n'), 'Found a match!')

    def test_match_found_with_question_mark_and_characters_and_digits_and_punctuation_and_spaces_and_newline_and_tabs(self):
        self.assertEqual(text_match_zero_one('ab? c123!\n\t'), 'Found a match!')
