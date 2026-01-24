import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):
    def test_valid_match(self):
        self.assertEqual(text_lowercase_underscore('valid_match'), 'Found a match!')

    def test_invalid_match_no_underscore(self):
        self.assertEqual(text_lowercase_underscore('validMatch'), 'Not matched!')

    def test_invalid_match_no_letters(self):
        self.assertEqual(text_lowercase_underscore('123'), 'Not matched!')

    def test_invalid_match_no_first_letter(self):
        self.assertEqual(text_lowercase_underscore('_valid'), 'Not matched!')

    def test_invalid_match_no_last_letter(self):
        self.assertEqual(text_lowercase_underscore('valid_'), 'Not matched!')

    def test_invalid_match_multiple_underscores(self):
        self.assertEqual(text_lowercase_underscore('valid_multiple_underscores'), 'Not matched!')

    def test_invalid_match_special_characters(self):
        self.assertEqual(text_lowercase_underscore('valid_#'), 'Not matched!')
