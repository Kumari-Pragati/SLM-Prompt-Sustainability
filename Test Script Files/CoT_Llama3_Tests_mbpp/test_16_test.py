import unittest
from mbpp_16_code import text_lowercase_underscore

class TestTextLowercaseUnderscore(unittest.TestCase):

    def test_match(self):
        self.assertEqual(text_lowercase_underscore('hello_world'), 'Found a match!')

    def test_no_match(self):
        self.assertEqual(text_lowercase_underscore('Hello World'), 'Not matched!')

    def test_edge_case(self):
        self.assertEqual(text_lowercase_underscore('hello'), 'Not matched!')

    def test_edge_case2(self):
        self.assertEqual(text_lowercase_underscore('_hello'), 'Not matched!')

    def test_edge_case3(self):
        self.assertEqual(text_lowercase_underscore('hello_world123'), 'Found a match!')

    def test_edge_case4(self):
        self.assertEqual(text_lowercase_underscore('hello_world123!'), 'Found a match!')

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            text_lowercase_underscore(123)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            text_lowercase_underscore(None)
