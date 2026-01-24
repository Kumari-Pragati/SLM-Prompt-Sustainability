import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):
    def test_simple_match(self):
        self.assertEqual(text_lowercase_underscore('hello_world'), 'Found a match!')

    def test_simple_no_match(self):
        self.assertEqual(text_lowercase_underscore('HELLO WORLD'), 'Not matched!')

    def test_edge_case_empty_input(self):
        self.assertEqual(text_lowercase_underscore(''), 'Not matched!')

    def test_edge_case_single_word(self):
        self.assertEqual(text_lowercase_underscore('hello'), 'Not matched!')

    def test_edge_case_multiple_words(self):
        self.assertEqual(text_lowercase_underscore('hello world'), 'Not matched!')

    def test_edge_case_non_alphabetic_characters(self):
        self.assertEqual(text_lowercase_underscore('hello!world'), 'Not matched!')

    def test_edge_case_non_underscore_characters(self):
        self.assertEqual(text_lowercase_underscore('helloWorld'), 'Not matched!')

    def test_edge_case_non_alphabetic_and_non_underscore_characters(self):
        self.assertEqual(text_lowercase_underscore('hello!@#world'), 'Not matched!')

    def test_edge_case_multiple_underscores(self):
        self.assertEqual(text_lowercase_underscore('hello_world_world'), 'Found a match!')

    def test_edge_case_multiple_words_with_underscores(self):
        self.assertEqual(text_lowercase_underscore('hello_world world'), 'Found a match!')

    def test_edge_case_multiple_words_with_and_without_underscores(self):
        self.assertEqual(text_lowercase_underscore('hello world world'), 'Not matched!')
