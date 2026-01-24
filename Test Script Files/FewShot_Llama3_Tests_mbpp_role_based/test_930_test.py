import unittest
from mbpp_930_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_match_found(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_pattern_with_question_mark(self):
        self.assertEqual(text_match('ab?'), 'Found a match!')

    def test_pattern_with_star(self):
        self.assertEqual(text_match('ab*'), 'Found a match!')

    def test_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            text_match(123)
