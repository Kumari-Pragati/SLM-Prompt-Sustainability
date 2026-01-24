import unittest
from mbpp_756_code import text_match_zero_one

class TestTextMatchZeroOne(unittest.TestCase):

    def test_found_match(self):
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')

    def test_not_found_match(self):
        self.assertEqual(text_match_zero_one('abc'), 'Not matched!')

    def test_found_match_with_question_mark(self):
        self.assertEqual(text_match_zero_one('ab?'), 'Found a match!')

    def test_found_match_with_question_mark_and_characters(self):
        self.assertEqual(text_match_zero_one('ab?c'), 'Found a match!')

    def test_not_found_match_with_question_mark(self):
        self.assertEqual(text_match_zero_one('abc?'), 'Not matched!')
