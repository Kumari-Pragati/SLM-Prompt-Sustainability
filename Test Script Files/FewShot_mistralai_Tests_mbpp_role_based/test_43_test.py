import unittest
from mbpp_43_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_valid_match(self):
        self.assertEqual(text_match('example_variable'), 'Found a match!')

    def test_invalid_match(self):
        self.assertEqual(text_match('example_variable_number'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_special_characters(self):
        self.assertEqual(text_match('example_variable_#'), 'Not matched!')

    def test_uppercase_letters(self):
        self.assertEqual(text_match('EXAMPLE_VARIABLE'), 'Not matched!')

    def test_numbers(self):
        self.assertEqual(text_match('example_variable_123'), 'Not matched!')
