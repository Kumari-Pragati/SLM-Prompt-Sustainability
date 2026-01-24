import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_lowercase_underscore('valid_example'), 'Found a match!')

    def test_case_sensitivity(self):
        self.assertEqual(text_lowercase_underscore('Valid_Example'), 'Not matched!')

    def test_min_length(self):
        self.assertEqual(text_lowercase_underscore('a_'), 'Not matched!')

    def test_max_length(self):
        self.assertEqual(text_lowercase_underscore('aaa_bbb_ccc'), 'Not matched!')

    def test_multiple_words(self):
        self.assertEqual(text_lowercase_underscore('multiple_words_with_underscores'), 'Not matched!')

    def test_special_characters(self):
        self.assertEqual(text_lowercase_underscore('valid_example_123'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_lowercase_underscore(''), 'Not matched!')
