import unittest
from mbpp_787_code import text_match_three

class TestTextMatchThree(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_match_three('abbb'), 'Found a match!')

    def test_no_match_case(self):
        self.assertEqual(text_match_three('ab'), 'Not matched!')

    def test_multiple_matches(self):
        self.assertEqual(text_match_three('abbbabbb'), 'Found a match!')

    def test_empty_string(self):
        self.assertEqual(text_match_three(''), 'Not matched!')

    def test_single_character(self):
        self.assertEqual(text_match_three('a'), 'Not matched!')

    def test_multiple_characters_after_b(self):
        self.assertEqual(text_match_three('abbbc'), 'Found a match!')

    def test_special_characters(self):
        self.assertEqual(text_match_three('ab%$#@'), 'Not matched!')

    def test_numbers_after_b(self):
        self.assertEqual(text_match_three('ab123'), 'Found a match!')
