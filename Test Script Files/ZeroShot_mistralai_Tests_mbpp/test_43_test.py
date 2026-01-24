import unittest
from mbpp_43_code import text_match

class TestTextMatch(unittest.TestCase):

    def test_valid_match(self):
        self.assertEqual(text_match('valid_example'), 'Found a match!')
        self.assertEqual(text_match('AnotherValidExample'), 'Found a match!')
        self.assertEqual(text_match('Valid_with_CamelCase'), 'Not matched!')

    def test_invalid_match(self):
        self.assertEqual(text_match('Invalid_example_with_numbers'), 'Not matched!')
        self.assertEqual(text_match('Invalid_example_with_special_characters'), 'Not matched!')
        self.assertEqual(text_match('Invalid_example_with_underscores_only'), 'Not matched!')
