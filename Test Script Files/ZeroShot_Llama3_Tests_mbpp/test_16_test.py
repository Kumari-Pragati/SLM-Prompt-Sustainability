import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(text_lowercase_underscore('hello_world'), 'Found a match!')

    def test_invalid_input(self):
        self.assertEqual(text_lowercase_underscore('HELLO WORLD'), 'Not matched!')

    def test_empty_input(self):
        self.assertEqual(text_lowercase_underscore(''), 'Not matched!')

    def test_input_with_numbers(self):
        self.assertEqual(text_lowercase_underscore('hello123_world'), 'Not matched!')

    def test_input_with_special_characters(self):
        self.assertEqual(text_lowercase_underscore('hello@world'), 'Not matched!')

    def test_input_with_spaces(self):
        self.assertEqual(text_lowercase_underscore('hello world'), 'Not matched!')

    def test_input_with_punctuation(self):
        self.assertEqual(text_lowercase_underscore('hello, world'), 'Not matched!')
