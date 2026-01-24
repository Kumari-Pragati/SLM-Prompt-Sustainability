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

    def test_match_not_found_with_empty_string(self):
        self.assertEqual(text_match_zero_one(''), 'Not matched!')

    def test_match_not_found_with_single_character(self):
        self.assertEqual(text_match_zero_one('a'), 'Not matched!')

    def test_match_not_found_with_single_character_and_question_mark(self):
        self.assertEqual(text_match_zero_one('a?'), 'Not matched!')

    def test_match_not_found_with_single_character_and_question_mark_and_characters(self):
        self.assertEqual(text_match_zero_one('a?b'), 'Not matched!')

    def test_match_not_found_with_single_character_and_question_mark_and_characters_and_digits(self):
        self.assertEqual(text_match_zero_one('a?b123'), 'Not matched!')

    def test_match_not_found_with_single_character_and_question_mark_and_characters_and_digits_and_punctuation(self):
        self.assertEqual(text_match_zero_one('a?b123!'), 'Not matched!')

    def test_match_not_found_with_single_character_and_question_mark_and_characters_and_digits_and_punctuation_and_spaces(self):
        self.assertEqual(text_match_zero_one('a? b123!'), 'Not matched!')

    def test_match_not_found_with_single_character_and_question_mark_and_characters_and_digits_and_punctuation_and_spaces_and_newline(self):
        self.assertEqual(text_match_zero_one('a? b123!\n'), 'Not matched!')
