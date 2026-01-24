import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(text_lowercase_underscore(''), 'Not matched!')

    def test_single_word(self):
        self.assertEqual(text_lowercase_underscore('word'), 'Not matched!')

    def test_multiple_words(self):
        self.assertEqual(text_lowercase_underscore('word1Word2'), 'Not matched!')

    def test_underscore_at_beginning(self):
        self.assertEqual(text_lowercase_underscore('_word'), 'Not matched!')

    def test_underscore_at_end(self):
        self.assertEqual(text_lowercase_underscore('word_'), 'Not matched!')

    def test_underscore_in_middle(self):
        self.assertEqual(text_lowercase_underscore('word_word'), 'Not matched!')

    def test_valid_input(self):
        self.assertEqual(text_lowercase_underscore('valid_input'), 'Found a match!')

    def test_valid_input_with_numbers(self):
        self.assertEqual(text_lowercase_underscore('valid_input123'), 'Not matched!')

    def test_valid_input_with_special_characters(self):
        self.assertEqual(text_lowercase_underscore('valid_input#'), 'Not matched!')

    def test_valid_input_with_uppercase_letters(self):
        self.assertEqual(text_lowercase_underscore('VALID_INPUT'), 'Not matched!')
