import unittest
from mbpp_44_code import text_match_string

class TestTextMatchString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(text_match_string(''), 'Not matched!')

    def test_single_word(self):
        self.assertEqual(text_match_string('Hello'), 'Found a match!')

    def test_multiple_words(self):
        self.assertEqual(text_match_string('Hello World'), 'Not matched!')

    def test_leading_spaces(self):
        self.assertEqual(text_match_string(' Hello'), 'Found a match!')

    def test_trailing_spaces(self):
        self.assertEqual(text_match_string('Hello '), 'Found a match!')

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(text_match_string(' Hello World '), 'Found a match!')

    def test_numbers_and_symbols(self):
        self.assertEqual(text_match_string('Hello123@#$'), 'Not matched!')

    def test_only_numbers(self):
        self.assertEqual(text_match_string('1234567890'), 'Not matched!')

    def test_only_symbols(self):
        self.assertEqual(text_match_string('@#$%^&*()_+-=[]{}|;:,.<>/?~'), 'Not matched!')
