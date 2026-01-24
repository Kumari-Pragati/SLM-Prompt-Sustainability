import unittest
from mbpp_43_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(text_match('valid_identifier'), 'Found a match!')

    def test_edge_case_uppercase(self):
        self.assertEqual(text_match('VALID_IDENTIFIER'), 'Found a match!')

    def test_edge_case_numbers(self):
        self.assertEqual(text_match('valid_identifier123'), 'Not matched!')

    def test_edge_case_special_characters(self):
        self.assertEqual(text_match('valid_identifier_'), 'Not matched!')
        self.assertEqual(text_match('valid_identifier_123'), 'Not matched!')
        self.assertEqual(text_match('valid_identifier_123_'), 'Not matched!')

    def test_edge_case_underscores_only(self):
        self.assertEqual(text_match('__'), 'Not matched!')

    def test_invalid_input_non_alphabetic(self):
        self.assertEqual(text_match('123'), 'Not matched!')

    def test_invalid_input_no_underscores(self):
        self.assertEqual(text_match('valid'), 'Not matched!')
