import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(text_lowercase_underscore('valid_example'), 'Found a match!')

    def test_edge_case_uppercase(self):
        self.assertNotEqual(text_lowercase_underscore('VALID_EXAMPLE'), 'Found a match!')

    def test_edge_case_numbers(self):
        self.assertNotEqual(text_lowercase_underscore('valid_example123'), 'Found a match!')

    def test_edge_case_special_characters(self):
        self.assertNotEqual(text_lowercase_underscore('valid_example!'), 'Found a match!')

    def test_edge_case_multiple_underscores(self):
        self.assertNotEqual(text_lowercase_underscore('valid_example__'), 'Found a match!')

    def test_edge_case_empty_string(self):
        self.assertEqual(text_lowercase_underscore(''), 'Not matched!')

    def test_edge_case_single_word(self):
        self.assertEqual(text_lowercase_underscore('valid'), 'Not matched!')

    def test_edge_case_no_underscore(self):
        self.assertEqual(text_lowercase_underscore('valid_example_'), 'Not matched!')
