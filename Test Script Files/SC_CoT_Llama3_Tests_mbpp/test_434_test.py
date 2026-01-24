import unittest
from mbpp_434_code import text_match_one

class TestTextMatchOne(unittest.TestCase):

    def test_match_found(self):
        self.assertEqual(text_match_one('abab'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match_one('abc'), 'Not matched!')

    def test_match_found_at_start(self):
        self.assertEqual(text_match_one('abababc'), 'Found a match!')

    def test_match_found_at_end(self):
        self.assertEqual(text_match_one('abcab'), 'Found a match!')

    def test_match_found_multiple_times(self):
        self.assertEqual(text_match_one('ababab'), 'Found a match!')

    def test_match_found_with_non_matching_text(self):
        self.assertEqual(text_match_one('def'), 'Not matched!')

    def test_match_found_with_empty_text(self):
        self.assertEqual(text_match_one(''), 'Not matched!')

    def test_match_found_with_non_string_input(self):
        with self.assertRaises(TypeError):
            text_match_one(123)

    def test_match_found_with_none_input(self):
        with self.assertRaises(TypeError):
            text_match_one(None)
