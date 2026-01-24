import unittest
from mbpp_930_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_match_found(self):
        self.assertEqual(text_match('ab'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match('xyz'), 'Not matched!')

    def test_match_found_with_multiple_occurrences(self):
        self.assertEqual(text_match('abab'), 'Found a match!')

    def test_match_found_with_non_matching_characters(self):
        self.assertEqual(text_match('abc'), 'Not matched!')

    def test_match_found_with_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_match_found_with_non_string_input(self):
        with self.assertRaises(TypeError):
            text_match(123)
