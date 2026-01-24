import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(text_lowercase_underscore('hello_world'), 'Found a match!')

    def test_edge_case_single_word(self):
        self.assertEqual(text_lowercase_underscore('helloworld'), 'Not matched!')

    def test_edge_case_no_underscore(self):
        self.assertEqual(text_lowercase_underscore('hello_world123'), 'Not matched!')

    def test_edge_case_multiple_underscores(self):
        self.assertEqual(text_lowercase_underscore('hello__world'), 'Not matched!')

    def test_edge_case_empty_string(self):
        self.assertEqual(text_lowercase_underscore(''), 'Not matched!')

    def test_error_case_non_string_input(self):
        with self.assertRaises(TypeError):
            text_lowercase_underscore(123)
