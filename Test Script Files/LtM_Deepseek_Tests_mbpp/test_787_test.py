import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):

    def test_simple_match(self):
        self.assertEqual(text_match_three('abbb'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_match_three('abbc'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match_three(''), 'Not matched!')

    def test_single_character(self):
        self.assertEqual(text_match_three('a'), 'Not matched!')

    def test_multiple_matches(self):
        self.assertEqual(text_match_three('abbbabbbabbb'), 'Found a match!')

    def test_leading_trailing_spaces(self):
        self.assertEqual(text_match_three(' abbb '), 'Found a match!')

    def test_special_characters(self):
        self.assertEqual(text_match_three('abbb@#$'), 'Found a match!')

    def test_numbers_in_text(self):
        self.assertEqual(text_match_three('abbb123'), 'Found a match!')

    def test_case_sensitivity(self):
        self.assertEqual(text_match_three('Abbb'), 'Not matched!')
