import unittest
from mbpp_285_code import text_match_two_three

class TestTextMatchTwoThree(unittest.TestCase):
    def test_match_found(self):
        self.assertEqual(text_match_two_three('ababab'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match_two_three('abc'), 'Not matched!')

    def test_match_found_with_multiple_occurrences(self):
        self.assertEqual(text_match_two_three('abababab'), 'Found a match!')

    def test_match_found_with_non_matching_text(self):
        self.assertEqual(text_match_two_three('abab'), 'Found a match!')

    def test_empty_string(self):
        self.assertEqual(text_match_two_three(''), 'Not matched!')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            text_match_two_three(123)
