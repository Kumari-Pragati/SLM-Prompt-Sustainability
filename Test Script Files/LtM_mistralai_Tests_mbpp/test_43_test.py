import unittest
from mbpp_43_code import text_match

class TestTextMatch(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_match('example_name'), 'Found a match!')

    def test_case_sensitivity(self):
        self.assertEqual(text_match('Example_Name'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_match(''), 'Not matched!')

    def test_special_characters(self):
        self.assertEqual(text_match('1example_name'), 'Not matched!')
        self.assertEqual(text_match('example_number'), 'Not matched!')
        self.assertEqual(text_match('example_123'), 'Not matched!')

    def test_multiple_words(self):
        self.assertEqual(text_match('multiple_words'), 'Not matched!')

    def test_numbers_and_underscores(self):
        self.assertEqual(text_match('123_example'), 'Not matched!')
        self.assertEqual(text_match('example_1234'), 'Not matched!')
