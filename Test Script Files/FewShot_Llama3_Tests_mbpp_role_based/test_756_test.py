import unittest
from mbpp_756_code import text_match_zero_one

class TestTextMatchZeroOne(unittest.TestCase):
    def test_match_found(self):
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match_zero_one('abc'), 'Not matched!')

    def test_pattern_with_question_mark(self):
        self.assertEqual(text_match_zero_one('a?b'), 'Found a match!')

    def test_pattern_without_question_mark(self):
        self.assertEqual(text_match_zero_one('ab'), 'Found a match!')

    def test_empty_string(self):
        self.assertEqual(text_match_zero_one(''), 'Not matched!')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            text_match_zero_one(123)
