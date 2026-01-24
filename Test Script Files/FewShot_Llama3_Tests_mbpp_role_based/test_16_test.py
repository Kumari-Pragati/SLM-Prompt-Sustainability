import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):
    def test_valid_input(self):
        self.assertEqual(text_lowercase_underscore('hello_world'), 'Found a match!')

    def test_invalid_input(self):
        self.assertEqual(text_lowercase_underscore('Hello World'), 'Not matched!')

    def test_edge_case_input(self):
        self.assertEqual(text_lowercase_underscore('abc_def'), 'Found a match!')

    def test_empty_input(self):
        self.assertEqual(text_lowercase_underscore(''), 'Not matched!')

    def test_non_string_input(self):
        with self.assertRaises(TypeError):
            text_lowercase_underscore(123)
