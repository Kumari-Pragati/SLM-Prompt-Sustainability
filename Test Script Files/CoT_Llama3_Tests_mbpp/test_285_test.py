import unittest
from mbpp_285_code import text_match_two_three

class TestTextMatchTwoThree(unittest.TestCase):
    def test_match_found(self):
        self.assertEqual(text_match_two_three('abab'), 'Found a match!')

    def test_match_not_found(self):
        self.assertEqual(text_match_two_three('abc'), 'Not matched!')

    def test_match_found_at_start(self):
        self.assertEqual(text_match_two_three('ababab'), 'Found a match!')

    def test_match_found_at_end(self):
        self.assertEqual(text_match_two_three('abababc'), 'Found a match!')

    def test_match_found_multiple_times(self):
        self.assertEqual(text_match_two_three('abababab'), 'Found a match!')

    def test_match_found_at_start_and_end(self):
        self.assertEqual(text_match_two_three('ababababc'), 'Found a match!')

    def test_match_found_with_spaces(self):
        self.assertEqual(text_match_two_three(' abab abc'), 'Found a match!')

    def test_match_found_with_punctuation(self):
        self.assertEqual(text_match_two_three('abab!abc'), 'Found a match!')

    def test_match_found_with_newline(self):
        self.assertEqual(text_match_two_three('abab\nabc'), 'Found a match!')

    def test_match_not_found_with_non_alphabetic_characters(self):
        self.assertEqual(text_match_two_three('123abc'), 'Not matched!')

    def test_match_not_found_with_empty_string(self):
        self.assertEqual(text_match_two_three(''), 'Not matched!')

    def test_match_not_found_with_single_character(self):
        self.assertEqual(text_match_two_three('a'), 'Not matched!')

    def test_match_not_found_with_single_character_space(self):
        self.assertEqual(text_match_two_three(' a'), 'Not matched!')

    def test_match_not_found_with_single_character_punctuation(self):
        self.assertEqual(text_match_two_three('!'), 'Not matched!')

    def test_match_not_found_with_newline_and_spaces(self):
        self.assertEqual(text_match_two_three('\n abc'), 'Not matched!')
