import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_lowercase_underscore('hello_world'), 'Found a match!')

    def test_single_word(self):
        self.assertEqual(text_lowercase_underscore('helloworld'), 'Not matched!')

    def test_multiple_words(self):
        self.assertEqual(text_lowercase_underscore('hello_world_example'), 'Not matched!')

    def test_empty_string(self):
        self.assertEqual(text_lowercase_underscore(''), 'Not matched!')

    def test_numeric_string(self):
        self.assertEqual(text_lowercase_underscore('123_456'), 'Not matched!')

    def test_special_characters(self):
        self.assertEqual(text_lowercase_underscore('hello@_world'), 'Not matched!')

    def test_capital_letters(self):
        self.assertEqual(text_lowercase_underscore('Hello_World'), 'Not matched!')

    def test_underscore_only(self):
        self.assertEqual(text_lowercase_underscore('_'), 'Not matched!')

    def test_single_underscore(self):
        self.assertEqual(text_lowercase_underscore('hello_'), 'Not matched!')
