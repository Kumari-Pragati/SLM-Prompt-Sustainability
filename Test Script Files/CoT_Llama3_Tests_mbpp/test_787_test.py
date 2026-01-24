import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):

    def test_match_found(self):
        self.assertEqual(text_match_three('ababab'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match_three('abc'), 'Not matched!')

    def test_match_found_at_start(self):
        self.assertEqual(text_match_three('abababc'), 'Found a match!')

    def test_match_found_at_end(self):
        self.assertEqual(text_match_three('abcabab'), 'Found a match!')

    def test_match_found_multiple_times(self):
        self.assertEqual(text_match_three('abababab'), 'Found a match!')

    def test_match_found_at_start_and_end(self):
        self.assertEqual(text_match_three('ababababc'), 'Found a match!')

    def test_match_found_with_spaces(self):
        self.assertEqual(text_match_three(' ababab '), 'Found a match!')

    def test_match_found_with_punctuation(self):
        self.assertEqual(text_match_three('ababab!'), 'Found a match!')

    def test_match_found_with_uppercase(self):
        self.assertEqual(text_match_three('ABABAB'), 'Found a match!')

    def test_match_found_with_mixed_case(self):
        self.assertEqual(text_match_three('AbAbAb'), 'Found a match!')

    def test_match_not_found_with_non_matching_text(self):
        self.assertEqual(text_match_three('def'), 'Not matched!')

    def test_match_not_found_with_empty_text(self):
        self.assertEqual(text_match_three(''), 'Not matched!')

    def test_match_not_found_with_none_text(self):
        self.assertEqual(text_match_three(None), 'Not matched!')
